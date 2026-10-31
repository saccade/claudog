"""Dog Math, 10-31 pass: the product tables and their sentences come in (from the Straight Dope, 10-20 15:43,
reconciled with today's words), and the doc gets condensed. Claude (Anthropic), 2026-10-31, on doc's ask:
"please put the tables and the sentence definitions into the dog math doc, then condense it down some, I feel
like it's gotten repetitive."

Usage: python3 condense_2610311114.py LIVE.txt OUT.txt
LIVE.txt is the live doc's text, one paragraph per line (blank lines included), as read through the Docs API.
Every replacement asserts it hits exactly once, so a changed source stops the script instead of misapplying."""
import sys

src = open(sys.argv[1]).read()
if not src.endswith("\n"): src += "\n"


def rep(text, old, new, n=1):
    assert text.count(old) == n, (text.count(old), old[:70])
    return text.replace(old, new)


def cut(text, start, end):
    """The text from the line `start` up to (not including) the line `end`."""
    i = text.index("\n" + start + "\n") + 1
    j = text.index("\n" + end + "\n", i) + 1
    return text[i:j]


def heading(title):
    return f"{title}\n{'-' * len(title)}\n\n"


head = src[:src.index("\n1. Playing with ideas\n") + 1]
s1 = cut(src, "1. Playing with ideas", "2. House rules")
s2 = cut(src, "2. House rules", "3. The units")          # house rules and the steps-aside list
s3 = cut(src, "3. The units", "4. Saying products")
s4 = cut(src, "4. Saying products", "5. Verbing")
s5v = cut(src, "5. Verbing", "6. Ghosts")
s6 = cut(src, "6. Ghosts", "7. Verbing the ghosts")
s7 = cut(src, "7. Verbing the ghosts", "8. Ghost manners, and the letter")
s8 = cut(src, "8. Ghost manners, and the letter", "9. Turning words")
s9 = cut(src, "9. Turning words", "10. Balanced, with the d's on different sides")
s10 = cut(src, "10. Balanced, with the d's on different sides", "11. Electricity")
s11 = cut(src, "11. Electricity", "12. Light and clocks (on trial)")
s12 = cut(src, "12. Light and clocks (on trial)", "13. Stealth mode")
s13 = cut(src, "13. Stealth mode", "14. Road-legal mode")
s14 = cut(src, "14. Road-legal mode", "15. At talking speed")
s15 = cut(src, "15. At talking speed", "16. For outside eyes")
s16 = cut(src, "16. For outside eyes", "17. A few problems, said strong")
s17 = cut(src, "17. A few problems, said strong", "18. Blocks to hand off")
s18 = src[src.index("\n18. Blocks to hand off\n") + 1:]

# ---- 1 and 2: cross-references; the rules themselves stand
s1 = rep(s1, "is for outside eyes (sections 14 and 16).", "is for outside eyes (section 15).")
s2 = rep(s2, "    use it (section 9).", "    use it (section 10).")
s2 = rep(s2, "    up and out (section 9).", "    up and out (section 10).")

# ---- 3: doc's note on the card ("Card [not specifically] counts profiles"); ring lives in section 10
s3 = rep(s3, "Ring is the phase rate of anything that oscillates or waves, a\nstroke of phase a second (trial).\n\n", "")
old_card = [l for l in s3.split("\n") if l.startswith("Sheet and blanket count")][0]
i = s3.index(old_card); j = s3.index("\n\n", i)
s3 = s3[:i] + ("Sheet, blanket, and card all count area: a wing, a field, a\n"
               "floor, a drum's face. Profiles, which carry no mass, come out in\n"
               "area too, and the card is the handy size for them.") + s3[j:]

# ---- 4: the retired lot; "on" doesn't always divide (doc 10-27, queued); the table moves to section 5
s4 = rep(s4, "    of       leads with the operator: the sweep of the lot, the\n",
             "    of       leads with the operator: the sweep of the bulk, the\n")
s4 = rep(s4, "    at       leads with the thing: the lot at pace, a mass at a\n",
             "    at       leads with the thing: the bulk at pace, a mass at a\n")
s4 = rep(s4, "    on       divides: 3 roll on half a wheel\n",
             "    on       divides a rate spread on a lever (3 roll on half a\n"
             "             wheel), or lays one thing across another (a 0.1 mm\n"
             "             coat on 40 sheet is 4 liters of paint); the units\n"
             "             say which\n")
old = ("Duration and rate are rows in the multiplication table, not\n"
       "columns. Say \"z is the fluxion of y\" (force is the fluxion of the\n"
       "motion) and \"y adds z over time\" (a push adds motion over\n"
       "time). Mass is handled by the ghost version beneath each cell.\n")
s4 = rep(s4, old, "Say \"z is the fluxion of y\" (force is the fluxion of the motion)\n"
                  "and \"y adds z over time\" (a push adds motion over time). The\n"
                  "whole multiplication table is section 5.\n")

# ---- 5: the product tables, new
s5 = heading("5. The product tables") + """\
Products of the things a setup has, in five tables on one scheme,
rows 1 to 17 and columns a to u, so a cell's address needs no table
number. The sentence for each filled cell comes after the tables.

A setup is a body, or several, and an axis. Movement is a set-up
body's motion: the motion of a body turning about the setup's axis.

Rows are actions and rates; columns are things a setup has. A
scalar (a time, a mass) takes no column: the mass rides in the
ghost under each body cell, in parentheses. The ghost of the bulk
is the lever, of the movement the pace, of the inertia the profile.
The diagonal is the reflex, always a dot, out and back.

A product cell holds the other factor stable: torque is the pickup
of stable inertia. Let the inertia change and the rate of spin
gains a second term, the sweep of the spread; with no torque, the
pickup of the inertia equals the sweep of the tuck (the skater).

Lever each bit, then add: inertia, spin, and torque are taken bit
by bit, and never from a bulk or a movement that's already a sum.
A balanced wheel's bulks and movements add to nothing while its
inertia and spin are whole. Products along the axis (swing, sweep,
torque, spin) hold through a whole swing while they're steady;
products through the lever's direction (lever, bulk, movement)
hold moment to moment, so arc, transit, shift, work, and action add
up step by step.

A cell in the backward order carries its minus; running text says
the positive sentence, the lever at pace or the bulk at pace.

Table 1: the setup's starting pieces (rows 1 to 6, columns a to c)

+---------------+---------------------+----------+--------------+
| of →          | a lever ι           | b mass m | c bulk β     |
+---------------+---------------------+----------+--------------+
| 1 rate of     | pace                |          | movement     |
| 2 swing of    | arc                 |          | transit      |
| 3 sweep of    | pace                |          | movement     |
| 4 pickup of   | acceleration around |          | force around |
| 5 leverage of | profile (reflex)    | bulk     | inertia      |
| 6 pace of     | −swirl              | movement | −spin        |
+---------------+---------------------+----------+--------------+

The bulk column is the lever column with the mass in it, and the
mass column is the seam between them. 5a and 5c are reflexes, the
lever twice, so they dot. Row 6's minuses are the backward order.

Why the lever comes in twice: going out, the sweep of the lever
gives the pace; there, the mass at that pace gives the movement;
coming back, the leverage of that movement gives the spin. The
same arm does two jobs, taking the sweep out to the moving mass and
bringing the movement back into spin about the axis. The two
crosses are two quarter turns, and they land back on the axis,
facing the way the sweep faced; reverse either one and the spin
lands backward, row 6's minus. Take the mass away and what's left
of the trip is the profile. (The lever here is square to the axis;
general three-dimensional turning is out of scope.)
    ξ = ι × (m (ω × ι))

Table 2: the motion ledger (rows 7 to 12, columns d to i)

+-------------+----------------+-----------------+-----------------+
| of →        | d bulk β       | e inertia η     | f movement p    |
|             |   (lever ι)    |   (profile)     |   (pace ν)      |
+-------------+----------------+-----------------+-----------------+
| 7 duration  |                |                 | shift           |
|             |                |                 | (displacement)  |
+-------------+----------------+-----------------+-----------------+
| 8 rate      | movement       | spread          | force           |
|             | (pace)         | (splay)         | (acceleration)  |
+-------------+----------------+-----------------+-----------------+
| 9 swing     | transit (arc)  |                 |                 |
+-------------+----------------+-----------------+-----------------+
| 10 sweep    | movement       | spin            | center force    |
|             | (pace)         | (swirl)         | (center accel.) |
+-------------+----------------+-----------------+-----------------+
| 11 pickup   | force around   | torque, stable  | yerk            |
|             | (accel. around)| inertia (twirl) |                 |
+-------------+----------------+-----------------+-----------------+
| 12 leverage | inertia        |                 | spin            |
|             | (profile)      |                 | (swirl)         |
+-------------+----------------+-----------------+-----------------+

+-------------+----------------+-----------------+-----------------+
| of →        | g force F      | h torque χ      | i spin ξ        |
|             |   (accel. a)   |   (twirl)       |   (swirl)       |
+-------------+----------------+-----------------+-----------------+
| 7 duration  | impulse,       | boost, Δspin    |                 |
|             | Δmovement      | (Δswirl)        |                 |
|             | (Δpace)        |                 |                 |
+-------------+----------------+-----------------+-----------------+
| 8 rate      | yank (jerk)    |                 | torque (twirl)  |
+-------------+----------------+-----------------+-----------------+
| 12 leverage | torque, moment,|                 |                 |
|             | or torsion     |                 |                 |
|             | (twirl)        |                 |                 |
+-------------+----------------+-----------------+-----------------+

Rows 9 to 11 are empty in the second half. Empty cells are empty on
purpose: the leverage of the inertia is m r³ along the arm, and
nothing is measured in it; the arm enters a quantity exactly twice.
12g splits three ways against the arm. Free to turn, it's a torque
(slew brake off); held, it's a moment (brake on); along the arm's
own line, it's torsion.

Table 3: the energy ledger (rows 13 to 16, columns j to m; every
cell a dot)

+------------+--------------+------------+------------+--------------+
| of →       | j movement p | k force F  | l torque χ | m spin ξ     |
+------------+--------------+------------+------------+--------------+
| 13 path    | action       | work       |            |              |
| 14 swing   |              |            | work       | action       |
| 15 pace    | reflected    | power      |            |              |
|            | punch        |            |            |              |
| 16 sweep   |              |            | power      | reflected    |
|            |              |            |            | hook         |
+------------+--------------+------------+------------+--------------+

The same per mass for straight motion and per inertia for turning,
for the unafraid (rows 13 to 16, columns n to q):

+------------+--------------+------------+------------+--------------+
| of →       | n pace ν     | o accel. a | p pickup α | q sweep ω    |
+------------+--------------+------------+------------+--------------+
| 13 path    | zam          | zug        |            |              |
| 14 swing   |              |            | zlug       | zlam         |
| 15 pace    | reflected    | zow        |            |              |
|            | zip          |            |            |              |
| 16 sweep   |              |            | zlow       | reflected    |
|            |              |            |            | zing         |
+------------+--------------+------------+------------+--------------+

The reflected cells are reflexes: the pace of the movement, ν · p,
and the sweep of the spin, ω · ξ. Each is twice its store, because
the two factors grow together. The velocity of added motion is
stored as punch: each bit goes in at the velocity the body has
then, so from rest the store fills the triangle under the climb,
and the reflex is the whole rectangle. That holds with the mass
fixed; hook goes the same way with the inertia fixed.

Table 4: the bulk meeting things (row 17, columns r to u)

+-----------+------------+------------+-------------+-------------+
| bulk →    | r lever ι  | s pace ν   | t accel.    | u gravity g |
|           |            |            | around a    |             |
+-----------+------------+------------+-------------+-------------+
| 17 of /   | inertia    | spin       | torque      | load moment |
| at / under| (profile)  | (swirl)    | (twirl)     | or torque   |
+-----------+------------+------------+-------------+-------------+

The bulk is the one quantity that goes both ways: operators lead it
(the sweep of the bulk, 10d) and things follow it (the bulk at
pace, 17s). The bulk of the lever is a dot, both along the arm; the
other three cross. Under gravity the dot is there too, and it's the
heft: the bulk's upward part hefts, and its level part cranks
(section 4).

The cells, in sentences. A quantity that turns up in several cells
is said once, with every cell it fills.

  pace ν (1a, 3a): the rate at the lever's end; the sweep of the
      lever. ν = Δι / Δt = ω × ι
  arc (2a): the swing of the lever, ψ r long; step by step,
      Δx = Δψ × ι
  acceleration around a (4a): the pickup of the lever. a = α × ι
  profile (5a): the reflex of the lever. ι · ι = r²
  bulk β (5b): the leverage of the mass; mass on an arm, out along
      the arm. β = ι × m
  inertia η (5c, 12d, 17r): the leverage of the bulk; the bulk of
      the lever. η = ι · β
  swirl (6a): the lever at pace; the pace of the lever is minus it.
      ν × ι = −swirl
  movement p (1c, 3c, 6b, 8d, 10d): a set-up body's motion; the
      rate of the bulk, the sweep of the bulk, the pace of the mass.
      p = Δβ / Δt = ω × β = ν × m
  transit (2c, 9d): the swing of the bulk, mass along the arc; it
      keeps counting past a turn, like distance. transit = ψ m r
  force around (4c, 11d): the pickup of the bulk. F = α × β
  spin ξ (6c, 10e, 12f, 17s): the leverage of the movement; the
      sweep of the inertia; the bulk at pace (the pace of the bulk
      is minus it). ξ = ι × p = ω × η = β × ν
  shift (7f): the movement carried over time, steady movement only;
      a turning body's shift adds up step by step. Δshift = p × Δt
  impulse (7g): the duration of a net force, the movement it adds.
      Δp = F × Δt
  boost (7h): the duration of a net torque, the spin it adds.
      Δξ = χ × Δt
  spread (8e): the rate of the inertia; its opposite is the tuck,
      and for a ghost, splay and fold. spread = Δη / Δt
  force F (8f): the fluxion of the movement; a push or pull adds
      movement over time. F = Δp / Δt
  yank (8g): the fluxion of the force (its ghost is the jerk).
      yank = ΔF / Δt
  torque χ (8i, 11e, 12g, 17t): the fluxion of the spin; the pickup
      of stable inertia; the leverage of a force about the axis the
      setup is free on; the bulk of the acceleration around. It
      cranks, and can do work around the axle.
      χ = Δξ / Δt = α × η = ι × F = β × a
  moment M (12g, 17u): the leverage of a force across an arm that
      holds; it loads the arm and does no work around the axle. The
      load moment is the bulk under gravitation. M = ι × F = β × g
  torsion (12g): the leverage of a force around the arm's own line,
      through the offset; it wrings the arm. A wrench on a shaft is
      all offset.
  heft (the dot in 17u): the bulk's upward part under gravitation.
      heft = g (↑ · β)
  center force F⊙ (10f): the sweep of the movement, the force that
      keeps it on center. F⊙ = ω × p
  yerk (11f): the pickup of the movement, the growing part of the
      yank. yerk = α × p
  action (13j, 14m): the movement along the path; the spin through
      the swing. action = Σ p · Δx = ξ · ψ, with the spin steady
  work W (13k, 14l): a force along a path; a torque through a swing.
      W = Σ F · Δx = ψ · χ
  power P (15k, 16l): the pace of the force; the sweep of the
      torque. P = ν · F = ω · χ
  reflected punch (15j): the pace of the movement, twice the punch.
      ν · p
  reflected hook (16m): the sweep of the spin, twice the hook. ω · ξ

Columns n to q say the same with the mass or the inertia out: zug
is work per lump and zlug work per wheel, zow and zlow the power,
zam and zlam the action (section 3).

"""

# ---- 6 to 9: renumbered; doc's notes on the ghost letter applied ("usually Z ... most of the ghost quantities
# start with z" / "if there are multiple ghosts all of them should be Z or omega, not a mixture")
s5v = rep(s5v, "5. Verbing\n----------\n", "6. Verbing\n----------\n")
s6 = rep(s6, "6. Ghosts\n---------\n", "7. Ghosts\n---------\n")
s7 = rep(s7, "7. Verbing the ghosts\n---------------------\n", "8. Verbing the ghosts\n---------------------\n")
s8 = rep(s8, "8. Ghost manners, and the letter\n", "9. Ghost manners, and the letter\n")
i = s8.index("  - The familiar ones, velocity and the sweep, soothe, and need"); j = s8.index("  - The conventional quantities")
s8 = s8[:i] + """\
  - The familiar ones, velocity and the sweep, soothe, and need
    no letter. A problem with one scary ghost can give it a
    letter, and the letter is Z, since most of the ghosts' names
    start with z: Z for the one scary ghost, and Z_profile,
    Z_zing, Z_zlow when several are in play. Marks stay (Z₁, Z₂,
    Z₊, Z₋); a different ghost gets a different subscript, and a
    repeated symbol is the same quantity. Where impedance needs Z,
    the ghosts take Ω instead.

""" + s8[j:]
i = s8.index("  - All the ghosts wear"); j = s8.index("\n\n", i)
s8 = s8[:i] + ("  - All the ghosts wear the same letter, Z or Ω, never a mix.\n"
               "    Nobody gets left visible alone. If a later room needs the\n"
               "    switch, the earlier rooms change with it.") + s8[j:]
s8 = rep(s8, "    inertia meet. The ghosts give\n    way to them, never the other way round.", "    inertia meet. The ghosts give way to them, never the other\n    way round.")
s8 = rep(s8, "    shares an expression with the ohm:", "    shares an expression with the ohm:")   # stays: the ohm is spelled out beside Ω
for k, (a, b) in enumerate([("9. Turning words", "10. Turning words"),
                            ("10. Balanced, with the d's on different sides", "11. Balanced, with the d's on different sides"),
                            ("11. Electricity", "12. Electricity"),
                            ("12. Light and clocks (on trial)", "13. Light and clocks (on trial)")]):
    pass
s9 = rep(s9, "9. Turning words\n----------------\n", "10. Turning words\n-----------------\n")
s10 = rep(s10, "10. Balanced, with the d's on different sides\n---------------------------------------------\n",
               "11. Balanced, with the d's on different sides\n---------------------------------------------\n")
s10 = rep(s10, "for it. Roll kept and the wheel shrinking: each wheel lost adds a zing of hook.\n",
               "for it. Roll kept and the wheel shrinking: each wheel lost adds a\nzing of hook.\n")
s11 = rep(s11, "11. Electricity\n---------------\n", "12. Electricity\n---------------\n")
s12 = rep(s12, "12. Light and clocks (on trial)\n-------------------------------\n",
               "13. Light and clocks (on trial)\n-------------------------------\n")

# ---- 13 to 16: stealth; road-legal takes in "for outside eyes" and doc's note on soft edges
s13 = rep(s13, "13. Stealth mode\n----------------\n", "14. Stealth mode\n----------------\n")
s13 = rep(s13, "    problem (section 9).", "    problem (section 10).")
s13 = rep(s13, "  - Don't point at the ghosts (section 8).", "  - Don't point at the ghosts (section 9).")
s14 = rep(s14, "14. Road-legal mode\n-------------------\n", "15. Road-legal mode\n-------------------\n")
old = s14[:s14.index("  - No ramp.")]
s14 = rep(s14, old, old + """\
It's also the way to write for outside eyes. When doc says a piece
is for college, for high school, or for anyone outside the park,
write it road-legal: the dog units stay in the dog park, the rules
still hold (round hard, name things), and the verbs still run. The
2 kg center, running at 3.0 m/s, punches 9.0 J.

The modes have soft edges. The mansion solutions are road-legal,
but they show off the language a bit, past a plain commute, so
expect any rule here to get trampled now and then.

""")
s14 = rep(s14, "The definitions are the ones in sections 4 to 12, shortened.", "The definitions are the ones in sections 4 to 13, shortened.")
s15 = rep(s15, "15. At talking speed\n--------------------\n", "16. At talking speed\n--------------------\n")

# ---- 18: one key handed with every block, so nothing is said three times
blocks = s18
def block(name, nxt=None):
    i = blocks.index("    " + name + "\n")
    j = blocks.index("    " + nxt + "\n") if nxt else len(blocks)
    return blocks[i:j]
arrows = block("READING THE ARROWS", "CHECKING A DOG-MATH SOLUTION")
check = block("CHECKING A DOG-MATH SOLUTION", "WRITING A SIDE-BY-SIDE")
side = block("WRITING A SIDE-BY-SIDE", "WRITING IN DOG MATH")
write = block("WRITING IN DOG MATH")
units = check[check.index("    Units: hand 0.1 m"):check.index("    Quantities:")]
quant = check[check.index("    Quantities:"):check.index("    So \"zip per lump\" is a slip.")]
for b in (side, write):
    assert units in b and quant in b, "the shared paragraphs differ between blocks"
assert "\n\n" not in units.strip("\n")
key = arrows.replace("    READING THE ARROWS\n", "    THE KEY\n") + units + quant
check = check.replace(units, "").replace(quant, "")
check = rep(check, "    So \"zip per lump\" is a slip.\n",
                   "    Zip, zing, zump, and swirl are already per mass or per\n"
                   "    inertia, so \"zip per lump\" is a slip.\n")
i = check.index("    Arrows name directions in the scene, not on the page."); j = check.index("    Check both ledgers")
check = check[:i] + ("    Before calling a step inconsistent, make sure you didn't\n"
                     "    translate → as page-right or ↺ as clockwise.\n\n") + check[j:]
side = side.replace(units, "").replace(quant, "")
i = side.index("    Put this key at the top:\n"); j = side.index("    Say what holds, and why")
side = side[:i] + "    Put THE KEY's first paragraph, on the arrows, at the top.\n\n" + side[j:]
write = write.replace(units, "").replace(quant, "")
write = rep(write, "    \"over\" divide: 5 cat on 1 hand sweeps at 50.",
                   "    \"over\" divide a rate spread on a lever: 5 cat on 1 hand\n"
                   "    sweeps at 50. \"On\" also lays a coat on an area, a product:\n"
                   "    0.1 mm on 40 sheet is 4 liters of paint. The units say which.\n   ")
intro = blocks[:blocks.index("    READING THE ARROWS\n")]
intro = rep(intro, "Each block below is written to be handed whole to a helper, a bot\n"
                   "given one job, so each one stands alone and repeats what it needs.\n"
                   "People can read them too: they're the doc in brief.\n",
                   "Each block below is written to be handed to a helper, a bot given\n"
                   "one job. Hand THE KEY over with any of the others; the two together\n"
                   "stand alone. People can read them too: they're the doc in brief.\n")
s18 = intro + key + check + side + write

# ---- more condensing: what other sections already say
s2 = rep(s2, """19. In a side-by-side, both columns start from the same inputs,
    and each one stands alone: read without the other, every
    number on it has a source on it. The dog column is still
    math. Each quantity that keeps coming back gets an English
    name and one line on why to believe the name. Translate one
    to one first; flip, model, and reflip only where the
    translation reads badly.
""", """19. In a side-by-side, both columns start from the same inputs,
    and each one stands alone; the dog column is still math
    (section 18, WRITING A SIDE-BY-SIDE).
""")
s3 = rep(s3, """| whirl       | pickup of a body turning on  | 1 rad/s^2       |
|             | itself: a sweep per second.  |                 |
|             | A train picking up around a  |                 |
|             | track's center counts in     |                 |
|             | pickup, not whirl            |                 |
""", """| whirl       | pickup of a body turning on  | 1 rad/s^2       |
|             | itself (a train round a track|                 |
|             | picks up in pickup)          |                 |
""")
s3 = rep(s3, """| swirl       | spin per mass; for a point,  | 1 m^2/s         |
|             | the lever at pace; for a     |                 |
|             | body, lever each bit's       |                 |
|             | motion, add, then divide     |                 |
|             | by the mass; along the axis  |                 |
| twirl       | torque per mass; for a point,| 1 m^2/s^2       |
|             | the lever at acceleration;   |                 |
|             | for a body, lever each bit's |                 |
|             | push, add, then divide by    |                 |
|             | the mass (a balanced wheel   |                 |
|             | can twirl with its center    |                 |
|             | still); along the axis       |                 |
""", """| swirl       | spin per mass: the lever at  | 1 m^2/s         |
|             | pace, along the axis         |                 |
| twirl       | torque per mass: the lever at| 1 m^2/s^2       |
|             | acceleration, along the axis |                 |
""")
for line in ("    1 blanket                   = 10 sheet\n", "    1 wheel                     = a ponder at a meter\n",
             "    1 thump                     = a lump lifted a hand, dog gravity\n",
             "    dog gravity                 = 10 zoom\n", "    a turn                      = about 6.3 stroke\n"):
    s3 = rep(s3, line, "")
i = s11.index("Verbing them right:"); j = s11.index("Two problems, said strong")
s11 = s11[:i] + """Verbing them right: a can cans charge at a voltage, and doesn't
can voltage ("the can cans 24 mC at 12 V"). A coil coils flux at a
current, and doesn't coil current: the current runs around the
turns, and the flux is what threads them ("the coil coils 1.2 Wb
at 3.0 A"). A resistor burns power, and cans and coils nothing.

""" + s11[j:]

out = head + s1 + s2 + s3 + s4 + s5 + s5v + s6 + s7 + s8 + s9 + s10 + s11 + s12 + s13 + s14 + s15 + s17 + s18
out = rep(out, "\n\n\n", "\n\n", n=out.count("\n\n\n"))
open(sys.argv[2], "w").write(out)
lines = out.split("\n")
print(len(src.split("\n")), "->", len(lines), "lines;", max(len(l) for l in lines), "widest")
