"""Checks every number in the below-stairs problems (cabinet, funhouse, understage).

Claude (Anthropic), 2026-10-21. One section per drawer or problem; run it and
every line should print OK.
"""
from fractions import Fraction as F
import math

g = 10.0


def ok(name, got, want, tol=1e-9):
    good = abs(got - want) <= tol * max(1.0, abs(want))
    print(("OK  " if good else "BAD ") + f"{name}: {got} (want {want})")
    assert good


# Drawer 1: the kitchen's two 3-4-5s
# Governor: arm hinged on the axis; cos(theta) = g/(l w^2).
l = 0.50
cos_target = 0.8                      # the 4 of a 3-4-5, height over arm
w = math.sqrt(g / (l * cos_target))
ok("governor speed for cos = 4/5", w, 5.0)
ok("ball rises", l * (1 - cos_target), 0.10)
ok("reach (3 of 3-4-5, times l/5)", l * math.sqrt(1 - cos_target**2), 0.30)

# Spool: a = F (1 - r/R) / (m + I/R^2), pulled horizontally from the hub's bottom.
m, R, r, Fpull = 2.0, 0.20, 0.12, 6.0
I = 0.040
ok("I/R^2", I / R**2, 1.0)
ok("I is a uniform disc's", I, m * R**2 / 2)
a = Fpull * (1 - r / R) / (m + I / R**2)
ok("spool acceleration", a, 0.80)
# same thing counted about the contact: crank F(R - r) on inertia I + m R^2
alpha = Fpull * (R - r) / (I + m * R**2)
ok("pickup about the contact times R", alpha * R, a)
# and about the centre, both ledgers, forward and forward-rolling positive.
# Forces below the centre pushing forward turn it backward, so
#   m a = F + f,   I a/R = -F r - f R
f = m * a - Fpull
ok("friction (backward)", f, -4.4)
ok("centre ledger: I a/R = -F r - f R", I * a / R, -Fpull * r - f * R)
# balance angle: line of pull through the contact, cos = r/R
ok("balance cos", r / R, 0.60)
ok("balance angle in degrees", math.degrees(math.acos(r / R)), 53.13010235415598)

# Drawer 2: the wall lets go. Ladder L, top at h0, frictionless.
L, h0 = 3.0, 2.4
assert abs(F(1,4)+F(1,12)-F(1,3))==0      # profiles add to L^2/3
y_leave = 2*h0/3
ok("top leaves the wall at", y_leave, 1.6)
# center's sideways speed^2 ~ y^2 (h0 - y): peak by brute force
ys=[h0*i/100000 for i in range(1,100000)]
yb=max(ys,key=lambda y:y*y*(h0-y))
ok("peak of y^2 (h0-y)", yb, y_leave, tol=1e-4)
w2 = 3*g*(h0-y_leave)/L**2
ok("omega^2 at leaving", w2, 8/3)
ok("center speed at leaving", (L/2)*math.sqrt(w2), math.sqrt(6))
# energy check: heft released = (1/6) m L^2 w^2 (per kg)
ok("heft = (1/6) L^2 w^2", g*(h0-y_leave)/2, L**2*w2/6)

# Drawer 3: turning about the contact
assert F(2,5)+1==F(7,5)
a_basin = F(5,7)
ok("basin period equals 1 m knife", 2*math.pi*math.sqrt(7*float(a_basin)/(5*g)), 2*math.pi*math.sqrt(1/g))
ok("rolling KE over bead KE", 0.5*float(F(7,5))/0.5, 1.4)
R=0.050
ok("cue height for rolling at once", 7*R/5, 0.070)
# impulse about the center check: J(H-R) = (2/5) m R^2 (v/R), J = m v
J, m1 = 2.0, 1.0
v=J/m1
ok("angular impulse about center", J*(7*R/5-R), 0.4*m1*R*v)

# Drawer 4: the double pendulum's tones from its shapes (l = 1, g = 10)
for sgn in (+1,-1):
    w2 = (2 - sgn*math.sqrt(2))*g
    ok(f"first balance, shape {sgn:+d}sqrt2", (2+sgn*math.sqrt(2))*w2, 2*g)
    ok(f"second balance, shape {sgn:+d}sqrt2", (1+sgn*math.sqrt(2))*w2, sgn*math.sqrt(2)*g)
wa, wb = math.sqrt((2-math.sqrt(2))*g), math.sqrt((2+math.sqrt(2))*g)
ok("slow tone", round(wa,2), 2.42); ok("fast tone", round(wb,2), 5.84)
ok("ratio", wb/wa, 1+math.sqrt(2))

# Drawer 5: C so the loop matches the slow tone
C = 1/(0.10*wa**2)
ok("C", round(C,2), 1.71)
ok("turn of the slow tone", round(2*math.pi/wa,2), 2.60)

# Drawer 6: crest speeds
u=1.0e8; f1, f2 = 5.0e6, 4.0e6
ok("fast crest", u*(f1+f2)/(f1-f2), 9.0e8)
ok("slow crest", u*(f1-f2)/(f1+f2), u/9)
ok("fast crest over c", u*(f1+f2)/(f1-f2)/3.0e8, 3.0)
# identity check at a random point
import random
k1,k2,w1,w2_=2*math.pi*f1/u,2*math.pi*f2/u,2*math.pi*f1,2*math.pi*f2
for _ in range(5):
    x,t=random.uniform(-5,5),random.uniform(-1e-6,1e-6)
    lhs=math.cos(k1*x-w1*t)+math.cos(k2*x+w2_*t)
    rhs=2*math.cos(((k1-k2)*x-(w1+w2_)*t)/2)*math.cos(((k1+k2)*x-(w1-w2_)*t)/2)
    ok("sum identity", lhs, rhs, tol=1e-9)

# Drawer 7: the two lights
r=4
beta=(r-1)/(r+1); gam=1/math.sqrt(1-beta**2)
ok("beta", beta, 0.6); ok("gamma", gam, 1.25); ok("gamma formula", (r+1)/(2*math.sqrt(r)), gam)
s=math.sqrt((1-beta)/(1+beta))
ok("bright pulse in H", 80*s, 40.0); ok("dim pulse in H", 20/s, 40.0)
ok("triangle", (r-1)**2+(2*math.sqrt(r))**2, (r+1)**2)

print("all checks pass")
