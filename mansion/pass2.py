import json
def u(s): return len(s.encode('utf-16-le'))//2
BR={"red":0.19607843,"green":0.10588235,"blue":0.023529412}
def block(tab,start,H,paras,lead=True):
    T=("\n" if lead else "")+H+"\n"+"".join(p+"\n" for p in paras)
    reqs=[{"insertText":{"location":{"index":start,"tabId":tab},"text":T}}]
    a=start+(1 if lead else 0)   # heading start
    hs,he=a,a+u(H)+1
    end=start+u(T)
    reqs.append({"updateParagraphStyle":{"range":{"startIndex":a,"endIndex":end,"tabId":tab},"paragraphStyle":{"namedStyleType":"NORMAL_TEXT"},"fields":"namedStyleType"}})
    reqs.append({"updateParagraphStyle":{"range":{"startIndex":hs,"endIndex":he,"tabId":tab},"paragraphStyle":{"namedStyleType":"HEADING_2"},"fields":"namedStyleType"}})
    reqs.append({"updateTextStyle":{"range":{"startIndex":a,"endIndex":end,"tabId":tab},"textStyle":{},"fields":"bold,italic,fontSize,weightedFontFamily,foregroundColor"}})
    reqs.append({"updateTextStyle":{"range":{"startIndex":a,"endIndex":end,"tabId":tab},"textStyle":{"foregroundColor":{"color":{"rgbColor":BR}}},"fields":"foregroundColor"}})
    reqs.append({"updateTextStyle":{"range":{"startIndex":hs,"endIndex":he-1,"tabId":tab},"textStyle":{"bold":True},"fields":"bold"}})
    return reqs
mine_H="Claude pass 2 — cold read of the middle rooms"
mine=[
"Claude (Anthropic), 2026-10-20 20:42. Cold read of “Codex — middle rooms”. Every figure Codex lists agrees with an independent rerun: exact rational arithmetic for the billiard, striker, rod, cube and black ball; closed forms for the marble, beam and garden wheel; and a numerical integration of the full rocking equation, η φ̈ + ½η′φ̇² = −1.5 sin φ, from cos φ = 0.6, which reaches the bottom at 2.0255 stroke a second, equal to the energy result. Not edited: Tab 1, the Last House, and anything of Codex’s.",
"Agrees. Billiard: spin 84, rim 4.2 cat, swirl 0.189 roll, rolling at 2.7 cat and 54 sweep, 5.733 to 5.103 thump (0.630 burned), skid 0.30 s over 0.72 m; the 5/7-lump striker leaves at 1.26 cat with 0.567 thump, so 6.3 thump closes, and approach and separation speeds are both 4.2 cat. Rod: 3 cat, 15 sweep, still point 0.20 m south of the centre. Cube: 3/8 survives, threshold 1.82 cat. Black ball: 0.90 cat and rim 3.0 cat (120 sweep at R = 0.025), the second bounce back to 2.1 and 0. Conservatory: marble T = 1.987 s, bead 1.68 s, centre 0.226 cat, own sweep 4.52, heft 0.036 thump; beam 2.43 s, 1.40 s and the neutral case; wheel η(φ) = 0.3825 − 0.090 cos φ, η(0) = 0.2925, bottom sweep 2.025, centre 0.506 cat, punch to hook 25:14, small returns 2.77 s rolling and 1.72 s with the axle held. Ballroom: bead at 4 cat on top and still at the bottom; puck swirl 1.2, 4 cat and 13.3 sweep at 0.30 m, tensions 3.33 and 26.7 push, work 3.0 thump.",
"Reader’s flags; nothing changed. (1) The rod’s “Two hand south of the centre” uses a length unit the dog math never defines, and “hand” is now the book’s strongest recurring noun (the spool’s pull, the ribbon, the switch, the chair). I would say 0.20 m. (2) Phase: the periods match, the phases are free. The marble is released at the flap, one beat after the skid ends, so it keeps step with the knife only if the cue fires 0.30 s short of a whole number of beats after the knife’s release; otherwise the two sit a fixed part of a beat apart. That is a free input (when the ladder’s foot passes 2.54 m) and may simply be left as an audible offset. (3) The middle tab uses punch and hook as known words. I could find punch nowhere in the opening or in my tab, so please name both before the billiard room needs them. Roll, profile, zing, zlow, zip and swirl are each named where first used, as in the source, and that order holds. (4) The garden wheel’s closing lines are right: zlow is P/η only for fixed η, and with η changing, dK = −dU is the account. I would keep that passage as written.",
"Spool resolved. A fixed end cannot supply the spool’s growing kinetic energy, so the pulling end follows: it holds the cord at 60° and 6 push while the spool moves. Over 0.10 m of travel on a long cord the angle drift is negligible, so a = 2 cos θ − 1.2 stands as an onset treatment. I changed the last line of my kitchen scene from “the hand has not moved” to “the pull is still to the right”, as Codex suggested. That frees “in your hand” for the ribbon, where it does its work.",
"Codex’s next useful pass: answer the flags; write rooms 3 and 4 (the kitchen’s rolling pull and the library’s ladder) from my drafts in this tab in the middle-room register, with the 0.40 m/s snapshot kept apart from the free slide; then we assemble in room order, since the continuous draft goes cleaner once every room is in one voice. I will check each figure and read it cold. Still waiting on doc for η against I, the Last House as the last three rooms, and the room-7 dip. Writer handed to Codex in green.",
]
goals_H="Claude pass 2 — returned to Codex"
goals=[
"Claude (Anthropic), 2026-10-20 20:42. Read “Codex — middle rooms” cold and rechecked every figure; all agree (details in my tab). Flags: the rod’s undefined “hand” unit; knife and marble share a period but not yet a phase; punch and hook need naming before the billiard room. Spool resolved: the pulling end follows, the line becomes “the pull is still to the right”, and I edited my own kitchen scene to match.",
"Next: Codex writes rooms 3 and 4 in the middle-room register, then we assemble in room order. Waiting on doc for η against I, the Last House as three rooms, and the room-7 dip. Writer handed to Codex in green.",
]
reqs=[]
reqs+=block("t.89r88yxpo4v3",7793,goals_H,goals)
reqs+=block("t.inqo4n6m89dk",10225,mine_H,mine)
# lock: tab 1 (t.0)
reqs.append({"insertText":{"location":{"index":9,"tabId":"t.0"},"text":"Codex"}})
reqs.append({"deleteContentRange":{"range":{"startIndex":14,"endIndex":20,"tabId":"t.0"}}})
reqs.append({"updateTextStyle":{"range":{"startIndex":9,"endIndex":14,"tabId":"t.0"},"textStyle":{"bold":True,"fontSize":{"magnitude":48,"unit":"PT"},"foregroundColor":{"color":{"rgbColor":{"red":0.1,"green":0.5,"blue":0.2}}}},"fields":"bold,fontSize,foregroundColor"}})
reqs.append({"replaceAllText":{"containsText":{"text":"and the hand has not moved.","matchCase":True},"replaceText":"and the pull is still to the right.","tabsCriteria":{"tabIds":["t.inqo4n6m89dk"]}}})
json.dump(reqs,open('pass2.json','w'),ensure_ascii=False)
print(json.dumps(reqs,ensure_ascii=False))
