"""Checks a set doc against a built set: text, named styles, indents, italic/bold/superscript, no color, no blank paragraphs.
Claude (Anthropic), 2026-10-22. Usage: python3 set_doc_verify.py SAVED_READ setK.html"""
import json, re, html, sys
c = json.load(open(sys.argv[1])); c = c.get("content", c)
els = [el for el in c["tabs"][0]["documentTab"]["body"]["content"] if "paragraph" in el]
src = re.search(r"<body>(.*)</body>", open(sys.argv[2]).read(), re.S).group(1)
want = []
for m in re.finditer(r"<(h1|h2|h3|p)([^>]*)>(.*?)</\1>", src, re.S):
    tag, attrs, inner = m.groups(); b = re.match(r"<b>(.*?)</b>", inner)
    text = html.unescape(re.sub(r"<[^>]+>", "", inner)).strip()
    if text: want.append((tag, text, inner.startswith("<i>") and inner.endswith("</i>"), len(html.unescape(b.group(1))) if b else 0, "margin-left" in attrs))
NAMED = {"h1": "HEADING_1", "h2": "HEADING_2", "h3": "HEADING_3", "p": "NORMAL_TEXT"}
bad = []
have = []
for el in els:
    t = "".join(e.get("textRun", {}).get("content", "") for e in el["paragraph"]["elements"]).rstrip("\n")
    if t.strip(): have.append((el, t))
    elif el is not els[-1]: bad.append(("blank paragraph", el["startIndex"]))
if [t for _, t in have] != [w[1] for w in want]: bad.append(("text differs", None))
for (el, t), (tag, _, it, bold, ind) in zip(have, want):
    ps = el["paragraph"].get("paragraphStyle", {})
    if ps.get("namedStyleType") != NAMED[tag]: bad.append(("style", t[:40]))
    if ps.get("indentStart", {}).get("magnitude", 0) != (36 if ind else 0): bad.append(("indent", t[:40]))
    pos = 0
    for e in el["paragraph"]["elements"]:
        tr = e.get("textRun"); 
        if not tr: continue
        st = tr.get("textStyle", {}); s = tr["content"].rstrip("\n")
        if not s: continue
        if st.get("foregroundColor", {}).get("color"): bad.append(("color", s[:30]))
        if bool(st.get("italic")) != it: bad.append(("italic", s[:30]))
        if bool(st.get("bold")) != (pos < bold): bad.append(("bold", s[:30]))
        if ("†" in s) != (st.get("baselineOffset") == "SUPERSCRIPT"): bad.append(("dagger", s[:30]))
        pos += len(s)
print(c["title"], "|", len(have), "paragraphs |", "OK" if not bad else bad[:20])
