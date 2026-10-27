"""A backspun ball bouncing off a rough floor at a slant: checks for the side-by-side. Claude, 2026-10-26; inputs matched 2026-10-27.

Solid ball, radius R = 0.1 m (1 hand), coming in at 10 m/s, 8 forward and 6 down, with backspin
sweeping at 60 strokes a second. Restitution 5/6 on the downward part. The floor grips well enough
that the ball leaves rolling. Everything is per lump: the mass never enters.
"""

import numpy as np
from fractions import Fraction as F

R = 0.1
fwd, up, out = np.eye(3)                       # →, ↑, ↺ (out of the wall)
v0 = 8*fwd - 6*up
w0 = 60*out                                    # backspin on a ball running → is ↺
k = 2/5                                        # solid ball: inertia per mass is k R²

# Both columns get the same inputs (doc's rule 19): 8 forward and 6 down, backspin at 60.
assert np.isclose(np.linalg.norm(v0), 10) and np.isclose(R*60, 6)   # 10 cat in all; rim pace 6 cat

# Slip at the bottom before: center's motion plus the spin's pace there (sweep × lever).
bottom = -R*up
slip0 = v0 + np.cross(w0, bottom)
assert np.isclose(slip0 @ fwd, 14)                # the down part is the bounce's business

# Swirl (spin per mass) about the contact point, which the floor can't change.
def swirl(v, w):
    return np.cross(R*up, v) + k*R**2*w
s0 = swirl(v0, w0)
assert np.allclose(s0, -0.56*out)              # 0.56 m²/s, ↻: 5.6 hand-cat

# After: up part 5/6 of the down part, and rolling (the bottom stops sliding along the floor;
# it still rises at 5 cat). Impact taken as instantaneous: no travel, no gravity during the push.
v1x = s0 @ -out / (R*(1 + k))
v1 = v1x*fwd + 5*up
w1 = -(v1x/R)*out
assert np.isclose(v1x, 4) and np.allclose(swirl(v1, w1), s0)
assert np.allclose(v1 + np.cross(w1, bottom), 0*fwd + 5*up)   # no forward slip at the bottom
assert np.isclose(w1 @ out, -40)               # topspin, ↻, sweeping at 40

# Exact fractions for the arrow way, in hand-cat (1 hand × 1 cat = 0.1 m²/s).
before = F(8) - F(2, 5)*6                       # 8 ↻ and 2.4 ↺
assert before == F(28, 5)
assert before / F(7, 5) == 4

# Grip needed: friction's share of the floor's push.
J = v1 - v0                                    # impulse per mass
assert np.allclose(J, -4*fwd + 11*up) and F(4, 11) < F(37, 100)
# Same instant, same share: friction averaged 4/11 of the floor's push, so the grip must be at least that.

# Both ledgers: energy per lump (thump per lump) before and after; the rest went to heat in the bounce and the skid.
def per_lump(v, w):
    return v @ v / 2 + k*R**2*(w @ w)/2
e0, e1 = per_lump(v0, w0), per_lump(v1, w1)
assert np.isclose(e0, 57.2) and np.isclose(e1, 23.7) and e1 < e0
bounce = (6**2 - 5**2)/2                       # the down part's share, lost in the bounce
assert np.isclose(bounce, 5.5) and np.isclose(e0 - e1 - bounce, 28)   # the rest, lost in the skid
# The one backward pull: each cat off the travel moves the rim's pace 1/k = 5/2 cat.
assert np.isclose((v0 - v1) @ fwd / k, 10)      # 6 forward at the bottom to 4 back
print(f'out: {v1x:g} cat forward, 5 cat up, topspin sweeping at {-w1 @ out:g}; '
      f'{e0:g} thump per lump before, {e1:g} after; grip needs 4/11. All checks pass.')
