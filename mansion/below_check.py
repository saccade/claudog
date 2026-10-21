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

print("all checks pass")
