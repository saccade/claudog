> **READ FIRST (mansion and dog math work):** motivate a change of notation, don't start with it. Keep the usual textbook notation (cos θ, signed terms, 2π) until it starts to look goofy, then bring the new one in where it earns its keep, explained at first use. Consistency through a doc is not the goal here. (doc, 2026-10-22; ledger R-107)

# claudog

Claude's programs and working files for the straight-> mechanics / dog
math project. Written by Claude (Anthropic). Public repo: no book prose,
no credentials. Keep it that way.

- typeset/   fixed-width text tools. wrap.py and reflow.py fill prose to
             66 columns (nonbreaking units, no hyphen breaks); wc.py,
             count.py, plural.py are small checkers.
- problems/  generators and editors for the haunted/second/last house
             problem sets (build_*, haunt*, last*, edit_*, walls*, ...).
- mansion/   helpers for the Mansion collaboration doc: watch.py diffs two
             saved reads, check_mid.py is the numeric check template,
             pass2.py builds batches. Run python with -I.
- checks/    sympy/numeric checks (spin ladder, last four).
- builders/  PDF and text builders for the older problem sets.
- docs/      Dog Math text (canonical copy is the Google Doc, once made),
             idiom list, z-forms table, the five-problems files.

Paths inside the scripts still point at the old session folders
(/home/claude/out, scratchpad). Fix a path when you reuse a script.
