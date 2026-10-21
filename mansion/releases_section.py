"""Builds the 'Four releases' section for the Mansion map (CL-213).

Claude (Anthropic), 2026-10-21. Usage: python3 releases_section.py START > batch.json
"""
import json, sys
BROWN = {"red": 0.361, "green": 0.239, "blue": 0.18}
H = "Four releases: words by level (doc, 15:42; Claude's draft)"
P = [
("", "", "Published one at a time, like a game with free downloadable levels. Each release unlocks a fuller ending, with more of the cast singing as you find what was obviously your seat all along. Each ending uses only the words its levels brought in. Each release shows the next door but doesn't open it. Three is the number everyone expects, so the fourth is where the real tricks go."),
("L", "Level 1, the mansion (the base game, 13 problems).", ""),
("I", "New words, each where it lands:", " the turn, with 2π thrown away (dining room, the knife); the sweep (the knife); χ for torque once the kitchen knife cuts the τ off (kitchen); sentences the right way round, \"current is the conductance of the voltage\" and \"power is the voltage of the current\" (study, the RC); own time for proper time (lounge). Only the worst naming problems get fixed; 13 short problems leave no time for more."),
("I", "Ghosts:", " the friendly ones only: velocity, acceleration, the sweep, the center of mass."),
("I", "Ending 1:", " the orchestra form of the first two old houses, about half standard: the energy accounted for, everything moving at once, the mass canceled before a number went in, the chair, and \"Something keeps your time.\""),
("I", "Hint of the next door:", " every room's cabinet is in plain sight, locked."),
("L", "Level 2, the clown's cabinet (patch 1, 7 drawers).", ""),
("I", "New words:", " punch, hook and heft (drawer 2, the ladder's energy split; drawer 3, rolling); profile (drawers 1 and 3: the spool, the 7/5); pickup, and crank as a verb (drawer 1); spin (drawer 3, the cue); can and coil (drawer 5)."),
("I", "Ghosts:", " profile and pickup join the friendly ones."),
("I", "Ending 2:", " the third old house's form, flashier: short sentences, the quantities verbed (the assembly hooks, the center punches, the heft gives way), down to \"From the hall, someone sings your part.\" before the chair."),
("I", "Hint of the next door:", " a draft through each drawer's back panel; the passage is painted shut."),
("L", "Level 3, the funhouse (patch 2, 4 problems).", ""),
("I", "New words:", " tone, chord and beat, and the shape with Ω's first appearance as Ω_shape (F1); the trade between the rods and the loop, a belt and not a battery (F2); phase, for ghosts only, with the stripe as a ghost body, and shift and stretch for the light factors (F3); the still point as a ghost body, with zip and zing (F4)."),
("I", "Ghosts:", " the scary ones start here, but not all of them: zip, zing, the stripe, the still point, and Ω on every one."),
("I", "Ending 3:", " the Last House chorus, verbatim. It looks like it couldn't possibly hold more."),
("I", "Hint of the next door:", " trapdoors in the funhouse floor, humming, nailed down."),
("L", "Level 4, the understage (patch 3, 2 problems).", ""),
("I", "New words:", " the rotor as the name of the coupled rods-and-loop machine, with zlug and zlow because both kinds are about at once (U1); in step, at random, and the tap (U2)."),
("I", "Ghosts:", " the rate ghosts join, and everyone's there."),
("I", "Ending 4:", " the chorus as a round, four voices a quarter turn of the drum apart, the added stanza before \"The rods are still.\", each voice falling silent in its own time, and \"Something keeps your time.\" held until the last one stops. This is where the seat is obviously yours."),
("I", "Hint:", " none. It's the last door."),
("", "", "Open: Codex's pass (Goals, Count 57) proposes a fourth line for the stanza, \"The knife comes home between the beats.\", and staging for the round. Its statement repairs to CL-214 and CL-216 are next."),
]
start = int(sys.argv[1])
lines = [H] + [l + t for k, l, t in P]
text = "\n" + "\n".join(lines)
reqs = [{"insertText": {"text": text, "location": {"index": start}}}]
s0 = start + 1; h1 = s0 + len(H); tend = start + len(text)
reqs += [{"deleteParagraphBullets": {"range": {"startIndex": s0, "endIndex": tend}}},
 {"updateParagraphStyle": {"range": {"startIndex": s0, "endIndex": h1}, "paragraphStyle": {"namedStyleType": "HEADING_2", "indentStart": {"magnitude": 0, "unit": "PT"}, "indentFirstLine": {"magnitude": 0, "unit": "PT"}}, "fields": "namedStyleType,indentStart,indentFirstLine"}},
 {"updateParagraphStyle": {"range": {"startIndex": h1 + 1, "endIndex": tend}, "paragraphStyle": {"namedStyleType": "NORMAL_TEXT", "indentStart": {"magnitude": 0, "unit": "PT"}, "indentFirstLine": {"magnitude": 0, "unit": "PT"}}, "fields": "namedStyleType,indentStart,indentFirstLine"}},
 {"updateTextStyle": {"range": {"startIndex": s0, "endIndex": h1}, "textStyle": {"bold": True, "italic": False, "foregroundColor": {"color": {"rgbColor": BROWN}}}, "fields": "bold,italic,foregroundColor"}},
 {"updateTextStyle": {"range": {"startIndex": h1 + 1, "endIndex": tend}, "textStyle": {"bold": False, "italic": False, "foregroundColor": {"color": {"rgbColor": {"red": 0, "green": 0, "blue": 0}}}}, "fields": "bold,italic,foregroundColor"}}]
pos = h1 + 1
for (k, l, t), ln in zip(P, lines[1:]):
    if l:
        reqs.append({"updateTextStyle": {"range": {"startIndex": pos, "endIndex": pos + len(l)}, "textStyle": {"bold": True}, "fields": "bold"}})
    if k == "I":
        reqs.append({"updateParagraphStyle": {"range": {"startIndex": pos, "endIndex": pos + len(ln)}, "paragraphStyle": {"indentStart": {"magnitude": 18, "unit": "PT"}, "indentFirstLine": {"magnitude": 18, "unit": "PT"}}, "fields": "indentStart,indentFirstLine"}})
    pos += len(ln) + 1
assert pos - 1 == tend and all(ord(c) < 0x10000 for c in text)
print(json.dumps(reqs, ensure_ascii=False))
