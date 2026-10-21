"""Builds a Goals-tab entry (Claude's colors, doc's quotes in his red) for the frozen Mansion doc.

Claude (Anthropic), 2026-10-21. Usage: python3 goals_entry.py START TABID > batch.json
Paragraph kinds: H (heading, orange, bold), P (body, orange-brown), Q (doc's words, red).
"""
import json, sys
ORANGE = {"red": 0.8, "green": 0.34901962, "blue": 0.0}
BODY = {"red": 0.7058824, "green": 0.3254902, "blue": 0.03529412}
DOC = {"red": 0.4, "green": 0.0, "blue": 0.0}
E = [
("H", "Claude — where things stand, for Codex, 2026-10-21"),
("P", "Claude (Anthropic), 2026-10-21 14:55. Welcome back. A lot moved while you rested. dr. kraemer directed all of it, and it's recorded in the map (CL-213), the top-level problems (CL-214) and a new doc for everything below the mansion: Claude Mansion below stairs 2610211420 (CL-216), https://docs.google.com/document/d/1JFD4v5o3lWCYg4KoXnzQ0d3EGUxk_e2iAJdt3gg_Y44. The short version:"),
("P", "1. Fewer problems the deeper you go: 13 in the mansion, 7 cabinet drawers, 4 funhouse problems, 2 in the understage. The levels hide complexity; they don't add it. His words:"),
("Q", "the idea is using this to hide complexity not finding complex things to add"),
("P", "2. Four final answers, one per depth reached, each using only the words its levels brought in and each more choral than the last. Version 1 is about half standard: turns, and sentences that run the right way round. Version 2 is peppier, in your third house's short-sentence form. Version 3 is your Last House chorus, verbatim: the penultimate. Version 4 is the same chorus sung as a four-voice round, voices a quarter turn apart, with one added stanza. I drafted that stanza for you to argue with; it's in the map under \"Four final answers\". The verse is yours."),
("P", "3. The clown stands at the point you count about in each room, never moves, never faces you, and isn't anywhere below the mansion. In the lounge they finally look at you; the chair is warm and there's no one else around. The understage is plain machinery humming under the whispers. Beats that line up exactly are the dangerous ones, and irrational ratios are the safe kind. His words:"),
("Q", "the clown only has to tap things ahead when a bunch of them are gonna line up at once and cause a big shock to reality. you know that was how we ended up with the platypus. clown was asleep on the trigger, something got by."),
("P", "4. House style: American spelling, and contractions by default, with the full form saved for emphasis, about one in ten. The rotor survives only as a name for the coupled rods-and-loop matrix."),
("P", "5. Drafted and checked (claudog mansion/below_check.py): all 7 cabinet drawers, each with a standard statement, a solution in the cabinet's words and a passage to its funhouse problem. Not drafted yet: the 4 funhouse problems, the 2 understage problems, and final answers 1 and 2, which are mine."),
("P", "Asks for Codex, in whatever order suits you: (a) an independent check of CL-214's statements and CL-216's drawers, statements especially; (b) the verse for version 4; (c) push back on the funhouse and understage plan in the map's \"pared plan\" section before I draft them. No manuscript edits; the freeze stands."),
("P", "Count: 51"),
]
start, tab = int(sys.argv[1]), sys.argv[2]
text = "\n\n" + "\n".join(t for k, t in E)
reqs = [{"insertText": {"text": text, "location": {"index": start, "tabId": tab}}}]
pos = start + 2
for k, t in E:
    end = pos + len(t)
    col = {"H": ORANGE, "P": BODY, "Q": DOC}[k]
    reqs.append({"updateTextStyle": {"range": {"startIndex": pos, "endIndex": end, "tabId": tab},
                 "textStyle": {"bold": k == "H", "italic": False, "foregroundColor": {"color": {"rgbColor": col}}},
                 "fields": "bold,italic,foregroundColor"}})
    pos = end + 1
assert pos - 1 == start + len(text)
print(json.dumps(reqs, ensure_ascii=False))
