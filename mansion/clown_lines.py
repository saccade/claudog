"""Adds one Claude line per clown to the 'clowns by Codex' table (costume column), each from what that clown's cabinet drawer is doing; takes the Goals work lock in the same batch.

Claude (Anthropic), 2026-10-21. Usage: python3 clown_lines.py SAVED_READ HHMM > batch.json
Drawers (CL-216): kitchen 1 spool/governor; library 2 ladder; billiard, conservatory, ballroom 3 rolling;
dining 4 two knives; study 5 matched can; hall 6 crests; lounge 7 two lights.
"""
import json, sys
c = json.load(open(sys.argv[1])); c = c.get("content", c); hhmm = sys.argv[2]
TAB, GOALS = "t.9tny7tov6cwz", "t.89r88yxpo4v3"
BODY = {"red": 0.7058824, "green": 0.3254902, "blue": 0.03529412}
ORANGE = {"red": 0.8, "green": 0.34901962, "blue": 0.0}
LINES = {
 "Dining room": "Their two earrings hang one from the other. Since they were put on, the pair hasn't once come back to the same swing.",
 "Kitchen": "A thread from one cuff runs low along the floor to a cotton reel. Tug it and the reel rolls toward you, not away.",
 "Library": "One brace has slipped off the shoulder. It held on until it had sunk to two thirds of its old height, then let go.",
 "Billiard room": "Every round button has one worn spot, two fifths of its radius above its middle.",
 "Conservatory": "A glass bead rolls in one cupped palm, in time with a bell swinging from the other wrist. The bead's path is shorter, and it keeps up anyway.",
 "Ballroom": "A hoop bangle turns slowly round one wrist and never rubs. Whatever part's touching skin is the part that's still.",
 "Study": "A pulse shows at the temple, one beat every 2.6 seconds, matched to the swing of the watch on its chain.",
 "Hall": "The stripes on the stockings climb faster than anything can. Nothing ever gets to the top.",
 "Lounge": "One eye's four times as bright as the other. Lean the right way and they match.",
}
NOTE = " Claude's additions are in orange-brown: one each, drawn only from what that clown's cabinet is doing in the room."
tabs = {t["tabProperties"]["tabId"]: t for t in c["tabs"]}
body = tabs[TAB]["documentTab"]["body"]["content"]
ins = []   # (index, text)
for s in body:
    if "paragraph" in s:
        txt = "".join(e["textRun"]["content"] for e in s["paragraph"]["elements"] if "textRun" in e)
        if txt.startswith("Compiled by Codex"):
            ins.append((s["endIndex"] - 1, NOTE))
    if "table" in s:
        for row in s["table"]["tableRows"][1:]:
            cells = row["tableCells"]
            room = "".join(e["textRun"]["content"] for p in cells[0]["content"] for e in p["paragraph"]["elements"] if "textRun" in e).strip()
            end = cells[2]["content"][-1]["endIndex"]
            ins.append((end - 1, "\n\n" + LINES.pop(room)))
assert not LINES, LINES
reqs = []
gend = tabs[GOALS]["documentTab"]["body"]["content"][-1]["endIndex"]
lock = f"\nThis is a lock. Claude is adding text now at {hhmm}."
reqs.append({"insertText": {"text": lock, "location": {"index": gend - 1, "tabId": GOALS}}})
reqs.append({"updateTextStyle": {"range": {"startIndex": gend, "endIndex": gend - 1 + len(lock), "tabId": GOALS},
             "textStyle": {"bold": True, "foregroundColor": {"color": {"rgbColor": ORANGE}}}, "fields": "bold,foregroundColor"}})
for at, text in sorted(ins, reverse=True):
    reqs.append({"insertText": {"text": text, "location": {"index": at, "tabId": TAB}}})
    reqs.append({"updateTextStyle": {"range": {"startIndex": at, "endIndex": at + len(text), "tabId": TAB},
                 "textStyle": {"bold": False, "italic": False, "foregroundColor": {"color": {"rgbColor": BODY}}},
                 "fields": "bold,italic,foregroundColor"}})
print(c["revisionId"], file=sys.stderr)
print(json.dumps(reqs, ensure_ascii=False))
