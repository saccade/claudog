"""Brings a set doc up to a built set with small replaceAllText edits (no positions, no guard), paragraph by paragraph.

Claude (Anthropic), 2026-10-22. Usage: python3 set_doc_patch.py SAVED_READ setK.html > batch.json
Each changed paragraph is cut to its differing middle plus enough context to be unique in the doc.
A paragraph the doc doesn't have yet goes in after the one before it, as a new paragraph;
a dropped paragraph is emptied (delete the blank line after, with a guarded batch).
"""
import json, re, html, difflib, sys, unicodedata
import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "workbook")); from tabsel import tab_doc, tabify
TAB = sys.argv[sys.argv.index("--tab") + 1] if "--tab" in sys.argv else None   # a workbook tab ID (2026-10-23)
c = json.load(open(sys.argv[1])); c = c.get("content", c)
a = []
for el in tab_doc(c, TAB)["body"]["content"]:
    if "paragraph" in el:
        s = "".join(e.get("textRun", {}).get("content", "") for e in el["paragraph"]["elements"]).rstrip("\n")
        if s.strip(): a.append(s)
full = "\n".join(a)
h = open(sys.argv[2]).read()
b = [x for x in (html.unescape(re.sub("<[^>]+>", "", m.group(2))).strip() for m in re.finditer(r"<(h1|h2|h3|p)[^>]*>(.*?)</\1>", h, re.S)) if x]
reqs = []
def rep(old, new):
    # Docs' replaceAllText matches without regard to combining marks: "a" + U+0307 matched every plain "a"
    # (2026-10-22, 1511 replacements, undone). Never send a combining character in a search.
    assert not any(unicodedata.combining(ch) for ch in old + new), "combining mark in a replaceAllText"
    assert full.count(old) == 1, old[:80]
    reqs.append({"replaceAllText": {"containsText": {"text": old, "matchCase": True}, "replaceText": new}})
def pair(o, n):
    p = 0
    while p < min(len(o), len(n)) and o[p] == n[p]: p += 1
    s = 0
    while s < min(len(o), len(n)) - p and o[-1 - s] == n[-1 - s]: s += 1
    for ctx in (6, 9, 12, 25, 40, 80, 200, 10**6):
        lo, hi = max(0, p - ctx), min(len(o), len(o) - s + ctx)
        old = o[lo:hi]; new = n[lo:len(n) - (len(o) - hi)]
        if any(unicodedata.combining(ch) for ch in old + new): continue   # a θ̈ in the context: widen or narrow past it
        if full.count(old) == 1:
            return rep(old, n[lo:len(n) - (len(o) - hi)])
    # a combining mark sits inside the changed span: patch the paragraph's separate changes one at a time
    ops = [op for op in difflib.SequenceMatcher(None, o, n, autojunk=False).get_opcodes() if op[0] != "equal"]
    groups = []
    for op in ops:
        if groups and op[1] - groups[-1][2] < 30: groups[-1] = (groups[-1][0], groups[-1][1], op[2], groups[-1][3], op[4])
        else: groups.append(op)
    for _, i1, i2, j1, j2 in groups:
        for ctx in (6, 9, 12, 20):
            lo, hi = max(0, i1 - ctx), min(len(o), i2 + ctx)
            old = o[lo:hi]; new = o[lo:i1] + n[j1:j2] + o[i2:hi]
            if any(unicodedata.combining(ch) for ch in old + new): continue
            if full.count(old) == 1: rep(old, new); break
        else: raise SystemExit("no unique context: " + o[:80])
for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
    if op == "equal": continue
    if op == "replace" and i2 - i1 == j2 - j1:
        for o, n in zip(a[i1:i2], b[j1:j2]): pair(o, n)
    elif op == "replace" and i2 - i1 == j2 - j1 + 1:   # one paragraph dropped: empty the first, pair the rest
        rep(a[i1], "")
        for o, n in zip(a[i1 + 1:i2], b[j1:j2]): pair(o, n)
    elif op == "delete":   # a paragraph the build doesn't have (a note to the bots): empty it
        for o in a[i1:i2]: rep(o, "")
    elif op == "insert" and i1 == 0:   # new paragraphs before the first one: put them ahead of its head (Codex, 15:05)
        head = a[0][:60]
        rep(head, "\n".join(b[j1:j2]) + "\n" + head)
    elif op == "insert":
        prev = a[i1 - 1]
        tail = prev[-60:]
        rep(tail, tail + "\n" + "\n".join(b[j1:j2]))
    elif op == "replace":   # any other shape: the first old paragraph takes all the new ones, the rest are emptied
        rep(a[i1], "\n".join(b[j1:j2]))
        for o in a[i1 + 1:i2]: rep(o, "")
    else:
        raise SystemExit(f"unhandled {op} {i1}:{i2} {j1}:{j2}")
print(json.dumps(tabify(reqs, TAB), ensure_ascii=False))
