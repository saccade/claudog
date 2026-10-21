import re, sys, textwrap
exec(open("/tmp/claude-0/-home-claude/703a9c19-4a4f-5d49-a5f7-811fca7a3452/scratchpad/haunt144.py").read().split("para(\"So the angular")[0])
GLUE += ["3 m g", "v0 (R + h)", "v_max", "R + h = 7R/5", "0.63 joule", "m Z v / R", "Z v / R"]
def lit(old, new):
    global t
    assert t.count(old) == 1, old[:60]; t = t.replace(old, new)

# room 3: its own letter for the tipping speed
a = t.index("3. The cube that meets a ridge"); b = t.index("4. The yo-yo on the slope")
sec = t[a:b]; n = sec.count("v0"); sec = sec.replace("call it v0, for which", "call it v_max, for which").replace("v0", "v_max")
t = t[:a] + sec + t[b:]
lit("""    (b) Find the largest v, call it v_max, for which the cube does
        not tip over the ridge.""", """    (b) Find the largest v, call it v_max, for which the cube
        does not tip over the ridge.""")
para("About the ridge's line, the cube's angular momentum is its movement levered at the height of its centre, s/2:",
     "About the ridge's line, the cube's angular momentum is its movement levered at the height of its centre, s/2. Call it its spin:")
para("which we'll call hook: half the spin, sweeping at omega. The cube hooks over the ridge only if its hook covers the heft it gains:",
     "which we'll call hook: half the spin, sweeping at omega. Taken about the ridge, which stays still, the hook is all of the cube's kinetic energy. The cube hooks over the ridge only if its hook covers the heft it gains:")
para("New house, new ghost. Z here is the yo-yo's profile, and it isn't the cube's: the old Z stayed in the old house.",
     "New room, new ghost. Z here is the yo-yo's profile, and it isn't the cube's: the old Z stayed in the old room.")
para("Work about the line where the yo-yo touches the slope.",
     "Work about the line of the yo-yo that touches the slope at this instant.")
para("contact's acceleration points straight at the centre.",
     "contact's acceleration points straight at the centre, which is the centre of mass.")
para("rolling ties to it; and this house's Z,", "rolling ties to it; and this room's Z,")
para("Then the profile, this house's Z, about the contact once it rolls:", "Then the profile, this room's Z, about the contact once it rolls:")
para("That has to be the swirl the cue gave it:",
     "That has to be the swirl the cue gave it. By now the ball is well along the table, away from the line the cue's boost was taken about, and that doesn't matter: about any line across the table, the centre's movement runs level, R above it, so the spin is the same about every one of them. That has to be the swirl the cue gave it:")
# the duplicated clause reads badly; collapse it
para("so the spin is the same about every one of them. That has to be the swirl the cue gave it:",
     "so the spin is the same about every one of them.")
para("its spin there is m Z v / R. Per mass, Z v / R.",
     "its spin there is m Z v / R. Per mass, Z v / R. That has to be the swirl the cue gave it.")
para("Strike at R + h = 7R/5, the sweet spot about the table,",
     "Strike at R + h = 7R/5, the sweet spot about the table, Z over the centre's lever R,")
para("we'll call it zing, and a profile across a zing is hook per mass: the ball zings as it turns.",
     "we'll call it zing, and a profile across a zing is hook per mass: the ball zings as it turns. About a line that is still, even for an instant, the hook is all the energy, as with the cube; about the centre, the centre's punch comes on top.")
para("having burned 0.63 J for each", "having burned 0.63 joule for each")

d = "20%s-%s-%s %s:%s" % (stamp[0:2], stamp[2:4], stamp[4:6], stamp[6:8], stamp[8:10])
t, n2 = re.subn(r"Written by Claude \(Anthropic\), \d{4}-\d\d-\d\d \d\d:\d\d\.", "Written by Claude (Anthropic), %s." % d, t); assert n2 == 1
open(dst, "w").write(t)
