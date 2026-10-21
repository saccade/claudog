import sys, textwrap, re
src, dst, stamp = sys.argv[1:4]
t = open(src).read()
d = "20%s-%s-%s %s:%s" % (stamp[0:2], stamp[2:4], stamp[4:6], stamp[6:8], stamp[8:10])
t = t.replace("STAMP", d)
GLUE = ["0.40 m/s","0.30 m/s","0.50 m/s","0.25 m/s","0.20 m/s","0.15 m/s","1.5 m","3.0 m","1.8 m","2.4 m","1.6 m","0.60 m","0.20 m","0.80 m","3.0 m/s","2.42 m/s","1.29 m/s","1.62 rad/s","15 rad/s","0.17 rad/s","1.08 kg m^2/s","0.072 wheel","0.12 m^2","0.16 m^2","3.0 m^2","1.8 kg m/s","2.1 m/s","0.90 m/s","120 rad/s","2.21 J/kg","0.41 J/kg","1.80 J/kg","1.19 s","1.00 s","L / 2","R - b","b sin phi","m g b sin phi","(1/2) I omega^2","(1/2) m v^2","v^2 / 2","omega^2 / 2","v_x R + Z omega","v - R omega","m L^2 / 12","L^2 / 12","L^2 / 4","2 R^2 / 5","7 b^2 / 5","k^2","1/6","sin theta","dr. kraemer's","N m","0.25 m","(R - b) / b","(-0.6, 0.8)","(0.9, 1.2)","(0.20, -0.15)","(1.8 m, 2.4 m)","g (R - b)","5 v_x / (2 R)","-3 v_x / 4","v_x = R omega","12 kg","3.0 m^2","29 N","29 oompf","58 roll","36 wheel","4.85 m/s","(m/7)(v_x - R omega)^2","omega^2 = 9.8 (0.8 / 3) = 2.6","(3g/4)(1 - u^2)","(3g/4) u^2","(L / 2) u","b s","0.8 - u","u = 0.8","phi^2 / 2","(3g/4) cos^2 theta","(3g/4) sin^2 theta","3g/4","2.2 J","0.4 J","1.8 J","2 R^2 / 5 of profile","on 0.072 wheel","L^2 / 12 = 0.12 m^2","m across Z","(L / 2) omega","v = 0"]
def W(s):
    s = " ".join(s.split())
    for g in sorted(GLUE, key=len, reverse=True): s = s.replace(g, g.replace(" ", "\x00"))
    return textwrap.fill(s, 66, break_long_words=False).replace("\x00", " ")
def rows(widths, cells):
    G = lambda x: x.replace("v0 (R + h)", "v0\x00(R\x00+\x00h)").replace("v = 0", "v\x00=\x000")
    cols = [[y.replace("\x00"," ") for y in textwrap.wrap(G(c), w, break_on_hyphens=False)] or [""] for c, w in zip(cells, widths)]
    n = max(len(c) for c in cols)
    for c in cols: c += [""] * (n - len(c))
    return "\n".join("| " + " | ".join("%-*s" % (w, c[i]) for c, w in zip(cols, widths)) + " |" for i in range(n))
def table(widths, head, body):
    sep = "+" + "+".join("-" * (w + 2) for w in widths) + "+"
    return "\n".join([sep, rows(widths, head), sep] + [rows(widths, r) for r in body] + [sep])
reg = table([10, 15, 22, 19], ["Room", "Familiar", "Z, and what else got out", "What stays still"], [
 ["1 Ladder", "velocity, sweep", "none", "a point in the air, the rectangle's fourth corner"],
 ["2 Rod", "velocity, sweep", "Z = L^2 / 12, profile about the centre", "a point on the rod, two thirds down"],
 ["3 Ladder", "sweep, the centre's speed-up", "Z = L^2 / 3, profile about the still point", "the point in the air again"],
 ["4 Ball", "velocity, sweep", "Z = 2 R^2 / 5, profile about the centre. Also out: the swirl, zip, zing", "a line in the floor"],
 ["5 Marble", "sweep, pickup", "Z = 7 b^2 / 5, profile about the contact", "the contact"]])
side = table([10, 27, 27], ["Problem", "Textbook route", "straight->"], [
 ["1 Ladder", "Differentiate x^2 + y^2 = L^2; find the instantaneous centre from the perpendiculars to two velocities.", "Every pace is the sweep of a lever from the still point."],
 ["2 Rod", "Impulse gives v_cm; angular impulse about the centre gives omega; find where v = 0.", "The boost on the inertia sets the sweep; the still point sits Z over the struck lever from the centre, and the struck end is its sweet spot."],
 ["3 Ladder", "Energy with I_cm and v_cm; the wall's force from a_cm; set it to zero.", "Hook about the still point with Z = L^2 / 3; the wall lets go when the centre stops speeding up sideways."],
 ["4 Ball", "Angular momentum about the contact and energy; solve the quadratic.", "The swirl holds and the zip and zing hold; the slip reverses; two bounces bring it back."],
 ["5 Marble", "Energy with I_cm, v_cm and the rolling constraint, or torques about the centre with friction.", "Gravity cranks about the contact; the torque on m across Z is the pickup; the square root of Z over b^2 slows the clock."]])
out = []
for block in t.split("\n\n"):
    if block.strip() == "TABLE_REGISTER": out.append(reg)
    elif block.strip() == "TABLE_SIDE": out.append(side)
    elif block.startswith("    ") or re.match(r"^.+\n[=-]+$", block) or "\n" in block.strip() and all(l.startswith("    ") for l in block.split("\n")[1:]):
        out.append(block.rstrip("\n"))
    else: out.append(W(block))
open(dst, "w").write("\n\n".join(out).rstrip() + "\n")
