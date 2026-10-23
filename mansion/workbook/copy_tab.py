"""Copy one Docs tab into an empty workbook tab: text, paragraph and text styles, links, bullets, an inline image, tables.

Claude (Anthropic), 2026-10-23, for the workbook move (Codex's review: keep structure and destinations, not just text).
Usage:
  python3 copy_tab.py text  SRC_READ SRC_TAB DST_TAB [--relink OLD=NEW ...]  > batch.json
      Everything but tables; each table becomes a placeholder paragraph "[[TABLE k]]".
  python3 copy_tab.py table SRC_READ SRC_TAB DST_READ DST_TAB               > batch.json
      Replaces each placeholder with an empty native table of the source's shape and column widths.
  python3 copy_tab.py fill  SRC_READ SRC_TAB DST_READ DST_TAB [--relink ...] > batch.json
      Fills the destination's empty tables cell by cell, last cell first, with the source's text and styles.
Styles are compressed: one request per run of identical style, never one per paragraph.
"""
import json, sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from tabsel import walk

PS = ("namedStyleType", "alignment", "lineSpacing", "spaceAbove", "spaceBelow", "indentStart", "indentFirstLine")
TS = ("bold", "italic", "underline", "strikethrough", "smallCaps", "foregroundColor", "backgroundColor",
      "fontSize", "baselineOffset", "weightedFontFamily", "link")
u16 = lambda s: len(s.encode("utf-16-le")) // 2

def tab(read, tid):
    c = json.load(open(read)); c = c.get("content", c)
    return next(t for t in walk(c["tabs"]) if t["tabProperties"]["tabId"] == tid)["documentTab"]

def relinks():
    a = sys.argv; out = {}
    if "--relink" in a:
        for x in a[a.index("--relink") + 1:]:
            if "=" in x: k, v = x.split("=", 1); out[k] = v
    return out

def textstyle(st, rl):
    st = {k: v for k, v in st.items() if k in TS}
    if "link" in st:
        url = st["link"].get("url")
        if url:
            for old, new in rl.items():
                if url.startswith(old): st["link"] = {"url": new}
    return st

def runs_of(paras, base, rl):
    """paras: list of (paragraph, text-without-images-adjustment). Returns text, paragraph spans, text runs, images, bullets."""
    text = ""; pspans = []; truns = []; images = []
    for p in paras:
        a = base + u16(text)
        for e in p["elements"]:
            if "textRun" in e:
                s = e["textRun"]["content"]; st = textstyle(e["textRun"].get("textStyle", {}), rl)
                truns.append((base + u16(text), base + u16(text) + u16(s), json.dumps(st, sort_keys=True)))
                text += s
            elif "inlineObjectElement" in e:
                images.append((base + u16(text), e["inlineObjectElement"]["inlineObjectId"]))
        ps = {k: v for k, v in p.get("paragraphStyle", {}).items() if k in PS}
        if "bullet" in p: ps = {k: v for k, v in ps.items() if not k.startswith("indent")}
        pspans.append((a, base + u16(text), json.dumps(ps, sort_keys=True), p.get("bullet")))
    return text, pspans, truns, images

def merge(spans):
    out = []
    for a, b, sig in spans:
        if out and out[-1][2] == sig and out[-1][1] == a: out[-1][1] = b
        else: out.append([a, b, sig])
    return out

def style_reqs(pspans, truns, tid, clear_to=None):
    reqs = []
    for a, b, sig in merge([(a, b, s) for a, b, s, _ in pspans]):
        ps = json.loads(sig)
        if ps: reqs.append({"updateParagraphStyle": {"range": {"startIndex": a, "endIndex": b, "tabId": tid},
                            "paragraphStyle": ps, "fields": ",".join(ps)}})
    for a, b, sig in merge(truns):
        st = json.loads(sig)
        if not st or a == b: continue
        reqs.append({"updateTextStyle": {"range": {"startIndex": a, "endIndex": b, "tabId": tid},
                     "textStyle": st, "fields": ",".join(st)}})
    return reqs

def bullet_reqs(pspans, lists, tid):
    reqs = []; i = 0
    while i < len(pspans):
        bl = pspans[i][3]
        if bl:
            j = i
            while j + 1 < len(pspans) and pspans[j + 1][3] and pspans[j + 1][3]["listId"] == bl["listId"]: j += 1
            g = lists.get(bl["listId"], {}).get("listProperties", {}).get("nestingLevels", [{}])[0]
            preset = "NUMBERED_DECIMAL_ALPHA_ROMAN" if "glyphType" in g and g.get("glyphType") not in ("GLYPH_TYPE_UNSPECIFIED", None) else "BULLET_DISC_CIRCLE_SQUARE"
            reqs.append({"createParagraphBullets": {"range": {"startIndex": pspans[i][0], "endIndex": pspans[j][1], "tabId": tid},
                         "bulletPreset": preset}})
            i = j
        i += 1
    return reqs

def body_items(dt):
    return [el for el in dt["body"]["content"] if "paragraph" in el or "table" in el]

def mode_text(src, stid, dtid):
    dt = tab(src, stid); rl = relinks(); paras = []; k = 0
    for el in body_items(dt):
        if "table" in el:
            paras.append({"elements": [{"textRun": {"content": f"[[TABLE {k}]]\n", "textStyle": {}}}], "paragraphStyle": {"namedStyleType": "NORMAL_TEXT"}}); k += 1
        else: paras.append(el["paragraph"])
    text, pspans, truns, images = runs_of(paras, 1, rl)
    # the empty tab already ends in a newline: insert all but the source's final newline
    assert text.endswith("\n"); text = text[:-1]
    # inline images are not text: their index is a position in the final text, inserted last (later indices shift by one)
    reqs = [{"insertText": {"location": {"index": 1, "tabId": dtid}, "text": text}}]
    reqs += style_reqs(pspans, truns, dtid)
    reqs += bullet_reqs(pspans, dt.get("lists", {}), dtid)
    for pos, oid in reversed(images):
        emb = dt["inlineObjects"][oid]["inlineObjectProperties"]["embeddedObject"]
        reqs.append({"insertInlineImage": {"location": {"index": pos, "tabId": dtid}, "uri": emb["imageProperties"]["contentUri"],
                     "objectSize": emb["size"]}})
    return reqs

def dst_items(read, tid):
    return body_items(tab(read, tid))

def mode_table(src, stid, dst, dtid):
    tables = [el["table"] for el in body_items(tab(src, stid)) if "table" in el]; reqs = []
    for el in reversed(dst_items(dst, dtid)):
        if "paragraph" not in el: continue
        t = "".join(e.get("textRun", {}).get("content", "") for e in el["paragraph"]["elements"])
        if t.startswith("[[TABLE "):
            k = int(t[8:t.index("]]")]); tb = tables[k]; a = el["startIndex"]
            reqs.append({"deleteContentRange": {"range": {"startIndex": a, "endIndex": a + u16(t) - 1, "tabId": dtid}}})
            reqs.append({"insertTable": {"rows": tb["rows"], "columns": tb["columns"], "location": {"index": a, "tabId": dtid}}})
    return reqs

def mode_fill(src, stid, dst, dtid):
    rl = relinks()
    stabs = [el["table"] for el in body_items(tab(src, stid)) if "table" in el]
    dtabs = [el for el in dst_items(dst, dtid) if "table" in el]
    reqs = []
    from collections import Counter
    for st, del_ in reversed(list(zip(stabs, dtabs))):
        dtb = del_["table"]; start = del_["startIndex"]; grown = 0
        cells = []
        for r, (srow, drow) in enumerate(zip(st["tableRows"], dtb["tableRows"])):
            for c, (sc, dc) in enumerate(zip(srow["tableCells"], drow["tableCells"])): cells.append((r, c, sc, dc))
        # the commonest paragraph style and font size go on the whole table at the end; cells carry only their differences
        built = []
        for r, c, sc, dc in cells:
            paras = [p["paragraph"] for p in sc["content"] if "paragraph" in p]
            built.append(runs_of(paras, dc["content"][0]["startIndex"], rl))
        pcommon = Counter(s for _, ps, _, _ in built for _, _, s, _ in ps).most_common(1)[0][0]
        fcommon = Counter(json.dumps(json.loads(s).get("fontSize")) for _, _, tr, _ in built for _, _, s in tr).most_common(1)[0][0]
        # NOTE (2026-10-23, found in use): setting namedStyleType on a paragraph resets its character styles, so the
        # whole-table and per-paragraph style passes below wipe the per-cell text styles applied here. After a fill,
        # reapply the cell text styles from a fresh read (see compare_tab.py), or fold this into one pass.
        late = []
        for (r, c, sc, dc), (text, pspans, truns, _) in reversed(list(zip(cells, built))):
            at = dc["content"][0]["startIndex"]
            text = text[:-1]   # the empty cell already has its newline
            if text: reqs.append({"insertText": {"location": {"index": at, "tabId": dtid}, "text": text}}); grown += u16(text)
            trs = []
            for a, b, s in truns:
                d = json.loads(s)
                if json.dumps(d.get("fontSize")) == fcommon: d.pop("fontSize", None)
                trs.append((a, b, json.dumps(d, sort_keys=True)))
            reqs += style_reqs([], trs, dtid)
            late += [(at, a, b, s) for a, b, s, _ in pspans if s != pcommon]   # positions shift with later inserts: fixed below
        # cell styles: one request per run of rows whose cells all share one style
        rows = []
        for r, row in enumerate(st["tableRows"]):
            sigs = {json.dumps({k: v for k, v in cl.get("tableCellStyle", {}).items() if k not in ("columnSpan", "rowSpan", "contentDirection")}, sort_keys=True) for cl in row["tableCells"]}
            rows.append(sigs.pop() if len(sigs) == 1 else None)
        r = 0
        while r < len(rows):
            j = r
            while j + 1 < len(rows) and rows[j + 1] == rows[r] and rows[r] is not None: j += 1
            if rows[r]:
                cs = json.loads(rows[r])
                reqs.append({"updateTableCellStyle": {"tableRange": {"tableCellLocation": {"tableStartLocation": {"index": start, "tabId": dtid},
                             "rowIndex": r, "columnIndex": 0}, "rowSpan": j - r + 1, "columnSpan": st["columns"]}, "tableCellStyle": cs, "fields": ",".join(cs)}})
            r = j + 1
        end = del_["endIndex"] + grown
        ps = json.loads(pcommon)
        reqs.append({"updateParagraphStyle": {"range": {"startIndex": start, "endIndex": end, "tabId": dtid}, "paragraphStyle": ps, "fields": ",".join(ps)}})
        if fcommon != "null":
            reqs.append({"updateTextStyle": {"range": {"startIndex": start + 1, "endIndex": end - 1, "tabId": dtid}, "textStyle": {"fontSize": json.loads(fcommon)}, "fields": "fontSize"}})
        # the differing paragraphs: their final positions are their read positions plus everything inserted before them
        ins = sorted((x["insertText"]["location"]["index"], u16(x["insertText"]["text"])) for x in reqs if "insertText" in x)
        for at, a, b, s in late:
            shift = sum(n for i, n in ins if i < at)   # the cells before this one; its own text is already in a and b
            p = json.loads(s)
            reqs.append({"updateParagraphStyle": {"range": {"startIndex": a + shift, "endIndex": b + shift, "tabId": dtid}, "paragraphStyle": p, "fields": ",".join(p)}})
        for ci, cp in enumerate(st.get("tableStyle", {}).get("tableColumnProperties", [])):
            reqs.append({"updateTableColumnProperties": {"tableStartLocation": {"index": start, "tabId": dtid}, "columnIndices": [ci],
                         "tableColumnProperties": cp, "fields": ",".join(cp)}})
    return reqs

if __name__ == "__main__":
    m = sys.argv[1]
    if m == "text": out = mode_text(sys.argv[2], sys.argv[3], sys.argv[4])
    elif m == "table": out = mode_table(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    else: out = mode_fill(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    print(json.dumps(out, ensure_ascii=True, separators=(",", ":")))
