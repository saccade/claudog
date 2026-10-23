"""Brings a set doc's styles up to a built set once its text matches: one guarded batch.

Claude (Anthropic), 2026-10-22. Usage: python3 set_doc_style.py SAVED_READ setK.html > batch.json  (revisionId on stderr)
Clears color, italic, bold and baseline over the whole body (sets 2-4 were pale), resets every paragraph's
named style and indent where they differ, puts back italic paragraphs, bold leads and superscript daggers,
then deletes empty paragraphs from the bottom up. Paragraph styles go first: a named style sent after a
text style resets it.
"""
import json, re, html, sys
import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "workbook")); from tabsel import tab_doc, tabify
TAB = sys.argv[sys.argv.index("--tab") + 1] if "--tab" in sys.argv else None   # a workbook tab ID (2026-10-23)
c = json.load(open(sys.argv[1])); c = c.get("content", c)
els = [el for el in tab_doc(c, TAB)["body"]["content"] if "paragraph" in el]
src = re.search(r"<body>(.*)</body>", open(sys.argv[2]).read(), re.S).group(1)
want = []
for m in re.finditer(r"<(h1|h2|h3|p)([^>]*)>(.*?)</\1>", src, re.S):
    tag, attrs, inner = m.groups()
    b = re.match(r"<b>(.*?)</b>", inner)
    text = html.unescape(re.sub(r"<[^>]+>", "", inner)).strip()
    if text: want.append((tag, text, inner.startswith("<i>") and inner.endswith("</i>"), len(html.unescape(b.group(1))) if b else 0, "margin-left" in attrs))
NAMED = {"h1": "HEADING_1", "h2": "HEADING_2", "h3": "HEADING_3", "p": "NORMAL_TEXT"}
have, empty = [], []
for el in els:
    t = "".join(e.get("textRun", {}).get("content", "") for e in el["paragraph"]["elements"]).rstrip("\n")
    (have if t.strip() else empty).append((el, t))
assert [t for _, t in have] == [w[1] for w in want], "text differs from the build: patch first"
end = els[-1]["endIndex"]
pre, txt = [], [{"updateTextStyle": {"range": {"startIndex": 1, "endIndex": end - 1}, "textStyle": {},
                                     "fields": "bold,italic,underline,strikethrough,baselineOffset,foregroundColor,backgroundColor"}}]
for (el, t), (tag, _, it, bold, ind) in zip(have, want):
    ps = el["paragraph"].get("paragraphStyle", {})
    s, e = el["startIndex"], el["endIndex"]
    cur_ind = ps.get("indentStart", {}).get("magnitude", 0)
    if ps.get("namedStyleType") != NAMED[tag] or cur_ind != (36 if ind else 0) or ps.get("indentFirstLine", {}).get("magnitude", 0):
        pre.append({"updateParagraphStyle": {"range": {"startIndex": s, "endIndex": e},
            "paragraphStyle": {"namedStyleType": NAMED[tag], "indentStart": {"magnitude": 36 if ind else 0, "unit": "PT"}, "indentFirstLine": {"magnitude": 0, "unit": "PT"}},
            "fields": "namedStyleType,indentStart,indentFirstLine"}})
    if it: txt.append({"updateTextStyle": {"range": {"startIndex": s, "endIndex": e - 1}, "textStyle": {"italic": True}, "fields": "italic"}})
    if bold: txt.append({"updateTextStyle": {"range": {"startIndex": s, "endIndex": s + len(t[:bold].encode("utf-16-le")) // 2}, "textStyle": {"bold": True}, "fields": "bold"}})
    off = 0
    for ch in t:
        if ch == "†": txt.append({"updateTextStyle": {"range": {"startIndex": s + off, "endIndex": s + off + 1}, "textStyle": {"baselineOffset": "SUPERSCRIPT"}, "fields": "baselineOffset"}})
        off += len(ch.encode("utf-16-le")) // 2
dele = [{"deleteContentRange": {"range": {"startIndex": el["startIndex"], "endIndex": el["endIndex"]}}}
        for el, _ in sorted(empty, key=lambda x: -x[0]["startIndex"]) if el["endIndex"] < end]
print(c["revisionId"], file=sys.stderr)
print(json.dumps(tabify(pre + txt + dele, TAB), ensure_ascii=False))
