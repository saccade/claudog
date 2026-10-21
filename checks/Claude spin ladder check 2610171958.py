#!/usr/bin/env python3
"""
Written by Claude (Anthropic), 2026-10-17 19:58, for doc's Straight-> Mechanics work.
Not doc's text. Working notes only; the physics is his responsibility, the words here are the model's.

Checks the "spin ladder" identities in the rotation glossary as full 3-vectors,
for one body of mass m on a rigid lever ι about an axis k, sweeping at ω.

Two candidate definitions of the LOT are tested:
    lot_radial = ι × m          (lever, weighed; points along the lever)
    lot_around = η × ι          (inertia × lever; points around the circle)
    lot_back   = ι × η          (lever × inertia; the other order)
with inertia η = m ⤷ taken as m times the axis direction k.

Each identity is printed as HOLDS or FAILS, with the actual vectors when it fails.
Convention: ⤷ = +k (widdershins seen from +k), right-handed cross products.
"""
import sympy as sp

m, r, w, a = sp.symbols('m r omega alpha', positive=True)
Fx, Fy, Fz = sp.symbols('F_x F_y F_z', real=True)
ix, iy, iz = sp.symbols('iota_x iota_y iota_z', real=True)

def V(*c): return sp.Matrix(c)
def cross(u, v): return u.cross(v)
def dot(u, v): return (u.T * v)[0]
def eq(u, v): return sp.simplify(u - v) == sp.zeros(*u.shape) if hasattr(u, 'shape') else sp.simplify(u - v) == 0

k      = V(0, 0, 1)            # axis direction ⤷
omega  = w * k                 # sweep
alpha  = a * k                 # pickup
iota   = V(r, 0, 0)            # lever, perpendicular to axis (rigid, no wobble)
eta    = m * k                 # inertia = mass around
F      = V(Fx, Fy, Fz)         # some force at the free end

# the three settled crosses
nu  = cross(omega, iota)       # pace = sweep of the lever
p   = m * nu                   # motion = pace of the mass (scalar m)
xi  = cross(iota, p)           # spin = leverage of motion
chi = cross(iota, F)           # torque = leverage of force
Mom = cross(F, iota)           # the rejected order

lot_radial = m * iota
lot_around = cross(eta, iota)
lot_back   = cross(iota, eta)

results = []
def check(name, lhs, rhs):
    ok = eq(lhs, rhs)
    results.append((name, ok, sp.simplify(lhs), sp.simplify(rhs)))

# --- ladder row 1: motion ---
check("motion = sweep of lot_radial   (ω × (ι m))",        cross(omega, lot_radial), p)
check("motion = sweep of lot_around   (ω × (η × ι))",      cross(omega, lot_around), p)
check("motion = sweep of lot_back     (ω × (ι × η))",      cross(omega, lot_back),   p)
check("motion = scalar ω times lot_around",                 w * lot_around,           p)
check("motion = pace of inertia as cross (ν × η)",          cross(nu, eta),           p)
check("motion = pace of inertia as scalar (ν m)",           nu * m,                   p)

# --- ladder row 2: spin ---
beta_A = cross(iota, cross(eta, iota))     # ι × (η × ι)
beta_B = cross(cross(iota, eta), iota)     # (ι × η) × ι
check("bulk A = ι × (η × ι) = m r² ⤷",                      beta_A, m*r**2*k)
check("bulk B = (ι × η) × ι = m r² ⤷",                      beta_B, m*r**2*k)
check("spin = scalar ω times bulk A",                        w * beta_A, xi)
check("spin = sweep × bulk A (cross)",                        cross(omega, beta_A), xi)
check("spin = pace of lot_around as cross (ν × (η×ι))",      cross(nu, lot_around), xi)
check("spin = leverage of (ω × lot_radial)",                  cross(iota, cross(omega, lot_radial)), xi)
check("|spin| = pace · lot_around",                          sp.Matrix([dot(nu, lot_around)]), sp.Matrix([sp.sqrt(dot(xi, xi))]))

# --- torque and power ---
check("torque picks up bulk: χ_free = α β_A (for F = m α×ι)", a * beta_A, cross(iota, m*cross(alpha, iota)))
check("power: sweep · torque = force · pace",                 sp.Matrix([dot(omega, chi)]), sp.Matrix([dot(F, nu)]))
check("F × ι = −(ι × F)  (the order the words caught)",      Mom, -chi)

# --- turn force (centripetal) ---
check("turn force = ω × p = −m ω² ι",                         cross(omega, p), -m*w**2*iota)
check("sweep of lot_around (cross) = −(turn force)/ω ... i.e. radial", cross(omega, lot_around), -m*w*iota)

# --- bulk as the inertia tensor applied to the axis (general lever, not nec. ⊥ axis) ---
iota_g = V(ix, iy, iz)
I_tensor = m * (dot(iota_g, iota_g) * sp.eye(3) - iota_g * iota_g.T)
check("ι × (η × ι) = (inertia tensor)·⤷ for a general lever", cross(iota_g, cross(eta, iota_g)), I_tensor * k)

# --- report ---
lines = ["Claude spin ladder check — results (2026-10-17)", ""]
for name, ok, lhs, rhs in results:
    lines.append(f"{'HOLDS' if ok else 'FAILS'}  {name}")
    if not ok:
        lines.append(f"        lhs = {list(lhs)}")
        lines.append(f"        rhs = {list(rhs)}")
lines += ["",
 "Reading:",
 " * lot_radial (ι m, along the lever) is the only lot whose SWEEP is the motion.",
 " * lot_around (η × ι) is tangential; sweeping it (cross) gives a radial arrow, not motion.",
 "   Scalar-times-vector 'works' but that is not what 'sweep of' means elsewhere (turn force = ω × p).",
 " * 'pace of inertia' holds only as a scalar product; as a cross it is radial.",
 " * bulk = ι × (η × ι) is axial with scale m r² and equals the textbook inertia tensor",
 "   applied to the axis direction; the other grouping (ι × η) × ι is the same vector.",
 " * spin = ω β needs β as a scalar about the axis (or scalar ω × vector β); ω × β crossed is zero.",
 " * ω·χ = F·ν: sweep of the torque is the force of the pace (power, trundle rate).",
]
out = "\n".join(lines)
print(out)
with open("/home/claude/check/Claude spin ladder check results 2610171958.txt", "w") as f:
    f.write(out + "\n")
