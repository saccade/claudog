"""Builds the lineup page for the four Mansion solution sets.

Claude (Anthropic), 2026-10-22. Runs lineup_sets.py's cut, then lineup (github.com/saccade/lineup)
on the four folders, with two changes for prose rather than code, made here so lineup itself is
untouched: the side-by-side pieces go in pset order (lineup puts the most widely shared first),
and lines wrap in a reading font.
Usage: python3 lineup_page.py LINEUP_DIR OUTDIR   (writes OUTDIR/mansion-sets.html, a page fragment for the artifact host)
"""
import os, sys
LINEUP, OUT = sys.argv[1], sys.argv[2]
sys.path.insert(0, LINEUP)
import lineup, lineup_sets

lineup_sets.main(OUT)
here = os.path.dirname(os.path.abspath(__file__))
argv = [os.path.join(OUT, "mansion-sets.html")] + [f"set{k}={os.path.join(OUT, f'set{k}')}" for k in (1, 2, 3, 4)] + [
    "--base", "set1", "--derived", "set2", "--derived", "set3", "--derived", "set4",
    "--label", "set1=path 1, the mansion", "--label", "set2=path 2, with the cabinet",
    "--label", "set3=path 3, with the funhouse", "--label", "set4=path 4, the whole house",
    "--page", "Overview=" + os.path.join(here, "lineup_overview.md"),
    "--title", "Mansion Paths", "--fragment",
    "--byline", "Written by Claude (Anthropic) for dr. kraemer, from the four path docs, solutions only (the statements are in the problem set)."]

PROSE = ("<style>/* prose, not code */ .code table { font-family: var(--body); font-size: 0.9rem; } "
         ".code td.c { white-space: pre-wrap; overflow-wrap: anywhere; } "
         ".cols { grid-auto-columns: minmax(22rem, 1fr); }</style>\n")

real_build = lineup.build
def build(a):
    data = real_build(a)
    data["compare"].sort(key=lambda c: c["name"])
    return data
lineup.build = build
lineup.main(argv)
path = argv[0]
s = open(path, encoding="utf-8").read()
open(path, "w", encoding="utf-8").write(s + PROSE)   # last, so it wins over lineup's own rules
print("prose style added")
