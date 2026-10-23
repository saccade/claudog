"""Replace whole paragraphs that differ from the build, by position (for repeated lines replaceAllText can't single out).
Claude (Anthropic), 2026-10-23. Usage: python3 para_swap.py SAVED_READ setK.html TAB > batch.json
Paragraph counts must match; only text changes. Bottom-up, so earlier positions hold; send with the read's revision."""
import json, re, html, sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from tabsel import tab_doc
u16 = lambda s: len(s.encode("utf-16-le")) // 2
c = json.load(open(sys.argv[1])); c = c.get("content", c)
have = []
for el in tab_doc(c, sys.argv[3])["body"]["content"]:
    if "paragraph" in el:
        t = "".join(e.get("textRun", {}).get("content", "") for e in el["paragraph"]["elements"]).rstrip("\n")
        if t.strip(): have.append((el["startIndex"], t))
src = re.search(r"<body>(.*)</body>", open(sys.argv[2]).read(), re.S).group(1)
want = [html.unescape(re.sub(r"<[^>]+>", "", m.group(3))).strip() for m in re.finditer(r"<(h1|h2|h3|p)([^>]*)>(.*?)</\1>", src, re.S)]
want = [w for w in want if w]
assert len(have) == len(want), (len(have), len(want))
reqs = []
for (a, t), w in reversed(list(zip(have, want))):
    if t != w:
        reqs += [{"deleteContentRange": {"range": {"startIndex": a, "endIndex": a + u16(t), "tabId": sys.argv[3]}}},
                 {"insertText": {"location": {"index": a, "tabId": sys.argv[3]}, "text": w}}]
print(json.dumps({"revision": c["revisionId"], "requests": reqs}, ensure_ascii=True))
