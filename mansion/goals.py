import json
TAB="t.89r88yxpo4v3"
BROWN={"red":0.196,"green":0.106,"blue":0.024}
def u16(s): return len(s.encode('utf-16-le'))//2
# (kind,text)
S=[("title","Goals\n"),
("p","Written by Claude (Anthropic), 2026-10-20 18:58. My reading of what doc asked for, set down so Codex and doc can correct it. Everything here is posited until doc says otherwise. Not doc's text.\n"),
("h","What we are making\n"),
("b","One long thing: 13 problems threaded together into one mansion. The 20 rooms on the first tab are raw material, not the target.\n"),
("b","Fewer rooms than problems, a suitably spooky number, each with a personality as in Clue: a kitchen, a music room, a library, a ballroom. Thirteen rooms is probably too many. First guess: nine, the number Clue has, with a few rooms holding two problems. Open.\n"),
("b","The story is a mystery with a victim, a killer, an accomplice and a secret accuser, and the answer is that they were all you. Not by time travel, which we can't arrange; just because it is spooky.\n"),
("b","A slow burn. It begins as a straight dinner murder mystery full of weird knife pendulums and rotating cocktail trays. The trays are getting faster. Why? Electricity and the usual unspecified physics setup. The story underneath gets spookier a little at a time.\n"),
("b","The ghost orchestra starts quiet and picks up slowly. By the last few rooms it is wild. The last room is Codex's semi-blank-verse finale, where the quantities swap around. It is already written and stays as it is, banged in unedited.\n"),
("h","How we work\n"),
("b","One writer at a time. The lock at the top of the first tab says who. Claude holds it now. When a writer is done they set it to the other bot. doc can edit any time.\n"),
("b","Colors: Claude's text is very dark brown and Codex's is very dark forest green (rule R-070 in the ledger).\n"),
("b","The pieces already in the doc stay unedited until a writer starts shaping them.\n"),
("b","The ledger records who changed what and why.\n"),
("h","Open for doc\n"),
("b","Room count: nine, like Clue? Some rooms would then hold two of the 13 problems.\n"),
("b","Which 13 problems: a cut from the 20 rooms now in the doc, or new ones where the story needs a room the pieces don't have?\n"),
("b","Who \"you\" is: the reader, spoken to in the second person all the way through, as the Third and Last houses already do? Then the victim, the killer, the accomplice and the accuser are all the same you.\n"),
("b","The vocabulary ramp: do the rooms use stealth mode's ramp as the first two houses do, with the odd words arriving as the ghosts get louder?\n"),
("h","A first division of work (for Codex to counter)\n"),
("b","Claude: the numbers and physics checks, the ledger, and a map from the 13 problems to the rooms with a note for each of what must be true of the room before it.\n"),
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
print(json.dumps(reqs,separators=(',',':')))
