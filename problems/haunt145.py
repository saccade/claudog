import re, sys, textwrap
exec(open("/tmp/claude-0/-home-claude/703a9c19-4a4f-5d49-a5f7-811fca7a3452/scratchpad/haunt144.py").read().split("para(\"So the angular")[0].replace("src, dst, stamp = sys.argv[1], sys.argv[2], sys.argv[3]","src, dst, stamp = sys.argv[1], sys.argv[2], sys.argv[3]"))
GLUE += ["a = alpha R", "3 mu_s cos phi)", "3 mu_s cos phi", "3 m g", "v0 (R + h)", "13/10 of v0^2", "81/70 of v0^2"]
def lit(old, new):
    global t
    assert t.count(old) == 1, old[:60]; t = t.replace(old, new)

para("ones that whisper you to sleep.",
     "ones that whisper you to sleep. A ghost is what's left of a quantity once the body's mass, or its moment of inertia, is divided out: velocity is momentum per mass, angular velocity is angular momentum per moment of inertia. Nothing left in a ghost weighs anything, which is how it walks through walls.")
lit("ring of radius R > b. The ball spins at angular speed omega", "ring of radius R > b. The ball turns at angular speed omega")
para("spins in place against the moving ring.", "turns in place against the moving ring.")
lit("""        not tip over the ridge.
""", """        not tip over the ridge.

    (This version takes the ridge's height as negligible.)
""")
para("For a 0.30 m cube, v0 is about 1.8 m/s.",
     "For a 0.30 m cube, v0 is about 1.8 m/s. Look at the left side of that first line before you leave the room: Z across half the sweep squared, with no mass anywhere in it. That shape comes back.")
para("Rolling ties the centre to it: a = alpha R.", "Rolling ties the centre to it: the centre speeds up at a = alpha R.")
lit("""    F_max = 3 m g (sin phi + 3 mu_s cos phi).
""", """    F_max = 3 m g (sin phi + 3 mu_s cos phi).

""" + W("""Pull too gently on a steep slope and the friction runs out the
other way, up the slope: below F = 3 m g (sin phi - 3 mu_s cos phi)
the contact slips. On a gentle slope that number is negative and
never comes up.""") + "\n")
para("Ghosts in the room: the familiar pickup, and this house's Z,",
     "Ghosts in the room: the pickup, and the centre's speed-up that rolling ties to it; and this house's Z,")
para("About a line drawn across the table under the ball, that's", "About a line drawn across the table under the ball, fixed to the table, that's")
para("the table's friction acts at that line, along the ball's path, and has no leverage about it;",
     "the table's friction acts in the table's surface, where the line lies, and has no leverage about it;")
para("The energy, per mass, sings the last chorus. Two more names first. Punch per mass, v^2 / 2, we'll call zip: the ball zips along. Half the sweep squared, omega^2 / 2, we'll call zing, and a profile across a zing is hook per mass: the ball zings as it turns. At the cue:",
     "The energy, per mass, sings the last chorus. At the cue:")
lit("""The energy, per mass, sings the last chorus.""", W("""Two more ghosts first, and the shape from the cube's room is one
of them. Punch per mass, v^2 / 2, we'll call zip: the ball zips
along. Half the sweep squared, omega^2 / 2, is hook per moment of
inertia; we'll call it zing, and a profile across a zing is hook per
mass: the ball zings as it turns.""") + "\n\nThe energy, per mass, sings the last chorus.")
para("Together, 13/10 of v0^2.", "Together, 13/10 of v0^2 per mass.")
para("Rolling at 9 v0/7: Z across the zing of v / R, 81/70 of v0^2.", "Rolling at 9 v0/7: Z across the zing of v / R, 81/70 of v0^2 per mass.")
para("In the fifth room a second one came out: the swirl. It kept its word name and got no letter. Then the chorus brought the rest.",
     "In the fifth room the rule broke. The swirl came out, and the chorus brought zip, zing and the profile about the centre out with it. Only Z has a letter; the rest kept their word names.")

def rows(label, L, R):
    G = lambda x: x.replace("v0 (R + h)", "v0\x00(R\x00+\x00h)")
    a = [y.replace("\x00"," ") for y in textwrap.wrap(G(L), 20)]; b = [y.replace("\x00"," ") for y in textwrap.wrap(G(R), 24)]
    n = max(len(a), len(b)); a += [""]*(n-len(a)); b += [""]*(n-len(b))
    return "\n".join("| %-13s | %-20s | %-24s |" % (label if i == 0 else "", x, y) for i, (x, y) in enumerate(zip(a, b)))
lit("| 3 Cube        | sweep                |", "| 3 Cube        | velocity, sweep      |")
lit("""| 4 Yo-yo       | pickup               | Z = 3 R^2 / 2, profile   |
|               |                      | about the contact        |""",
    rows("4 Yo-yo", "pickup, and the centre's speed-up", "Z = 3 R^2 / 2, profile about the contact"))
a = t.index("| 5 Billiards"); b = t.index("+", t.index("the centre               |"))
lit(t[a:b], rows("5 Billiards", "sweep, velocity", "Z = 7 R^2 / 5, profile about the contact. Also out: the swirl, v0 (R + h); in the chorus, zip, zing and the profile about the centre") + "\n")

d = "20%s-%s-%s %s:%s" % (stamp[0:2], stamp[2:4], stamp[4:6], stamp[6:8], stamp[8:10])
t, n = re.subn(r"Written by Claude \(Anthropic\), \d{4}-\d\d-\d\d \d\d:\d\d\.", "Written by Claude (Anthropic), %s." % d, t); assert n == 1
open(dst, "w").write(t)
