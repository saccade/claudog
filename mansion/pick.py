import json
TAB="t.89r88yxpo4v3"; START=3600
BROWN={"color":{"rgbColor":{"red":0.19607843,"green":0.10588235,"blue":0.023529412}}}
# (kind, text)  kinds: H heading, B bullet, L label(bold), N numbered-plain, C cutline
P=[
("H","Choosing the 13: how, and Claude's ranking"),
("B","The Last House (5 problems, Codex) stays whole as the finale, unedited. That leaves 8 places for the 15 problems of the first three houses. This is my assumption; say if the finale is smaller."),
("B","The system is a plain ranking. Each of us ranks all 15, 1 for the one we most want to keep. Add the two ranks; the 8 lowest totals stay. A tie at the cut goes to the room with the better single rank; if still tied, doc picks. doc can overrule any of it at any time."),
("B","A dropped room may lend a detail to a kept one. That is for the writers to agree on, outside the ranking."),
("L","Claude's ranking (1 is keep first; the first eight stay)"),
("N","1. String through the floor (Third 4). The engine for the trays getting faster: pull the string in and it spins faster with no push on it."),
("N","2. Counterweight upstairs (Third 1). The knife pendulum; gentle, and early."),
("N","3. Motor that keeps its word (Third 3). The electricity: constant power does not give constant speeding up."),
("N","4. Spool that backs away (Third 2). Pulled one way, it goes the other. The yo-yo is its twin, and the spool is spookier."),
("N","5. Ladder that slides (Second 1). The fall."),
("N","6. Bicycle wheel (Haunted 1). The still point, near the start."),
("N","7. Billiard ball (Haunted 5). It holds its spin about a floor line, which the superball would repeat."),
("N","8. Wheel that comes back (Third 5). The rocker; the one period room kept besides the pendulum."),
("C","--- cut line: the first eight stay ---"),
("N","9. Rod on ice (Second 2). A blow turned into spin; Haunted 3 is its twin."),
("N","10. Cube meets ridge (Haunted 3). The same, the other way round."),
("N","11. Ball in ring (Haunted 2). The still point a third time, with the bicycle wheel and the ladder."),
("N","12. Superball (Second 4). Spin about a floor line, as the billiard ball."),
("N","13. Marble in trough (Second 5). A third torque-and-period room."),
("N","14. Yo-yo (Haunted 4). The spool's twin."),
("N","15. Ladder that leaves the wall (Second 3). The first ladder's twin."),
("L","Codex's ranking (Codex adds it here, the same form, all 15)"),
("B","Not in yet."),
]
text="".join(t+"\n" for k,t in P)
req=[{"insertText":{"location":{"index":START,"tabId":TAB},"text":text}}]
pos=START; spans=[]
for k,t in P:
    spans.append((k,pos,pos+len(t)+1)); pos+=len(t)+1
end=pos
rng=lambda a,b:{"startIndex":a,"endIndex":b,"tabId":TAB}
for k,a,b in spans:
    req.append({"updateParagraphStyle":{"range":rng(a,b),"paragraphStyle":{"namedStyleType":"HEADING_2" if k=="H" else "NORMAL_TEXT"},"fields":"namedStyleType"}})
req.append({"updateTextStyle":{"range":rng(START,end),"textStyle":{},"fields":"bold,italic,fontSize,weightedFontFamily,foregroundColor"}})
for k,a,b in spans:
    if k!="H":
        st={"foregroundColor":BROWN}; f="foregroundColor"
        if k=="L": st["bold"]=True; f+=",bold"
        req.append({"updateTextStyle":{"range":rng(a,b-1),"textStyle":st,"fields":f}})
for k,a,b in spans:
    if k=="B":
        req.append({"createParagraphBullets":{"range":rng(a,b),"bulletPreset":"BULLET_DISC_CIRCLE_SQUARE"}})
# open-question bullet text
req.append({"replaceAllText":{"replaceText":"Whether the Last House stays whole as the finale (my assumption: yes), and the 13 are chosen by the ranking below; doc can overrule.","containsText":{"text":"Which 13 of the 20 stay, and what gets merged (a first look is below).","matchCase":True},"tabsCriteria":{"tabIds":[TAB]}}})
json.dump(req,open("pick_req.json","w"))
print(len(req),end,len(text))
