"""Path 4's highlights reel: the old material said briskly, in the established vocabulary, like a fast car: not
minimal, just good clean fun (doc, 20:44).

Claude (Anthropic), 2026-10-22, from doc's 20:43: "short is good on the last one, we've established the vocab by then.
no one at that point can seriously doubt that it works ... bang the old stuff out like everyone has known power is the
sweep of torque since middle school." Every part the problem set asks still gets its answer; the numbers are the
checked ones (two figures). New to path 4 and kept at full length: the zing and zlow landing at 2-b, the body
highlight at 9-c, under the stage (α, β), the crown line, and the ending.
build_sets applies REEL4 to path 4's final text: each labeled part is replaced, and the unlabeled working lines that
followed it are dropped, except the house's story beats (KEEP).
"""
H = " "
D = f"{H}·{H}"

KEEP = ("The pen begins", "The back of this drawer", "Trapdoor", "In the far glass", "Each costume is missing",
        "They were all cut", "From a corner", "Its twin", "“Zlam", "The hum covers")

REEL4 = {
 '1-a': '(1-a) A 0.10 rad lean lifts the knife ℓθ²/2, 5 mm, and 10 N of weight through 5 mm hefts 0.050 J.',
 '1-b': '(1-b) Let go, it trades the whole 0.050 J of heft for punch by the bottom. The mass rides on both sides and cancels: v² = 2gh = 0.10 m²/s², and the knife comes through at 0.32 m/s.',
 '1-c': '(1-c) ℓω² = g puts the cycle at √10, about 3.2 sweep, and T = τ/√10: two seconds a turn, near enough. No stray 2 this time; the turn brought its own sign.',
 '1-d': "(1-d) Double the mass and you double the heft, the punch, and the reluctance to be hurried, all together. T doesn't budge. The cycle never asked for the mass.",
 'd-1': "(d-1) In a mode both rods pick up at ω² of their lean, back toward vertical. The upper rod's balance, (2 ± √2)ω² = 2g/ℓ, hands back ω² = (2 ∓ √2)g/ℓ, and the lower rod's agrees. Lean the same way, +√2, and you get the slow one.",
 'd-2': '(d-2) 5.9 and 34 per second squared: the slow tone sweeps at 2.4, the fast at 5.8, and they stand at 1 + √2. Irrational, so the pair never quite comes round together.',
 '1-α': '(1-α) Let the lower rod lean Ω_shape of the upper. The two balances read (2 + Ω_shape)ω² = 2g/ℓ and (1 + Ω_shape)ω² = Ω_shape g/ℓ; divide them and the sweep drops out: Ω_shape² = 2. Plus or minus √2: lean together, or flip the lower rod.',
 '1-β': '(1-β) ω_a² = (2 − √2)g/ℓ and ω_b² = (2 + √2)g/ℓ, whose product is 2(g/ℓ)². Fast over slow is 1 + √2, slow over fast √2 − 1, and the two multiply to one: flip the rod, flip the tone.',
 '1-γ': "(1-γ) Sound both tones and the chord's phase sweeps at the gap, 3.4 sweep: equal shares of the upper lean pile up every 1.8 s, and the signed envelope comes home in twice that. The chord itself never does; the ratio's irrational.",
 '2-a': "(2-a) Fifteen joules of heat-in, three of work, twelve of heat-out, and the engine's back where it began: 20%, and at a cycle a second, 3.0 W.",
 '2-b': "(2-b) 0.50 kg m² sweeping at 4.0 hooks 4.0 J. Four seconds at 3.0 W pour in 12 J of hook, 16 J in all, and the wheel's sweeping at 8.0: four times the hook buys twice the sweep. Take the inertia out of the hook and what's left is the zing, ½ω²: the wheel zings at 8 to start and 32 to finish. Power on the inertia is the zlow, and its verb is zlower: 3.0 W on 0.50 kg m² is a zlow of 6, so the engine zlowers the wheel at a steady 6 zing a second, 8 to 32 in four seconds flat. Power on the mass is the zow, and it zowers.",
 '2-c': "(2-c) Power is the sweep of torque. Grab the χ off the wall like usual, no time to slow down here: P = ωχ. At 4.0 sweep the engine's 3.0 W cranks with 0.75 N m; at 8.0, with 0.38. Twice the sweep, half the crank, and the wheel picks up at 1.5 sweep a second, then 0.75.",
 '3-a': "(3-a) The arm's pull holds the weight with its upward part and bends the path with its inward part, mω² of the reach. Those parts stand as the arm's drop to its reach, so the reach cancels and the ball hangs g/ω² = 10/25 = 0.40 m below the hinge: cos θ = 0.80 on the 0.50 m arm, a 3–4–5 about 37° off vertical. Each ball has climbed 0.10 m and hefts 1.0 J.",
 '3-b': "(3-b) The drop g/ω² can't outgrow the 0.50 m arm. Below √(g/ℓ) = √20, about 4.5 sweep, the governor gives up and hangs straight down.",
 '3-c': '(3-c) Both ledgers in arrows: ma → = F → + f → for the center, and Iα ↻ = [Fr + fR] ↺ about the axle, tied by α = a/R. Together, (m + I/R²)a = F(1 − r/R): the spool loads the cord like 3.0 kg, the cord pulls like 2.4 N, and it rolls toward the pull at 0.80 m/s² →. The grip comes out 1.6 N → + 6.0 N ← = 4.4 N ←, cranking ↻ harder than the cord cranks ↺.',
 '3-d': f'(3-d) Hold it still and the grip is →{D}F{D}←, which read from its other end is ←{D}F{D}→, cranking ↺ right along with the cord: Fr ↺ + (←{D}F) R ↺ = 0. The forward part of the pull is r/R of it: cos θ = 0.60, θ = 53°, the 3–4–5 with its 3 on the counter. The inertia never gets a vote.',
 'a-1': "(a-1) The governor's move again: the ball hangs g/ω² below the hinge, and that drop is ℓ cos θ, so cos θ = g/(ℓω²). Below ω = √(g/ℓ), straight down is the only way to hang.",
 'a-2': "(a-2) Drop 4, reach 3, arm 5: cos θ = 4/5, ω² = g/(ℓ · 4/5) = 25, and ω = 5.0 sweep, the kitchen's own shaft. The ball's up 0.10 m.",
 'a-3': "(a-3) Count about the contact; its acceleration points at the axle, so the count is fair, and friction and the counter's push get no leverage there. The cord's line runs R − r above the counter and cranks F(R − r) on the inertia about the contact, I + mR², and the center speeds up at R of that pickup: a = F(1 − r/R)/(m + I/R²). The center's two ledgers say the same.",
 'a-4': '(a-4) 3.0 kg at the axle means I/R² = 1.0 kg: I = 0.040 kg m², half of mR², a plain uniform disk. 2.4 N on 3.0 kg rolls it at 0.80 m/s² →, with friction hauling 4.4 N ←.',
 'a-5': "(a-5) A spool at rest isn't turning, so the pull gets no leverage about the contact: its line, R cos θ − r from the contact, has to run right through it. cos θ = r/R = 3/5, θ = 53°, whatever I is.",
 '4-a': f"(4-a) The ladder won't stretch, so it dots to zero against the top's velocity less the foot's: (1.8 m ← + 2.4 m ↑){D}(0.40 m/s ← + v ↑) = 0.72 m²/s + 2.4 m v = 0. The top comes down at 0.30 m/s ↓.",
 '4-b': '(4-b) The center falls from 1.2 m to 0.80 m, and 80 N through 0.40 m lets go 32 J of heft.',
 '4-c': "(4-c) Count about the still point, L/2 from the center: the profile there is L²/12 + L²/4 = L²/3, and all 32 J is turning about it. The center's punch takes three quarters, 24 J, and the hook about the center the other 8. 8.0 kg punching 24 J runs at √6, about 2.4 m/s, with the ladder sweeping at 2v/L, about 1.6 sweep.",
 'b-1': '(b-1) Foot x out, top y up, center at half of each: half of √(x² + y²) = L from the corner. The center rides a circle of radius L/2.',
 'b-2': '(b-2) Profiles add: L²/4 for riding the circle and L²/12 for turning about itself, L²/3 in all, so the ladder carries ½m(L²/3)ω² = (1/6)mL²ω².',
 'b-3': "(b-3) The heft let go, mg(h₀ − y)/2, sets ω² = 3g(h₀ − y)/L², and the center's sideways speed is ωy/2. Only the wall can speed that up, and its square goes as y²(h₀ − y), which tops out at y = 2h₀/3. Past there the center would have to be pulled back, and a wall can't pull. It lets go, right on schedule.",
 'b-4': "(b-4) Two thirds of 2.4 m is 1.6 m; ω² = 3 × 10 × 0.8/9 = 8/3; and the center's doing 1.5√(8/3) = √6, about 2.4 m/s.",
 '4-α': '(4-α) The foot only slides and the top only drops, so the still point sits over the foot and level with the top: x out, y up.',
 '4-β': "(4-β) The center's halfway between the corner and the still point, so a flip about the center swaps them: the still point is L/2 from the center, same as the corner.",
 '4-γ': "(4-γ) Profile L²/3 about the still point, across the zing, ½ω² = 4/3 per second squared with L = 3.0 m: 4 J/kg, and 8.0 kg makes the 32 J. The center's zip is 3 of the 4; turning about the center is the other 1.",
 '5-a': '(5-a) The cue lands 2.0 N s → on 1.0 kg, and the center punches off at 2.0 m/s →.',
 '5-b': '(5-b) The blow leaves (H − R) ↑ × J → = (H − R) J ↻ of spin about the center. Rolling at once means ω ↻ × R ↓ = ω R ← cancels v →, so ω = v/R ↻, and the spin is (2/5) m R² (v/R) ↻ = (2/5) R J ↻. Same sense, so H − R = 2R/5: the cue goes in at 7R/5 = 0.070 m, two fifths of a radius over center.',
 '5-c': f'(5-c) 40 sweep ↻ and 0.040 kg m²/s ↻ of spin. ½ (2.0 m/s →){D}(2.0 N s →) = 2.0 J of punch and ½ (40 ↻){D}(0.040 kg m²/s ↻) = 0.80 J of hook: two fifths again, the center zipping at 2.0 J/kg and the ball zinging at 800.',
 '6-a': "(6-a) ω² = 5g/(7a) = 10, so T = τ/√10, about 2.0 s: exactly the knife's time, on a 5/7 m arc. Again.",
 '6-b': '(6-b) The bead skips the turning: ω² = g/a = 14, and T = τ/√14, about 1.7 s.',
 '6-c': "(6-c) The ball pays 2 J of hook for every 5 J of punch, so the same heft runs it slower and it comes round late. About the contact its profile is (7/5)R², and an arc 5/7 the knife's pays the 7/5 right back.",
 '7-a': '(7-a) 0.25 m sweeping at 8.0 runs at 2.0 m/s.',
 '7-b': "(7-b) The rim's 2.0 m/s rides on top of the center's: 4.0 m/s at the top, nothing at the bottom, the still point for that instant.",
 '7-c': '(7-c) The front point is √2 radii from the still point, so it runs at √2 of 2.0 m/s, about 2.8 m/s, τ/8 (45°) below →.',
 'c-1': "(c-1) Rolling, the ball turns about the contact, profile (2/5)R² + R² = (7/5)R², and at v/R it hooks (7/10)mv²: 7/5 of a sliding bead's punch.",
 'c-2': "(c-2) Heft mgaθ²/2 traded against (7/10)ma²θ̇² cycles where (7/5)aω² = g: the statement's T. For the knife's meter, a = 5/7 m.",
 'c-3': '(c-3) During the blow nothing else gets leverage about the line under the ball, so JH of spin there has to match (7/5)mR²(v/R) = (7/5)RJ: H = 7R/5.',
 'c-4': "(c-4) Top 2v, bottom 0. The still point never stays put; a moment later it's a different point.",
 '8-a': '(8-a) The ribbon only pulls at the hole, so the spin about the hole, mvr, holds: halve the radius and the puck doubles to 4.0 m/s, its sweep climbing from about 3.3 to 13.',
 '8-b': '(8-b) mv²/r bends the path: 3.3 N at the start, 27 N at the end. Half the radius, eight times the pull.',
 '8-c': '(8-c) The puck punches 1.0 J, then 4.0 J: the ribbon did 3.0 J of work, through the sliver of velocity that follows the inward spiral. Its other end has been in your hand.',
 '9-a': '(9-a) T = τ/ω: τ/2.4 = 2.6 s for the slow tone and τ/5.8 = 1.1 s for the fast.',
 '9-b': '(9-b) (2 + √2)/(2 − √2) = (2 + √2)²/2, so the sweeps stand at 1 + √2, and flipped, √2 − 1. Irrational: no count of slow cycles ever matches a count of fast ones.',
 '10-a': '(10-a) Current is the conductance of the voltage, power is the voltage of the current, and the can cans the capacitance of its voltage: by now it says itself. Empty, the can leaves the resistor all 6.0 V: 0.30 A. RC = 2.0 s. With the can at 4.0 V, the resistor has 2.0 V and passes 0.10 A; the can has canned 0.40 C and 0.80 J, and the resistor burns 0.20 W.',
 '10-b': '(10-b) LC = 1/ω_a², so the loop on its own rings at the slow tone, 2.4 sweep, exactly.',
 '10-c': "(10-c) The current cranks the rod with χ_em = κi and delivers κiȧ; the rod's motion pushes κȧ back against the current, so the circuit gives up κȧ of i. Same number, opposite ledgers: a belt, not a battery. Crank against the sweep and the belt runs the other way.",
 '10-d': '(10-d) (2/3) × 2.4 = 1.6 and (3/2) × 2.4 = 3.6 sweep, multiplying to ω₀² and standing at 9 to 4: a mirror pair about ω₀, the two tones of one machine, rods and loop together.',
 'e-1': "(e-1) C = 1/(Lω₀²) = 1/(2 − √2) F, about 1.7 F. The tuning wants the exact value; 1.7 is just how it's written down.",
 'e-2': "(e-2) Free, both take 2.6 s a turn: the loop keeps the slow motion's time.",
 '2-α': '(2-α) Put the trials in: (D − ηω²)A = κωQ for the swing and (1/C − Lω²)Q = κωA for the loop. Multiply, with D = ηω₀² and 1/C = Lω₀², and out comes ηL(ω₀² − ω²)² = κ²ω², the charge a quarter turn behind the lean.',
 '2-β': '(2-β) Take the root, ω₀² − ω² = ±[κ/√(ηL)]ω. Subtract the low balance from the high and the sum cancels, leaving Δω√(ηL) = κ; the low one then gives ω_low ω_high = ω₀². A mirror pair.',
 '2-γ': '(2-γ) 3/2 − 2/3 = 5/6, so κ = (5/6)ω₀√(ηL), and the tones run at 1.6 and 3.6 sweep. Every bit of κiȧ the field puts in the swing, the loop gives up.',
 '11-a': "(11-a) L′C′u² = 1: u = 1.0 × 10⁸ m/s, a third of light's speed. C′Z² = L′: Z = 50 ohm.",
 '11-b': "(11-b) Where the pulses overlap, 12 V and not an amp to show for it: their 0.12 A currents run opposite ways and cancel. All of it's canned, ½ × 0.20 × 10⁻⁹ × 144 = 14 nJ/m, the two pulses' 7.2 nJ/m stacked in one place.",
 '11-c': "(11-c) Crests at u/9 = 1.1 × 10⁷ m/s and 9u = 9.0 × 10⁸ m/s, three times light's speed. The fast one's a stripe: two waves already there, lining up, carrying nothing. A signal rides its wave at u, and nobody sent the stripe.",
 'f-2': "(f-2) A crest holds its factor's inside fixed, so it moves at the time coefficient over the place coefficient: u(f₁ + f₂)/(f₁ − f₂) for one, u(f₁ − f₂)/(f₁ + f₂) for the other.",
 'f-3': "(f-3) Sum 9 MHz, difference 1 MHz: crests at 9u and u/9. The fast one is the hall's stripe.",
 'f-4': "(f-4) Nine times u needs 5.0 MHz + f₂ = 9 (5.0 MHz − f₂), so f₂ = 4.0 MHz, and the slow crests run at u/9: the hall's 4.0 MHz.",
 '12-a': '(12-a) 100 mJ in all, and the momenta, 80 mJ/c → and 20 mJ/c ←, leave 60 mJ/c →: 2.0 × 10⁻¹⁰ kg m/s →.',
 '12-b': '(12-b) 100² = 60² + 80², so Mc² = 80 mJ: the 3–4–5, twenty times over. (How many is that now? Never mind. Keep moving.)',
 '12-c': '(12-c) v = pc²/E = 0.60c, and γ = 1.25. Ride along and the shift is 2: the 80 mJ pulse halves and the 20 mJ pulse doubles, 40 and 40, with the stretch at (2 + 1/2)/2 = 5/4.',
 '12-d': '(12-d) A clock riding at 0.60c reads 8.0 s of its own time while S counts 10.',
 'g-1': '(g-1) With s = √((1 − β)/(1 + β)), equal means E₁s = E₂/s, so s² = 1/r and β = (r − 1)/(r + 1).',
 'g-2': '(g-2) 1 − β² = 4r/(r + 1)², so γ = (r + 1)/(2√r).',
 'g-3': '(g-3) r = 4 gives β = 3/5 and γ = 5/4: (r − 1)² + (2√r)² = (r + 1)², so a square ratio makes the triangle whole, and 4 makes 3–4–5. 40 mJ each.',
 '3-α': '(3-α) The two crest speeds multiply to u²: reflections about u, nine under and nine over.',
 '3-β': '(3-β) A sum of two squares is never less than twice their product, so (C′V² + L′I²)/2 ≥ |VI|/u: energy rides the line no faster than u. The stripe has a place, a velocity, and a phase, and no store of its own. Phase is for ghosts.',
 '3-γ': "(3-γ) Moving along the line multiplies one pulse by s and divides the other, so 80 × 20 = 40 × 40 holds: 40 mJ each where they match, 80 mJ of rest energy, s = 2, and a stretch of 5/4, drawer g's γ.",
 '13-a': '(13-a) q₀²/(2C) = 0.080 J with C about 1.7 F: q₀ = 0.52 C, and the can starts at 0.31 V.',
 '13-b': "(13-b) q gets back to q₀ only when both hands point → again: 4νT and 9νT both whole turns. Four and nine share nothing, so the first time is νT = τ, four turns low and nine high, the one machine's return: T = 6τ/ω₀, about 16 s. It was 16 s last time, too.",
 '13-c': "(13-c) Halfway, the slow hand points → and the fast ←: q/q₀ = → · (9/13 → + 4/13 ←) = 5/13, no current, both rods through vertical. The can holds 25/169 of the 80 mJ, about 12 mJ, and the rods punch the other 144/169, 68 mJ: a 5–12–13.",
 '13-d': '(13-d) In S, γT = 1.25 × 16 s = 20 s, and the receiver covers 0.60c × 20 s = 3.6 × 10⁹ m. Its seat rides x = vt, so x_H = 0 throughout. This is RUN: nothing taps the machine, so its tones lining up add nothing.',
}


def apply(out):
    import re
    res, dropping = [], False
    for t, x in out:
        if t in ("p", "eq") and isinstance(x, str):
            m = re.match(r"\((\d+-[a-d]|[a-g]-\d|\d-[αβγ]|[αβ]-\d)\) ", x)   # a part label, not an equation's "(H − R) ↑ …"
            if m:
                lab = m.group(1)
                if lab in REEL4:
                    res.append(("p", REEL4[lab])); dropping = True; continue
                dropping = False
            elif dropping and not x.startswith(KEEP):
                continue
            elif x.startswith(KEEP):
                dropping = False
        else:
            dropping = False
        res.append((t, x))
    return res
