"""Builds the four end-to-end Mansion solution sets, one per level, as simple HTML.

READ FIRST (doc, 2026-10-22, R-107): motivate a change of notation, don't start with it. Keep the textbook
notation (cos θ, signed terms, 2π) until it starts to look goofy; bring the new one in where it earns its keep,
explained at first use. Set 1 goes slow and explains; sets 2-4 pick up the pace and lean on set 1.

Claude (Anthropic), 2026-10-21. Sources (flattened copies in this folder): Codex's four release
reading copies r1..r4 (main route, ending, and the appendix tabs open at that release) and
CL-214's standard statements. Set k = the mansion route of release k with every mansion solution
re-said in level-k words (levels.py), the problem statements put back in, and the optional
problems open at level k interleaved in the problem set's order:
  1 knife, drawer 4, F1 | 2, 3, drawer 1 | 4, drawer 2, F4 | 5 | 6 | 7, drawer 3 | 8 |
  9, 10, drawer 5, F2 | 11, drawer 6 | 12, drawer 7, F3 | 13, U1, U2 | ending k.
Usage: python3 build_sets.py   (writes set1.html .. set4.html and set*.txt beside it)
"""
import html, re
from levels import LEVEL

STAMP = "2610221000"
DATE = {1: "2026-10-22", 2: "2026-10-22", 3: "2026-10-22", 4: "2026-10-22"}   # the sweep, doc 2026-10-22 09:47
WORDS = {
 1: "the turn and τ, π for the flip, the cycle (it cycles), the sweep and the stroke, χ for torque, sentences the right way round (current is the conductance of the voltage; power is the voltage of the current, and the sweep of the torque), own time",
 2: "level 1's, plus heft, punch and hook; profile; pickup, and crank as a verb; spin; can and coil",
 3: "level 2's, plus zip and zing; the still point; flips and mirror pairs; tone, chord, beat and the shape Ω_shape; the trade (a belt, not a battery); the stripe and phase, for ghosts; shift and stretch",
 4: "level 3's, plus the one machine; zam and zlam; in step, at random, the tap; TEST and RUN; and doc's zow and zlow, with their verbs zower and zlower",
}
NAMES = {1: "the base game", 2: "with the cabinet", 3: "with the cabinet and the funhouse", 4: "the whole house"}

def read(path):
    lines = open(path, encoding="utf-8").read().split("\n")
    tabs, cur = {}, None
    for ln in lines[1:]:
        if ln.startswith("######## TAB"):
            cur = ln.split(" ", 3)[3]; tabs[cur] = []; continue
        if cur is not None and ln.strip():
            tabs[cur].append(ln)
    return tabs

def blocks(lines):
    """Split into [(heading, [lines])], heading None for anything before the first heading."""
    out, head, body = [], None, []
    for ln in lines:
        if ln.startswith("## "):
            out.append((head, body)); head, body = ln[3:], []
        else:
            body.append(ln)
    out.append((head, body))
    return out

def statements():
    tabs = read("cl214_now.txt"); bl = blocks(next(iter(tabs.values())))
    st = {}
    for h, body in bl:
        m = re.match(r"(\d+)\. ", h or "")
        if not m: continue
        n = int(m.group(1)); parts = []
        for ln in body:
            if ln.startswith("candle") or ln.startswith("the clown"): continue
            parts.append(ln)
        st[n] = parts
    return st

def apply_edits(text, k):
    for lev in range(1, k + 1):
        for old, new in LEVEL[lev]:
            c = text.count(old)
            assert c == 1, (lev, c, old[:80])
            text = text.replace(old, new)
    return text

NAV = [(re.compile(r" \(Appendix 1, drawer \d\.\)"), ""),
       (re.compile(r"Passage: from Appendix 1, drawers? [\d and]+, and back (the same way|either way)\. "), ""),
       (re.compile(r"Passage: the back of this drawer opens on Appendix b, F\d\. The passage is open\."), "The back of this drawer opens into the funhouse."),
       (re.compile(r"Passage: the back of this drawer opens on Appendix b, F\d\. Painted shut until patch 2\."), "Behind this drawer there's a draft; the panel at its back is painted shut."),
       (re.compile(r" \(Appendix γ\. The trapdoor is open\.\)"), " The trapdoor is open."),
       (re.compile(r" \(Appendix γ\. Nailed down until patch 3\.\)"), " It's nailed down."),
       (re.compile(r"Service entrance: any of the three trapdoors\. They all come down here, and any of them takes you back up\."), "Any of the three trapdoors comes down here."),
       (re.compile(r"Take the coupled machine of funhouse problem 2"), "Take the coupled machine of F2")]
SKIP = re.compile(r"^(Return to |Return the |Optional problems and worked route|each drawer opens)")
# words a set reaches before its level brings them in (set 2 only)
SET2_FIX = [("and a moment later a different point is: the still point keeps changing.", "and a moment later a different point is."),
            ("It carries nothing: that's the hall's stripe.", "It carries nothing.")]
TIMES = [("and the center speeds up at R times that:", "and the center speeds up at R of that:"),
         ("In a mode both rods pick up at −ω² times their angle.", "In a mode both rods pick up at ω² of their angle, back toward vertical."),
         ("In a mode both rods pick up at −ω² times their angle, and the lower rod leans Ω_shape times as far as the upper.", "In a mode both rods pick up at ω² of their angle, back toward vertical, and the lower rod leans Ω_shape of the upper's lean."),
         ("One tone is ω₀ times a factor and the other is ω₀ over it: a mirror pair.", "One tone is ω₀ at a factor and the other is ω₀ on it: a mirror pair.")]

SPOOL_I = [("(3) Write the statement’s moment of inertia as η. With the mass taken out, inertia is the profile: η on", "(3) With the mass taken out, inertia is the profile: I on"),
           ("(3) Write the statement’s moment of inertia as η. ", "(3) "),
           ("ηα = −Fr − fR", "Iα = −Fr − fR"), ("(m + η/R²)a", "(m + I/R²)a"), ("Here η/R²", "Here I/R²")]

# doc's set-1 edits of 2026-10-22 08:06, as discussed: arrows start at the governor, the spool's
# signs become senses (→ ← straight, ↻ ↺ turning), the grip is taken positive → and comes out ←,
# the hoop's eighth of a turn, the powdered clown. Each entry lists the level variants of one spot.
DOC_0806 = [
 [("(2) The cosine can't go over 1, so g/(ℓω²) has to stay under 1. Below a sweep of √(g/ℓ) = √20, about 4.5 stroke a second, hanging straight down is the only answer.",
   "(2) The ball hangs g/ω² below the hinge: 10/25 = 0.40 m here. A drop can't be longer than the arm. Below a sweep of √(g/ℓ) = √20, about 4.5 strokes a second, g/ω² would be longer than the 0.50 m arm, so hanging straight down is all that's left.")],
 [("Take forward, the way the cord pulls, as positive, and let f be the counter's grip on the spool, positive forward too. The center of mass speeds up as if both forces acted there: ma = F + f. For the turning, take the way the spool turns when it rolls forward as positive. The cord pulls forward 0.12 m below the axle and the grip acts 0.20 m below it, and a forward push below the axle turns the spool backward.",
   "The cord pulls forward (→). Take the counter's grip on the spool, f, as positive → too; the answer will say which way it really goes. The center of mass speeds up as if both forces acted on it directly: ma = F + f. Rolling →, the spool turns back around, ↻. The cord pulls → 0.12 m below the axle and the grip acts 0.20 m below it, and a → push below the axle turns the spool forward around, ↺.")],
 [("So the torques about the axle are −Fr and −fR, and Iα = −Fr − fR.", "So the torques about the axle are Fr ↺ and fR ↺, and Iα ↻ = [Fr + fR] ↺."),
  ("So the cord cranks the spool backward about the axle with −Fr, the grip cranks it with −fR, and Iα = −Fr − fR.", "So the cord cranks the spool ↺ about the axle with Fr, the grip cranks it ↺ with fR, and Iα ↻ = [Fr + fR] ↺.")],
 [("The center speeds up at 0.80 m/s², forward: the spool rolls toward the pull", "The center speeds up at 0.80 m/s² →: the spool rolls toward the pull")],
 [("The grip is f = 1.6 − 6.0 = −4.4 N. It pulls back, and about the axle it turns the spool forward harder than the cord turns it back.",
   "The grip is what's left when the cord's 6.0 N → comes off the 1.6 N → the center needs: f = 1.6 N → + 6.0 N ← = 4.4 N ←. It pulls back, and about the axle it turns the spool ↻ harder than the cord turns it ↺."),
  ("The grip is f = 1.6 − 6.0 = −4.4 N. It pulls back, and about the axle it cranks the spool forward harder than the cord cranks it back.",
   "The grip is what's left when the cord's 6.0 N → comes off the 1.6 N → the center needs: f = 1.6 N → + 6.0 N ← = 4.4 N ←. It pulls back, and about the axle it cranks the spool ↻ harder than the cord cranks it ↺.")],
 [("Forward 2.0 m/s and down 2.0 m/s make 2√2, about 2.8 m/s, 45° below forward.", "2.0 m/s → and 2.0 m/s ↓ make 2√2, about 2.8 m/s, 45° (τ/8) below →.")],
 [("a whiteface in damask", "a powdered clown in damask")],
 # doc 08:40-08:41: a hair space keeps ℓ and θ apart; the definite description, not the pronoun (only one thing has weight)
 [("lifts a point at distance ℓ by ℓ(1 − cos θ). For this small lean, that’s ℓθ²/2", "lifts a point ℓ away by ℓ(1 − cos θ). For this small lean, that’s ℓ\u200aθ²/2")],
 [("Its 10 N weight lifted through 5 mm", "The 10 N weight lifted through 5 mm")],
 [("the whiteface has gloves", "the powdered clown has gloves")],
]
NO_NEGATIVE_FORCES = [
 ("so its torque about the axle is still −Fr; only its forward part changes, to F cos θ. Then F cos θ + f = 0 and −Fr − fR = 0. The second gives f = −Fr/R, and the first then says cos θ = r/R = 0.60.",
  "so it still {turns} the spool ↺ with Fr; only its forward part changes, to F cos θ →. With nothing speeding up, the grip has to be F cos θ ←, and pulling ← 0.20 m below the axle it {turns} the spool ↻ with F cos θ at R. The two balance when F cos θ at R is Fr, so cos θ = r/R = 0.60."),
 ("The circuit's emf is ε = −κȧ, and the power the emf delivers to the circuit is the voltage of the current, εi = −κiȧ. The two add to zero: whatever the rod gets, the circuit gives up. When κi and ȧ have opposite signs, κiȧ is negative, and the rod's giving its energy to the circuit instead.",
  "The statement's minus in ε = −κȧ is a direction: the rod's motion drives an emf of κȧ back against the current that {turns} it, so the circuit gives up the voltage of the current, κȧ of i: the same κiȧ. Whatever the rod gets, the circuit gives up. When the current {turns} the rod against its sweep, the energy runs the other way, and the rod's giving its energy to the circuit instead."),
]

# The 2π is lugged around and noticed: the knife's rule and numbers (2nd and 3rd sightings, the 2 noticed),
# the flywheel's sweeps in turns (4th, 5th, noticed again), a torque through a whole turn (6th), and there
# the turn takes τ and torque takes χ, with doc's sentences.
SLOW_WALK = [
 ("The usual small-swing rule gives T = 2π√(ℓ/g). A whole turn has arrived wearing two flips. Give the full turn its own sign, τ.\nCall a radian a stroke. A whole turn is τ, about 6.3 strokes. Half a turn is π, the flip. A turn of the knife’s cycle brings it back to the same end; a flip of the cycle takes it to the opposite end.\nCount strokes each second and call that the sweep. The cycle’s sweep is ω. The small-swing rule balances as\n    ℓω² = g,\n     Tω = τ.\nHere the cycle sweeps at √10, about 3.2 strokes a second. Its turn takes T = τ/√10 = 1.99 s, about two seconds.",
  "Call a radian a stroke. All the way round is a turn, about 6.3 strokes, and half of that is π, the flip. A flip of the knife’s cycle takes it to the opposite end; a turn brings it back.\nCount strokes each second and call that the sweep. The cycle’s sweep is ω. The usual small-swing rule balances as\n    ℓω² = g,\n    Tω = 2π.\nHere the cycle sweeps at √10, about 3.2 strokes a second. Its cycle takes T = 2π/√10 = 1.99 s, about two seconds. There's a 2 riding along with that π."),
 ("The height, bottom speed and time for a turn stay the same.", "The height, bottom speed and time for a cycle stay the same."),
 ("At 4.0 strokes a second, half of 0.50 kg m² at 16 is 4.0 J. Four seconds at a net 3.0 W add 12 J, for 16 J, and 16 J on the same wheel needs the squared sweep to be 64. The wheel ends up sweeping at 8.0 strokes a second.",
  "At 4.0 strokes a second, half of 0.50 kg m² at 16 is 4.0 J. Counted in turns, 4.0 strokes a second is 4.0/2π, about 0.64 of a turn a second. Four seconds at a net 3.0 W add 12 J, for 16 J, and 16 J on the same wheel needs the squared sweep to be 64. The wheel ends up sweeping at 8.0 strokes a second: 8.0/2π, about 1.3 turns a second. The 2 again: every sweep we count in turns gets divided by it."),
 ("(3) Torque usually gets the letter τ, but the turn has it now. A χ hung on the wall could apply a twist to something—use that for torque. The power a torque delivers is the sweep of the torque: P = ωχ. Put numbers to it once: 0.75 N m at 4.0 strokes a second delivers 3.0 W. So at the start the engine's 3.0 W takes χ = 0.75 N m, and at the end, at 8.0, it takes 0.38 N m.\nWhen the wheel goes twice as fast, applying the same power takes just half the torque.",
  "(3) The power a torque delivers is the sweep of the torque. Put numbers to it once: 0.75 N m at 4.0 strokes a second delivers 3.0 W. So at the start the engine's 3.0 W takes 0.75 N m, and at the end, at 8.0, it takes 0.38 N m.\nWhen the wheel goes twice as fast, applying the same power takes just half the torque.\nThrough one whole turn, 0.75 N m does 2π of itself: 4.7 J, and 0.64 of a turn a second at 4.7 J a turn is the engine's 3.0 W. There's the 2π again, two flips standing in for one turn. π only covers half of what the knife does, one swing across; the cycle is the whole of it. Give the whole turn its own sign, τ. The knife's rule is then Tω = τ, and the wheel's 4.0 strokes a second is 4.0/τ of a turn a second.\nTorque usually gets the letter τ, but the turn has it now. A χ hung on the wall could apply a twist to something—use that for torque: P = ωχ, with χ = 0.75 N m at the start."),
]

SLOW_WALK += [   # set 1 only for now (doc 09:03): the turning is a motion, so it carries an energy; it isn't one
 ("The center's energy is ½m(Lω/2)², or mL²ω²/8. The turning about the center is ½(mL²/12)ω², or mL²ω²/24.",
  "The center's motion carries ½\u200am\u200a(L\u200aω/2)², or m\u200aL²\u200aω²/8. The turning about the center carries ½\u200a(m\u200aL²/12)\u200aω², or m\u200aL²\u200aω²/24."),
 ("(3) The center moves at Lω/2 and the ladder", "(3) The center moves at L\u200aω/2 and the ladder"),   # doc's hair spaces, 09:03
]

SLOW_WALK += [   # doc 09:17/09:19, set 1: the cue ball in arrows, showing how they work through crosses and dots
 ("(1) Call the given impulse J. A 2.0 N s impulse on 1.0 kg leaves the center moving at 2.0 m/s.\n(2) The same impulse, struck H above the table, is H − R above the ball's center, so about the center it leaves an angular momentum of J(H − R). Rolling at once means the ball sweeps at v/R, and its angular momentum about the center is (2/5)mR² × v/R = (2/5)RJ. So H − R = 2R/5, and H = 7R/5 = 0.070 m: two fifths of a radius above the center.\n(3) The ball sweeps at 2.0/0.050 = 40 strokes a second. The center's motion carries ½ × 1.0 × 2.0² = 2.0 J. The turning carries ½ × (2/5)(1.0)(0.050)² × 40² = 0.80 J. That's two fifths as much again.",
  "(1) Call the given impulse J: 2.0 N s →. On 1.0 kg it leaves the center moving at 2.0 m/s →.\n(2) Take the lever from the ball's center up to where the cue strikes: (H − R) ↑. The angular momentum a blow leaves about the center is the leverage of the blow, with ↑ × → = ↻:\n    (H − R) ↑ × J → = (H − R) J ↻.\nRolling at once means the bottom of the ball isn't sliding. The bottom's lever from the center is R ↓, and the turning moves it at the sweep crossed into that lever: ω ↻ × R ↓ = ω R ←. That has to cancel the center's v →, so the ball sweeps at v/R ↻. About the center, its angular momentum is then its moment of inertia at that sweep:\n    (2/5) m\u200aR² (v/R) ↻ = (2/5)\u200aR\u200aJ ↻,\nsince m v is J. The two senses agree, so the cue went in above the center, and H − R = 2R/5: H = 7R/5 = 0.070 m, two fifths of a radius above the center.\n(3) The ball sweeps at 2.0/0.050 = 40 strokes a second ↻, and its angular momentum is (2/5)(0.050 m)(2.0 N s) = 0.040 kg m²/s ↻. Energy in motion is half the velocity dotted into the momentum, and for the turning, half the sweep dotted into the angular momentum:\n    ½ (2.0 m/s →) · (2.0 N s →) = 2.0 J,\n    ½ (40 ↻) · (0.040 kg m²/s ↻) = 0.80 J.\nEach pair points the same way, so each dot is just the product of the sizes. The turning carries two fifths as much again."),
 # doc 09:17, set 1: no contraction where 's reads as a possessive; hair spaces; doc's period sentence
 ("The ladder's sweeping at 2v/L", "The ladder is sweeping at 2v/L"),
 ("After the ladder's left the wall", "After the ladder has left the wall"),
 ("(1) The ball cycles with sweep ω where", "(1) T is the period—how long it takes to sweep through a full turn of the cycle. The ball cycles with sweep ω where"),
]

# The sweep (doc 09:47): sets 2-4 get set 1's changes in their own level's words, and the faster walk
# to τ (doc 08:30: "we can push it faster in later sets"): the 2π shows in the knife's rule and its
# number, the 2 is noticed, and the turn takes τ at the knife itself.
LATER = [
 [("The usual small-swing rule gives T = 2π√(ℓ/g). A whole turn has arrived wearing two flips. Give the full turn its own sign, τ.\nCall a radian a stroke. A whole turn is τ, about 6.3 strokes. Half a turn is π, the flip. A turn of the knife’s cycle brings it back to the same end; a flip of the cycle takes it to the opposite end.\nCount strokes each second and call that the sweep. The cycle’s sweep is ω. The small-swing rule balances as\n    ℓω² = g,\n     Tω = τ.\nHere the cycle sweeps at √10, about 3.2 strokes a second. Its turn takes T = τ/√10 = 1.99 s, about two seconds.",
   "Call a radian a stroke. All the way round is a turn, about 6.3 strokes, and half of that is π, the flip. A flip of the knife’s cycle takes it to the opposite end; a turn brings it back.\nCount strokes each second and call that the sweep. The cycle’s sweep is ω. The usual small-swing rule balances as\n    ℓω² = g,\n    Tω = 2π.\nHere the cycle sweeps at √10, about 3.2 strokes a second. Its cycle takes T = 2π/√10 = 1.99 s, about two seconds. There's a 2 riding along with that π: two flips standing in for one turn. π only covers half of what the knife does, one swing across; the cycle is the whole of it. Give the whole turn its own sign, τ, and the rule says so:\n    Tω = τ.")],
 # R-097: sweep comes in as a unit where pickup arrives (level 2); from here on a stroke a second is a sweep
 [("θ̈ = −(g/ℓ)θ.", "θ̈ = −(g/ℓ)θ. A stroke a second makes a handy unit of sweep, so call it a sweep too: the cycle sweeps at 3.2 sweep. At either end the knife picks up at 10 of its 0.10 lean: 1.0 sweep a second, back toward the bottom.")],
 [("The height, bottom speed and time for a turn stay the same.", "The height, bottom speed and time for a cycle stay the same.")],
 # the ladder: doc's hair spaces (R-094) and R-098
 [("(3) The center runs at Lω/2 and the ladder sweeps about its center at the same ω. The center punches ½m(Lω/2)², or mL²ω²/8. About the center the profile is L²/12, so the turning hooks ½(mL²/12)ω², or mL²ω²/24.",
   "(3) The center runs at L ω/2 and the ladder sweeps about its center at the same ω. The center punches ½ m (L ω/2)², or m L² ω²/8. About the center the profile is L²/12, so the turning hooks ½ (m L²/12) ω², or m L² ω²/24.")],
 [("After the ladder's left the wall", "After the ladder has left the wall")],
 [("The ladder's sweeping at 2v/L", "The ladder is sweeping at 2v/L")],
 # the cue ball in arrows (doc 09:17/09:19, 09:41), in spin, punch and hook
 [("(1) Call the given impulse J. The strike is a blow; what it leaves in the center's motion is punch. A 2.0 N s blow on 1.0 kg leaves the center running at 2.0 m/s.\n(2) The same impulse, struck H above the table, is H − R above the ball's center, so about the center it leaves J(H − R) of spin, the angular momentum. Rolling at once means the ball sweeps at v/R. Its profile about the center is (2/5)R², so (2/5)mR² sweeping at v/R carries (2/5)RJ of spin. So H − R = 2R/5, and H = 7R/5 = 0.070 m: two fifths of a radius above the center.\n(3) The ball sweeps at 2.0/0.050 = 40 strokes a second. The center punches ½ × 1.0 × 2.0² = 2.0 J. The turning hooks ½ × (2/5)(1.0)(0.050)² × 40² = 0.80 J: two fifths of the punch again.",
   "(1) Call the given impulse J: 2.0 N s →. The strike is a blow; what it leaves in the center's motion is punch. On 1.0 kg it leaves the center running at 2.0 m/s →.\n(2) Take the lever from the ball's center up to where the cue strikes: (H − R) ↑. The angular momentum a blow leaves about the center is spin, and it's the leverage of the blow, with ↑ × → = ↻:\n    (H − R) ↑ × J → = (H − R) J ↻.\nRolling at once means the bottom of the ball isn't sliding. The bottom's lever from the center is R ↓, and the turning moves it at the sweep crossed into that lever: ω ↻ × R ↓ = ω R ←. That has to cancel the center's v →, so the ball sweeps at v/R ↻. Its profile about the center is (2/5) R², and (2/5) m R² sweeping at v/R carries\n    (2/5) m R² (v/R) ↻ = (2/5) R J ↻\nof spin, since m v is J. The two senses agree, so the cue went in above the center, and H − R = 2R/5: H = 7R/5 = 0.070 m, two fifths of a radius above the center.\n(3) The ball sweeps at 2.0/0.050 = 40 strokes a second ↻, and its spin is (2/5)(0.050 m)(2.0 N s) = 0.040 kg m²/s ↻. The center punches half its velocity dotted into its momentum, and the turning hooks half the sweep dotted into the spin:\n    ½ (2.0 m/s →) · (2.0 N s →) = 2.0 J,\n    ½ (40 ↻) · (0.040 kg m²/s ↻) = 0.80 J.\nEach pair points the same way, so each dot is just the product of the sizes. The hook is two fifths of the punch again.")],
 [("(1) The ball cycles with sweep ω where", "(1) T is the period—how long it takes to sweep through a full turn of the cycle. The ball cycles with sweep ω where")],
]
# drawer 1 (sets 2-4): the spool's ledgers in senses, not signs (R-092, R-096), the book's turning senses (R-099)
DRAWER1 = [
 ("The center's ledgers agree. Forward will be positive, and a positive roll would also take the spool this way. With f the counter's grip, positive forward: ma = F + f and Ia/R = −Fr − fR. Put the second into the first and the same a comes out. The grip comes out negative, pulling back, so the cord cranks the spool backward about the axle and the counter's grip cranks it forward, harder.",
  "The center's ledgers agree. Take the counter's grip f as positive → too, like the cord: ma → = F → + f →. Rolling →, the spool turns back around, and both pulls below the axle crank it forward around: I a/R ↻ = [Fr + fR] ↺. Put the second into the first and the same a comes out. The grip comes out ←, so the cord cranks the spool ↺ about the axle and the counter's grip cranks it ↻, harder."),
 ("a = 0.80 m/s², forward, the way the cord pulls. Friction pulls back 4.4 N.", "a = 0.80 m/s² →, the way the cord pulls. Friction pulls 4.4 N ←."),
 ("and ω = 5.0 rad/s: the kitchen's shaft.", "and ω = 5.0 sweep: the kitchen's shaft."),
]
SWEEP_UNIT = [(re.compile(r"(?<=[0-9]) strokes a second each second"), " sweep a second"),
              (re.compile(r"(?<=[0-9]) strokes a second"), " sweep")]

# doc 10:08-10:15: spreading the arrows and getting rid of sin and cos are the same job (Dog Math 4, 9, 13).
# Forwardness → · θ (or θ / →), upwardness ↑ · θ (or θ / ↑); a cross only where a turning sense is the point.
# Set 1 first; sets 2-4 at the next sweep.
ARROWS = [
 ("(1) Leaning through θ lifts a point ℓ away by ℓ(1 − cos θ). For this small lean,",
  "(1) An arm ℓ long, leaning θ, hangs ↓ · ℓ below the pivot instead of ℓ. That's the downward part of ℓ: how much of the arm points straight down, the statement's ℓ cos θ. So the lean lifts its end by ℓ − ↓ · ℓ. For this small lean,"),
 ("(1) The arm's pull does two jobs at once. Its upward part holds up the ball's weight, mg. Its inward part bends the ball's path round the shaft, and that takes the mass at the squared sweep, at the ball's distance from the shaft: mω²ℓ sin θ. The pull runs along the arm, so the two parts stand in the arm's own slope: tan θ = ℓω² sin θ/g. For an arm off the vertical the sine cancels, and cos θ = g/(ℓω²) = 10/(0.50 × 25) = 0.80. The arm hangs 0.40 m down and reaches 0.30 m out:",
  "(1) The arm's pull does two jobs at once. Its upward part holds up the ball's weight, mg. Its inward part bends the ball's path round the shaft, and that takes the mass at the squared sweep, at the ball's reach from the shaft: mω² of the reach. The pull runs along the arm, so its two parts stand to each other as the arm's drop to its reach: mg is to mω² of the reach as the drop is to the reach. For an arm off the vertical the reach cancels, and the ball hangs g/ω² below the hinge: 10/25 = 0.40 m. That's the arm's downward part, ℓ / ↓: 0.40 m of its 0.50 m. The arm hangs 0.40 m down and reaches 0.30 m out:"),
 ("(2) The ball hangs g/ω² below the hinge: 10/25 = 0.40 m here. A drop can't be longer than the arm.", "(2) A drop can't be longer than the arm."),
 ("only its forward part changes, to F cos θ →. With nothing speeding up, the grip has to be F cos θ ←, and pulling ← 0.20 m below the axle it turns the spool ↻ with F cos θ at R. The two balance when F cos θ at R is Fr, so cos θ = r/R = 0.60.",
  "only its forward part changes. The forward part of F, → · F, is how much of the pull goes forward; as a force it points forward, → F · →. With nothing speeding up, the grip has to be ← F · →, and pulling ← 0.20 m below the axle it turns the spool ↻ with → · F at R. The two balance when → · F at R is Fr, so the pull's forward fraction, F / →, is r/R = 0.60 of it."),
 ("(2) The two cosine weights are positive and add to one, so q reaches its initial maximum q₀ only when both cosines return to 1. Then 4νT and 9νT are each a whole number of turns; the sine terms and the velocities return too.",
  "(2) The statement's cosines are each part's cycle dotted into where it started, → · 4νt_H and → · 9νt_H, and its sines are ↑ · 4νt_H and ↑ · 9νt_H. The weights 9/13 and 4/13 are positive and add to one, so q is back at q₀ only when both cycles point → again. Then 4νT and 9νT are each a whole number of turns, and the ↑ parts and the velocities return too."),
 ("(3) At T/2 the slow part has made two whole turns and the fast part four turns and a flip. So the slow cosine is back at 1 and the fast one is at −1, and q/q₀ = 9/13 − 4/13 = 5/13. The sines are both zero there,",
  "(3) At T/2 the slow part has made two whole turns and the fast part four turns and a flip. So the slow cycle points → and the fast one ←, and q/q₀ = (9/13)(→ · →) + (4/13)(→ · ←) = 9/13 − 4/13 = 5/13. Both cycles lie along the start line, and their ↑ parts are zero there,"),
]

# doc 10:59: "symmetry everywhere, make everything into mobiles". The dot also scales, so a part as a force is
# → · F · → (symmetric, read from either end); arrows hug the operator with hair spaces, sizes hang outside with
# full spaces; a cross keeps its arrows in order. The chair's cycles become hands, so no angle gets dotted.
H = " "; DOT = H + "·" + H; CROSS = H + "×" + H
MOBILES = [
 (f"The forward part of F, →{DOT}F, is how much of the pull goes forward; as a force it points forward, → F{DOT}→. With nothing speeding up, the grip has to be ← F{DOT}→,",
  f"The forward part of F, →{DOT}F, is how much of the pull goes forward, and as a force it points forward too: →{DOT}F{DOT}→. With nothing speeding up, the grip has to be the same size pointing back, →{DOT}F{DOT}←,"),
 ("with ↑ × → = ↻:", f"with ↑{CROSS}→ = ↻:"),
 ("    (H − R) ↑ × J → = (H − R) J ↻.", f"    (H − R) ↑{CROSS}→ J = (H − R) J ↻."),
 ("ω ↻ × R ↓ = ω R ←", f"ω ↻{CROSS}↓ R = ω R ←"),
 ("    ½ (2.0 m/s →) · (2.0 N s →) = 2.0 J,", f"    [½ 2.0 m/s →{DOT}→ 2.0 N s] = 2.0 J,"),
 ("    ½ (40 ↻) · (0.040 kg m²/s ↻) = 0.80 J.", f"    [½ 40 ↻{DOT}↻ 0.040 kg m²/s] = 0.80 J."),
 ("(2) The statement's cosines are each part's cycle dotted into where it started, → · 4νt_H and → · 9νt_H, and its sines are ↑ · 4νt_H and ↑ · 9νt_H. The weights 9/13 and 4/13 are positive and add to one, so q is back at q₀ only when both cycles point → again.",
  "(2) Picture each part's cycle as a hand swinging round from →, the slow one 4νt_H and the fast one 9νt_H. The statement's cosines are the hands' forward parts and its sines their upward parts. The weights 9/13 and 4/13 are positive and add to one, so q is back at q₀ only when both hands point → again."),
 ("the ↑ parts and the velocities return too.", "the upward parts and the velocities return too."),
 ("So the slow cycle points → and the fast one ←, and q/q₀ = (9/13)(→ · →) + (4/13)(→ · ←) = 9/13 − 4/13 = 5/13. Both cycles lie along the start line, and their ↑ parts are zero there,",
  f"So the slow hand points → and the fast one ←. The forward arrow comes out of both terms, and the hands add on their own first: q/q₀ = →{DOT}(9/13 → + 4/13 ←), and 9/13 → + 4/13 ← is 5/13 →, so q/q₀ = 5/13 →{DOT}→ = 5/13. Both hands lie along the start line, and their upward parts are zero there,"),
]

# doc 11:05-11:07: pull the shared arrow out and let the directions add on their own before one dot or cross; 'make the rest that way'
PRETTY = [('The cord pulls → 0.12 m below the axle and the grip acts 0.20 m below it, and a → push below the axle turns the spool forward around, ↺. So the torques about the axle are Fr ↺ and fR ↺, and Iα ↻ = [Fr + fR] ↺.', 'The cord pulls → 0.12 m below the axle and the grip acts → 0.20 m below it. Each torque is its lever crossed into its pull. Both levers point ↓ and both pulls →, so ↓\u200a×\u200a→ comes out of both, and the sizes add on their own first: r F ↓\u200a×\u200a→ + R f ↓\u200a×\u200a→ = (Fr + fR) ↓\u200a×\u200a→ = (Fr + fR) ↺. A → push below the axle turns the spool forward around. So Iα ↻ = (Fr + fR) ↺.'), ("it turns the spool ↻ with →\u200a·\u200aF at R. The two balance when →\u200a·\u200aF at R is Fr, so the pull's forward fraction", "it turns the spool ↻ with →\u200a·\u200aF at R. The two turnings add on their own: Fr ↺ + (→\u200a·\u200aF) R ↻ = (Fr − (→\u200a·\u200aF) R) ↺, and with nothing turning that's zero. So →\u200a·\u200aF at R is Fr, and the pull's forward fraction"), ("(1) The ladder doesn't stretch: with the foot x out from the wall and the top y up, x² + y² = L² the whole time. As both change, x of the foot's velocity and y of the top's velocity cancel: 1.8 m of 0.40 m/s against 2.4 m of the top's. So the top moves at x/y of the foot's speed, the other way: 0.30 m/s, downward.", "(1) The ladder doesn't stretch, so its two ends move the same amount along it: the ladder dotted into the top's velocity less the foot's is zero. From foot to top the ladder runs 1.8 m ← + 2.4 m ↑. Take the top's velocity as v ↑; the answer will say which way it really goes. Less the foot's 0.40 m/s →, that's 0.40 m/s ← + v ↑. The arrows add on their own and dot pair by pair, and ←\u200a·\u200a↑ gives nothing:\n    (1.8 m ← + 2.4 m ↑)\u200a·\u200a(0.40 m/s ← + v ↑) = 0.72 m²/s ←\u200a·\u200a← + 2.4 m v ↑\u200a·\u200a↑ = 0.\nSo 2.4 m of v is 0.72 m²/s the other way: v ↑ = 0.30 m/s ↓."), ('At the top the two point the same way and add, for 4.0 m/s. At the bottom they point opposite ways and cancel. The bottom point is still for that instant.', 'At the top the two point the same way: 2.0 m/s → + 2.0 m/s → = 4.0 m/s →. At the bottom they point opposite ways: 2.0 m/s → + 2.0 m/s ← = 0. The bottom point is still for that instant.'), ("Each pulse's current is 6.0/50 = 0.12 A in its own direction of travel, and they travel opposite ways, so the currents cancel: no current at all.", "Each pulse's current is 6.0/50 = 0.12 A in its own direction of travel, and they travel opposite ways: 0.12 A → + 0.12 A ← = 0, no current at all."), ("A light pulse's momentum is its energy over c, and these point opposite ways, so the total is (80 − 20) mJ/c = 2.0 × 10⁻¹⁰ kg m/s, to the right.", "A light pulse's momentum is its energy over c, and these point opposite ways: 80 mJ/c → + 20 mJ/c ← = 60 mJ/c →, which is 2.0 × 10⁻¹⁰ kg m/s →."), ("ω ↻\u200a×\u200a↓ R = ω R ←. That has to cancel the center's v →, so the ball sweeps at v/R ↻.", "ω ↻\u200a×\u200a↓ R = ω R ←. Add the center's v →, and the bottom moves at v → + ω R ← = (v − ω R) →, which is zero when the ball sweeps at v/R ↻.")]

# doc 11:10: name what dropped out, or put it back. Net torques, the top's velocity seen from the foot, the slip, the pair's
# momentum all mean something; the chair's summed hand doesn't (its upward part is no physical quantity: the current
# weights both sines by 36/13 ν, not 9/13 and 4/13), so the chair goes back to each part's own share of the charge.
MEANING = [('= (Fr + fR) ↓\u200a×\u200a→ = (Fr + fR) ↺.', '= (Fr + fR) ↓\u200a×\u200a→ = (Fr + fR) ↺: the net torque about the axle.'), ("= (Fr − (→\u200a·\u200aF) R) ↺, and with nothing turning that's zero.", "= (Fr − (→\u200a·\u200aF) R) ↺, the net torque about the axle, and with nothing turning that's zero."), ('So 2.4 m of v is 0.72 m²/s the other way: v ↑ = 0.30 m/s ↓.', "So 2.4 m of v is 0.72 m²/s the other way: v ↑ = 0.30 m/s ↓. The second arrow, 0.40 m/s ← + v ↑, is the top's velocity as seen from the foot: 0.40 m/s ← + 0.30 m/s ↓, 0.50 m/s, square to the ladder. From the foot the top only swings round, and the ladder is sweeping at 0.50/3.0, about 0.17 strokes a second."), ('= (v − ω R) →, which is zero when', "= (v − ω R) →: the bottom's slip over the cloth, which is zero when"), ('At the top the two point the same way: 2.0 m/s → + 2.0 m/s → = 4.0 m/s →.', "At the top the two point the same way: 2.0 m/s → + 2.0 m/s → = 4.0 m/s →, the top point's velocity."), ('and these point opposite ways: 80 mJ/c → + 20 mJ/c ← = 60 mJ/c →, which is', "and these point opposite ways. The pair's momentum is 80 mJ/c → + 20 mJ/c ← = 60 mJ/c →, which is"), ('So the slow hand points → and the fast one ←. The forward arrow comes out of both terms, and the hands add on their own first: q/q₀ = →\u200a·\u200a(9/13 → + 4/13 ←), and 9/13 → + 4/13 ← is 5/13 →, so q/q₀ = 5/13 →\u200a·\u200a→ = 5/13.', "So the slow hand points → and the fast one ←. The charge reads each part's share, 9/13 and 4/13, off its hand's forward part. Take that forward part once, outside, and let the hands work out their differences together inside: q/q₀ = →\u200a·\u200a(9/13 → + 4/13 ←) = 5/13 →\u200a·\u200a→ = 5/13.")]

# doc's own edits to set 1's way in, 2026-10-22 11:3x (his words; his (?) marks kept until he settles them). Set 1 only for now.
SETUP_DOC = [('The inquiry has a place and an hour. It has no name for the dead.', 'The inquiry has a place and an hour. Left unspecified: who should arrive, and who will depart.'), ('A visitor has come to find out how it was done. The door is unlatched. A loose sheet of questions lies beside a small ruled book; the book has been opened to a page someone has already used.', 'A visitor arrives to find out how it was all done. The door is unlatched. A loose question sheet lies beside a small blank book, opened to a page half-full of notes.'), ('In the dining room the roast is going cold under its cover. A strip of paper moves beneath a pen. Above it, a knife swings.', 'In the dining room the roast goes cold under its cover. A strip of paper moves beneath a pen. Above it swings a knife.'), ('At the silver centerpiece’s pivot, a powdered clown in damask has stopped partway into a curtsy. The flowers on one repaired cuff face inward; every other spray faces out. The curtsy doesn’t deepen.', 'At the silver pivot, a powdered clown in damask is partway into a curtsy. The flowers on one repaired cuff face inward; every other spray faces out. The curtsy does not deepen.'), ('A silver canteen stands locked on the sideboard. Its lid bears a painted juggler. The little lock has been polished more recently than the lid.', 'A trim silver canteen with an enamel juggler on the lid stands locked on the sideboard. The lock has been polished more recently than the lid.'), ('The visitor watches the knife go across and come back. On the paper, the same curve begins again.', 'The visitor watches the knife cycle across and back. On the paper, the curve cycles with it.')]

# doc 11:36: enamel, not paint (paint would be gone fast); the book is blank unless its rules are used in a problem (they aren't).
# Applies wherever the text appears (sets 2-4: drawer 4's door, ending 4); set 1's way in already has doc's words.
EVERYWHERE = [("a juggler painted on the lid", "an enamel juggler on the lid"),
              ("The pencil marks in the ruled book are cues", "The notes in the book are cues")]

# doc 11:55: the slash only where it's really a fraction; spool part 3 is where set 1 takes its time (orientation, curling arrows from
# crosses, why rolling → turns back around, one cross at a time, the opposite-sides balance, a check that it really turns ↻).
SLOWDOWN = [("(3) The cord pulls forward (→). Take the counter's grip on the spool, f, as positive → too; the answer will say which way it really goes. The center of mass speeds up as if both forces acted on it directly: ma = F + f. Rolling →, the spool turns back around, ↻. The cord pulls → 0.12 m below the axle and the grip acts → 0.20 m below it. Each torque is its lever crossed into its pull. Both levers point ↓ and both pulls →, so ↓\u200a×\u200a→ comes out of both, and the sizes add on their own first: r F ↓\u200a×\u200a→ + R f ↓\u200a×\u200a→ = (Fr + fR) ↓\u200a×\u200a→ = (Fr + fR) ↺: the net torque about the axle. A → push below the axle turns the spool forward around. So Iα ↻ = (Fr + fR) ↺. Rolling ties the two together: α = a/R. Put together, the ledgers balance as:", "(3) Start with which way is which. → is forward: the way the cord pulls. ← is back, the opposite of forward. Take the counter's grip on the spool, f, as → too; the answer will say which way it really goes. The center of mass speeds up as if both forces acted on it directly:\n    m a → = F → + f →.\nTurning has two senses too, and each one comes from a cross: a lever crossed into a push gives the turning that push makes about the axle. A forward push below the axle turns the spool forward around, ↺, and a forward push above it turns the spool back around, ↻:\n    ↓\u200a×\u200a→ = ↺,    ↑\u200a×\u200a→ = ↻.\n↻ is the opposite of ↺, the way ← is the opposite of →.\nWhich way does a spool rolling → turn? Look at the bottom, where it touches the counter. Rolling means the bottom isn't sliding, so the turning has to carry the bottom ← as fast as the center goes →. The bottom's lever from the axle is R ↓, and turning back around moves it back: ↻\u200a×\u200a↓ = ←. So a spool rolling → turns back around, ↻, and speeding up it picks up its turning ↻ at α = a/R.\nNow the torques, one cross at a time. The cord pulls → 0.12 m below the axle, and the grip, taken →, acts 0.20 m below it:\n    r F ↓\u200a×\u200a→ = Fr ↺,    R f ↓\u200a×\u200a→ = fR ↺.\nBoth levers point ↓ and both pulls →, so the sizes add: (Fr + fR) ↺, the net torque about the axle. The net torque picks up the turning:\n    I α ↻ = (Fr + fR) ↺.\nThe two sides carry opposite senses, and that's fine. The pickup is written ↻ because that's how a forward roll turns; the torques are written ↺ because that's how forward pulls below the axle turn. ↻ is the opposite of ↺, so the balance says Iα is the opposite of Fr + fR. It's the same move as the grip taken →: the numbers will say which way it really goes. Rolling ties the two ledgers together through α = a/R, and put together they balance as:"), ('It pulls back, and about the axle it turns the spool ↻ harder than the cord turns it ↺.', 'It pulls back, and about the axle it turns the spool ↻ harder than the cord turns it ↺. Check the turning: the cord gives 0.72 N m ↺ and the grip 0.88 N m ↻, so the net torque is 0.16 N m ↻. The spool picks up at a/R = 4.0 strokes a second each second, and 0.040 kg m² at 4.0 is 0.16 N m. It really does turn back around.'), ("That's the arm's downward part, ℓ / ↓: 0.40 m of its 0.50 m.", "That's the downward part of the arm, ↓\u200a·\u200aℓ = 0.40 m of its 0.50 m."), ("So →\u200a·\u200aF at R is Fr, and the pull's forward fraction, F / →, is r/R = 0.60 of it.", 'So →\u200a·\u200aF at R is Fr, and the forward part is r/R = 0.60 of the pull.')]

# doc 12:13: motivate the change, don't start with it. The knife and the governor keep the textbook cos θ; the dot arrives at
# spool part 4, after the arrows have earned their place at spool part 3, with the usual F cos θ said first.
LATE_DOT = [("(1) An arm ℓ long, leaning θ, hangs ↓\u200a·\u200aℓ below the pivot instead of ℓ. That's the downward part of ℓ: how much of the arm points straight down, the statement's ℓ cos θ. So the lean lifts its end by ℓ − ↓\u200a·\u200aℓ. For this small lean,", '(1) Leaning through θ lifts a point ℓ away by ℓ(1 − cos θ). For this small lean,'), ("That's the downward part of the arm, ↓\u200a·\u200aℓ = 0.40 m of its 0.50 m.", "On the 0.50 m arm that's cos θ = 0.80."), ('only its forward part changes. The forward part of F, →\u200a·\u200aF, is how much of the pull goes forward, and as a force it points forward too: →\u200a·\u200aF\u200a·\u200a→.', "only its forward part changes, to F cos θ in the usual notation. With the arrows already doing the directions, there's a plainer way to say it: the forward part of F is →\u200a·\u200aF, the pull dotted with forward, and as a force it points forward too, →\u200a·\u200aF\u200a·\u200a→.")]

DOC_1320 = [("one swing across; the cycle is the whole of it. Give the whole turn its own sign, τ.", "one swing across—the cycle is the whole of it.\nGive the whole turn its own sign, τ."),
            ("use that for torque: P = ωχ, with χ = 0.75 N m at the start.", "use that for torque. Power is the sweep of torque (P = ωχ), which starts at χ = 0.75 N m."),
            ("A small steam engine takes in 15 J of heat and does 3.0 J of work in each cycle, returning to its initial state at the end of each cycle. It completes one cycle per second.",
             "A small steam engine takes in 15 J of heat to do 3.0 J of work per one-second cycle.")]   # doc 16:03: returning to its initial state just redefines cycle
DOC_1320_SET1 = [("Of the 15 J that goes in, 3.0 J comes out as work and the other 12 J goes out as heat. Work over heat in is 3/15: 20 percent.",
                  "Call the heat that comes in the heat-in, and the heat that leaves the heat-out. Of 15 J of heat-in, 3.0 J comes out as work and the other 12 J is heat-out. Work over heat-in is 3/15: 20%.")]
DOC_1320_LATER = [("Of the 15 J that goes in, 3.0 J comes out as work and the other 12 J goes out as heat. Work over heat in is 3/15: 20 percent.",
                   "Of 15 J of heat-in, 3.0 J comes out as work and the other 12 J is heat-out. Work over heat-in is 3/15: 20%.")]

STATEMENT_FIX = [("pivoted so it swings freely in a vertical plane. It's released from rest", "pivoted to swing freely in a vertical plane. It gets released from rest"),   # doc's own edit, set 1 doc, 12:1x
                 ("the center moves at speed Lω/2, where", "the center moves at speed L\u200aω/2, where"),
                 ("(moment of inertia 2mR²/5)", "(moment of inertia 2\u200am\u200aR²/5)"),   # doc's hair spaces, 09:17
                 ("A spool of mass 2.0 kg, outer radius R = 0.20 m and hub radius r = 0.12 m has moment of inertia 0.040 kg m²† about its axle. It rests on a level counter.",
                  "A spool rests on a level counter. It has mass 2.0 kg, outer radius R = 0.20 m, hub radius r = 0.12 m, and moment of inertia 0.040 kg m²† about its axle."),
                 # doc, set 1 doc, 13:20 (the problem set has the rest of the willing-reader pass)
                 ("each on a massless 0.50 m arm", "each on a massless 0.5 m arm"),
                 ("outer radius R = 0.20 m, hub radius r = 0.12 m, and moment of inertia 0.040 kg m²†", "outer radius R = 0.2 m, hub radius r = 0.12 m, and moment of inertia 0.04 kg m²†"),
                 ("The spool rolls without slipping. Find its acceleration and the direction it rolls.", "If the spool rolls without slipping, how does it accelerate?"),
                 ("If the cord is instead pulled at an angle θ above horizontal, for what θ does the spool stay at rest?", "If the cord is instead pulled partly upward, at what angle does the spool stay at rest?")]
# turn-family units are count nouns and take a plural (doc, 08:06); dog park units stay bare (R-041)
STROKES = re.compile(r"(?<=[0-9√τ]) stroke\b")
LEGEND = "A value marked † is supplied: chosen so the house works, with the reason somewhere below the mansion."

def clean(ln, k):
    for rx, rep in NAV: ln = rx.sub(rep, ln)
    for old, new in TIMES: ln = ln.replace(old, new)
    if k == 2:
        for old, new in SET2_FIX: ln = ln.replace(old, new)
    return ln

def number_parts(lines):
    """Statement lines: first is setup; later bare lines become numbered parts unless they already are."""
    out, n = [], 0
    for i, ln in enumerate(lines):
        if i == 0 or ln.startswith("Use g"):
            out.append(("p", ln)); continue
        m = re.match(r"(\d+)\.\s+(.*)", ln)
        n = int(m.group(1)) if m else n + 1
        out.append(("p", f"{n}. {m.group(2) if m else ln}"))
    return out

def appendix_items(tabs, k):
    """Drawer/funhouse/understage problems as {key: [(kind, text)]}, plus scenery lines per appendix."""
    items, scenery = {}, {}
    for title, lines in tabs.items():
        if not title.startswith("Appendix"): continue
        bl = blocks(lines); app = title.split(" ")[1]
        pre = []
        for h, body in bl:
            if h is None: continue
            if h.startswith("Appendix"):
                pre = [ln for ln in body if not SKIP.match(ln)]; scenery[app] = pre; continue
            if h == "Solution":
                items[key] += [("b", "Solution")] + [("p", clean(ln, k)) for ln in body if not SKIP.match(ln)]
                continue
            if h == "The four voices": continue
            key = h.split(":")[0]
            if k == 2: h = h.replace("the second knife's two tones", "the second knife's two motions")
            body = [clean(ln, k) for ln in body if not SKIP.match(ln)]
            intro = [ln for ln in body if ln.startswith(("Door", "Doors", "Passage", "A long", "Two facing", "A hall", "A tilted", "Any of", "On the chassis"))]
            rest = [ln for ln in body if ln not in intro]
            items[key] = [("h3", h)] + [("i", ln) for ln in intro] + number_parts(rest)
    return items, scenery

def build(k):
    tabs = read(f"r{k}_now.txt")
    main = tabs["The mansion"]
    i0 = main.index("## The way in"); iE = next(i for i, l in enumerate(main) if l.startswith("## Ending"))
    route = "\n".join(main[i0:iE])
    # doc's own corrections in release 4 (21:4x) are what LEVEL[1] applies everywhere; undo them here so one edit list fits all four
    route = route.replace("needs the squared sweep to be 64.", "needs the square of the sweep to be 64.")
    route = route.replace("is the the sweep of the torque [ see how this means something and the other one is not English? ]  torque times the sweep:", "is the torque times the sweep:")
    route = apply_edits(route, k)
    # doc 2026-10-22: a letter moves when it's needed. Nothing needs I for anything else at the spool,
    # so it keeps the statement's I; inertia moves to η only where current has taken I (F2, U1).
    route = route.replace("a page somebody has already used", "a page someone has already used")   # doc, set 1, 07:31
    for old, new in SPOOL_I:
        if old in route: route = route.replace(old, new)
    assert "η" not in route, "η left in the mansion route"
    for alts in DOC_0806:   # each entry: one or more (old, new) variants; at least one must apply
        hit = False
        for old, new in alts:
            if old in route: route = route.replace(old, new); hit = True
        assert hit, alts[0][0][:70]
    turns = "turns" if k == 1 else "cranks"   # crank is a level-2 verb
    for old, new in NO_NEGATIVE_FORCES:   # doc 08:50: there are no negative forces, just directions
        new = new.format(turns=turns, turn=turns[:-1])
        assert route.count(old) == 1, old[:70]
        route = route.replace(old, new)
    route = STROKES.sub(" strokes", route)
    for old, new in SETUP_DOC:   # doc's way in, every set (sets 2-4 take it at the next sweep)
        if route.count(old) != 1:   # from level 2 the canteen stands unlatched
            old, new = old.replace("locked", "unlatched"), new.replace("locked", "unlatched")
        assert route.count(old) == 1, old[:70]
        route = route.replace(old, new)
    if k == 1:   # doc 2026-10-22 08:29: the slow walk to τ, in set 1
        for old, new in SLOW_WALK:
            assert route.count(old) == 1, old[:70]
            route = route.replace(old, new)
        for old, new in ARROWS + MOBILES + PRETTY:
            assert route.count(old) == 1, old[:70]
            route = route.replace(old, new)
        for old, new in MEANING:
            assert route.count(old) == 1, old[:70]
            route = route.replace(old, new)
        for old, new in SLOWDOWN:
            assert route.count(old) == 1, old[:70]
            route = route.replace(old, new)
        for old, new in LATE_DOT:
            assert route.count(old) == 1, old[:70]
            route = route.replace(old, new)
    else:        # the sweep, 09:47: the faster walk and set 1's other changes, in level-k words
        for alts in LATER:
            hit = False
            for old, new in alts:
                if route.count(old) == 1: route = route.replace(old, new); hit = True
            assert hit, alts[0][0][:70]
    # doc, set 1 doc, 13:20: his flywheel edits; heat-in and heat-out (his question, yes); 20% (R-114)
    for old, new in (DOC_1320 + DOC_1320_SET1 if k == 1 else DOC_1320_LATER):   # the τ walk and the χ sentence are set 1's own
        assert route.count(old) == 1, old[:70]
        route = route.replace(old, new)
    ending = main[iE:]
    items, scen = appendix_items(tabs, k)
    st = statements()
    out = [("h1", f"The Mansion, solution set {k} of 4: {NAMES[k]}")]
    out.append(("p", f"<b>Written by Claude (Anthropic), {DATE[k]}, for dr. kraemer.</b> Set {k} of four: the whole problem set done through, end to end, the way a reader at level {k} would do it, with every optional problem open at that level placed right after the room it belongs to. Assembled from Codex's (OpenAI) release copies and the checked drafts; the thirteen mansion solutions are re-said in this level's words. The ideas and vocabulary are dr. kraemer's; the words are the models'. Statements stay in standard language."))
    out.append(("i", f"Words this set uses: {WORDS[k]}."))
    out.append(("i", LEGEND))
    after = {"1. The knife": ["Drawer 4", "F1"], "3. The governor and the spool": ["Drawer 1"],
             "4. The ladder": ["Drawer 2", "F4"], "7. The hoop": ["Drawer 3"],
             "10. The coils and the capacitor": ["Drawer 5", "F2"], "11. The line": ["Drawer 6"],
             "12. The two lights": ["Drawer 7", "F3"], "13. The chair": ["U1", "U2"]}
    shown = set()
    for h, body in blocks(route.split("\n")):
        if h is None: continue
        m = re.match(r"(\d+)\. ", h)
        hold = []
        if h.startswith("12."):
            hold = [ln for ln in body if ln.startswith("In the chair’s frame")]
            body = [ln for ln in body if ln not in hold]
        body = [clean(ln, k) for ln in body]
        if m:
            n = int(m.group(1))
            out.append(("h3", h))
            sl = [x for x in st[n]]
            for old, new in STATEMENT_FIX: sl = [x.replace(old, new) for x in sl]
            sl = [x.replace("problem 12(c)", "problem 12, part 3").replace("problem 10(d)", "problem 10, part 4") for x in sl]
            if n == 10: sl = ["Four parts."] + sl
            out += [(t, s) for t, s in number_parts(sl)][1 if n == 10 else 0:]
            out.append(("b", "Solution"))
            out += [("eq" if ln.startswith("    ") or ln.startswith(("(m + η", "(m + I/R²)a")) or ln.startswith("a = F(1") else "p", ln.strip()) for ln in body]
            for key in after.get(h, []):
                if key in items:
                    if key.startswith("F") and "b" not in shown and "b" in scen:
                        out.append(("h2", "Into the funhouse")); out += [("i", s) for s in scen["b"]]; shown.add("b")
                    if key.startswith("Drawer") and "1" not in shown and "1" in scen:
                        out.append(("h2", "Into the cabinet")); out += [("i", s) for s in scen["1"]]; shown.add("1")
                    if key.startswith("U") and "γ" not in shown and "γ" in scen:
                        out.append(("h2", "Under the stage")); out += [("i", s) for s in scen["γ"]]; shown.add("γ")
                    out += items[key]
            if hold:
                out += [("i", s) for s in hold]
        else:
            out.append(("h2", h)); out += [("i", ln) for ln in body]
    # the chair paragraph held from 12 goes before 13: move it
    for idx, (t, s) in enumerate(out):
        if t == "h3" and s.startswith("13."):
            j = next(j for j, (tt, ss) in enumerate(out) if tt == "i" and ss.startswith("In the chair’s frame"))
            if j > idx:
                para = out.pop(j); out.insert(idx, para)
            break
    eh = ending[0][3:]
    out.append(("h2", eh))
    for ln in ending[1:]:
        if ln.startswith("## "): out.append(("h3", ln[3:]))
        else: out.append(("p", ln))
    out = [(t, STROKES.sub(" strokes", x)) for t, x in out]
    for old, new in EVERYWHERE:
        out = [(t, x.replace(old, new)) for t, x in out]
    if k >= 2:
        for old, new in DRAWER1:
            n = sum(x.count(old) for _, x in out); assert n == 1, (n, old[:60])
            out = [(t, x.replace(old, new)) for t, x in out]
        # R-097: after the knife brings sweep in as a unit, a stroke a second is a sweep (solutions only)
        i0 = next(i for i, (t, x) in enumerate(out) if "call it a sweep too" in x)
        sol = False
        for i in range(i0 + 1, len(out)):
            t, x = out[i]
            if t == "b" and x == "Solution": sol = True
            elif t in ("h2", "h3"): sol = t == "h2"   # a new problem's statement is standard language
            if sol:
                for rx, rep in SWEEP_UNIT: x = rx.sub(rep, x)
                out[i] = (t, x)
    return out

def to_html(items):
    h = ['<html><head><meta charset="utf-8"></head><body>']
    for t, s in items:
        e = html.escape(s, quote=False).replace("&lt;b&gt;", "<b>").replace("&lt;/b&gt;", "</b>").replace("†", "<sup>†</sup>")
        if t in ("h1", "h2", "h3"): h.append(f"<{t}>{e}</{t}>")
        elif t == "i": h.append(f"<p><i>{e}</i></p>")
        elif t == "b": h.append(f"<p><b>{e}</b></p>")
        elif t == "eq": h.append(f'<p style="margin-left:36pt">{e}</p>')
        else: h.append(f"<p>{e}</p>")
    h.append("</body></html>")
    return "\n".join(h)

if __name__ == "__main__":
    for k in (1, 2, 3, 4):
        items = build(k)
        open(f"set{k}.html", "w").write(to_html(items))
        open(f"set{k}.txt", "w").write("\n".join(("## " if t.startswith("h") else "") + re.sub("</?b>", "", s) for t, s in items))
        print(k, len(items), sum(len(s) for _, s in items))
