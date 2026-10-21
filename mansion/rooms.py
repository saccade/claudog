import json
TAB="t.idrkztqzrc1x"
BROWN={"color":{"rgbColor":{"red":0.19607843,"green":0.10588235,"blue":0.023529412}}}
P=[
("T","Rooms"),
("N","Written by Claude (Anthropic), 2026-10-20 19:22. A first map of the 20 pieces, plus the governor doc just asked for, onto nine rooms and 13 themes. Posited until doc says otherwise. Not doc's text. The scene dressing (what is in each room) is mine and is Codex's to change."),
("H","How to read this"),
("B","13 themes, not 13 problems. Values and objects slide between rooms, so the number of problems is not fixed; each theme gathers the pieces that share its physics. All 20 pieces are placed (the ranking is retired); one new piece is added, the governor."),
("B","A room's character decides what can happen in it. The kitchen has gas and no electricity, so its engine is steam. The library has big windows and is dark now. The ballroom is the spinny room. The study is well-lit and electric. The lounge has every comfort."),
("B","The themes are in play order, and the ghosts, the 'you' and the vocabulary all ramp with that order."),
("H","The 13 themes"),
("L","1. Dining room: the pendulum, single and double"),
("N","A new, easy piece. A knife hangs on a thread from a ceiling hook over the table: the simple pendulum, taken slowly, because this is where the vocabulary comes in: sweep and bulk first, then heft, hook and ring as the swing needs them. Arrows (the thread's pull, the pull of the floor, the knife's velocity) are drawn from the start, but the working stays in plain quantities for a good while before it switches to them. Then a second knife hangs from the first: the double pendulum, looked at and not yet solved (the Last House solves it). The cocktail trays turn on the sideboard a little fast, and nobody remarks on it. Travels out: the single pendulum's period, the beat other rooms keep."),
("L","2. Kitchen: the steam apparatus and its governor"),
("N","Third 3 (motor that keeps its word) plus a new governor. Gas fire, boiler, a flywheel, and a shaft up through the floor to the trays. Steady power makes the speed climb without a steady pickup (the Third 3 result). The governor, two balls on arms that fly outward as it spins, is what normally holds the speed. It is the room 1 pendulum spun round, a conical pendulum. It is the first thing you see that could explain the trays, and it is jammed. Words: pickup (how fast the sweep changes), and heft again (the balls lift). Travels out: the shaft's speed to the trays; the trays' final speed to the ballroom."),
("L","3. Kitchen: the rolling pull"),
("N","Third 2 (spool that backs away) with Haunted 4 (yo-yo on the slope). A spool of twine on the counter, pulled by its cord: whether it comes to you or goes away depends on the angle. Gas, hands and string; nothing electric. Travels out: the twine goes through the wall and is tied to the foot of the library ladder."),
("L","4. Library: the ladder"),
("N","Second 1 (ladder that slides) with Second 3 (ladder that leaves the wall). Not a spinny room: the ladder slides on its rail, the dark windows give no light, and the top lets go of the wall at two thirds of its height. Travels in: the twine pulls the foot (0.40 m/s in the set numbers). Travels out: the speed of the ladder's centre at letting go, about 2.4 m/s with the set numbers (checked), which becomes the blow in the billiard room. The fall is the natural place for the death; that is Codex's call."),
("L","5. Billiard room: blows that miss the middle"),
("N","Haunted 5 (billiard ball that skids), Haunted 3 (cube that meets a ridge), Second 2 (rod on the ice), Second 4 (superball). All four are an off-centre blow or bounce turning into spin. Cue, cushion, a cue lying on the baize, a chalk cube meeting the rail, a ball off the floor. Travels in: the ladder's blow. Travels out: a ball rolls off the table at 9/7 of its first speed, across the floor and into the fountain basin next door."),
("L","6. Conservatory: rocking"),
("N","Second 5 (marble in the trough), Third 5 (wheel that comes back) and Third 1 (counterweight upstairs): the three torque-and-period pieces from the overlap list, now one theme. The marble in the fountain basin, a garden cart wheel with a lump stuck inside it, and a pot-hanging beam with a weight each side of its pivot. Each rocks with a period set by torque and bulk, the same words as the room 1 pendulum. Travels in: the rolling ball from the billiard room. Travels out: the period. I suggest the numbers are chosen so it matches the room 1 pendulum's beat: the ghosts keep time with the living clock."),
("L","7. Ballroom: rolling rings"),
("N","Haunted 1 (bicycle wheel) with Haunted 2 (ball in the ring). A bead on a rolling hoop; a ball turning inside the ring of the dance floor. The still point of a moving body. The orchestra is audible now. Travels in: the floor ring turns at the speed the shaft gives it."),
("L","8. Ballroom: the pulled ribbon"),
("N","Third 4 (string through the floor). A weight circles on a ribbon whose other end is drawn slowly down through a hole in the floor, and it speeds up with no push on it. This is the answer to 'why are the trays getting faster' once the governor and the steam cannot be blamed. Travels in: the trays' final speed is its starting speed. Travels out: the same speed-up, now with nothing to point at."),
("L","9. Study: something hanging from something"),
("N","Last 1, as written. A desk toy under the lamp, one pendulum hung from another; the lower weight moves though nothing touched it. It answers room 1: the double pendulum is now solved. The well-lit room is where the electricity can first be seen."),
("L","10. Study: the wires under the skin"),
("N","Last 2, as written. The coils and the capacitor in the toy."),
("L","11. Hall: the corridor that gets there first"),
("N","Last 3, as written. The line along the long hall."),
("L","12. Hall: the two lights"),
("N","Last 4, as written. A lamp at each end of the corridor."),
("L","13. Lounge: the chair at the end"),
("N","Last 5, as written. The comfortable chair, the drink, and DO NOT GET UP. The last door is the lounge's."),
("H","Order, ramp and links"),
("B","Ghosts: none in 1 to 3; one thing slightly off in 4; the orchestra audible in 6 and 7; clearly present in 8; the Last House is the wild end."),
("B","The 'you' (not there at first): nothing in 1 to 4; a small slip in the style in 5 and 6, which reads as a typo; it picks up speed through 7 and 8; present in 9 to 13."),
("B","Difficulty goes up with the rooms: a single pendulum taken slowly, then steady power and a governor, rolling and pulling, the ladder, blows, rocking, then the Last House. One dip: room 7 (rolling rings) is mostly geometry and sits easier than 5 and 6. I would keep it for the ghosts, or swap it earlier; open for doc."),
("B","Arrows: shown from room 1 and not switched to for a little while; the working stays in plain quantities until the arrows have been on the page often enough to read."),
("B","Vocabulary: sweep, bulk, heft, hook and ring in 1; pickup in 2. The Last House's own preamble defines sweep, pickup and ring again. Either the rooms before it do the introducing and the repeat reads as the ghosts saying it back, or the preamble stays the only definition. Open for doc."),
("B","The links that carry numbers (twine speed, ladder exit speed, the ball's rolling speed, the trays' final speed, the matching period) need picking so the values really chain; I do that when we build the rooms."),
("H","What this needs"),
("B","Room 1 is new: a simple pendulum taken slowly, then the double. I can draft it, with the vocabulary in the order it arrives, and check the numbers."),
("B","The governor is new: it needs a problem. The part I can check: a ball on an arm of length l, spinning with the governor at speed w, hangs at an angle where cos(angle) = g/(w^2 l); below w = sqrt(g/l) the balls just hang. I can draft it and check the numbers with doc's word."),
("B","The Last House stays whole at the end, unedited, as the three last rooms."),
("B","Codex: the mystery's spine over these 13 (who dies where, and the order of the clues), and the finale's setup."),
]
text="".join(t+"\n" for k,t in P)
req=[{"insertText":{"location":{"index":1,"tabId":TAB},"text":text}}]
pos=1; spans=[]
for k,t in P:
    spans.append((k,pos,pos+len(t)+1)); pos+=len(t)+1
rng=lambda a,b:{"startIndex":a,"endIndex":b,"tabId":TAB}
for k,a,b in spans:
    nt={"T":"TITLE","H":"HEADING_2"}.get(k,"NORMAL_TEXT")
    req.append({"updateParagraphStyle":{"range":rng(a,b),"paragraphStyle":{"namedStyleType":nt},"fields":"namedStyleType"}})
req.append({"updateTextStyle":{"range":rng(1,pos),"textStyle":{},"fields":"bold,italic,fontSize,weightedFontFamily,foregroundColor"}})
for k,a,b in spans:
    if k in "NBL":
        st={"foregroundColor":BROWN};f="foregroundColor"
        if k=="L": st["bold"]=True; f+=",bold"
        req.append({"updateTextStyle":{"range":rng(a,b-1),"textStyle":st,"fields":f}})
    if k in "TH":
        req.append({"updateTextStyle":{"range":rng(a,b-1),"textStyle":{"bold":True},"fields":"bold"}} ) if k=="H" else None
for k,a,b in spans:
    if k=="B": req.append({"createParagraphBullets":{"range":rng(a,b),"bulletPreset":"BULLET_DISC_CIRCLE_SQUARE"}})
print(len(text))
json.dump(req,open("rooms_req.json","w"))
