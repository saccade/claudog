"""Long passages one path repeats from another: the reruns to turn into highlights or nods.
Claude (Anthropic), 2026-10-23, for doc's 10:20: "the long explicatory bits belong in one path each" (R-111, R-128).
Usage: python3 reruns.py [MIN_CHARS] [MIN_RATIO]   (from mansion/sets, after build_sets.py; defaults 250 and 0.85)
For each later path, lists every paragraph of at least MIN_CHARS that matches a paragraph of an earlier path at
MIN_RATIO or better (difflib), with its label ("scene" for unlabeled story lines, which are not explanations and may
stay), its length, the match ratio, and the earliest path it already appears in.
"""
import difflib, re, sys

MIN = int(sys.argv[1]) if len(sys.argv) > 1 else 250
RATIO = float(sys.argv[2]) if len(sys.argv) > 2 else 0.85
P = {k: [l for l in open(f"set{k}.txt").read().split("\n") if len(l) >= MIN and not l.startswith("## ")] for k in (1, 2, 3, 4)}

def label(line):
    m = re.match(r"\(([^)]+)\)", line)
    return m.group(1) if m else "scene"

total = 0
for b in (2, 3, 4):
    rows = []
    for x in P[b]:
        for a in range(1, b):
            r = max((difflib.SequenceMatcher(None, x, y).ratio() for y in P[a]), default=0)
            if r >= RATIO:
                rows.append((label(x), len(x), round(r, 2), a)); break
    expl = [r for r in rows if r[0] != "scene"]
    total += len(expl)
    print(f"path {b}: {len(expl)} explanations and {len(rows) - len(expl)} scenes already in an earlier path")
    for lab, n, r, a in rows:
        print(f"  {lab:>6}  {n:4d} chars  {r:.2f}  first in path {a}")
print(f"{total} long explanations appear in more than one path")
