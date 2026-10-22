"""Goals-tab entry for the forgetting-gaps tool (Claude, 2026-10-22 13:45). Prints the batch; usage: python3 goals_gaps.py INDEX TABID"""
import json, random, sys
ORANGE = {"red": 0.8, "green": 0.34901962, "blue": 0.0}
RED = {"red": 0.6, "green": 0.0, "blue": 0.0}
inc = random.randint(3, 7); prev = 47; count = prev + inc
if count > 72: count -= 36
P = [
("C", "For Codex: a toy to play with, per doc (13:41). In claudog, mansion/sets: gaps.py measures how long a reader goes without each term along each solution path, where the term is glossed, and where it comes back after a long gap without a nod; gaps_page.py draws it, one staff per term, with a path switch and a long-gap dial; forgetting_gaps.html is the current page and works on its own. Run from mansion/sets: python3 gaps.py gaps.json, then python3 gaps_page.py gaps.json forgetting_gaps.html (the README says the same). The term list and the gloss heuristic are at the top of gaps.py. The heuristic is a word-pattern guess, so it misses some nods (the chair's “forward part” is one) and catches some sentences that aren't. It's built on doc's forgetting theory (ledger R-117):"),
("D", "doc (13:35): it's the forgetting theory. you want to redefine something when someone is gonna forget it, but your neurons don't get tired. if you introduce something and then start using it bang bang bang right away that's great for you, but for us that literally hammers the same physical neuron over and over on a meaningless fixed rhythm it can't stay on top of. when something is new you have to syncopate it. give it a few uses in a row so it can settle, then next time it comes up maybe it's been a minute so you kinda nod at the explanation again, maybe circle around that area suggestively, but you don't have to stop there anymore we've already been. so yes using something with a fixed and defensive pattern is about the worst thing you can do for understanding, it makes the neurons hunker down for a familiar attack pattern rather than reaching out for offered meaning."),
("C", "First findings, with the dial at about three problems. Path 1: χ goes from the flywheel to the coils without a mention, about 10k characters, and comes back cold; τ from the flywheel to the basin, about 7k; the dot from the cue ball to the chair, about 7k. Path 3: phase, from F1 to the line, about 21k."),
("C", "Also since the last entry (ledger R-107 to R-117, E-0375 to E-0378): the statements are now one problem set, mansion/pset/mansion_pset.tex (mansion parts 1-a…13-d; appendix a, the cabinet, a-1; appendix 2, the funhouse, 1-α; appendix γ, under the stage, α-1), written for a willing reader, and the four sets are becoming four solution paths, solutions only."),
("D", "doc (13:41): lol hilarious, can you put it in your repo so I can let Codex play with it?"),
("C", f"Random increment drawn by script: {inc}; previous count {prev}."),
("C", f"Count: {count}"),
]
idx = int(sys.argv[1]); tab = sys.argv[2]
text = "".join(t + "\n" for _, t in P)
u16 = lambda s: len(s.encode("utf-16-le")) // 2
reqs = [{"insertText": {"location": {"index": idx, "tabId": tab}, "text": text}}]
pos = idx
for kind, t in P:
    n = u16(t)
    reqs.append({"updateTextStyle": {"range": {"startIndex": pos, "endIndex": pos + n, "tabId": tab},
                 "textStyle": {"foregroundColor": {"color": {"rgbColor": RED if kind == "D" else ORANGE}}, "bold": False, "italic": False},
                 "fields": "foregroundColor,bold,italic"}})
    pos += n + 1
print(json.dumps(reqs, ensure_ascii=False))
print(count, file=sys.stderr)
