"""Level-by-level wording for the thirteen mansion solutions, as cumulative edits.

Claude (Anthropic), 2026-10-21. The base text is the mansion route in the release copies
(Codex's assembly of CL-218). LEVEL[1] holds doc's corrections and the house rule they show:
products are said with "of" (leads with the operator) or "at" (leads with the thing), not "times".
LEVEL[2] adds the cabinet's words, LEVEL[3] the funhouse's, LEVEL[4] the understage's, each word
introduced plainly where the set first uses it. Each edit must match exactly once.
Words by level follow CL-213's "Four releases: words by level"; zow, zlow and the verbs
zower and zlower are doc's 21:49 idea (posited), placed at level 4.
"""

LEVEL = {1: [], 2: [], 3: [], 4: []}

# ---------------- Level 1: doc's corrections, and products said in words ----------------
LEVEL[1] += [
 ("With rolling tying the two motions together, the ledgers balance as:", "Put together, the ledgers balance as:"),
 ("A flywheel's energy is half its moment of inertia times the square of its sweep. At 4.0 stroke a second, half of 0.50 kg m² times 16 is 4.0 J.",
  "A flywheel's energy is half its moment of inertia at the squared sweep. At 4.0 stroke a second, half of 0.50 kg m² at 16 is 4.0 J."),
 ("needs the square of the sweep to be 64.", "needs the squared sweep to be 64."),
 ("The power a torque delivers is the torque times the sweep: P = χω. At the start, 3.0 W at 4.0 stroke a second takes χ = 0.75 N m. At the end, at 8.0, it takes 0.38 N m.",
  "The power a torque delivers is the sweep of the torque: P = ωχ. Put numbers to it once: 0.75 N m at 4.0 stroke a second delivers 3.0 W. So at the start the engine's 3.0 W takes χ = 0.75 N m, and at the end, at 8.0, it takes 0.38 N m."),
 # doc, 2026-10-22 07:31, typed into set 1: how χ is picked, and his closing sentence
 ("Torque gets χ. The power a torque delivers", "A χ hung on the wall could apply a twist to something—use that for torque. The power a torque delivers"),
 (" The same power needs half the torque once the wheel's going twice as fast.", "\nWhen the wheel goes twice as fast, applying the same power takes just half the torque."),
 ("and that takes m times the square of the sweep times the ball's distance from the shaft, mω²ℓ sin θ.",
  "and that takes the mass at the squared sweep, at the ball's distance from the shaft: mω²ℓ sin θ."),
 ("As both change, x times the foot's velocity plus y times the top's velocity is zero. So the top moves at x/y times the foot's speed, the other way: 1.8/2.4 × 0.40 = 0.30 m/s, downward.",
  "As both change, x of the foot's velocity and y of the top's velocity cancel: 1.8 m of 0.40 m/s against 2.4 m of the top's. So the top moves at x/y of the foot's speed, the other way: 0.30 m/s, downward."),
 ("(1) Rolling without slipping, the center moves at the radius times the sweep: 0.25 m × 8.0 = 2.0 m/s.",
  "(1) Rolling without slipping, the center runs at the radius sweeping at 8.0 stroke a second: 0.25 m sweeping at 8.0 runs at 2.0 m/s."),
 ("The power the current delivers to the rod is that torque times the rod's sweep, κiȧ.",
  "The power the current delivers to the rod is the rod's sweep of that torque, κiȧ."),
 ("the resistor's burning the voltage of the current, 2.0 V × 0.10 A = 0.20 W, as heat.",
  "the resistor's burning the voltage of the current, 2.0 V of 0.10 A, 0.20 W, as heat."),
]

# ---------------- Level 2: punch, hook, heft; profile; pickup, crank; spin; can, coil ----------------
LEVEL[2] += [
 # knife: heft and punch introduced; pickup introduced
 ("Its 10 N weight lifted through 5 mm stores 0.050 J.",
  "Its 10 N weight lifted through 5 mm stores 0.050 J. Energy stored in height is heft: the weight pulls, and the height hefts. The knife hefts 0.050 J."),
 ("(2) At the bottom that energy is all in the knife’s motion. Both the stored energy mgh and the kinetic energy ½mv² carry the same mass. It cancels:",
  "(2) At the bottom the heft has all gone into the knife’s motion. Energy in a body's motion is its punch, ½mv². The heft mgh and the punch ½mv² carry the same mass. It cancels:"),
 ("(4) Twice the mass doubles the stored energy and the resistance to being sped up.",
  "(4) Twice the mass doubles the heft, the punch and the resistance to being sped up."),
 ("The knife turns back while the cycle sweeps on.",
  "The knife turns back while the cycle sweeps on. The rate the sweep changes is the pickup: swung θ off vertical, the knife picks up at g/ℓ of its lean, back toward the bottom, θ̈ = −(g/ℓ)θ."),
 # flywheel: hook, crank, pickup
 ("A flywheel's energy is half its moment of inertia at the squared sweep. At 4.0 stroke a second, half of 0.50 kg m² at 16 is 4.0 J. Four seconds at a net 3.0 W add 12 J, for 16 J, and 16 J on the same wheel needs the squared sweep to be 64. The wheel ends up sweeping at 8.0 stroke a second. The engine paid in equal energy every second, not equal sweep, so four times the energy only doubles the sweep.",
  "Energy in turning is hook: a flywheel hooks half its moment of inertia at the squared sweep. 0.50 kg m² sweeping at 4.0 stroke a second hooks 4.0 J. Four seconds at a net 3.0 W add 12 J of hook, for 16 J, and 16 J of hook on the same wheel needs the squared sweep to be 64. The wheel ends up sweeping at 8.0. The engine paid in equal hook every second, not equal sweep, so four times the hook only doubles the sweep."),
 ("The power a torque delivers is the sweep of the torque: P = ωχ. Put numbers to it once: 0.75 N m at 4.0 stroke a second delivers 3.0 W. So at the start the engine's 3.0 W takes χ = 0.75 N m, and at the end, at 8.0, it takes 0.38 N m.\nWhen the wheel goes twice as fast, applying the same power takes just half the torque.",
  "A torque cranks. The power a crank delivers is the sweep of the crank: P = ωχ. Put numbers to it once: 0.75 N m cranking at 4.0 stroke a second delivers 3.0 W. So at the start the engine cranks the wheel with χ = 0.75 N m, and at the end, sweeping at 8.0, with 0.38 N m.\nWhen the wheel goes twice as fast, the same power cranks just half as hard. On 0.50 kg m², those cranks pick the wheel up at 1.5 stroke a second each second at the start and 0.75 at the end."),
 # governor heft; spool profile, crank, pickup
 ("Each ball hangs 0.40 m below the hinge instead of 0.50 m, so it's risen 0.10 m.",
  "Each ball hangs 0.40 m below the hinge instead of 0.50 m, so it's risen 0.10 m, and each 1.0 kg ball hefts 1.0 J."),
 ("(3) Write the statement’s moment of inertia as η. Take forward,",
  "(3) Write the statement’s moment of inertia as η. With the mass taken out, inertia is the profile: η on the spool's 2.0 kg is a profile of 0.020 m² about the axle. Take forward,"),
 ("So the torques about the axle are −Fr and −fR, and ηα = −Fr − fR. Rolling ties the two together: α = a/R.",
  "So the cord cranks the spool backward about the axle with −Fr, the grip cranks it with −fR, and ηα = −Fr − fR. Rolling ties the pickup to the center: α = a/R."),
 ("Here η/R² = 0.040/0.040 = 1.0 kg. The mass and turning count as 3.0 kg at the axle, while 6.0 N × 0.40 gives 2.4 N on the other side. The center speeds up at 0.80 m/s², forward: the spool rolls toward the pull. The grip is f = 1.6 − 6.0 = −4.4 N. It pulls back, and about the axle it turns the spool forward harder than the cord turns it back.",
  "The profile over R² is 0.020/0.040 = 1/2, so the mass and the turning count as 2.0 kg at 3/2: 3.0 kg at the axle, while 6.0 N × 0.40 gives 2.4 N on the other side. The center speeds up at 0.80 m/s², forward: the spool rolls toward the pull, picking up at 4.0 stroke a second each second. The grip is f = 1.6 − 6.0 = −4.4 N. It pulls back, and about the axle it cranks the spool forward harder than the cord cranks it back."),
 ("The spool's inertia never comes into it, because a spool that doesn't turn never asks for it.",
  "The spool's inertia never comes into it, because a spool that doesn't pick up never asks for it."),
 # ladder: heft, punch, hook, profile
 ("With 80 N of weight, that's 32 J.", "With 80 N of weight, that's 32 J of heft let go."),
 ("(3) The center moves at Lω/2 and the ladder turns about its center at the same sweep. The center's energy is ½m(Lω/2)², or mL²ω²/8. The turning about the center is ½(mL²/12)ω², or mL²ω²/24. Those are 3 to 1, so the 32 J splits 24 J to the center's motion and 8 J to the turning. Then ½ × 8.0 kg × v² = 24 J gives v² = 6, and the center's moving at √6, about 2.4 m/s, when the top leaves the wall.",
  "(3) The center runs at Lω/2 and the ladder sweeps about its center at the same ω. The center punches ½m(Lω/2)², or mL²ω²/8. About the center the profile is L²/12, so the turning hooks ½(mL²/12)ω², or mL²ω²/24. Those are 3 to 1, so the 32 J of heft splits 24 J of punch and 8 J of hook. Then 8.0 kg punching 24 J runs at √6, about 2.4 m/s, when the top leaves the wall."),
 # cue ball: spin, profile, punch, hook
 ("(1) Call the given impulse J. A 2.0 N s impulse on 1.0 kg leaves the center moving at 2.0 m/s.",
  "(1) Call the given impulse J. The strike is a blow; what it leaves in the center's motion is punch. A 2.0 N s blow on 1.0 kg leaves the center running at 2.0 m/s."),
 ("so about the center it leaves an angular momentum of J(H − R). Rolling at once means the ball sweeps at v/R, and its angular momentum about the center is (2/5)mR² × v/R = (2/5)RJ.",
  "so about the center it leaves J(H − R) of spin, the angular momentum. Rolling at once means the ball sweeps at v/R. Its profile about the center is (2/5)R², so (2/5)mR² sweeping at v/R carries (2/5)RJ of spin."),
 ("The center's motion carries ½ × 1.0 × 2.0² = 2.0 J. The turning carries ½ × (2/5)(1.0)(0.050)² × 40² = 0.80 J. That's two fifths as much again.",
  "The center punches ½ × 1.0 × 2.0² = 2.0 J. The turning hooks ½ × (2/5)(1.0)(0.050)² × 40² = 0.80 J: two fifths of the punch again."),
 # basin: profile, punch, hook, heft
 ("(3) The ball has to turn about its own center as well as move along the arc. Some of what the drop lets go goes into that turning, two fifths as much again as the motion along the arc gets, so the same drop gives less speed and the ball comes round later.",
  "(3) The ball has to turn about its own center as well as move along the arc. Its profile about the center is (2/5)R², so for every 5 J of punch along the arc it hooks 2 more. The same heft gives less punch, the ball runs slower and comes round later. About the contact the profile is (7/5)R², and the shorter arc, 5/7 of the knife's, pays that 7/5 back exactly."),
 # ribbon: spin, punch
 ("and the puck's angular momentum about the hole, mvr, stays the same.",
  "and the puck's spin about the hole, mvr, stays put."),
 ("(3) The ribbon's work is the change in the puck's energy: ½ × 0.50 × (16 − 4.0) = 3.0 J.",
  "(3) The ribbon's work is the punch it adds: the puck punches 1.0 J at first and 4.0 J at the end, so 3.0 J."),
 # double pendulum: pickup
 ("whenever the upper mass swings one way, the lower one swings the other.",
  "whenever the upper mass swings one way, the lower one swings the other. In either mode, each rod picks up at ω² of its own lean, back toward vertical."),
 # coils: can and coil, crank
 ("At the start the capacitor holds no charge,",
  "A capacitor is a can: it cans charge, and the charge it cans is the capacitance of its voltage, q = CV. At the start the can holds no charge,"),
 ("When the capacitor's at 4.0 V, the resistor has the other 2.0 V, and the current is 0.10 A. The capacitor holds CV = 0.40 C and ½CV² = 0.80 J,",
  "When the can's at 4.0 V, the resistor has the other 2.0 V, and the current is 0.10 A. The can holds 0.40 C and ½CV² = 0.80 J,"),
 ("This is a different capacitor, in a separate LC loop.",
  "This is a different can, in a separate loop with a coil. A coil coils flux, and the flux it coils is the inductance of its current, Φ = Li."),
 ("The statement writes the torque τ_em; here it's χ_em = κi. The power the current delivers to the rod is the rod's sweep of that torque, κiȧ.",
  "The statement writes the torque τ_em; here it's χ_em = κi: the current cranks the rod. The power is the rod's sweep of that crank, κiȧ."),
 # line: can and coil per meter
 ("(1) The line’s values balance as", "(1) Per meter, the line cans C′ and coils L′. Its values balance as"),
 ("The energy per meter is all in the voltage there:", "The energy per meter is all canned there, none coiled:"),
 # chair: can, coil, heft, punch
 ("(1) The capacitor holds q₀²/(2C),", "(1) The can holds q₀²/(2C),"),
 ("The capacitor holds (5/13)² = 25/169 of 80 mJ, about 12 mJ. With no current the inductor holds nothing, and at vertical the rods hold no height, so the other 68 mJ is in the rods' motion.",
  "The can holds (5/13)² = 25/169 of 80 mJ, about 12 mJ. With no current the coil holds nothing, and at vertical the rods heft nothing, so the other 68 mJ is the rods' punch."),
]

# ---------------- Level 3: flips; tone, chord, beat, shape; trade; phase and stripe; shift, stretch; still point; zip, zing ----------------
LEVEL[3] += [
 ("Then 8.0 kg punching 24 J runs at √6, about 2.4 m/s, when the top leaves the wall.",
  "Then 8.0 kg punching 24 J runs at √6, about 2.4 m/s, when the top leaves the wall. Or count about the point that's still for the instant, where the perpendiculars to the foot's motion and the top's meet: call it the still point. It's L/2 from the center, the corner turned a flip about the center, so the profile there is L²/12 + L²/4 = L²/3, and all 32 J is turning about it. Take the mass out of the punch and it's the zip, ½v², energy per kilogram: 3 J/kg of zip for the center, and 1 J/kg more for the turning."),
 ("The turning hooks ½ × (2/5)(1.0)(0.050)² × 40² = 0.80 J: two fifths of the punch again.",
  "The turning hooks ½ × (2/5)(1.0)(0.050)² × 40² = 0.80 J: two fifths of the punch again. The center zips at 2.0 J/kg, and the ball zings at ½ × 40², 800."),
 ("The same heft gives less punch, the ball runs slower and comes round later.",
  "The same heft gives less punch, the ball runs slower and comes round later: per kilogram, the heft splits five to two between zip and the turning's share."),
 ("At the bottom they point opposite ways and cancel. The bottom point is still for that instant.",
  "At the bottom they point opposite ways and cancel. The bottom point is the still point for that instant, and a moment later a different point is."),
 ("Forward 2.0 m/s and down 2.0 m/s make 2√2, about 2.8 m/s, 45° below forward.",
  "Forward 2.0 m/s and down 2.0 m/s make 2√2, about 2.8 m/s, 45° below forward. From the still point at the bottom it's the same answer: the front point is √2 radii away, so it runs at √2 of 2.0 m/s, at right angles to the line from the still point."),
 ("the puck punches 1.0 J at first and 4.0 J at the end, so 3.0 J.",
  "the puck punches 1.0 J at first and 4.0 J at the end, so 3.0 J. Per kilogram, its zip goes from 2 to 8."),
 ("(2) The squares are in the ratio (2 + √2)/(2 − √2). Multiply top and bottom by 2 + √2 and it's (2 + √2)²/2, so the sweeps are in the ratio (2 + √2)/√2 = 1 + √2.",
  "(2) The squares are in the ratio (2 + √2)/(2 − √2). Multiply top and bottom by 2 + √2 and it's (2 + √2)²/2, so the sweeps are in the ratio (2 + √2)/√2 = 1 + √2. Flip it and the slow over the fast is √2 − 1: the two multiply to one."),
 ("(3) In the slow mode the lower angle is +√2 times the upper: both masses swing the same way, the lower one farther. In the fast mode it's −√2 times: whenever the upper mass swings one way, the lower one swings the other. In either mode, each rod picks up at ω² of its own lean, back toward vertical.",
  "(3) Each mode is a tone, and its shape is how far the lower rod leans for the upper's lean: Ω_shape = +√2 for the slow tone, both masses swinging the same way, the lower one farther; and −√2 for the fast tone, the lower rod flipped. In either tone, each rod picks up at ω² of its own lean, back toward vertical. Both tones at once make a chord, and the chord beats at the gap, 5.84 − 2.42 = 3.42 stroke a second."),
 ("When κi and ȧ have opposite signs, κiȧ is negative, and the rod's giving its energy to the circuit instead.",
  "When κi and ȧ have opposite signs, κiȧ is negative, and the rod's giving its energy to the circuit instead. It's a trade: a belt, not a battery. Nothing's made."),
 ("Their product is ω₀², 5.86 per second squared, and the faster is 9/4 of the slower: 4 to 9.",
  "Their product is ω₀², 5.86 per second squared, and the faster is 9/4 of the slower: 4 to 9. They're a mirror pair about ω₀: 2/3 and its flip, 3/2. These are the coupled machine's two tones."),
 ("It seems to arrive before anyone sends anything because nobody sent it.",
  "It seems to arrive before anyone sends anything because nobody sent it. The fast crest is a stripe: a ghost body with a place, a velocity and a phase, and nothing stored. Phase is for ghosts. The two crest speeds are each other's flip about u: u/9 and 9u multiply to u²."),
 ("There γ = 1/√(1 − 0.36) = 1/0.80 = 1.25.",
  "There γ = 1/√(1 − 0.36) = 1/0.80 = 1.25. From that frame the 80 mJ pulse is shifted down by 2 and the 20 mJ pulse up by 2: 40 mJ each. The stretch is the mean of the shift and its flip, (2 + 1/2)/2 = 5/4, the same γ."),
 ("Four and nine share no factor, so the first full return is νT = τ: four turns of the slow part and nine of the fast.",
  "Four and nine share no factor, so the first full return is νT = τ: four turns of the slow tone and nine of the fast, the chord whole again."),
]

# ---------------- Level 4: one machine; zam, zlam; in step, at random, the tap; TEST and RUN; zow, zlow (zower, zlower) ----------------
LEVEL[4] += [
 # path 4's first new arrival is the kitchen's pair, zing and zlow (path 2 opens on a word at the knife, path 3 on a place at the ladder)
 ("The engine paid in equal hook every second, not equal sweep, so four times the hook only doubles the sweep.",
  "The engine paid in equal hook every second, not equal sweep, so four times the hook only doubles the sweep. With the inertia taken out, hook is the zing, ½ω²: the wheel zings at 8 at the start and 32 at the end."),
 ("With the inertia taken out, hook is the zing, ½ω²: the wheel zings at 8 at the start and 32 at the end.",
  "With the inertia taken out, hook is the zing, ½ω²: the wheel zings at 8 at the start and 32 at the end. Power on the inertia is the zlow, and its verb is zlower: 3.0 W on 0.50 kg m² is a zlow of 6, so the engine zlowers the wheel at 6 zing a second, steadily, 8 to 32 in four seconds. Power on the mass would be the zow, and its verb zower."),
 ("These are the coupled machine's two tones.",
  "These are the two tones of one machine: rods and loop together."),
 ("four turns of the slow tone and nine of the fast, the chord whole again.",
  "four turns of the slow tone and nine of the fast, the chord whole again, the one machine's return."),
 ("so the other 68 mJ is the rods' punch.",
  "so the other 68 mJ is the rods' punch. That's 25 and 144 out of 169: a 5–12–13 triangle, the can's share and the rods'."),
 ("The chair stays at x_H = 0 for the whole run.",
  "The chair stays at x_H = 0 for the whole run. This is RUN: nothing taps the machine, so its two tones lining up adds nothing."),
]

# doc 17:17-17:18: the book's body factor (end of Straight→ Mechanics, and 1.1.1 Bodies), in paths 3 and 4 only.
# A stagehand: offstage until there's something to do. 9-3 asks about the masses; the shape is the rods'.
BODY_9_3 = ("The shape is the rods'. The question asks about the masses, and with two of them in one problem it helps to say whose each quantity is.\n"
 "Call the upper rod with its mass body U, and the lower one body L. A body is the thing as the physics sees it: where it is, how it moves, what it carries, and nothing else. "
 "Write the body last in a quantity, after its size and its direction, and read × as “of”: 1 m × U is the length of body U, and 0.10 rad → × U is its swing. The knife of the knife was the knife all along, but the knife of a ladder has nothing to be, and no place to go.\n"
 "A mass at the end of its rod is out by the rod's length of the rod's swing:\n"
 "    1 m × U × 0.10 rad → × U = 1 m × 0.10 rad → × U × U = 0.10 m → × U × U.\n"
 "That's 0.10 m forward of body U of body U, which is just body U: the upper mass is out 0.10 m → × U. "
 "The lower rod's length of the upper rod's swing, 1 m × L × 0.10 rad → × U, comes to 0.10 m → × L × U, body L of body U.\n"
 "So the lower mass can't take the upper swing through its own rod. It rides on the upper mass instead: it starts wherever U's mass is, 0.10 m → × L, and its own rod adds its own length of its own swing. "
 "In the slow tone the lower rod swings √2 as far the same way, 0.14 rad →:\n"
 "    0.10 m → × L + 1 m × L × 0.14 rad → × L = 0.24 m → × L.\n"
 "In a sum the bodies keep their parts apart, the way ← and ↑ do, so the two masses sit at 0.10 m → × U + 0.24 m → × L: both the same way, the lower one 1 + √2 times as far. "
 "In the fast tone the lower rod swings √2 as far the other way, 0.14 rad ←:\n"
 "    0.10 m → × L + 1 m × L × 0.14 rad ← × L = 0.041 m ← × L.\n"
 "The masses sit at 0.10 m → × U + 0.041 m ← × L. The lower one goes the other way, but only √2 − 1 as far, about 0.41. Its rod leans farther than the upper one, and the mass at its end moves less.\n")
LEVEL[3] += [
 ("and −√2 for the fast tone, the lower rod flipped. In either tone,",
  "and −√2 for the fast tone, the lower rod flipped.\n" + BODY_9_3 + "In either tone,"),
]
LEVEL[4] += [   # a highlight, not the cutscene again
 (BODY_9_3,
  "The shape is the rods'. Each mass is out by its own rod's length of its own swing, and the lower one rides on the upper: the L of the U has nothing to be. With the body written last, "
  "swinging the upper rod 0.10 rad → puts them at 0.10 m → × U + 0.24 m → × L in the slow tone and 0.10 m → × U + 0.041 m ← × L in the fast: "
  "the lower mass goes the other way, but only √2 − 1 as far.\n"),
]
