#!/usr/bin/env python3
# Written by Claude (Anthropic), 2026-10-20. Builds the insert for rooms 3 (spool) and 4 (ladder) of the assembled draft.
import json,sys
TAB,IDX,OUT=sys.argv[1],int(sys.argv[2]),sys.argv[3]
def u(s): return len(s.encode('utf-16-le'))//2
BR={"red":0.19607843,"green":0.10588235,"blue":0.023529412}
items=[
("H2","Kitchen: the spool"),
("N","The folded scrap stays under the governor’s sleeve. Beside the engine, twine leaves a spool on the counter. The spool has a mass of 2.0 kg, rims 0.20 m from its axle, and a hub 0.12 m from it. About the axle its moment of inertia is I = 0.040 kg m²."),
("N","The free cord is wound to turn the spool counterclockwise when pulled. Pulled flat, it leaves the underside of the hub. A spring balance reads 6.0 N. Its end is drawn along the cord as needed, and the reading and the angle are held steady during each short trial. The counter grips well enough for rolling."),
("H3","The card"),
("N","(a) Find which way the spool starts when the cord is pulled flat, at 60° above the horizontal, and straight up. (b) Find the direction that leaves it still. (c) Find how much grip, as the ratio of sideways force to normal force, the counter has to give in each case."),
("H3","The line of the pull"),
("N","Count torques about the line where the rim meets the counter. The counter’s support and its grip act there, and gravity runs through it, so none of those three has a lever about that line."),
("N","Counting clockwise as positive, the cord’s torque about that line is F(R cos θ − r): the rightward part of the pull works through the rim radius R, and the cord’s own turning about the hub works back through r. It balances the spool’s moment of inertia about the contact line, the axle’s plus mR² for the axle riding above it:"),
("N","I_contact α = F(R cos θ − r),        I_contact = I + mR² = 0.040 + 0.080 = 0.12 kg m²."),
("N","Why does the contact line work here? At the start nothing’s turning yet, so the point touching the counter has no acceleration. Once the spool turns, that point accelerates toward the axle, straight along the line to the mass centre, so the acceleration adds no extra torque about it. Being still for an instant wouldn’t have been enough on its own."),
("N","Rolling ties the centre’s acceleration to the pickup: a = Rα. With R = 0.20 m and r/R = 0.60, the balance becomes"),
("N","(3.0 kg) a = (6.0 N)(cos θ − 0.60),        a = 2.0(cos θ − 0.60) m/s²."),
("N","Here 3.0 kg is I_contact/R². Two kilograms have to travel, and the turning adds another kilogram’s worth, I/R², to this rolling balance."),
("N","Flat, a = +0.80 m/s²: the spool rolls right, toward the pull. At 60°, a = −0.20 m/s²: it goes left, away from the pull. Straight up, a = −1.20 m/s²: left again. (a) is done."),
("N","The spool stays at rest when cos θ = 0.60, a 3-4-5 direction about 53° above the horizontal; its upward part is then 0.80. The pull’s line passes through the contact. Steeper than that, the cord torques the spool left even while it pulls right."),
("N","The arrows pencilled at dinner can stay beside this drawing too. One shows the cord’s direction, one its rightward part, one its upward part. Their jobs are already different. The counter has to supply what’s missing from the centre’s horizontal balance, and carry what’s left of the weight:"),
("N","ma = F cos θ + f,        N + F sin θ = mg."),
("N","Take f positive rightward. The numbers give f = −(2 cos θ + 2.4) N and N = (20 − 6 sin θ) N. All three trials need grip to the left:"),
("N","flat:  f = −4.4 N on N = 20 N, so 0.22"),
("N","60°:  f = −3.4 N on N = 14.8 N, so 0.23"),
("N","up:  f = −2.4 N on N = 14 N, so 0.17"),
("N","Grip here means the available sideways force divided by the counter’s normal force. These three need at most about 0.23. A grip of 0.25 covers every angle between flat and upright: the bound reduces to 2 cos θ + 1.5 sin θ ≤ 2.6, and the left side never exceeds 2.5. (c) is 0.22, 0.23 and 0.17, with 0.25 enough for all."),
("H3","A second card: what the twine releases"),
("N","The guest sets the pull at 60°, and the spool starts from rest and goes left. A separate light line from its axle passes through the wall. It has 0.10 m of slack before it touches a sear. How long does the spool take to use up the slack, how fast is it going then, and how much energy does it hold just before the line takes the load? Compare that with the work the cord’s end did."),
("N","At −0.20 m/s², the spool crosses 0.10 m in 1.0 s and arrives at 0.20 m/s."),
("N","Call the centre’s travelling energy the punch. Two kilograms at 0.20 m/s punch ½mv² = 0.040 J. The spool is also turning at 1.0 rad/s, and about its axle that holds ½I ω² = 0.020 J. (That part gets a name next door.) Together they hold 0.060 J."),
("N","The cord’s end has been drawn 1.0 cm along the 6.0 N pull. Six newtons through one centimetre supply the same 0.060 J. The rolling contact stayed still while the cord end travelled."),
("N","The sear needs under 0.02 N through its short release stroke. Against the 3.0 kg rolling balance, that load changes the acceleration by under 0.007 m/s², about 3%. The sear releases the ladder’s catch. The line slips off, leaving the ladder free."),
("N","The pull is still to the right."),
("H3","A third card: the other winding"),
("N","A third card puts the same rims on a sloped board. This version has a narrower hub, one third of the rim radius, and the cord leaves its top, pulled uphill parallel to the board. The mass and the axle’s moment of inertia stay the same. The board has sin φ = 0.60 and cos φ = 0.80, and the grip coefficient is 0.20. Find the range of pulls for which the spool rolls without slipping."),
("N","Now the cord has lever R + r about the contact line. Gravity’s downhill part has lever R. The support and the grip still have no lever there. Counting uphill travel and the matching turning as positive:"),
("N","I_contact α + mgR sin φ = F(R + r),        a = Rα."),
("N","The centre’s own balance is ma = F + f − mg sin φ. Put the two together, and the uphill grip f obeys"),
("N","9f + F = 3mg sin φ,        N = mg cos φ."),
("N","A gentle pull can leave the grip working uphill. A hard pull makes it work downhill. With friction coefficient μ, rolling needs −μN ≤ f ≤ μN, and the two limiting pulls are"),
("N","F_low = 3mg sin φ − 9μmg cos φ,        F_high = 3mg sin φ + 9μmg cos φ."),
("N","With 3mg sin φ = 36 N and 9μmg cos φ = 28.8 N, these two kilograms roll without slipping for pulls from 7.2 N to 64.8 N. Below the first, the board can’t give enough uphill grip. Above the second, it can’t give enough downhill grip."),
("N","A weak pull can lose the rolling just as a strong one can. The first spool’s direction asked where the line passed. This winding’s limits ask how much the contact can hold."),
("H2","Library: the ladder"),
("N","The windows are large and give no light. The host lies beneath the ladder. A line from the kitchen ends at the empty catch on the floor."),
("N","The ladder is uniform: 8.0 kg, 3.0 m long. Before release its foot stood 1.8 m from the wall and its top 2.4 m up. The wall and floor have no friction. The host wasn’t on the ladder; the falling ladder reached the host only after its top had left the wall."),
("H3","The card"),
("N","(a) Find what held the ladder before release. (b) A calibration card records a different run: from the same pose, the foot was being drawn outward at 0.40 m/s. Find the speed of the ladder’s centre and the ladder’s angular speed at that moment. (c) Now let the unloaded ladder go from rest. Find the height at which the wall loses contact, the speed of the centre then, and how far the foot has travelled."),
("H3","Before anything moved"),
("N","The floor carries 80 N. The weight acts halfway along the ladder, 0.9 m from the foot horizontally, and torques the ladder 72 N m about the foot. The wall’s push, 2.4 m above the foot, balances that with 30 N."),
("N","The wall pushes right. The catch holds the foot left with 30 N. A tiny sear can release a heavily loaded catch; it needn’t carry that 30 N load through its own trigger stroke. (a) is done."),
("H3","The trial on the card"),
("N","Write the foot’s distance as x and the top’s height as y. The length holds the two together:"),
("N","x² + y² = L²,        x dx = −y dy."),
("N","At x = 1.8 m and y = 2.4 m, the top comes down at 0.30 m/s. The centre travels half as far as each endpoint: right at 0.20 m/s, down at 0.15. Its speed is 0.25 m/s."),
("N","Half of x and half of y are the centre’s coordinates. They stay 1.5 m from the corner at the wall’s foot. The centre follows a circle, although neither end of the ladder does."),
("N","At the corner 1.8 m out and 2.4 m up, the foot’s rightward speed and the top’s downward speed fit one turning: counterclockwise at one sixth of a radian a second (0.40 m/s over a lever of 2.4 m; 0.30 m/s over 1.8 m). Every point of the ladder has that same instantaneous turning about the corner. The corner is momentarily still, without a hinge there. (b) is 0.25 m/s and 1/6 rad/s."),
("H3","What the fall held"),
("N","Reset the ladder and hold it still. The kitchen line releases the catch and disengages. Let θ be the lean above the floor, so y = L sin θ. That lean decreases during the fall; the ladder’s counterclockwise sweep has magnitude ω = −θ̇."),
("N","The centre runs at Lω/2. Its travel punches ½m(Lω/2)². The ladder also turns about its own centre, with moment of inertia mL²/12, and that turning holds ½(mL²/12)ω². Call it the hook. The punch and the hook are different parts of the energy, and they add:"),
("N","2K = (mL²/3)ω²."),
("N","The centre has fallen half as far as the top. Every metre the top comes down releases half the ladder’s weight through a metre: the heft. The energy balance, with the initial lean θ₀, is"),
("N","K + (mgL/2) sin θ = (mgL/2) sin θ₀,        Lω² + 3g sin θ = 3g sin θ₀."),
("N","That gives the sweep at every pose where the wall’s still attached. It doesn’t say the wall can stay attached. The wall can only push."),
("H3","Where the wall lets go"),
("N","The centre’s circular path bends its motion. Its sideways acceleration has two parts: the increasing sweep carries it outward, while the turning of its velocity bends it back. With α the pickup, taking the derivative of the energy balance gives it, and the centre’s horizontal motion gives the second line:"),
("N","2Lα = 3g cos θ,        2a_x + Lω² cos θ = Lα sin θ."),
("N","Only the wall supplies a horizontal force during the free slide, so N_wall = ma_x. Use the energy balance for the sweep and the first line for its pickup. The wall’s push comes out"),
("N","4N_wall = 3mg cos θ (3 sin θ − 2 sin θ₀)."),
("N","While the ladder stood still, the wall held 30 N. Immediately after release it holds 28.8 N; the centre has started picking up. The old statics no longer apply."),
("N","As the ladder falls, the two parts of the sideways acceleration approach cancellation. The wall’s push reaches zero when 3 sin θ = 2 sin θ₀. The top is then at two thirds of its first height: 1.60 m."),
("N","Keeping the top against the wall below that height would take a leftward pull. The window supplies none. The top leaves; it doesn’t wait for the ladder to be flat."),
("N","At that instant ω² = 8/3 rad²/s². The ladder sweeps at about 1.63 rad/s and its centre runs at √6, about 2.45 m/s. The centre punches 24 J; the turning about the centre hooks 8 J. The 32 J together equal the lost heft: 80 N descending through the centre’s 0.40 m. (c) is 1.60 m and 2.45 m/s; the foot’s travel comes next."),
("H3","Where the next act begins"),
("N","The foot is now √(9 − 1.60²) ≈ 2.54 m from the wall. It has travelled about 0.74 m. A pin set at that place trips the billiard-room sear. Its load is neglected in the free-slide model."),
("N","The ladder supplies the release. The spring beyond the wall supplies the blow. The cue was cocked before the kitchen line moved."),
("N","The wall stopped touching the ladder before the ladder touched the host."),
("N","In the dark glass, the ladder’s still leaning."),
]
text="";spans=[];pos=IDX
for k,t in items:
    n=u(t); spans.append((k,pos,pos+n+1)); text+=t+"\n"; pos+=n+1
reqs=[{"insertText":{"location":{"index":IDX,"tabId":TAB},"text":text}}]
reqs.append({"updateParagraphStyle":{"range":{"startIndex":IDX,"endIndex":pos,"tabId":TAB},"paragraphStyle":{"namedStyleType":"NORMAL_TEXT"},"fields":"namedStyleType"}})
reqs.append({"updateTextStyle":{"range":{"startIndex":IDX,"endIndex":pos,"tabId":TAB},"textStyle":{},"fields":"bold,italic,fontSize,weightedFontFamily,foregroundColor"}})
reqs.append({"updateTextStyle":{"range":{"startIndex":IDX,"endIndex":pos,"tabId":TAB},"textStyle":{"foregroundColor":{"color":{"rgbColor":BR}}},"fields":"foregroundColor"}})
for k,a,b in spans:
    if k in("H2","H3"):
        reqs.append({"updateParagraphStyle":{"range":{"startIndex":a,"endIndex":b,"tabId":TAB},"paragraphStyle":{"namedStyleType":{"H2":"HEADING_2","H3":"HEADING_3"}[k]},"fields":"namedStyleType"}})
        reqs.append({"updateTextStyle":{"range":{"startIndex":a,"endIndex":b-1,"tabId":TAB},"textStyle":{"bold":True,"foregroundColor":{"color":{"rgbColor":BR}}},"fields":"bold,foregroundColor"}})
json.dump(reqs,open(OUT,'w'),ensure_ascii=False)
print(len(reqs),pos-IDX)
