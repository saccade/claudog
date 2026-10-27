"""Where a 20 cat nozzle can reach: checks for the side-by-side. Claude, 2026-10-27.

Water leaves the nozzle at 20 cat (20 m/s) in any direction; gravity 10 zoom; no air.
The usual way finds the boundary from a discriminant. The dog way reads height at a
distance as a hill in launch slope, and the two streams that reach a point merge at its top.
"""

import numpy as np
from fractions import Fraction as F

u, g = 20, 10
fwd, up = np.array([1., 0]), np.array([0., 1])

def stream(slope):
    """Launch velocity at a launch slope: up part = slope x forward part, 20 cat in all."""
    f = u/np.sqrt(1 + slope**2)
    return f*fwd + slope*f*up

def height_at(x, slope):
    v0 = stream(slope); t = x/(v0 @ fwd)
    return (v0 @ up)*t - g*t**2/2

def drop(x):
    """stream drop: a level stream reaches x in x/20 s and falls 5 t^2."""
    return g*(x/u)**2/2

H = u**2/(2*g)                                                   # straight-up height
assert H == 20 and np.isclose(u/g * u/2, 20)                     # 2 s at an average of 10 cat

# The dog column's hill: height at distance x is the aim line's rise less (1 + s^2) drops.
for x in (5, 20, 32, 30, 40, 55):
    for s in (-1, 0, .5, 1, 2, 3, 4/3):
        assert np.isclose(height_at(x, s), s*x - drop(x)*(1 + s**2))
        # completed square: the top is the straight-up height above the level stream's curve
        assert np.isclose(height_at(x, s), H - drop(x) - drop(x)*(s - u**2/(g*x))**2)

# At 20 m: drop 5, hill 15 - 5 (s - 2)^2; slopes 1 and 3 both reach 10 m; the top is 15 at slope 2.
assert drop(20) == 5
assert np.isclose(height_at(20, 1), 10) and np.isclose(height_at(20, 3), 10)
assert np.isclose(height_at(20, 2), 15)

# The usual column: A p^2 - x p + (y + A) = 0, real roots iff x^2 >= 4 A (y + A).
x, y = 20, 10
A = F(g*x**2, 2*u**2)
assert A == 5 and sorted(np.roots([5, -20, 15])) == [1, 3]
assert x**2 - 4*A*(15 + A) == 0                                 # 15 m is the edge: one double root
assert np.isclose(float(x/(2*A)), 2)                             # the root that merges: slope 2

# Ground point: 32 m out, slopes 1/2 and 2, headroom 7.2 m.
assert np.isclose(height_at(32, .5), 0) and np.isclose(height_at(32, 2), 0)
assert np.isclose(H - drop(32), 7.2)

# What's special where they merge: the water arrives square to its aim.
for x in (10, 20, 30, 40):
    s = u**2/(g*x)
    v0 = stream(s); t = x/(v0 @ fwd)
    v = v0 - g*t*up
    assert np.isclose(v0 @ v, 0)                                 # launch and arrival are square
    assert np.isclose(v0 @ v, u**2 - g*s*x)                      # in general: 400 less 10 zoom of the aim line's rise
# At 20 m: aimed at slope 2, arriving at slope -1/2.
v0 = stream(2); t = 20/(v0 @ fwd); v = v0 - g*t*up
assert np.isclose((v @ up)/(v @ fwd), -.5)
assert np.isclose(2*20, 40)                                      # the best aim line passes 40 m over the target's spot
# Nudging the aim swings the water square to the aim; at the merge that swing runs along the stream.
def where(slope, t):
    return stream(slope)*t - g*t**2/2*up
a = np.arctan(2); da = 1e-6
swing = (where(np.tan(a + da), t) - where(np.tan(a - da), t))/(2*da)
assert np.isclose(swing @ v0, 0, atol=1e-4)                      # the swing is square to the aim
assert np.isclose(swing[0]*v[1] - swing[1]*v[0], 0, atol=1e-3)   # and it lies along the arrival velocity

# A 3-4-5 check at 30 m: aim 12 forward and 16 up, arrive 12 forward and 9 down.
v0 = stream(4/3); t = 30/(v0 @ fwd); v = v0 - g*t*up
assert np.allclose(v0, [12, 16]) and np.isclose(t, 2.5) and np.allclose(v, [12, -9])
assert np.isclose(height_at(30, 4/3), H - drop(30)) and np.isclose(H - drop(30), 8.75)

# Focus and directrix: on the boundary, distance from the nozzle plus height is 40 m.
for x in (0, 10, 20, 30, 40, 50):
    yb = H - drop(x)
    assert np.isclose(np.hypot(x, yb) + yb, 2*H)

print('boundary: y = 20 m - x^2/(80 m); at 20 m forward, 15 m up, reached only at slope 2, '
      'arriving square to the aim. All checks pass.')
