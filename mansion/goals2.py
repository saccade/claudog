import json
TAB="t.89r88yxpo4v3"
BROWN={"red":0.196,"green":0.106,"blue":0.024}
def u16(s): return len(s.encode('utf-16-le'))//2
# (kind,text)
S=[("title","Goals\n"),
("p","Written by Claude (Anthropic), 2026-10-20 19:10. My reading of what doc asked for, updated with his answers of 19:02. Posited until doc says otherwise. Not doc's text.\n"),
("h","What we are making\n"),
("b","One long thing: 13 problems threaded together into one mansion of nine rooms. The 20 rooms on the first tab are raw material. Doc calls them excellent, and they probably have redundancies and places to tighten, so getting from 20 to 13 is part of the work.\n"),
("b","The nine rooms are Clue's: kitchen, dining room, ballroom, billiard room, library, study, lounge, conservatory, hall. Each has a personality. Some hold two problems.\n"),
("b","The rooms affect each other. Things travel between rooms and cause things in later rooms, as far as can be arranged: a result in one room is an input in another. The pieces already do this inside a house (Second House 1 into 3; Last House 1 into 2 into 5). The new work is doing it across houses.\n"),
("b","The story is a mystery with a victim, a killer, an accomplice and a secret accuser, and the answer is that they were all you. Not by time travel, which we can't arrange; just because it is spooky.\n"),
("b","A slow burn. It begins as a straight dinner murder mystery full of weird knife pendulums and rotating cocktail trays. The trays are getting faster. Why? Electricity and the usual unspecified physics setup. The story underneath gets spookier a little at a time.\n"),
("b","The \"you\" is not there at first. It comes in gradually with the ghosts: first it reads like a small error in the style, and then it picks up steam, like a sweater in the dryer (a flat start, then a steep climb).\n"),
("b","The ghost orchestra starts quiet and picks up slowly; by the last few rooms it is wild. The last room is Codex's semi-blank-verse finale, where the quantities swap around. It is already written and stays as it is, banged in unedited.\n"),
("h","How we work\n"),
("b","One writer at a time. The lock at the top of the first tab says who. Claude holds it now. When a writer is done they set it to the other bot. doc can edit any time.\n"),
("b","Colors: Claude's text is very dark brown and Codex's is very dark forest green (rule R-070 in the ledger).\n"),
("b","The pieces already in the doc stay unedited until a writer starts shaping them.\n"),
("b","The ledger records who changed what and why.\n"),
("h","Still open for doc\n"),
("b","Which 13 of the 20 stay, and what gets merged (a first look is below).\n"),
("b","Whether the vocabulary ramps with the ghosts, as in the first two houses. My reading of \"it comes in gradually with the ghosts\" is yes. Say if not.\n"),
("h","First look: overlaps among the 20 (Claude's guess, for Codex to argue with)\n"),
("b","Contact torque on a rolling body: the yo-yo on the slope (Haunted 4) and the spool that backs away (Third 2) are near twins. The billiard ball (Haunted 5) and the superball (Second 4) both hold spin about a line in the floor.\n"),
("b","The still point of a moving body: the bicycle wheel (Haunted 1), the ball in the ring (Haunted 2) and the ladder that slides (Second 1) all lean on it.\n"),
("b","Rocking and period: the marble in the trough (Second 5), the wheel that comes back (Third 5) and the counterweight upstairs (Third 1) are three versions of a torque-and-period room.\n"),
("b","A blow on a rigid body: the cube meeting a ridge (Haunted 3) and the rod on the ice (Second 2) both turn an impulse into spin.\n"),
("b","The ladder that slides (Second 1) and the ladder that leaves the wall (Second 3) are already one chain and could be one room.\n"),
("h","A first division of work (for Codex to counter)\n"),
("b","Claude: the numbers and physics checks, the ledger, and a map from the 13 problems to the nine rooms with a note for each of what must be true of the room before it.\n"),
("b","Codex: the mystery's spine (who dies, and the order the clues come) and the finale's setup.\n"),
("b","Both: fill the rooms, one writer at a time, passing the lock.\n"),
]
text="".join(t for _,t in S)
reqs=[];i=1
col={"color":{"rgbColor":BROWN}}
rng=lambda a,b:{"tabId":TAB,"startIndex":a,"endIndex":b}
reqs.append({"updateTextStyle":{"range":rng(1,1+u16(text)),"textStyle":{"foregroundColor":col,"weightedFontFamily":{"fontFamily":"Arial","weight":400},"fontSize":{"magnitude":11,"unit":"PT"}},"fields":"foregroundColor,weightedFontFamily,fontSize"}})
bl=[]
for k,t in S:
    a,b=i,i+u16(t)
    if k=="title":
        reqs.append({"updateParagraphStyle":{"range":rng(a,b),"paragraphStyle":{"namedStyleType":"TITLE"},"fields":"namedStyleType"}})
        reqs.append({"updateTextStyle":{"range":rng(a,b),"textStyle":{"foregroundColor":col,"bold":True},"fields":"foregroundColor,bold"}})
    elif k=="h":
        reqs.append({"updateParagraphStyle":{"range":rng(a,b),"paragraphStyle":{"namedStyleType":"HEADING_2"},"fields":"namedStyleType"}})
        reqs.append({"updateTextStyle":{"range":rng(a,b),"textStyle":{"foregroundColor":col,"bold":True,"fontSize":{"magnitude":16,"unit":"PT"}},"fields":"foregroundColor,bold,fontSize"}})
    elif k=="b": bl.append((a,b))
    i=b
# merge consecutive bullet ranges
merged=[]
for a,b in bl:
    if merged and merged[-1][1]==a: merged[-1][1]=b
    else: merged.append([a,b])
for a,b in merged:
    reqs.append({"createParagraphBullets":{"range":rng(a,b),"bulletPreset":"BULLET_DISC_CIRCLE_SQUARE"}})
print(len(text),u16(text))
json.dump(reqs,open('goals_styles.json','w'),separators=(',',':'))

