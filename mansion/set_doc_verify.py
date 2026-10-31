"""Checks a set doc against a built set: text, named styles, indents, italic/bold/superscript, no color, no blank paragraphs.
Claude (Anthropic), 2026-10-22. Usage: python3 set_doc_verify.py SAVED_READ setK.html"""
import json, re, html, sys
import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "workbook")); from tabsel import tab_doc, tabify
TAB = sys.argv[sys.argv.index("--tab") + 1] if "--tab" in sys.argv else None   # a workbook tab ID (2026-10-23)
c = json.load(open(sys.argv[1])); c = c.get("content", c)
els = [el for el in tab_doc(c, TAB)["body"]["content"] if "paragraph" in el]
def em_spans(inner):
    """UTF-16 (start, end) of each <em> span in a paragraph's unescaped, tag-stripped text (spoken stress, in italic)."""
    out, pos = [], 0
    for part in re.split(r"(</?em>)", inner):
        if part == "<em>": a = pos
        elif part == "</em>": out.append((a, pos))
        else: pos += len(html.unescape(re.sub(r"<[^>]+>", "", part)).encode("utf-16-le")) // 2
    return out

src = re.search(r"<body>(.*)</body>", open(sys.argv[2]).read(), re.S).group(1)
want = []
for m in re.finditer(r"<(h1|h2|h3|p)([^>]*)>(.*?)</\1>", src, re.S):
    tag, attrs, inner = m.groups(); b = re.match(r"<b>(.*?)</b>", inner)
    text = html.unescape(re.sub(r"<[^>]+>", "", inner)).strip()
    if text: want.append((tag, text, inner.startswith("<i>") and inner.endswith("</i>"), len(html.unescape(b.group(1))) if b else 0, "margin-left" in attrs, em_spans(inner.strip())))
NAMED = {"h1": "HEADING_1", "h2": "HEADING_2", "h3": "HEADING_3", "p": "NORMAL_TEXT"}
bad = []
have = []
for el in els:
    t = "".join(e.get("textRun", {}).get("content", "") for e in el["paragraph"]["elements"]).rstrip("\n")
    if t.strip(): have.append((el, t))
    elif el is not els[-1]: bad.append(("blank paragraph", el["startIndex"]))
if [t for _, t in have] != [w[1] for w in want]: bad.append(("text differs", None))
for (el, t), (tag, _, it, bold, ind, ems) in zip(have, want):
    ps = el["paragraph"].get("paragraphStyle", {})
    if ps.get("namedStyleType") != NAMED[tag]: bad.append(("style", t[:40]))
    if ps.get("indentStart", {}).get("magnitude", 0) != (36 if ind else 0): bad.append(("indent", t[:40]))
    pos = 0
    for e in el["paragraph"]["elements"]:
        tr = e.get("textRun"); 
        if not tr: continue
        st = tr.get("textStyle", {}); s = tr["content"].rstrip("\n")
        if not s: continue
        link = st.get("link")   # a link run carries the link's own blue and underline (path 4's pointer, 10-31)
        if st.get("foregroundColor", {}).get("color") and not link: bad.append(("color", s[:30]))
        for mark in ("strikethrough", "underline", "backgroundColor"):   # doc's markup is a message, not styling: report it
            if st.get(mark) and not (link and mark == "underline"): bad.append((mark, s[:40]))
        q = len(t[:pos].encode("utf-16-le")) // 2; qe = q + len(s.encode("utf-16-le")) // 2
        if bool(st.get("italic")) != (it or any(a <= q and qe <= z for a, z in ems)): bad.append(("italic", s[:30]))
        if bool(st.get("bold")) != (pos < bold): bad.append(("bold", s[:30]))
        if ("†" in s) != (st.get("baselineOffset") == "SUPERSCRIPT"): bad.append(("dagger", s[:30]))
        pos += len(s)
print(c["title"] + (f" [{TAB}]" if TAB else ""), "|", len(have), "paragraphs |", "OK" if not bad else bad[:20])
sys.exit(1 if bad else 0)   # a mismatch is a failure, not just a printout (Codex, 2026-10-22 15:05)
