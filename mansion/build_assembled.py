#!/usr/bin/env python3
# Written by Claude (Anthropic), 2026-10-20. Builds the batch for the assembled Mansion draft tab (pilot: rooms 1-2).
import json,sys
TAB=sys.argv[1]
def u(s): return len(s.encode('utf-16-le'))//2
BR={"red":0.19607843,"green":0.10588235,"blue":0.023529412}
items=[
("B","Written by Claude (Anthropic), 2026-10-20 22:12."),
("H1","Assembled draft, themes 1–8: the pilot (rooms 1 and 2)"),
("N","Each room runs story, then the problem in plain AP, then a solution built piece by piece from named quantities. The words arrive on doc’s ramp: sweep first, bulk because the knife needs it, pickup and heft in the kitchen; the rest wait their rooms. SI units throughout until they start to look stodgy. Tab 1, Codex’s tabs and the Last House are untouched. Nothing here is settled; the notes at the end say what I chose."),
("H2","Dining room"),
("N","Dinner is laid for four. The cards read HOST, GUEST, ATTENDANT and WITNESS. The ATTENDANT card is missing a corner. One glass has been poured. The host has gone to the library."),
("N","A knife hangs over the table from a light rod. Its centre is one metre below the hook. In the little model on the place card, the knife counts as a point mass of one kilogram and the rod has no mass. Take g = 10 m/s²."),
("N","Three arrows have been pencilled beside the drawing: gravity straight down, the rod’s pull toward the hook, and the knife’s speed along its arc. For now they can stay in the drawing."),
("N","A thin strip of paper moves steadily past a light pen linked to the knife. Each return writes another crest. Along the edge is one printed word: POSITION. The pen is light enough to leave the beat unchanged in this model."),
("H3","The card"),
("N","The knife is pulled aside by 0.10 rad and released from rest. (a) Find its kinetic energy at the bottom of the swing. (b) Find its greatest speed. (c) Find the time between returns to the release point. (d) What changes if the knife has twice the mass?"),
("H3","The knife comes back"),
("N","Start with what gravity lifted. Pulled aside by 0.10 rad, the knife has risen h = ℓ(1 − cos θ), which for a small angle is ℓθ²/2 = 0.0050 m. Its potential energy is mgh = 0.050 J."),
("N","At the bottom the height is spent, so all of that is motion: 0.050 J. Then ½mv² = 0.050 gives v = √0.10, about 0.32 m/s. (a) is 0.050 J and (b) is 0.32 m/s."),
("N","The rod is turning, so say it the rod’s way. Call how fast the rod turns, in radians a second, the sweep. At a one-metre lever the knife’s speed is the lever times the sweep, so the greatest sweep is about 0.32 a second. It is zero at either end, greatest at the bottom, and then it runs the other way."),
("N","The beat needs the turning effect of gravity. The knife puts its mass out at the end of a lever, and mass times lever is a number of its own, here 1 kg m. Call that the bulk, β = mℓ. Gravity’s turning effect at a lean θ is gβ sin θ, which is about gβθ for small leans. What resists the turning is the moment of inertia about the hook, which I’ll write η = mℓ². Together,"),
("N","ηθ̈ = −gβθ,        ω₀² = gβ/η = g/ℓ = 10 s⁻²."),
("N","The motion repeats at ω₀ ≈ 3.2 rad/s, so the time between returns is T = 2π/ω₀ ≈ 1.99 s. (c) is about 2.0 s."),
("N","(d) Twice the mass doubles the bulk and doubles η, so gβ/η is untouched: same beat. There is twice the knife to lift, so the energy doubles to 0.10 J, but m cancels in mgh = ½mv², so the greatest speed stays 0.32 m/s."),
("N","A second little frame stands under glass: one knife hangs from the hinge of another. That one can wait."),
("N","The trays on the sideboard turn a little too fast."),
("H2","Kitchen"),
("N","The kitchen is lit by gas. A small steam engine turns the shaft that disappears into the ceiling. Two weights stand out from its governor. A folded scrap keeps the sleeve from rising."),
("H3","The card"),
("N","The engine’s four-second test has been written on a card. With the governor held in place, the whole rotating assembly has a moment of inertia of 0.50 kg m² and starts turning at 4.0 rad/s. The engine delivers a steady net power of 3.0 W to the assembly; friction and the other loads are already allowed for in that figure. (a) Find the angular speed after 4.0 s. (b) Find the angle turned in that time. (c) Find the driving torque at the start and at the end."),
("N","Then the governor itself. Each of its two weights is 1.0 kg on a 0.50 m arm hinged to the shaft; neglect the sleeve’s weight and the effort needed to move the valve. (d) At a steady 5.0 rad/s, find each arm’s angle from the vertical and each weight’s distance from the shaft."),
("H3","What the engine promised"),
("N","Half a kilogram metre squared turning at 4 rad/s holds ½ηω² = ½(0.50)(16) = 4.0 J. In four seconds the engine adds 3.0 W × 4.0 s = 12 J. The assembly ends with 16 J, and ½(0.50)ω² = 16 gives ω = 8.0 rad/s. (a) is 8.0 rad/s."),
("N","A steady power supplies equal portions of energy, but each later portion goes into something already turning faster, so each portion adds less sweep than the one before. Call how fast the sweep changes the pickup, α. The same power rides a torque that falls as the sweep rises:"),
("N","P = τω,        τ = ηα."),
("N","At the start τ = 3.0/4.0 = 0.75 N m and the pickup is α = 1.5 rad/s². At the end τ = 3.0/8.0 ≈ 0.38 N m and the pickup is 0.75 rad/s². The shaft is getting faster and the effort is getting smaller. (c) is 0.75 N m, then 0.38 N m."),
("N","The angle follows by giving each differential its own side. The energy changes by ηω dω, and the shaft turns through dθ = ω dt, so P dt = ηω dω and"),
("N","P dθ = ηω² dω,        θ = η(8³ − 4³)/(3P) = 0.50(448)/9.0 ≈ 25 rad."),
("N","(b) is about 25 rad, four turns. The promise was in watts. Nothing promised a steady pickup."),
("H3","What the governor does"),
("N","Each circling weight needs an inward force of mω²r to keep turning. The arm’s pull T supplies it, and the arm’s upward part holds the weight up: T cos θ = mg, and the inward part T sin θ = mω²(ℓ sin θ). Divide out T and m:"),
("N","ℓω² cos θ = g."),
("N","At 5 rad/s, cos θ = 10/(25 × 0.50) = 0.80. The arm hangs 0.40 m below its hinge and the weight sits 0.30 m from the shaft: the 3-4-5 triangle. The lean is about 37°. (d) is 37° and 0.30 m."),
("N","Hung at rest the weight would sit 0.50 m below the hinge, so it has been lifted 0.10 m. A weight lifted that way holds energy because of where it is. Call that the heft: here 1.0 kg × 10 m/s² × 0.10 m = 1.0 J each. A faster shaft spreads the weights further, lifts them higher, and raises the sleeve."),
("N","The sleeve normally closes admission as the shaft speeds up. The scrap holds it down. The engine kept its promise because something prevented the governor from keeping its own."),
("N","Only the last three letters show on the folded scrap: ANT."),
("H2","Notes on the pilot (for doc and Codex)"),
("N","Claude (Anthropic), 2026-10-20 22:12. Rooms 1 and 2 only; I wanted you to see the register before I write the other six. Numbers checked in check_rooms12.py (claudog repo): 0.0050 m, 0.050 J, 0.316 m/s, T = 1.987 s; 4 J to 16 J, 8 rad/s, 24.89 rad (an Euler integration agrees to 4 places), 0.75 and 0.375 N m; cos θ = 0.8, 0.30 m out, 0.40 m down, 1.0 J of heft each."),
("N","What I chose. (1) Room 1 uses only sweep and bulk; Codex’s stroke, wheel, hook and ring wait. The words the reader meets are textbook ones: kinetic energy, moment of inertia. (2) η arrives in room 1 as a letter only, the swap doc ruled for I; the Mansion’s statements still say “moment of inertia” in words. If plain-AP statements should keep I until the book says otherwise, say so and I’ll change the statements only. (3) Room 2 adds pickup and heft. No hook, pow or crank yet. (4) No cats and pushes: speeds are m/s and forces would be newtons. Per doc, the cat is how fast a cat goes, about 1 m/s, and I’ll say that in one light line when the unit first shows. (5) Codex’s “governing motion” paragraph, with oompf and the weights’ opposite movements cancelling, is left out of room 2 because oompf waits for a room where momentum is the point. (6) Codex’s closing “Mechanical joins” items (ribbon transmission, basin transfer) come in as I reach those rooms."),
("N","Next: rooms 3 and 4 (billiards), then the rest in order, the Last House whole and last. The lock stays with Claude (orange) until the assembly is done."),
]
text="";spans=[]
pos=1
for k,t in items:
    n=u(t)
    spans.append((k,pos,pos+n+1)); text+=t+"\n"; pos+=n+1
reqs=[{"insertText":{"location":{"index":1,"tabId":TAB},"text":text}}]
end=pos
reqs.append({"updateParagraphStyle":{"range":{"startIndex":1,"endIndex":end,"tabId":TAB},"paragraphStyle":{"namedStyleType":"NORMAL_TEXT"},"fields":"namedStyleType"}})
reqs.append({"updateTextStyle":{"range":{"startIndex":1,"endIndex":end,"tabId":TAB},"textStyle":{},"fields":"bold,italic,fontSize,weightedFontFamily,foregroundColor"}})
reqs.append({"updateTextStyle":{"range":{"startIndex":1,"endIndex":end,"tabId":TAB},"textStyle":{"foregroundColor":{"color":{"rgbColor":BR}}},"fields":"foregroundColor"}})
for k,a,b in spans:
    if k in("H1","H2","H3"):
        reqs.append({"updateParagraphStyle":{"range":{"startIndex":a,"endIndex":b,"tabId":TAB},"paragraphStyle":{"namedStyleType":{"H1":"HEADING_1","H2":"HEADING_2","H3":"HEADING_3"}[k]},"fields":"namedStyleType"}})
        reqs.append({"updateTextStyle":{"range":{"startIndex":a,"endIndex":b-1,"tabId":TAB},"textStyle":{"bold":True},"fields":"bold"}})
    if k=="B":
        reqs.append({"updateTextStyle":{"range":{"startIndex":a,"endIndex":b-1,"tabId":TAB},"textStyle":{"bold":True},"fields":"bold"}})
json.dump(reqs,open(sys.argv[2],'w'),ensure_ascii=False)
print(len(reqs),end)
