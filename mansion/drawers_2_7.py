"""Builds the Docs batch that appends cabinet drawers 2-7 to the below-stairs doc (CL-216).

Claude (Anthropic), 2026-10-21. Usage: python3 drawers_2_7.py START > batch.json
"""
import json, sys

B = []  # (kind, text): H3, DOOR, P, ITEM, H4, PASS
def drawer(title, door, stmt_intro, items, sols, passage=None):
    B.append(("H3", title)); B.append(("DOOR", door))
    if stmt_intro: B.append(("P", stmt_intro))
    for i, t in enumerate(items, 1): B.append(("ITEM", f"{i}. {t}"))
    B.append(("H4", "Solution"))
    for t in sols: B.append(("P", t))
    if passage: B.append(("PASS", passage))

drawer("Drawer 2: the wall lets go",
 "Door: the library. A gentleman's reading kit in circus colors: a folding rule, spectacles, a little ladder leaning on a painted wall.",
 "A uniform ladder of mass m and length L leans on a frictionless wall from a frictionless floor, its top at height h₀. It's released from rest. Use g = 10 m/s².",
 ["While both ends touch, show that the ladder's center stays L/2 from the corner where the wall meets the floor.",
  "While both ends touch, show that the ladder's kinetic energy is (1/6)mL²ω², where ω is its angular speed.",
  "The wall can push but can't pull. Show that the top leaves the wall when its height is 2h₀/3.",
  "For L = 3.0 m and h₀ = 2.4 m, find that height and the center's speed then."],
 ["(1) Call the ladder's angle with the floor φ. The foot is L cos φ out and the top L sin φ up, so the center sits at half of each. That's a circle of radius L/2 about the corner.",
  "(2) The center runs round its circle at (L/2)ω and punches ½m(L/2)²ω². The ladder's own turning hooks ½m(L²/12)ω² on top. The profiles add, L²/4 + L²/12 = L²/3, so the whole is ½m(L²/3)ω² = (1/6)mL²ω².",
  "(3) With the top at height y, the center has dropped (h₀ − y)/2, so the heft let go is mg(h₀ − y)/2, and ω² = 3g(h₀ − y)/L². The wall's push is the only sideways force, so it's what speeds the center up sideways. The center's sideways speed is (L/2)ω sin φ = ωy/2, and its square, 3gy²(h₀ − y)/(4L²), grows while y²(h₀ − y) grows. That peaks where 2h₀y = 3y², at y = 2h₀/3. Past there the center would have to slow down sideways, and that takes a pull. The wall can't pull, so it lets go.",
  "(4) Two thirds of 2.4 m is 1.6 m. Then ω² = 3 × 10 × 0.8/9 = 8/3, and the center runs at 1.5√(8/3) = √6 = 2.4 m/s."],
 "Passage: the back of this drawer opens on funhouse problem 4.")

drawer("Drawer 3: turning about the contact",
 "Doors: the conservatory, the billiard room, the ballroom. A clockwork diorama under a striped dome: a glass marble in a tin basin, a tiny cue, a wire hoop.",
 "A uniform solid ball has mass m, radius R and moment of inertia (2/5)mR² about its center. Use g = 10 m/s².",
 ["It rolls without slipping, its center at speed v. Show that its kinetic energy is (7/10)mv², 7/5 of a sliding bead's at the same speed.",
  "It rolls back and forth in a basin, its center on an arc of radius a. Show that small oscillations have T = 2π√(7a/(5g)), and find the a that matches a simple pendulum 1.0 m long.",
  "A cue gives it a short horizontal impulse at height H above the table. Show that it rolls at once only if H = 7R/5.",
  "A hoop rolls with its center at speed v. Find the speeds of its top and bottom points. Which point of the hoop is still?"],
 ["(1) While it rolls, the bottom of the ball is still for that instant, so the ball turns about the contact. Its profile about its center is (2/5)R²; about the contact it gains R², the center's square, for (7/5)R². Sweeping at v/R, it hooks ½m(7/5)R²(v/R)² = (7/10)mv²: 7/5 of the ½mv² a sliding bead would punch.",
  "(2) Swung θ from the bottom, the center sits a(1 − cos θ) up, about aθ²/2, so the heft is mgaθ²/2. The center runs at aθ̇, so the energy in motion is (7/10)ma²θ̇². A heft that goes as the swing squared, traded against motion that goes as the sweep squared, cycles at ω² = ga/((7/5)a²) = 5g/(7a), so T = 2π√(7a/(5g)). The knife's 1.0 m needs 7a/5 = 1.0 m, so a = 5/7 m. The ball keeps the knife's time because a shorter arc pays for the extra two fifths of turning.",
  "(3) Count about the line on the table under the ball. During the blow nothing else has leverage there, so the blow J at height H leaves JH of spin about it. Rolling at once means the center runs at v = J/m while the ball sweeps at v/R, and that's (7/5)mR²(v/R) = (7/5)RJ of spin about the contact. So H = 7R/5: the cue goes in two fifths of a radius above the center.",
  "(4) The center runs at v and the rim sweeps round it at v. At the top the two add, for 2v; at the bottom they cancel. The bottom point is still for that instant, and a moment later a different point is: the still point keeps changing."])

drawer("Drawer 4: the second knife's two tones",
 "Door: the dining room. A silver canteen with a juggler painted on the lid; inside, under glass, one knife hanging from another.",
 "Two point masses m hang in series on light rods each ℓ long, swinging in one vertical plane. For small angles θ₁ (upper rod) and θ₂ (lower rod) from the vertical, 2θ̈₁ + θ̈₂ = −2(g/ℓ)θ₁ and θ̈₁ + θ̈₂ = −(g/ℓ)θ₂.",
 ["In a normal mode both angles go as cos ωt, with θ₂ = +√2 θ₁ or θ₂ = −√2 θ₁. Find ω² for each.",
  "With ℓ = 1.0 m and g = 10 m/s², find both ω and their ratio. Does a motion with both modes ever exactly repeat?"],
 ["(1) In a mode both rods pick up at −ω² times their angle. The first balance gives (2 ± √2)ω²θ₁ = 2(g/ℓ)θ₁, so ω² = 2g/((2 ± √2)ℓ) = (2 ∓ √2)g/ℓ. The second balance gives the same two. The shape where the lower rod leans the same way, +√2, is the slow one.",
  "(2) ω² = 10(2 − √2) = 5.86 and 10(2 + √2) = 34.1, so 2.42 and 5.84 rad/s. Their ratio is (2 + √2)/√2 = 1 + √2. That's irrational, so a motion with both modes never quite repeats."],
 "Passage: the back of this drawer opens on funhouse problem 1.")

drawer("Drawer 5: a can to match the knife",
 "Door: the study. A doctor's bag in striped oilcloth: a capacitor the size of a teacup, a coil, a card of figures.",
 "An LC circuit has L = 0.10 H.",
 ["Find the C that makes ω₀ = 1/√(LC) equal the slow mode of drawer 4, 2.42 rad/s.",
  "With that C, how long does one turn of the circuit take, and one turn of the slow mode?"],
 ["(1) C = 1/(Lω₀²), and ω₀² = 10(2 − √2) = 5.86 s⁻², so C = 1/(0.10 × 5.86) = 1.71 F.",
  "(2) Both take 2.60 s. Same ω, same turn: matched, the rods and the loop can trade energy turn for turn once they're coupled."],
 "Passage: the back of this drawer opens on funhouse problem 2.")

drawer("Drawer 6: two crests from two waves",
 "Door: the hall. A hatbox in red and white stripes; inside, a long coil of wire and two tuning forks.",
 "Two waves of equal amplitude A run in opposite directions on a line with wave speed u: A cos(k₁x − ω₁t) to the right and A cos(k₂x + ω₂t) to the left, with k = ω/u for each.",
 ["Show that their sum is 2A cos(½[(k₁ − k₂)x − (ω₁ + ω₂)t]) cos(½[(k₁ + k₂)x − (ω₁ − ω₂)t]).",
  "Find the speed of each factor's crests, in terms of u and the two frequencies.",
  "For 5.0 MHz and 4.0 MHz and u = 1.0 × 10⁸ m/s, find both speeds."],
 ["(1) cos P + cos Q = 2 cos(½(P − Q)) cos(½(P + Q)), with P = k₁x − ω₁t and Q = k₂x + ω₂t.",
  "(2) A crest of either factor keeps what's inside it fixed, so it moves at the time coefficient over the place coefficient: (ω₁ + ω₂)/(k₁ − k₂) = u(f₁ + f₂)/(f₁ − f₂) for the first, and u(f₁ − f₂)/(f₁ + f₂) for the second.",
  "(3) The sum is 9 MHz and the difference 1 MHz, so the crests run at 9u = 9.0 × 10⁸ m/s, three times light's speed, and u/9 = 1.1 × 10⁷ m/s. The fast crest is only where waves that were already there happen to line up. It carries nothing: that's the hall's stripe."],
 "Passage: the back of this drawer opens on funhouse problem 3.")

drawer("Drawer 7: two lights made equal",
 "Door: the lounge. A traveling clock case in faded red leather; inside, two little lamps, one brighter than the other.",
 "Seen from a frame moving at βc in a light pulse's own direction, the pulse's energy is multiplied by √((1 − β)/(1 + β)); seen from one moving against it, by √((1 + β)/(1 − β)). A pulse of energy E₁ runs right and one of E₂ runs left, with E₁ > E₂.",
 ["Find β for the frame moving right in which the two energies are equal, in terms of r = E₁/E₂.",
  "Show that γ = (r + 1)/(2√r) there.",
  "For r = 4, find β and γ, and show that r − 1, 2√r and r + 1 make a right triangle."],
 ["(1) Write s = √((1 − β)/(1 + β)). Equal means E₁s = E₂/s, so s² = 1/r, and β = (r − 1)/(r + 1).",
  "(2) 1 − β² = 4r/(r + 1)², so γ = (r + 1)/(2√r).",
  "(3) r = 4 gives β = 3/5 and γ = 5/4. (r − 1)² + (2√r)² = r² + 2r + 1 = (r + 1)², so a ratio that's a perfect square makes the triangle whole: 4 makes 3–4–5. The 80 mJ pulse is halved and the 20 mJ pulse doubled, 40 mJ each."],
 "Passage: the back of this drawer opens on funhouse problem 3.")

start = int(sys.argv[1])
lines = [t for k, t in B]
text = "\n" + "\n".join(lines)
reqs = [{"insertText": {"text": text, "location": {"index": start}}}]
s0 = start + 1; tend = start + len(text)
reqs.append({"deleteParagraphBullets": {"range": {"startIndex": s0, "endIndex": tend}}})
reqs.append({"updateTextStyle": {"range": {"startIndex": s0, "endIndex": tend}, "textStyle": {"bold": False, "italic": False}, "fields": "bold,italic"}})
pos = s0
named = {"H3": "HEADING_3", "H4": "HEADING_4"}
for k, t in B:
    end = pos + len(t)
    ps = {"namedStyleType": named.get(k, "NORMAL_TEXT"),
          "indentStart": {"magnitude": 30 if k == "ITEM" else 0, "unit": "PT"},
          "indentFirstLine": {"magnitude": 12 if k == "ITEM" else 0, "unit": "PT"}}
    reqs.append({"updateParagraphStyle": {"range": {"startIndex": pos, "endIndex": end + 1 if end < tend else end}, "paragraphStyle": ps, "fields": "namedStyleType,indentStart,indentFirstLine"}})
    if k in ("DOOR", "PASS"):
        reqs.append({"updateTextStyle": {"range": {"startIndex": pos, "endIndex": end}, "textStyle": {"italic": True}, "fields": "italic"}})
    pos = end + 1
assert pos - 1 == tend
assert all(ord(c) < 0x10000 for c in text)
print(json.dumps(reqs, ensure_ascii=False))
