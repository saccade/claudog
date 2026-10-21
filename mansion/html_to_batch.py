"""Turns a simple HTML draft (h1/h2/h3/p, with whole-paragraph <i>, a leading <b>, and margin-left) into one Docs batch for an empty doc.

Claude (Anthropic), 2026-10-21. Usage: python3 html_to_batch.py FILE.html > batch.json
"""
import json, re, sys, html
src = open(sys.argv[1]).read()
body = re.search(r"<body>(.*)</body>", src, re.S).group(1)
paras = []
for m in re.finditer(r"<(h1|h2|h3|p)([^>]*)>(.*?)</\1>", body, re.S):
    tag, attrs, inner = m.groups()
    italic = inner.startswith("<i>") and inner.endswith("</i>")
    bold = None
    b = re.match(r"<b>(.*?)</b>", inner)
    if b: bold = len(html.unescape(b.group(1)))
    text = html.unescape(re.sub(r"<[^>]+>", "", inner)).strip()
    paras.append((tag, text, italic, bold, "margin-left" in attrs))
text = "\n".join(p[1] for p in paras)
reqs = [{"insertText": {"text": text, "location": {"index": 1}}}]
pos = 1
NAMED = {"h1": "HEADING_1", "h2": "HEADING_2", "h3": "HEADING_3", "p": "NORMAL_TEXT"}
for tag, t, italic, bold, indent in paras:
    end = pos + len(t)
    ps = {"namedStyleType": NAMED[tag]}; fields = "namedStyleType"
    if indent: ps["indentStart"] = {"magnitude": 36, "unit": "PT"}; fields += ",indentStart"
    reqs.append({"updateParagraphStyle": {"range": {"startIndex": pos, "endIndex": end + 1}, "paragraphStyle": ps, "fields": fields}})
    if italic:
        reqs.append({"updateTextStyle": {"range": {"startIndex": pos, "endIndex": end}, "textStyle": {"italic": True}, "fields": "italic"}})
    if bold:
        reqs.append({"updateTextStyle": {"range": {"startIndex": pos, "endIndex": pos + bold}, "textStyle": {"bold": True}, "fields": "bold"}})
    pos = end + 1
assert all(ord(ch) < 0x10000 for ch in text)
print(json.dumps(reqs, ensure_ascii=False))
