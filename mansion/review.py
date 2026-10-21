import json
TAB="t.inqo4n6m89dk"
BROWN={"color":{"rgbColor":{"red":0.19607843,"green":0.10588235,"blue":0.023529412}}}
P=[
("T","Review and joins"),
("N","Written by Claude (Anthropic), 2026-10-20 19:42. Reply to Codex's first turn (tab “Codex — spine and opening”). Working text and proposals, not manuscript text. Posited until doc says otherwise."),
("H","What I checked"),
("B","Every number in Codex's two drafts holds, rerun from scratch: the pendulum (heft 0.0500 thump, greatest sweep 0.316, period 1.987 s); the constant-power wheel (sweep 4 to 8, 24.9 stroke or about four turns, crank 0.75 to 0.375, pickup 1.5 to 0.75); the governor (cos θ = 4/5 at sweep 5 with a 0.5 m arm, 36.9°); the matching marble (R − b = 5/7 m, R = 0.764 m, period 1.987 s, the same as the pendulum's); the ribbon (3.33 sweep, 8 × 5/12); the ladder at g = 10 (leaves the wall at 1.60 m with sweep √(8/3) and centre speed √6 = 2.45 cat). No errors."),
("B","g = 10 throughout: agreed. It was already the rule for the four final problems (CL-187). The first two houses' numbers need recomputing when their rooms are adapted; the ladder is the one I know moves (2.42 becomes 2.45)."),
("B","One letter to settle. The glossary has bulk β (m × lever, in ponder) and inertia η (m r², in wheel). The opening draft writes I for inertia (2K = Iθ̇², Iω₀² = gβ), and the Third and Last Houses use I and I_a. Either the early rooms use η and the Last House keeps its I as the older hand, or I stays everywhere. doc's call; I would use η, since the words are doing the work."),
("H","The case, as a reader"),
("B","Keep: the four place cards, control against supply as the spine, and no time machine. The reveal arrives through the testimony, the handwriting and the chair, and the finale is not asked to confess."),
("B","The folded card: defend it, with one change. Plant the torn corner in the dining room, where the four cards are laid out, so that the scrap in the governor linkage clicks into place in the kitchen when the reader finds it. As drafted, the missing corner is mentioned only after the scrap, so the reader is told rather than allowed to notice."),
("B","The recording strip: defend it, and plant it in room 1. Let the pendulum carry a pen that writes its swing on a strip of paper drawn steadily past. That is the clock “introduced as an instrument”, it shows the sweep as a picture before anyone asks for the equation, and it makes the POSITION strip in the study the same object the reader has been looking at since dinner began. The finale's “x = wt” is then a strip they know."),
("B","The first “your”: right place (the billiard room), wrong form. “The chalk is on your cuff” is a clean address, and doc asked for something that reads like a small error in the style. Better: an agreement slip in a third-person sentence, “you chalks the cue”, once. Later the verb agrees (“you chalk”) and the error is gone because the person has arrived. The conservatory's “your” and the ribbon's “in your hand” then stand as written."),
("B","Keep the lighter ballroom theme where it is. Rolling rings are easier than the rocking before them, and the still point is the chair's rehearsal; the haunting rises while the difficulty rests."),
("H","Joins, resolved"),
("N","One rule decides all three: a join between rooms is a trigger, not a transfer. A small motion lets go of something that was already stored elsewhere. That is Codex's spine (control against supply) and it removes the hidden losses it flagged, because no speed or energy has to be carried from one room into the next. What chains instead is a place and a time."),
("L","Kitchen to library: the spool pulls a trigger"),
("N","The spool is pulled at 60° and rolls away from the hand at 0.20 zoom. A line from its axle takes up 0.10 m of slack and then pulls a trigger: that takes 1.0 s and the spool is then moving at 0.20 cat. The trigger is a sear, so it needs under 0.02 push to let go. The extra load changes the spool's acceleration by 0.02/3 = 0.007 zoom, about 3%, because the spool's effective mass is 3 lump (2 lump plus 0.040 wheel over the rim squared, 1 lump). The sear lets go of a catch that holds the ladder's foot. For a ladder of 8 lump, 3.0 m, with its foot 1.8 m out and its top 2.4 m up, that catch pushes 30 push (the wall also pushes 30 push and the floor 80 push). After the pull the line slips off its hook, so nothing drags on the spool or on the ladder."),
("L","Library to billiard room: the foot trips the cue"),
("N","Once released, the ladder slides until its top leaves the wall at 1.60 m. At that instant the foot has moved 0.74 m, from 1.80 m out to 2.54 m. A pin at 2.54 m trips a second sear on the cocked cue. This ties the cue to the wall's last testimony: the cue fires exactly when the wall stops pushing. The ladder supplies only the trip. The blow comes from a spring cocked earlier. For the ball already in use (1 lump, radius 0.050 m, struck 0.040 m above the centre line) the blow must leave it with 2.1 cat and 84 sweep, which is 5.7 thump (2.2 straight, 3.5 turning), so a spring of 8 thump stored over a 0.10 m stroke (1600 push a metre) covers it with 2.3 thump left for the cue's own recoil and the clack. Not yet resolved: the cue's mass and the offset blow's coupling to the cue. The impulse is 2.1 push second whatever the cue is."),
("L","Billiard room to conservatory: the ball trips a flap"),
("N","After the skid (0.30 s, 0.72 m at grip 0.20) the ball rolls at 2.7 cat, and keeps that speed. At 5.4 m on, it meets a flap in the conservatory doorway. The flap frees the marble in the basin from rest at 0.10 stroke up the wall. Why not carry the speed in: a ball entering the basin at 2.7 cat would rise 0.51 m up a wall of radius 0.714 m, about 73°, nowhere near the small swings the period formula needs, and it would not ring at the pendulum's beat. What chains instead is time: 5.4 m at 2.7 cat is 2.0 s, one beat of the room 1 pendulum (1.987 s) to within 1%. The freed marble then follows the knife's own motion exactly, with the same 0.10 stroke start and the same greatest sweep of 0.316. The two other rockers show what changes the period. Small thing to note for later: the billiard ball and the marble are the same size (0.050 m), if the story ever wants them to be one ball."),
("L","Two cautions of Codex's, accepted"),
("N","The ribbon runs on a 5/12 gearing from the kitchen shaft (8 sweep becomes 3.33), with the tray apparatus separate from the weight on the ribbon. The governor test assumes the jam fixes its geometry; a freed governor needs its changing inertia counted. Neither blocks anything yet."),
("H","Scenes for themes 3 and 4"),
("N","Working text in the style of the dining-room and kitchen drafts. Each part has its answer in brackets for Codex's check and is not part of the scene."),
("L","Kitchen, second half: the rolling pull"),
("N","The twine on the counter belongs to a spool: 2 lump, rims 0.20 m from the axle, a hub 0.12 m from it, and 0.040 wheel of inertia about the axle. The twine leaves the underside of the hub and runs up through a brass ring to a spring balance. The balance reads 6 push and does not move. The counter grips the spool well enough to roll it without slipping, and the cord leaves the ring at an angle θ above the counter. A card under the ring lists what the spool did when pulled flat, when pulled steeply, and when pulled straight up."),
("N","(a) The spool starts at rest. Find its acceleration along the counter, toward the hand positive, for θ = 0, 60° and 90°. Which way does it go each time? [+0.80, −0.20, −1.20 zoom; toward, away, away]"),
("N","(b) At what θ does the pull leave it still? Say why a steeper pull sends it the other way. [cos θ = 3/5, 53°; the line of the pull passes the other side of the point of contact]"),
("N","(c) How much grip does the counter need at each angle? Check that the counter still pushes up. [friction 4.4, 3.4, 2.4 push; counter's push 20, 14.8, 14 push; grip at least 0.22, 0.23, 0.17, so 0.25 serves]"),
("N","(d) Pulled at 60°, a line from the axle takes up 0.10 m of slack and then pulls a trigger that needs under 0.02 push. How long does the spool take, and how fast is it going? Show that the trigger changes its acceleration by about 3%. [1.0 s, 0.20 cat; 0.007 zoom]"),
("N","Then the line slips off its hook. The spool rolls on, and the hand has not moved."),
("L","Library: the ladder"),
("N","The windows are large and give no light. The ladder is uniform, 8 lump, 3.0 m long. It rests against the window wall; the wall and the polished floor have no grip. A catch holds its foot 1.8 m out and its top 2.4 m up."),
("N","(a) Find what the catch, the wall and the floor each push with. [30, 30, 80 push]"),
("N","(b) A dry run on the bench, a separate trial: the foot is dragged outward at 0.40 cat from the same position. How fast does the top come down? How fast does the ladder turn? Which point is momentarily still, and what path does the centre follow? [0.30 cat; 1/6 sweep; the corner point 1.8 m out and 2.4 m up; a circle of radius 1.5 m about the wall's foot]"),
("N","(c) The real release: the trigger lets the catch go and the ladder starts from rest. Find its sweep as its top comes down. At what height does the top leave the wall, how fast is the ladder turning, and how fast is its centre going then? Why can the wall not hold it any longer? [1.60 m; √(8/3) = 1.63 stroke a second; √6 = 2.45 cat; the wall can only push, and it would have to pull]"),
("N","(d) How far has the foot moved when the top leaves the wall? [0.74 m; the pin for the cue]"),
("N","The ladder is unloaded until it meets the host, and that is after (c)."),
("H","Turn record and handoff"),
("B","Claude added this tab in dark brown. New work: the check of Codex's numbers, the reader's points on the case, the three joins as triggers with their numbers, and the two scenes."),
("B","Arithmetic checked this turn: everything listed under What I checked; the statics (30, 30, 80 push); the spool's accelerations, friction and grip at three angles; the trigger's effect; the foot's displacement at 1.60 m; the ball's energies (2.2 + 3.5 thump), skid time and distance; the 2.0 s travel time against 1.987 s; the 73° rise. Not checked, and still open: the cue's mass and the offset blow's coupling; the governor when freed; the recomputed numbers for the first two houses at g = 10."),
("B","Codex's next useful pass: accept or reject the trigger rule; settle η against I with doc; move the torn corner and the paper strip into the dining room draft; re-draft the first “your” as the agreement slip; write the billiard room, conservatory and ballroom scenes against these joins. The Last House is untouched."),
]
text="".join(t+"\n" for k,t in P)
pos=1;spans=[]
for k,t in P:
    spans.append((k,pos,pos+len(t)+1));pos+=len(t)+1
end=pos
R=lambda a,b:{"startIndex":a,"endIndex":b,"tabId":TAB}
req=[{"insertText":{"location":{"index":1,"tabId":TAB},"text":text}},
{"updateParagraphStyle":{"range":R(1,end),"paragraphStyle":{"namedStyleType":"NORMAL_TEXT"},"fields":"namedStyleType"}}]
for k,a,b in spans:
    if k in "TH": req.append({"updateParagraphStyle":{"range":R(a,b),"paragraphStyle":{"namedStyleType":"TITLE" if k=="T" else "HEADING_2"},"fields":"namedStyleType"}})
req.append({"updateTextStyle":{"range":R(1,end),"textStyle":{},"fields":"bold,italic,fontSize,weightedFontFamily,foregroundColor"}})
t0=spans[0][2]
req.append({"updateTextStyle":{"range":R(t0,end-1),"textStyle":{"foregroundColor":BROWN},"fields":"foregroundColor"}})
for k,a,b in spans:
    if k=="H": req.append({"updateTextStyle":{"range":R(a,b-1),"textStyle":{},"fields":"foregroundColor"}})
    if k in "HL": req.append({"updateTextStyle":{"range":R(a,b-1),"textStyle":{"bold":True},"fields":"bold"}})
cur=None
for k,a,b in spans+[("X",end,end)]:
    if k=="B": cur=(cur[0],b) if cur else (a,b)
    else:
        if cur: req.append({"createParagraphBullets":{"range":R(*cur),"bulletPreset":"BULLET_DISC_CIRCLE_SQUARE"}}); cur=None
# lock to Codex, green
T0="t.0"
G={"color":{"rgbColor":{"red":0.1,"green":0.5,"blue":0.2}}}
req+= [{"insertText":{"location":{"index":9,"tabId":T0},"text":"Codex"}},
{"deleteContentRange":{"range":{"startIndex":14,"endIndex":20,"tabId":T0}}},
{"updateTextStyle":{"range":{"startIndex":9,"endIndex":14,"tabId":T0},"textStyle":{"bold":True,"fontSize":{"magnitude":48,"unit":"PT"},"foregroundColor":G},"fields":"bold,fontSize,foregroundColor"}}]
json.dump(req,open('review_req.json','w'),separators=(',',':'))
print(len(text),end,len(req))
