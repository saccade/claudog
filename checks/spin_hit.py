"""A sidespun pool ball, skimming just clear of the cloth, hits a still one full on. Claude, 2026-10-26.

Seen from above: → forward along the line of centers, ↑ on the page is the shot's left, ↺ (widdershins
on the ground) points up out of the table. Equal solid balls, radius 3 cm. A comes in at 3 cat → with
sidespin ↺ sweeping at 200. Full bounce along the line of centers (restitution 1); ball-on-ball
friction 1/25, sliding the whole time. Per lump throughout; the hit is instantaneous, and the
table's push during it is only the weight, too small to count.
"""

import numpy as np

R, k, mu = 0.03, 2/5, 1/25
fwd, left, up = np.eye(3)                     # →, ↑ on the page, ↺ out of the table

vA, wA = 3*fwd, 200*up
vB, wB = 0*fwd, 0*up

# Energy per lump (thump per lump) before: most of it is in the spin.
def per_lump(v, w):
    return v @ v/2 + k*R**2*(w @ w)/2
before = per_lump(vA, wA) + per_lump(vB, wB)
assert np.isclose(per_lump(vA, wA), 11.7) and np.isclose(k*R**2*(wA @ wA)/2, 7.2)

# The hit along the line of centers: equal balls, full bounce, A hands over its forward part.
Jn = 3.0                                      # per lump, on B along →
# The skid between the faces: A's face is lever → from its center.
faceA = vA + np.cross(wA, R*fwd)
faceB = vB + np.cross(wB, -R*fwd)
slip = faceA - faceB
assert np.allclose(slip, 3*fwd + 6*left)      # the face slides 6 cat left past B (forward part is the hit's)
Jt = mu*Jn*left                                # friction on B, along A's slide; on A, the opposite

vA1, vB1 = vA - Jn*fwd - Jt, vB + Jn*fwd + Jt
wA1 = wA + np.cross(R*fwd, -Jt)/(k*R**2)
wB1 = wB + np.cross(-R*fwd, Jt)/(k*R**2)
assert np.allclose(vB1, 3*fwd + .12*left) and np.allclose(vA1, -.12*left)
assert np.isclose(wB1 @ up, -10) and np.isclose(wA1 @ up, 190)     # B ↻ at 10; A still ↺ at 190
# Like gears that slip: ↺ hands on ↻. Right english (↺) throws B left.
assert np.isclose(np.degrees(np.arctan(.12/3)), 2.29, atol=.01)

# Each cat of friction moves a ball's rim pace 5/2 cat, so the skid closed by (1 + 5/2) × 2 = 7 per cat.
slip1 = (vA1 + np.cross(wA1, R*fwd)) - (vB1 + np.cross(wB1, -R*fwd))
assert np.isclose(slip1 @ left, 6 - 7*.12) and slip1 @ left > 0        # still skidding: sliding all along

# Both ledgers: total motion kept; spin about B's start point kept; heat is friction over the average skid.
assert np.allclose(vA + vB, vA1 + vB1)
def spin_about(p, v, w, c):                     # per lump, about point c
    return np.cross(p - c, v) + k*R**2*w
pA, pB = -R*fwd, R*fwd
assert np.allclose(spin_about(pA, vA, wA, 0) + spin_about(pB, vB, wB, 0),
                   spin_about(pA, vA1, wA1, 0) + spin_about(pB, vB1, wB1, 0))
after = per_lump(vA1, wA1) + per_lump(vB1, wB1)
heat = .12*(6 + slip1 @ left)/2
assert np.isclose(before - after, heat) and np.isclose(heat, .6696)


# The arrow column's energy, worked as the velocity of added motion (doc's Dog Math, section 6).
m = 1/6
assert np.isclose(3*1.5, 4.5) and np.isclose(m*4.5, .75)                      # 4.5 zip; 0.75 thump of punch
assert np.isclose(k*6*3, 7.2) and np.isclose(m*7.2, 1.2)                      # 7.2 zump; 1.2 thump of hook
assert np.isclose(R*190, 5.7) and np.isclose(m*k*5.7**2/2, 1.083)             # A keeps about 1.08 of hook
assert np.isclose(m*.12*(6 + 5.16)/2, heat*m)                                 # 0.02 oompf at 5.58 cat: 0.11 thump
small = m*(.12**2/2 + .12**2/2 + k*(R*10)**2/2)
assert small < .01 and np.isclose(m*before, .75 + m*k*5.7**2/2 + small + m*heat)
# Afterward the cloth sets B rolling at 5/7 of its travel (its swirl about the cloth point holds).
assert np.isclose(3*5/7, 2.142857, atol=1e-6)
print(f'B: 3 cat →, {vB1 @ left:g} cat left, ↻ sweeping at {-wB1 @ up:g}. '
      f'A: stopped, {-vA1 @ left:g} cat right, ↺ at {wA1 @ up:g}. '
      f'{before:g} → {after:.4g} thump per lump, heat {heat:.4g}. All checks pass.')
