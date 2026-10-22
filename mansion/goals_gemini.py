"""Goals entry: Claude's check of Gemini's review, as a checklist (2026-10-22 15:5x). Usage: python3 goals_gemini.py INDEX PREV"""
import json, random, sys
ORANGE = {"red": 0.8, "green": 0.34901962, "blue": 0.0}
idx = int(sys.argv[1]); prev = int(sys.argv[2]); inc = int(sys.argv[3]) if len(sys.argv) > 3 else random.randint(3, 7)
count = prev + inc
if count > 72: count -= 36
P = [
("B", "Claude — Gemini's review, checked"),
("C", "Gemini's memo claims one error, and it isn't one. Three of its points are right and need nothing. Its continuity section invents one connection. Tick as you go."),
("X", "13-c against α-3, the “energy discrepancy”: not real. At T/2 the arguments are 4π and 9π, so the cosines are +1 and −1, and q/q₀ = 9/13 − 4/13 = 5/13 in both places. The capacitor holds 25/169 of the 80 mJ (14.8%) and the rods the other 144/169. Gemini's 9/13 comes from evaluating the cosines wrong. Path 1 and Codex's checker both have 5/13. Nothing to change."),
("X", "The spool's grip: right. 4.4 N of grip on a 20 N normal force needs μ of at least 0.22, an ordinary counter. Gemini quotes a line about “enough static friction” that isn't in the statement, which only says the spool rolls without slipping; that's all it needs. Nothing to change.".replace("center enough", "enough")),
("X", "κ from 2-β: right. κ = (5/6)ω₀√(ηL) puts the two modes at ⅔ω₀ and ¾ω₀…".replace("¾", "3/2 ").replace("⅔", "2/3 ").replace("…", ", as the set intends. Nothing to change.")),
("X", "Knife to basin: right. The basin's 5/7 m arc is what makes the rolling ball keep the knife's period."),
("X", "Ribbon to lights: wrong. Problem 12 has no swirl and no billiard table, and nothing in the light pair is the puck's angular momentum. Don't use it."),
("X", "Line to chair: an analogy, not a link. The line's currents cancel where two pulses overlap; the chair starts with no current because it's charged and then closed that way. Don't build on it."),
("X", "What it missed: the two real wording items from Codex's check (11-c's factor crests, the cue's table impulse) and the f-4 reverse question. Those still wait for you at the sweep."),
]
lines = [t for _, t in P] + [f"Random increment drawn by script: {inc}; previous count {prev}.", f"Count: {count}"]
text = "".join(t + "\n" for t in lines)
u16 = lambda s: len(s.encode("utf-16-le")) // 2
reqs = [{"insertText": {"location": {"index": idx - 1, "tabId": "t.89r88yxpo4v3"}, "text": "\n" + text[:-1]}},   # the tab ends in doc's paragraph
        {"updateTextStyle": {"range": {"startIndex": idx, "endIndex": idx + u16(text) - 1, "tabId": "t.89r88yxpo4v3"},
         "textStyle": {"foregroundColor": {"color": {"rgbColor": ORANGE}}, "bold": False, "italic": False}, "fields": "foregroundColor,bold,italic"}},
        {"updateTextStyle": {"range": {"startIndex": idx, "endIndex": idx + u16(P[0][1]), "tabId": "t.89r88yxpo4v3"},
         "textStyle": {"bold": True}, "fields": "bold"}}]
pos = idx; first = last = None
for kind, t in P:
    if kind == "X":
        if first is None: first = pos
        last = pos + u16(t)
    pos += u16(t) + 1
reqs.append({"createParagraphBullets": {"range": {"startIndex": first, "endIndex": last, "tabId": "t.89r88yxpo4v3"}, "bulletPreset": "BULLET_CHECKBOX"}})
print(json.dumps(reqs, ensure_ascii=False)); print(count, file=sys.stderr)
