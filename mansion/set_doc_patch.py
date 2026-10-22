"""Brings a set doc up to a built set with small replaceAllText edits (no positions, no guard), paragraph by paragraph.

Claude (Anthropic), 2026-10-22. Usage: python3 set_doc_patch.py SAVED_READ setK.html > batch.json
Each changed paragraph is cut to its differing middle plus enough context to be unique in the doc.
A paragraph the doc doesn't have yet goes in after the one before it, as a new paragraph;
a dropped paragraph is emptied (delete the blank line after, with a guarded batch).
"""
import json, re, html, difflib, sys
c = json.load(open(sys.argv[1])); c = c.get("content", c)
a = []
for el in c["tabs"][0]["documentTab"]["body"]["content"]:
    if "paragraph" in el:
        s = "".join(e.get("textRun", {}).get("content", "") for e in el["paragraph"]["elements"]).rstrip("\n")
        if s.strip(): a.append(s)
full = "\n".join(a)
h = open(sys.argv[2]).read()
b = [x for x in (html.unescape(re.sub("<[^>]+>", "", m.group(2))).strip() for m in re.finditer(r"<(h1|h2|h3|p)[^>]*>(.*?)</\1>", h, re.S)) if x]
reqs = []
def rep(old, new):
    assert full.count(old) == 1, old[:80]
    reqs.append({"replaceAllText": {"containsText": {"text": old, "matchCase": True}, "replaceText": new}})
def pair(o, n):
    p = 0
    while p < min(len(o), len(n)) and o[p] == n[p]: p += 1
    s = 0
    while s < min(len(o), len(n)) - p and o[-1 - s] == n[-1 - s]: s += 1
    for ctx in (12, 25, 40, 80, 200, 10**6):
        lo, hi = max(0, p - ctx), min(len(o), len(o) - s + ctx)
        old = o[lo:hi]
        if full.count(old) == 1:
            return rep(old, n[lo:len(n) - (len(o) - hi)])
    raise SystemExit("no unique context: " + o[:80])
for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
    if op == "equal": continue
    if op == "replace" and i2 - i1 == j2 - j1:
        for o, n in zip(a[i1:i2], b[j1:j2]): pair(o, n)
    elif op == "replace" and i2 - i1 == j2 - j1 + 1:   # one paragraph dropped: empty the first, pair the rest
        rep(a[i1], "")
        for o, n in zip(a[i1 + 1:i2], b[j1:j2]): pair(o, n)
    elif op == "insert":
        prev = a[i1 - 1]
        tail = prev[-60:]
        rep(tail, tail + "\n" + "\n".join(b[j1:j2]))
    else:
        raise SystemExit(f"unhandled {op} {i1}:{i2} {j1}:{j2}")
print(json.dumps(reqs, ensure_ascii=False))
