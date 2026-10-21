import re, sys, textwrap
src, dst, stamp = sys.argv[1], sys.argv[2], sys.argv[3]
t = open(src).read()
GLUE = ["V / R", "2 R^2/5", "(3/16) m v^2", "(1/2) m v^2", "2.1 m/s", "2.7 m/s", "0.63 J", "v + b omega", "2 v0 / R", "v / R", "v^2 / 2", "omega^2 / 2", "(1/2) I omega^2", "9 v0/7", "11 percent"]
def W(s):
    s = " ".join(s.split())
    for g in GLUE: s = s.replace(g, g.replace(" ", "\x00"))
    return textwrap.fill(s, 66).replace("\x00", " ")
def rep(old, new, wrap=True):
    global t
    assert t.count(old) == 1, old[:60]
    t = t.replace(old, W(new) if wrap else new)

rep("""Five rooms. The first two are lit, and only the ghosts everybody
already lives with are about: velocity and angular velocity, the
ones that whisper you to sleep. The third room has something new in
it. It goes by Z. Every room after that has a Z of its own, and we
never let two of them out of the walls at once if we can help it.
By the fifth room, we can't.""",
"""Five rooms. The first two are lit, and only the ghosts everybody
already lives with are about: velocity and angular velocity, the
ones that whisper you to sleep. The third room has something new in
it, and it goes by Z. Every room after that has a Z of its own: one
scary ghost to a room, and whichever it is gets the letter. By the
fifth room, a second one wants out.""")

rep("""That's the answer. Now the bead's pace, the speed it moves at, is
the centre's pace plus the sweep of its lever. At the top the two
point the same way and add: the bead runs at 2V. At the bottom they
point opposite ways and cancel: the bead stands still for an
instant. That instant is what rolling without slipping means.""",
"""That's the answer. Now the bead's pace, its velocity, is the
centre's pace plus the lever's own: a lever R long sweeping at V / R
runs at R times the sweep, V, square to the lever. At the top the
two point the same way and add: the bead runs at 2V. At the bottom
they point opposite ways and cancel: the bead stands still for an
instant. That instant is what rolling without slipping means.""")

rep("""The ball's surface there is the centre's pace plus the ball's own
sweep of its lever. That lever is b long, pointing outward from the
ball's centre to the ring, and sweeping forward around at omega it
runs forward around at b omega. So the ball's surface runs at
v + b omega.""",
"""The ball's surface there runs at the centre's pace plus its
lever's. That lever is b long, pointing outward from the ball's
centre to the ring, and sweeping forward around at omega it runs
forward around at b omega. So the ball's surface runs at
v + b omega.""")

rep("""Ghosts in the room: still only sweeps and paces. Two sweeps now,
singing in thirds.""",
"""Ghosts in the room: still only sweeps and paces, two sweeps now.""")

rep("""    (b) Find the largest v for which the cube does not tip over the
        ridge.""",
"""    (b) Find the largest v, call it v0, for which the cube does
        not tip over the ridge.""", wrap=False)

rep("""    Z = I_edge / m = 2 s^2 / 3.
""",
"""    Z = I_edge / m = 2 s^2 / 3.

""" + W("""Textbooks write it k^2, the square of the radius of gyration.
Here the rule is one scary ghost to a room, and whichever ghost it
is, the room calls it Z.""") + "\n", wrap=False)

rep("""(b) Wheeling over, the cube has to lift its centre from s/2 above
the ridge to s / sqrt(2), straight over it. The cube carries the
hook to do it: half its spin, sweeping at omega, (1/2) m Z omega^2.
It must cover the heft it gains:""",
"""(b) Wheeling over, the cube has to lift its centre from s/2 above
the ridge to s / sqrt(2), straight over it. That rise costs
potential energy, m g times the rise, which we'll call heft. What
pays for it is the kinetic energy of the turning, (1/2) I omega^2,
which we'll call hook: half the spin, sweeping at omega. The cube
hooks over the ridge only if its hook covers the heft it gains:""")

rep("""The collision keeps 3/16 of v^2 out of the 1/2 it came in with:
3/8 of the punch survives as hook, and the rest is burned in the
crunch.""",
"""The cube came in with (1/2) m v^2 of kinetic energy, all of it
straight-line, which we'll call punch. It leaves with hook,
(3/16) m v^2. So 3/8 of the punch survives as hook, and the rest is
burned in the crunch.""")

rep("""Work about the line where the yo-yo touches the slope. That line is
still for an instant, as in problem 1, and the slope's friction and
support both act on it, so neither has leverage there.""",
"""Work about the line where the yo-yo touches the slope. The slope's
friction and support both act on that line, so neither has leverage
there. Taking torques about a moving point needs a reason, and here
it is: a round body rolling on a flat slope has its contact still
for an instant, as in problem 1, and the contact's acceleration
points straight at the centre. About that line, torque over the
moment of inertia gives the angular acceleration, just as it would
about the centre.""")

rep("""    the cue with speed v0 and some spin, skids, and when it finally
    rolls without slipping its speed is 9 v0 / 7. Find h / R.""",
"""    the cue with speed v0 and some rotation, skids, and when it
    finally rolls without slipping its speed is 9 v0 / 7. Find
    h / R.""", wrap=False)

rep("""The textbook route: the blow's impulse J sets m v0 = J; its angular
impulse about the centre sets the spin, (2/5) m R^2 omega0 = J h;
then friction during the skid slows or speeds the centre while
changing the spin, two equations with the friction in both, until
v = R omega. It's a page.""",
"""The usual route: the blow's impulse J sets m v0 = J; its angular
impulse about the centre sets the spin, (2/5) m R^2 omega0 = J h;
then friction during the skid slows or speeds the centre while
changing the spin, two equations with the friction in both, until
v = R omega. The sharper textbooks (Kleppner and Kolenkow, for one)
skip the friction by taking angular momentum about a line on the
table. That's the route here too. What the names add is that the
mass drops out on the way.""")

rep("""acts along that line and has no leverage about it; the support and
the weight cancel. So the spin""",
"""acts along that line and has no leverage about it; the support and
the weight act along one upright line, equal and opposite, so their
leverages about it cancel. So the spin""")

rep("""The energy, per mass, sings the last chorus. At the cue: zip of
v0^2/2 for the centre, and the turning carries 4 v0^2/5 more: the
profile about the centre, 2 R^2/5, across the zing of its sweep.
Together, 13/10 of v0^2. Rolling at 9 v0/7: Z across the zing,
81/70 of v0^2. The skid burns the difference, exactly v0^2/7 for
every kilogram of ball. At 2.1 m/s off the cue, the ball rolls
away at 2.7 m/s, having burned 0.63 J for each kilogram of it in
the scuff.""",
"""The energy, per mass, sings the last chorus. Two more names first.
Punch per mass, v^2 / 2, we'll call zip: the ball zips along. Half
the sweep squared, omega^2 / 2, we'll call zing, and a profile
across a zing (across: times it) is hook per mass: the ball zings
as it turns. At the cue: zip of v0^2/2 for the centre, and the
turning carries 4 v0^2/5 more: the profile about the centre,
2 R^2/5, across the zing of its sweep, 2 v0 / R. Together, 13/10 of
v0^2. Rolling at 9 v0/7: Z across the zing of v / R, 81/70 of v0^2.
The skid burns the difference, exactly v0^2/7 for every kilogram of
ball, about 11 percent of what the cue gave. At 2.1 m/s off the
cue, the ball rolls away at 2.7 m/s, having burned 0.63 J for each
kilogram of it in the scuff.""")

rep("""the pace agree, the zip and the zing settle, and the table takes
its seventh.""",
"""the pace agree, the zip and the zing settle, and the table burns
its v0^2/7.""")

rep("""Z gets reused from room to room because it's a different ghost in
each house, and only one at a time. In the fifth room a second one
came out: the swirl. It kept its word name and got no letter. Then
the chorus brought the rest. If two ever need letters at once,
that's a new rule.""",
"""Z gets reused from room to room because the letter belongs to the
room, not the ghost: each room has one scary ghost, and that's the
one called Z. The cube's Z and the yo-yo's are different ghosts. In
the fifth room a second one came out: the swirl. It kept its word
name and got no letter. Then the chorus brought the rest. If two
ever need letters at once, that's a new rule.""")

def rows(label, L, R):
    a = textwrap.wrap(L, 27); b = textwrap.wrap(R, 27)
    n = max(len(a), len(b)); a += [""]*(n-len(a)); b += [""]*(n-len(b))
    return "\n".join("| %-10s | %-27s | %-27s |" % (label if i == 0 else "", x, y)
                     for i, (x, y) in enumerate(zip(a, b)))

rep("""| 1 Bicycle  | Rolling: omega = V / R;     | The lever swings back       |
|            | add centre and rim vectors. | around at V / R; the bead's |
|            |                             | pace is the centre's plus   |
|            |                             | the sweep of its lever.     |""",
rows("1 Bicycle", "Rolling: omega = V / R; add centre and rim vectors.",
     "The lever swings back around at V / R; the bead's pace is the centre's plus the lever's, R times the sweep."), wrap=False)

rep("""| 5 Billiard | Impulse and angular impulse | The cue's boost about the   |
|            | about the centre; friction  | table line is a swirl that  |
|            | in two equations; impose    | holds; Z turns it into the  |
|            | rolling.                    | rolling speed.              |""",
rows("5 Billiard", "About the centre: impulse, angular impulse, friction in two equations. Sharper texts: angular momentum about the table line.",
     "The cue's boost about the table line is a swirl that holds; Z turns it into the rolling speed, and the mass drops out."), wrap=False)

a=t.index("The cue gives the ball J of oompf"); b=t.index("at J (R + h).")+13
t=t[:a]+W(t[a:b])+t[b:]
d = "20%s-%s-%s %s:%s" % (stamp[0:2], stamp[2:4], stamp[4:6], stamp[6:8], stamp[8:10])
t, n = re.subn(r"Written by Claude \(Anthropic\), \d{4}-\d\d-\d\d \d\d:\d\d\. MIT 8\.01SC \(Fall\n2016\)",
               "Written by Claude (Anthropic), %s. MIT 8.01SC (Fall\n2016)" % d, t)
assert n == 1
open(dst, "w").write(t)
