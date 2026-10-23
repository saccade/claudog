"""Lists any line that appears more than once in a built path (doc, 10-23 09:33: nothing should repeat exactly).
Claude (Anthropic), 2026-10-23. Usage: python3 repeats.py   (from mansion/sets; exit 1 on a repeat)"""
import collections, sys
bad = 0
for k in (1, 2, 3, 4):
    lines = [l.strip() for l in open(f"set{k}.txt") if len(l.strip()) > 25]
    for l, c in collections.Counter(lines).items():
        if c > 1: bad += 1; print(f"path {k}: {c}x {l[:100]}")
print("no repeated lines" if not bad else f"{bad} repeated")
sys.exit(1 if bad else 0)
