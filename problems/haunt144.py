import re, sys, textwrap
src, dst, stamp = sys.argv[1], sys.argv[2], sys.argv[3]
t = open(src).read()
GLUE = ["V / R", "2 R^2/5", "(3/16) m v^2", "(1/2) m v^2", "2.1 m/s", "2.7 m/s", "0.63 J", "v + b omega", "2 v0 / R", "v / R", "v^2 / 2", "omega^2 / 2", "(1/2) I omega^2", "9 v0/7", "11 percent", "R Omega / b", "J (R + h)", "m g cos phi", "m g sin phi", "2 m s^2 / 3", "m Z", "4 v0^2/5", "9/5 R", "called Z:"]
def W(s):
    s = " ".join(s.split())
    for g in GLUE: s = s.replace(g, g.replace(" ", "\x00"))
    return textwrap.fill(s, 66).replace("\x00", " ")
N = lambda s: " ".join(s.split())
def para(old, new):
    global t
    blocks = t.split("\n\n"); hits = 0
    for i, b in enumerate(blocks):
        if b[:1] in " |+" : continue
        if N(old) in N(b):
            blocks[i] = W(N(b).replace(N(old), N(new))); hits += 1
    assert hits == 1, (hits, old[:50])
    t = "\n\n".join(blocks)

para("So the angular velocity is V / R.", "So the angular speed is V / R.")
para("runs at R times the sweep, V, square to the lever.", "runs at R times that sweep, which is V, square to the lever.")
para("the bead stands still for an instant. That instant is what rolling without slipping means.",
     "the bead stands still for an instant. Whatever point is at the bottom stands still for its instant: that is what rolling without slipping means.")
para("the centre stands still and the ball just spins in place against the moving ring.",
     "the centre stands still and the ball just spins in place against the moving ring. Any faster, and the centre runs back around.")
para("whatever the cube weighs. It doesn't belong to the cube. It belongs to the shape. It's the profile,",
     "whatever the cube weighs. It belongs to the shape and the line it turns about, not to the cube. It's the profile,")
para("the room calls it Z.",
     "the room calls it Z. Put the mass back across the ghost and the inertia comes out of the wall: m across Z, which is m times Z, 2 m s^2 / 3 of wheel.")
para("cranks back down the slope at m g R sin phi. In N m, which we'll call crank.",
     "cranks back down the slope at m g R sin phi. In N m, which we'll call crank. Gravity's other part, m g cos phi into the slope, also acts at the centre, but its line runs straight through the contact, so it has no leverage there.")
para("The angular acceleration is the net crank on the inertia. Call it the pickup: the yo-yo picks up at",
     "Crank is how fast spin grows, and the yo-yo's spin about the contact is m Z sweeping, as the cube's was about the ridge. So the angular acceleration is the net crank on the inertia. Call it the pickup: the yo-yo picks up at")
para("What the names add is that the mass drops out on the way.",
     "What the names add is a name for what's left when the mass drops out: Z.")
para("acts along that line and has no leverage about it;", "acts at that line, along the ball's path, and has no leverage about it;")
para("cue to the moment the ball rolls, at J (R + h).", "cue to the moment the ball rolls, at J (R + h) of roll.")
para("table drags the spin down and the speed up", "table drags the spin about the centre down and the speed up")
para("and a profile across a zing (across: times it) is hook per mass", "and a profile across a zing is hook per mass")
para("and the mass never once had to come out of the walls.", "and the mass cancelled before a single number went in.")
o = "| Room          | Familiar ghosts      |"; assert t.count(o) == 1
t = t.replace(o, "| Room          | Everyday ghosts      |")
d = "20%s-%s-%s %s:%s" % (stamp[0:2], stamp[2:4], stamp[4:6], stamp[6:8], stamp[8:10])
t, n = re.subn(r"Written by Claude \(Anthropic\), \d{4}-\d\d-\d\d \d\d:\d\d\.", "Written by Claude (Anthropic), %s." % d, t)
assert n == 1
# header paragraph got rewrapped? ensure first lines intact
open(dst, "w").write(t)
