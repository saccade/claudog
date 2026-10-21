"""Builds the Docs batch that appends the funhouse (F1-F4) and understage (U1-U2) to CL-216.

Claude (Anthropic), 2026-10-21. Usage: python3 below_levels.py START > batch.json
Kinds: H2 heading, CUE italic, H3, DOOR italic, P, ITEM indented, H4, PASS italic.
"""
import json, sys
B = []
def prob(title, door, intro, items, sols, passage=None):
    B.append(("H3", title)); B.append(("DOOR", door))
    if intro: B.append(("P", intro))
    for i, t in enumerate(items, 1): B.append(("ITEM", f"{i}. {t}"))
    B.append(("H4", "Solution"))
    for t in sols: B.append(("P", t))
    if passage: B.append(("PASS", passage))

B.append(("H2", "The funhouse"))
B.append(("CUE", "mirrors on every wall, some flat and some not; a floor that tilts one way and then the other; everything you know comes back at you flipped; no one else in here"))
prob("F1: the knives, flipped",
 "Passage: from drawer 4. A long mirror in which the second knife hangs upside down.",
 "The double pendulum of drawer 4 has 2θ̈₁ + θ̈₂ = −2(g/ℓ)θ₁ and θ̈₁ + θ̈₂ = −(g/ℓ)θ₂, with ℓ = 1.0 m and g = 10 m/s².",
 ["In a normal mode θ₂ = rθ₁ and both angles go as cos ωt. Use both equations to show that r² = 2.",
  "Show that the two modes' angular frequencies satisfy ω_b/ω_a = 1 + √2 and ω_a/ω_b = √2 − 1, and that ω_a²ω_b² = 2(g/ℓ)².",
  "With both modes present, at what angular frequency does the motion beat?"],
 ["(1) In a mode both rods pick up at −ω² times their angle, and the lower rod leans Ω_shape times as far as the upper. The first balance gives (2 + Ω_shape)ω² = 2g/ℓ and the second (1 + Ω_shape)ω² = Ω_shape g/ℓ. Divide one by the other: (2 + Ω_shape)Ω_shape = 2(1 + Ω_shape), so Ω_shape² = 2. The shape is +√2 or −√2: the same lean, or the lower rod flipped.",
  "(2) Each shape is a tone, and each tone's cycle sweeps at its own rate: ω_a² = (2 − √2)g/ℓ and ω_b² = (2 + √2)g/ℓ, whose product is 2(g/ℓ)². The fast over the slow is √((2 + √2)/(2 − √2)) = 1 + √2, and the slow over the fast is its reflection, √2 − 1. The two multiply to one. Flip the lower rod and you've flipped the tone.",
  "(3) Both tones at once make a chord, and the chord beats at the gap between them: 5.84 − 2.42 = 3.42 stroke a second. The ratio is irrational, so the beat never brings the chord exactly back."],
 "Trapdoor, the swing side: in the floor under the mirror, and through it the same two rods, full size, on a black iron chassis with a chipped ceramic insulator. They're humming. (Nailed down until patch 3.)")
prob("F2: the trade, both ways",
 "Passage: from drawer 5. Two facing mirrors; the can in one is the coil in the other.",
 "The slow mode of the double pendulum acts like one swing a with effective inertia η and stiffness D, so its free angular frequency is ω₀ = √(D/η). A coil in a magnetic field couples it to an LC circuit with the same ω₀ = 1/√(LC): ηä = −Da + κi and Lq̈ = −q/C − κȧ, with i = q̇.",
 ["Try a = A cos ωt and q = Q sin ωt. Show that ηL(ω₀² − ω²)² = κ²ω².",
  "Show that the two positive solutions multiply to ω₀² and differ by κ/√(ηL).",
  "What κ puts the two modes at (2/3)ω₀ and (3/2)ω₀? With ω₀ = 2.42 rad/s, find both."],
 ["(1) Put the trial motions in. The swing's balance gives (D − ηω²)A = κωQ and the loop's gives (1/C − Lω²)Q = κωA. Multiply them; D = ηω₀² and 1/C = Lω₀² turn the left side into ηL(ω₀² − ω²)²AQ, so ηL(ω₀² − ω²)² = κ²ω². The charge runs a quarter turn of the cycle from the lean.",
  "(2) Take the square root: ω₀² − ω² = ±sω, with s = κ/√(ηL). Each sign gives one positive root, and the two are (√(s² + 4ω₀²) ± s)/2. Their product is ω₀² and their gap is s: a mirror pair, one tone ω₀ times something and the other ω₀ over it.",
  "(3) 3/2 − 2/3 = 5/6, so s = (5/6)ω₀ and κ = (5/6)ω₀√(ηL). The tones cycle at 1.61 and 3.63 stroke a second. The power the field puts into the swing, κiȧ, is exactly what the loop gives up: a belt, not a battery. Energy goes round and comes back; nothing's made."],
 "Trapdoor, the circuit side: windings and a capacitor the size of a hatbox, wired into the same chassis, with the chipped insulator again. (Nailed down until patch 3.)")
prob("F3: two more mirrors",
 "Passage: from drawers 6 and 7. A hall of mirrors that never ends, and a lamp in it that can't decide how bright it is.",
 None,
 ["For the crests of drawer 6, show that the slow and fast crest speeds multiply to u², whatever the two frequencies.",
  "On a lossless line a wave pattern stores (C′V² + L′I²)/2 per meter and carries power VI. Show that |VI| is never more than u times the stored energy per meter. Can the fast crest carry a signal?",
  "For drawer 7's lights, show that the two energies multiply to the same number in every frame moving along the line, and check it with 80 mJ and 20 mJ. If flashes from something going away arrive s = 2 times farther apart, show that (s + 1/s)/2 is drawer 7's γ."],
 ["(1) u(f₁ − f₂)/(f₁ + f₂) times u(f₁ + f₂)/(f₁ − f₂) is u². The crests are each other's reflection about u: one nine times under it, one nine times over.",
  "(2) A sum of two squares is never less than twice their product, so (C′V² + L′I²)/2 ≥ √(C′L′)|VI| = |VI|/u. Energy goes no faster than u, and no signal outruns its energy. The fast crest is a stripe: where waves already there happen to line up. It has phase and nothing else, and phase is for ghosts. The stripe is one: a place and a velocity, carrying nothing.",
  "(3) From a frame moving along the line, one pulse's energy is multiplied by s and the other's divided by s, so their product stays put: 80 × 20 = 40 × 40. Twice its square root, 80 mJ, is the pair's rest energy. The shift is s = 2, and the stretch is the mean of the shift and its flip, (2 + 1/2)/2 = 5/4: drawer 7's γ."],
 "Trapdoor, the timing side: a clock face on the same chassis, one hand, marked in turns, with the chipped insulator under it. (Nailed down until patch 3.)")
prob("F4: the corner, turned over",
 "Passage: from drawer 2. A tilted floor, and a mirror at the end that shows the room upside down.",
 "The ladder of drawer 2 has its foot at (L cos φ, 0) and its top at (0, L sin φ), with the corner where the wall meets the floor at the origin.",
 ["The foot moves along the floor and the top along the wall. Show that the point that's still for the instant, where the perpendiculars to the two ends' motions meet, is (L cos φ, L sin φ).",
  "Show that this point is the corner turned a half turn about the ladder's center, so it's always L/2 from the center.",
  "About that point all the motion is turning. Show that the kinetic energy is ½m(L²/3)ω², and find the energy per kilogram when the top leaves the wall, in drawer 2's numbers."],
 ["(1) The foot only moves sideways, so the still point is straight above it. The top only moves up and down, so the still point is level with it: (L cos φ, L sin φ).",
  "(2) The center, at (L cos φ, L sin φ)/2, sits halfway between the corner and the still point. Turn the corner over through the center, a half turn, π, the flip, and it lands on the still point. So the still point is L/2 from the center, like the corner.",
  "(3) The ladder's profile about its center is L²/12; about the still point it gains (L/2)², for L²/3. All the motion is turning, so the energy per kilogram is that profile across the zing, ½ω²: (L²/3)(ω²/2). With L = 3.0 m and ω² = 8/3 per second squared as the wall lets go, that's 3 × 4/3 = 4 J/kg, and 8.0 kg of ladder makes 32 J: the heft let go. The center's own zip, ½((L/2)ω)², is 3 J/kg of it; turning about the center makes up the other 1."])

B.append(("H2", "The understage"))
B.append(("CUE", "a low room under the stage; one machine on a black iron chassis, bigger than it looked through the trapdoors; the chipped ceramic insulator; a hum not quite loud enough to cover the whispers; stagehand blacks on a nail, still warm; no one else down here"))
prob("U1: the machine, all of it",
 "Service entrance: any of the three trapdoors. They all come down here.",
 "Take the coupled machine of funhouse problem 2 with its tones at (2/3)ω₀ and (3/2)ω₀, written 4ν and 9ν, so ν = ω₀/6. Scale the swing and the charge as X = √η a and Y = √L q, so that Ẍ = −ω₀²X + sẎ and Ÿ = −ω₀²Y − sẊ, with s = 5ν. It starts with Y = Y₀, X = 0, and nothing moving.",
 ["Show that the slow mode has X = −B₁ sin 4νt and Y = B₁ cos 4νt, and the fast mode X = B₂ sin 9νt and Y = B₂ cos 9νt.",
  "Fit the start and show that B₁ = (9/13)Y₀ and B₂ = (4/13)Y₀.",
  "Find the first time the whole state returns, and how the energy is shared between the swing's motion and the capacitor halfway there.",
  "With ω₀ = 2.42 rad/s and 80 mJ in the machine, how long is the return?"],
 ["(1) Put each trial in. The swing's balance gives (ω₀² − ω²)A = −sωB and the loop's (ω₀² − ω²)B = −sωA, so A = ±B and ω₀² − ω² = ∓sω. In units of ν, 36 − 16 = 20 = 5 × 4 for the slow mode, with A = −B, and 36 − 81 = −45 = −5 × 9 for the fast one, with A = B.",
  "(2) At the start Y = B₁ + B₂ = Y₀, and the swing isn't moving: −4νB₁ + 9νB₂ = 0. So B₂ = (4/9)B₁, B₁ = (9/13)Y₀ and B₂ = (4/13)Y₀.",
  "(3) Both parts come back when 4νT and 9νT are whole turns. Four and nine share no factor, so the first time is νT = τ: four turns low and nine turns high. Halfway, the slow part has made two whole turns and the fast part four and a flip. Then Y = (5/13)Y₀ and Ẋ = −(12/13)ω₀Y₀, so the capacitor holds (5/13)² of the energy and the swing's motion (12/13)²: 25 and 144 out of 169, a 5–12–13 triangle made from 2² and 3².",
  "(4) T = τ/ν = 6τ/ω₀ = 15.6 s. Across the return the machine carries its 80 mJ through 15.6 s: 1.2 J s of action. Per kilogram of the rods' 2 kg, that's 0.62 zam, which nobody asked for."])
prob("U2: TEST, then RUN",
 "On the chassis: a switch with two positions, TEST and RUN, and a small drive arm that can tap the slow mode.",
 "In TEST a drive gives the machine's slow mode N equal short taps, each adding the same small speed to X. Start from rest, and let E₁ be the energy one tap gives the mode from rest.",
 ["If every tap lands at the same point of the cycle, show that after N taps the mode's energy is N²E₁, and that the k-th tap does (2k − 1)E₁ of work.",
  "If each tap lands at a random point of the cycle, independent of the others, show that the expected energy after N taps is NE₁.",
  "Compare the two after 100 taps.",
  "In RUN the drive is disconnected and the machine is lossless. Does its energy change when its two tones line up at the return?"],
 ["(1) Each tap adds the same arrow to the mode's state, an arrow that turns with the cycle. Landing at the same point of the cycle, the arrows all point the same way, so N of them make one N times as long, and the energy, which goes as its square, is N²E₁. The k-th tap meets a mode that's already moving and does k² − (k − 1)² = 2k − 1 units of work: the drive pays more for each one.",
  "(2) Landing at random points, the arrows point every which way. The square of the sum is the sum of the squares plus cross terms, and the cross terms average to zero, so the expected energy is NE₁: a random walk.",
  "(3) A hundred taps in step: a hundred times the amplitude and 10,000 E₁. At random: about ten times the amplitude and 100 E₁. Same taps, same drive, a hundred times the shake.",
  "(4) No. Lined up or not, the closed machine keeps its 80 mJ; the return just puts it all back in the capacitor. Lining up only matters while something's pushing. In TEST something is, and that's what a tap just ahead of a pile-up is for: it breaks the step."])

start = int(sys.argv[1])
lines = [t for k, t in B]
text = "\n" + "\n".join(lines)
reqs = [{"insertText": {"text": text, "location": {"index": start}}}]
s0 = start + 1; tend = start + len(text)
reqs.append({"deleteParagraphBullets": {"range": {"startIndex": s0, "endIndex": tend}}})
reqs.append({"updateTextStyle": {"range": {"startIndex": s0, "endIndex": tend}, "textStyle": {"bold": False, "italic": False}, "fields": "bold,italic"}})
named = {"H2": "HEADING_2", "H3": "HEADING_3", "H4": "HEADING_4"}
pos = s0
for k, t in B:
    end = pos + len(t)
    ps = {"namedStyleType": named.get(k, "NORMAL_TEXT"),
          "indentStart": {"magnitude": 30 if k == "ITEM" else 0, "unit": "PT"},
          "indentFirstLine": {"magnitude": 12 if k == "ITEM" else 0, "unit": "PT"}}
    reqs.append({"updateParagraphStyle": {"range": {"startIndex": pos, "endIndex": min(end + 1, tend)}, "paragraphStyle": ps, "fields": "namedStyleType,indentStart,indentFirstLine"}})
    if k in ("DOOR", "PASS", "CUE"):
        reqs.append({"updateTextStyle": {"range": {"startIndex": pos, "endIndex": end}, "textStyle": {"italic": True}, "fields": "italic"}})
    pos = end + 1
assert pos - 1 == tend and all(ord(c) < 0x10000 for c in text)
print(json.dumps(reqs, ensure_ascii=False))
