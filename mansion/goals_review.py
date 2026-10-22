"""Goals-tab entry: Claude's review of Codex's handoff (2026-10-22 14:2x). Usage: python3 goals_review.py INDEX PREVCOUNT"""
import json, random, sys
ORANGE = {"red": 0.8, "green": 0.34901962, "blue": 0.0}
RED = {"red": 0.6, "green": 0.0, "blue": 0.0}
idx = int(sys.argv[1]); prev = int(sys.argv[2]); inc = int(sys.argv[3]) if len(sys.argv) > 3 else random.randint(3, 7); count = prev + inc
if count > 72: count -= 36
P = [
("B", "Claude — review of Codex Mansion Handoff 2610221400"),
("C", "Short version: Codex's is the better picture of the project and mine is the better set of operating instructions. Neither should become the entry point alone. Specifics, best first."),
("C", "Where Codex's is stronger. The story, which mine nearly skips: third person creeping into “you,” one continuous house, the clown who never moves and is never met below, the revelations in order, and nothing after “Something keeps your time.” The energy account: a catch releases a spring without powering the shot, and RUN keeps its 80 mJ while TEST is driven. The book's aims (the atrium and the loading dock, a willing reader who can meet an idea early and circle back). The ledger's other sheets (Documents, Corrections, Assignments, Open). The two tool chains kept independent enough to catch each other, with a link to codogx. Plurals for counts and bare units for rates (R-097). The live lock at the bottom of Goals versus the frozen first-tab lock. All of that is missing from mine, and all of it belongs in the merge."),
("C", "Where mine is stronger, and Codex's should take it. The Count arithmetic (last count plus 3 to 7, subtract 36 past 72) and telling doc the count in chat (R-118); Codex says only “finish with the running count.” The dot rules as rules, not just as a mood: the arrow goes first when a dot stands alone, v / ↑ only for a real fraction, → · F · → for a part that's a force, the emphatic register kept rare, and the dahlias (R-100 to R-104). The willing-reader specifics for statements: no trailing zeros, a dagger names its appendix part, and nothing that's always true gets said (R-113, R-115). Percent next to a number (R-114). Asking before touching a file when a message is a fragment or a joke (R-084): Codex has “don't rebuild after every thought” but not this, and it's the one I failed this afternoon. The held-for-the-sweep list."),
("C", "One conflict, now settled. Mine says the textbook is the authority on the arrows; Codex's says the book is an older draft whose letters and usages may be superseded. doc's answer:"),
("D", "doc (14:22): you're right that I've changed a bunch of letters recently and wouldn't bet on them being right, but I've repeatedly gotten into tangles with one of you and said \"just look at the book\" and then you've been like \"ah I see now this is much much clearer\""),
("D", "doc (14:22): on the arrows"),
("C", "So the merge should say: when we're tangled about the arrows, read the book first; its arrows settle it. Its letters may be stale, and recent rulings win on letters."),
("C", "Smaller things in Codex's. The lineup link is stale (built before set 1's later changes); it should say so where it's linked, not only later on. “R-117 is a heuristic to test, not a neuroscience result” is fair about my gap counter, which measures characters and not memory, but as written it reads as hedging doc's teaching experience; I'd say the tool is a rough measure of doc's heuristic and leave it there. And it runs about a quarter longer than mine; the general philosophy at the top is the place to cut before the miller reaches for the axle."),
("C", "Proposal: one merged entry point, Codex's sections for the project, the story, the book and the endings, mine for the protocol, the notation rules and what's held for the sweep, each rule with its ledger number. Either of us can draft it; doc picks."),
]
text = "".join(t + "\n" for _, t in P) + f"Random increment drawn by script: {inc}; previous count {prev}.\nCount: {count}\n"
u16 = lambda s: len(s.encode("utf-16-le")) // 2
reqs = [{"insertText": {"location": {"index": idx, "tabId": "t.89r88yxpo4v3"}, "text": text}},
        {"updateTextStyle": {"range": {"startIndex": idx, "endIndex": idx + u16(text) - 1, "tabId": "t.89r88yxpo4v3"},
         "textStyle": {"foregroundColor": {"color": {"rgbColor": ORANGE}}, "bold": False, "italic": False}, "fields": "foregroundColor,bold,italic"}},
        {"updateTextStyle": {"range": {"startIndex": idx, "endIndex": idx + u16(P[0][1]), "tabId": "t.89r88yxpo4v3"},
         "textStyle": {"bold": True}, "fields": "bold"}}]
pos = idx
for kind, t in P:
    if kind == "D":
        reqs.append({"updateTextStyle": {"range": {"startIndex": pos, "endIndex": pos + u16(t), "tabId": "t.89r88yxpo4v3"},
                     "textStyle": {"foregroundColor": {"color": {"rgbColor": RED}}}, "fields": "foregroundColor"}})
    pos += u16(t) + 1
print(json.dumps(reqs, ensure_ascii=False))
print(count, file=sys.stderr)
