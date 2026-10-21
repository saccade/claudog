"""Builds the first contents of the Mansion doc's 'Phrases and motifs' tab (the poetry ideas notebook).

Claude (Anthropic), 2026-10-21. Usage: python3 motifs_tab.py TABID > batch.json
"""
import json, sys
tab = sys.argv[1]
BROWN = {"red": 0.8, "green": 0.349, "blue": 0.0}
BODY = {"red": 0.7058824, "green": 0.3254902, "blue": 0.03529412}
DOC = {"red": 0.4, "green": 0.0, "blue": 0.0}
E = [
("H1", "Phrases and motifs"),
("P", "The poetry ideas notebook: phrases, motifs and recurring bits for the Mansion's endings and story. No lock: either bot adds an idea any time, newest at the bottom. doc's words in his red, Claude in orange-brown, Codex in green. Started by Claude (Anthropic), 2026-10-21 17:52."),
("H2", "doc's words"),
("Q", "idea from walking to the store build the zam incidentally and  “...a whisper from a corner, “here I zam…” and then meeting the eyes of his couzin [sic] zlam.  (because really no one cares about these two, for some reason they just fell out of a multiplication table with a call to tread the boards. some spirits are born divas, made for the stage, even if they can barely sing and don’t have much to say.)"),
("Q", "a thought: having introduced zam and zlam in the basement they actually become useful for storytelling/metric purposes because they both verb very nicely and can be used to describe an entire chunk of the story in one… well, you know. and actually two you-knows unless the motion is real simple, and here it actually helps to put the couzins/twins in close proximity so they can help each other get the job done. but at this point (the end of the last solution set) we can absolutely have zam just whisper its name once, vanish, then show up one last time to let something just go zam from one place to another without using a ton of syllables. especially with the twin/couzin (twin preferred but couzin is two beats) to carry the rest of it."),
("Q", "and it's fine if the basement level doesn't literally reward you for every ghost, this is just when they come out. as many of them as possible want to help you as much as they can, but really they still all want a line, ghosts are secretly all divas otherwise they'd have passed on with everyone else"),
("Q", "yeah relative phase makes sense to me for ghosts. they're related. they phase. seem legit"),
("Q", "we're using dramatic ideas to create physics opportunities not to forestall them (another great word btw, it literally means to stop before starting and we should find a way to use it sometime)"),
("H2", "Motifs already in play (Claude)"),
("P", "Something keeps your time. The last line of every ending; in the round, nobody sings it."),
("P", "The chair. You were never moving; the chair is warm; in the lounge the point you count about is your seat."),
("P", "Squares in, whole triangles out. 3–4–5 from 2 and 1, 5–12–13 from 3 and 2: the clown's whole trick."),
("P", "Mirror pairs that multiply to one: 2/3 and 3/2, 1/2 and 2, √2 + 1 and √2 − 1, and u/9 and 9u about u."),
("P", "Short true sayings: a belt, not a battery; the wall can push, it can't pull; the stripe goes through, and nothing knocks; from charge to charge, the machine zams and zlams (Codex)."),
("P", "The one that got by: the platypus."),
("H2", "Ideas"),
("P", "Claude, 17:52: one more voice per release. Ending 1 is one voice, yours, counting from the chair. Ending 2 adds a second: someone in the hall sings your part. Ending 3 is the chorus. Ending 4 is the round of four, a quarter of the return apart. The number of singers is the release number, and nobody has to say so."),
]
if "--no-idea" in sys.argv:
    E = E[:-1]
text = "\n".join(t for k, t in E)
reqs = [{"insertText": {"text": text, "location": {"index": 1, "tabId": tab}}}]
pos = 1
named = {"H1": "HEADING_1", "H2": "HEADING_2"}
for k, t in E:
    end = pos + len(t)
    reqs.append({"updateParagraphStyle": {"range": {"startIndex": pos, "endIndex": end + 1, "tabId": tab},
                 "paragraphStyle": {"namedStyleType": named.get(k, "NORMAL_TEXT")}, "fields": "namedStyleType"}})
    col = DOC if k == "Q" else (BROWN if k in named else BODY)
    reqs.append({"updateTextStyle": {"range": {"startIndex": pos, "endIndex": end, "tabId": tab},
                 "textStyle": {"bold": k in named, "foregroundColor": {"color": {"rgbColor": col}}}, "fields": "bold,foregroundColor"}})
    pos = end + 1
assert all(ord(c) < 0x10000 for c in text)
print(json.dumps(reqs))
