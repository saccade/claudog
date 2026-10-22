"""Goals entry from a small spec: python3 goals_post.py SPEC.json SAVED_READ > batch.json   (count on stderr)

Claude (Anthropic), 2026-10-22, for the sweep. SPEC: {"paras": [[kind, text], ...], "links": {"phrase": "url"}}
kind: h (bold heading), doc (doc's words, his red), me (Claude's orange), li (orange bullet). The script finds the
Goals tab's end and the last "Count: N" in the saved read, draws the increment (3 to 7, minus 36 past 72), and
appends the increment and Count lines. Insert at end - 1 with a leading newline (the tab ends in a paragraph).
"""
import json, random, re, sys
spec = json.load(open(sys.argv[1])); c = json.load(open(sys.argv[2]))["content"]
TAB = "t.89r88yxpo4v3"
def walk(ts):
    for t in ts:
        yield t; yield from walk(t.get("childTabs", []))
tab = next(t for t in walk(c["tabs"]) if t["tabProperties"]["tabId"] == TAB)
els = [e for e in tab["documentTab"]["body"]["content"] if "paragraph" in e]
end = els[-1]["endIndex"]
texts = ["".join(r.get("textRun", {}).get("content", "") for r in e["paragraph"]["elements"]) for e in els]
prev = int([m.group(1) for t in texts for m in [re.match(r"Count: (\d+)", t)] if m][-1])
inc = random.randint(3, 7); count = prev + inc - (36 if prev + inc > 72 else 0)
paras = [tuple(p) for p in spec["paras"]] + [("me", f"Random increment drawn by script: {inc}; previous count {prev}."), ("me", f"Count: {count}")]
text = "\n" + "\n".join(t for _, t in paras)
idx = end - 1; reqs = [{"insertText": {"location": {"index": idx, "tabId": TAB}, "text": text}}]
pos = idx + 1; spans = []
for kind, t in paras: spans.append((kind, pos, pos + len(t.encode("utf-16-le")) // 2, t)); pos += len(t.encode("utf-16-le")) // 2 + 1
ORANGE = {"red": 0.8, "green": 0.34901962, "blue": 0}; RED = {"red": 0.6, "green": 0, "blue": 0}
for kind, a, b, t in spans:
    reqs.append({"updateTextStyle": {"range": {"startIndex": a, "endIndex": b, "tabId": TAB}, "textStyle": {"foregroundColor": {"color": {"rgbColor": RED if kind == "doc" else ORANGE}}, "bold": kind == "h", "italic": False}, "fields": "foregroundColor,bold,italic"}})
    for phrase, url in spec.get("links", {}).items():
        i = t.find(phrase)
        if i >= 0:
            u = lambda s: len(s.encode("utf-16-le")) // 2
            reqs.append({"updateTextStyle": {"range": {"startIndex": a + u(t[:i]), "endIndex": a + u(t[:i]) + u(phrase), "tabId": TAB}, "textStyle": {"link": {"url": url}}, "fields": "link"}})
runs = []   # one bullet range per run of li paragraphs, so a plain paragraph between two lists stays plain
for s in spans:
    if s[0] == "li":
        if runs and runs[-1][2] and runs[-1][1] == s[1] - 1: runs[-1][1] = s[2]
        else: runs.append([s[1], s[2], True])
    else: runs.append([0, 0, False])
for a, b, isli in runs:
    if isli: reqs.append({"createParagraphBullets": {"range": {"startIndex": a, "endIndex": b, "tabId": TAB}, "bulletPreset": "BULLET_DISC_CIRCLE_SQUARE"}})
print(json.dumps({"revision": c["revisionId"], "requests": reqs}, ensure_ascii=False)); print(count, file=sys.stderr)
