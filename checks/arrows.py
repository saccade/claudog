"""Do the arrows hold up? straight→ mechanics' arrows, checked against ordinary vector algebra.

Claude (Anthropic), 2026-10-22, at doc's request: "post it someplace where you can just push the big red button."
Push it before doubting the arrows. If it ever goes red, show doc and Codex exactly which line.

The arrows are names for unit vectors, nothing more. → is the moving body's forward and ← is its opposite, −→.
↑ is up and ↓ is −↑. ↺, forward around, is the sense ↓ × → gives, and ↻ is −↺. The dot and the cross are the
ordinary ones. This file builds those vectors in plain page coordinates (x right, y up, z out of the page), twice:
once with the body's forward drawn page-right, and once drawn page-left, the mirror. Then it checks
  1. every arrow identity Dog Math section 9 and path 1 use, as a vector equation;
  2. the mobile rules (sizes hang outside, a dot doesn't care about order, a cross does), on random forces;
  3. the path 1 problems that lean on the arrows, solved twice: as vector equations written in the arrows,
     and the way a textbook would, with signed scalars (x right, counterclockwise positive), independently;
  4. that the mirrored drawing gives the same answers in the body's own words;
  5. controls: wrong rules that must come out false, so the button can go red.
Usage: python3 arrows.py      (prints every check; exits 1 if any fails)
"""
import math, sys
import numpy as np

X, Y, Z = np.eye(3)
rows = []
def check(group, claim, ok, got=""):
    rows.append((group, claim, bool(ok), got))
def same(u, v): return np.allclose(np.asarray(u, float), np.asarray(v, float), atol=1e-9)

def arrows(face):
    """face = +1: the body's forward drawn page-right; face = -1: drawn page-left."""
    A = {"→": face * X, "↑": Y}
    A["←"], A["↓"] = -A["→"], -A["↑"]
    A["↺"] = np.cross(A["↓"], A["→"])           # the definition of forward around
    A["↻"] = -A["↺"]
    return A
FACES = {+1: "forward drawn page-right", -1: "forward drawn page-left (mirror)"}
dot, cross = np.dot, np.cross

# 1. Identities -----------------------------------------------------------------------------------
for face, where in FACES.items():
    A = arrows(face); g = f"identities, {where}"
    check(g, "← = −→, ↓ = −↑, ↻ = −↺", same(A["←"], -A["→"]) and same(A["↓"], -A["↑"]) and same(A["↻"], -A["↺"]))
    check(g, "↺ is a unit turning sense, out of the plane", same(np.linalg.norm(A["↺"]), 1) and abs(dot(A["↺"], X)) + abs(dot(A["↺"], Y)) < 1e-12)
    for (a, b, c) in [("↓", "→", "↺"), ("↑", "→", "↻"), ("↓", "←", "↻"), ("↑", "←", "↺"),
                      ("↻", "↓", "←"), ("↺", "↓", "→"), ("↻", "↑", "→"), ("↻", "→", "↓")]:
        check(g, f"{a} × {b} = {c}", same(cross(A[a], A[b]), A[c]))
    for (a, b, val) in [("→", "→", 1), ("←", "→", -1), ("←", "↑", 0), ("↻", "↻", 1), ("↻", "↺", -1)]:
        check(g, f"{a} · {b} = {val}", same(dot(A[a], A[b]), val))
    check(g, "↺ on the page is counterclockwise" if face > 0 else "↺ on the page is clockwise: forward around follows the body, not the page",
          same(A["↺"], face * Z), "↺ = %+d z" % face)

# 2. Mobile rules, on random forces --------------------------------------------------------------
rng = np.random.default_rng(20261022)
for face, where in FACES.items():
    A = arrows(face); g = f"mobile rules, {where}"; ok = {k: True for k in range(7)}
    for _ in range(2000):
        F = np.append(rng.normal(size=2) * 10, 0); r, R, a, b = rng.uniform(0.01, 3, 4)
        ok[0] &= same(dot(A["→"], F) * A["←"], dot(A["←"], F) * A["→"])
        ok[1] &= same(dot(A["→"], F) * R * A["↻"], dot(A["←"], F) * R * A["↺"])
        lhs = np.linalg.norm(F) * r * A["↺"] + dot(A["→"], F) * R * A["↻"]
        ok[2] &= same(lhs, (np.linalg.norm(F) * r + dot(A["←"], F) * R) * A["↺"]) and same(lhs, (np.linalg.norm(F) * r - dot(A["→"], F) * R) * A["↺"])
        ok[3] &= same(dot(A["→"], F) * A["→"] + dot(A["↑"], F) * A["↑"], F)
        ok[4] &= same(dot(a * A["→"], F), dot(F, a * A["→"]))
        ok[5] &= same(cross(a * A["↓"], b * A["→"]), a * b * A["↺"]) and same(cross(b * A["→"], a * A["↓"]), -a * b * A["↺"])
        ok[6] &= same(cross((a - b) * A["↑"], A["→"] * r), (a - b) * r * A["↻"])
    check(g, "→ · F · ← = ← · F · →   (read the mobile from the other end)", ok[0])
    check(g, "(→ · F) R ↻ = (← · F) R ↺   (the minus moves into the dot)", ok[1])
    check(g, "Fr ↺ + (→ · F) R ↻ = (Fr + (← · F) R) ↺ = (Fr − (→ · F) R) ↺   (one vector, three ways to write it)", ok[2])
    check(g, "→ · F · → + ↑ · F · ↑ = F   (the parts put back)", ok[3])
    check(g, "a dot doesn't care about order: the sizes step out of the way", ok[4])
    check(g, "a cross keeps its arrows in order: the sizes move, the arrows don't", ok[5])
    check(g, "(H − R) ↑ × → J = (H − R) J ↻", ok[6])

def body(A, v):
    """A vector in the body's own words: its parts along →, ↑, ↺."""
    return np.array([dot(A["→"], v), dot(A["↑"], v), dot(A["↺"], v)])

# 3. The path 1 problems ---------------------------------------------------------------------------
m, R, r, I, F = 2.0, 0.20, 0.12, 0.040, 6.0
answers = {}
for face, where in FACES.items():
    A = arrows(face); g = f"3-c spool, rolling, {where}"
    # unknown sizes along the arrows the solution declares: a →, grip f →, pickup α ↻
    #   m a → = F → + f →;   I α ↻ = r↓ × F→ + R↓ × f→;   rolling: a → + α↻ × R↓ = 0 (the bottom doesn't slide)
    M = np.column_stack([np.concatenate([m * A["→"], I * A["↻"] * 0, A["→"]]),
                         np.concatenate([-A["→"], -cross(R * A["↓"], A["→"]), 0 * A["→"]]),
                         np.concatenate([0 * A["→"], I * A["↻"], cross(A["↻"], R * A["↓"])])])
    rhs = np.concatenate([F * A["→"], cross(r * A["↓"], F * A["→"]), 0 * A["→"]])
    (a, f, al), *_ = np.linalg.lstsq(M, rhs, rcond=None)
    tc, tg = cross(r * A["↓"], F * A["→"]), cross(R * A["↓"], f * A["→"])
    check(g, "the center speeds up at 0.80 m/s² →: it rolls toward the pull", same(a, 0.8), f"a = {a:.4f}")
    check(g, "the grip is 4.4 N ←", same(f * A["→"], 4.4 * A["←"]), f"f = {f:+.4f} along →")
    check(g, "it picks up at 4.0 ↻: it really does turn back around", same(al, 4.0), f"α = {al:+.4f} along ↻")
    check(g, "cord 0.72 N m ↺, grip 0.88 N m ↻, net 0.16 N m ↻ = I α ↻",
          same(tc, 0.72 * A["↺"]) and same(tg, 0.88 * A["↻"]) and same(tc + tg, I * al * A["↻"]))
    check(g, "(m + I/R²) a = F (1 − r/R)", same((m + I / R**2) * a, F * (1 - r / R)))
    answers.setdefault("spool rolling", []).append(np.concatenate([body(A, a * A["→"]), body(A, f * A["→"]), body(A, al * A["↻"])]))
# textbook, independently: x right, counterclockwise positive; torque of (Fx, Fy) at (x, y) is x Fy − y Fx
#   2a = 6 + f;  0.04 α = (−(−0.12)(6)) + (−(−0.20) f);  contact at (0, −R): a + αR = 0
Mt = np.array([[m, -1, 0], [0, -R, I], [1, 0, R]]); a_t, f_t, al_t = np.linalg.solve(Mt, [F, r * F, 0])
check("3-c spool, textbook signs", "a = +0.8, f = −4.4, α = −4.0 (clockwise, with forward drawn right)",
      same([a_t, f_t, al_t], [0.8, -4.4, -4.0]), f"a = {a_t:+.3f}, f = {f_t:+.3f}, α = {al_t:+.3f}")
check("3-c spool, textbook signs", "matches the arrows: the minus signs are the arrows' ← and ↻", same([a_t, f_t, al_t], answers["spool rolling"][0][[0, 3, 8]]))   # slot 8 is the pickup's ↺ part: −4 is 4 ↻

def spool_at_rest(A, th):
    u = math.cos(th) * A["→"] + math.sin(th) * A["↑"]                  # the cord, pulled partly upward
    p = r * (math.sin(th) * A["→"] + math.cos(th) * A["↓"])             # where it leaves the hub: a tangent
    grip = (dot(A["←"], F * u)) * A["→"]                                # nothing speeds up: the backward part, pointing forward
    return u, p, grip, cross(p, F * u) + cross(R * A["↓"], grip)       # the normal force at R↓ is ↑: no turning
for face, where in FACES.items():
    A = arrows(face); g = f"3-d spool at rest, {where}"
    ok_t = all(abs(dot(spool_at_rest(A, t)[1], spool_at_rest(A, t)[0])) < 1e-12 and same(cross(spool_at_rest(A, t)[1], F * spool_at_rest(A, t)[0]), F * r * A["↺"])
               for t in np.linspace(0, 1.4, 15))
    check(g, "at any angle the cord leaves at a tangent and still turns the spool Fr ↺", ok_t)
    lo, hi = 0.1, 1.5                                                    # find the angle where the turnings cancel
    for _ in range(80):
        mid = (lo + hi) / 2
        if dot(spool_at_rest(A, mid)[3], A["↺"]) > 0: hi = mid      # F (r − R cos θ) ↺ grows with θ
        else: lo = mid
    th = (lo + hi) / 2; u, p, grip, net = spool_at_rest(A, th)
    check(g, "the turnings cancel where → · F is r/R = 3/5 of the pull: 53°", same(math.cos(th), r / R), f"θ = {math.degrees(th):.3f}°")
    check(g, "there Fr ↺ + (← · F) R ↺ = 0", same(F * r * A["↺"] + dot(A["←"], F * u) * R * A["↺"], 0 * X))
    check(g, "the grip is → · F · ← = ← · F · →, 3.6 N ←", same(grip, dot(A["→"], F * u) * A["←"]) and same(grip, 3.6 * A["←"]))
    answers.setdefault("spool at rest", []).append(np.array([th]))
check("3-d spool, textbook signs", "F r = F cos θ R gives cos θ = r/R = 0.6", same(math.degrees(math.acos(r / R)), math.degrees(answers["spool at rest"][0][0])))

for face, where in FACES.items():
    A = arrows(face); g = f"4-a ladder, {where}"
    L = 1.8 * A["←"] + 2.4 * A["↑"]; foot = 0.40 * A["→"]
    v = -dot(L, -foot) / dot(L, A["↑"])                                   # L · (v↑ − foot) = 0
    rel = v * A["↑"] - foot
    check(g, "the top moves 0.30 m/s ↓", same(v * A["↑"], 0.30 * A["↓"]), f"v = {v:+.4f} along ↑")
    check(g, "seen from the foot it's 0.50 m/s, square to the ladder", same(np.linalg.norm(rel), 0.5) and abs(dot(rel, L)) < 1e-12)
    answers.setdefault("ladder", []).append(body(A, v * A["↑"]))
check("4-a ladder, textbook signs", "x² + y² = L² gives ẏ = −x ẋ / y = −0.30", same(-1.8 * 0.40 / 2.4, -0.30))

mb, Rb, J = 1.0, 0.050, 2.0
for face, where in FACES.items():
    A = arrows(face); g = f"5 cue ball, {where}"
    v = J / mb
    # (H − R)↑ × J→ = (2/5) m R² ω, with the bottom not sliding: v→ + ω × R↓ = 0
    w_roll = np.linalg.lstsq(np.column_stack([cross(A["↺"], Rb * A["↓"])]), -v * A["→"], rcond=None)[0][0] * A["↺"]
    Lroll = 0.4 * mb * Rb**2 * w_roll
    H = Rb + dot(Lroll, A["↻"]) / J                                     # (H − R) J ↻ = L
    check(g, "it sweeps at 40 ↻ when it rolls at once", same(w_roll, 40 * A["↻"]))
    check(g, "H = 7R/5 = 0.070 m", same(H, 0.07), f"H = {H:.4f} m")
    check(g, "½ v→ · →J = 2.0 J and ½ ω↻ · ↻L = 0.80 J", same(0.5 * dot(v * A["→"], J * A["→"]), 2.0) and same(0.5 * dot(w_roll, Lroll), 0.8))
    answers.setdefault("cue", []).append(np.array([H]))
check("5 cue ball, textbook signs", "−(H − R) J = (2/5) m R² ω with ω = −v/R gives H = 0.070 m", same(Rb + 0.4 * mb * Rb**2 * (v / Rb) / J, 0.07))

for face, where in FACES.items():
    A = arrows(face); g = f"7 hoop, {where}"
    w = 8.0 * A["↻"]; c = 0.25 * 8.0 * A["→"]
    pt = lambda lev: c + cross(w, lev)
    check(g, "top 4.0 m/s →, bottom 0, front 2.0 m/s → + 2.0 m/s ↓",
          same(pt(0.25 * A["↑"]), 4 * A["→"]) and same(pt(0.25 * A["↓"]), 0 * X) and same(pt(0.25 * A["→"]), 2 * A["→"] + 2 * A["↓"]))
    answers.setdefault("hoop", []).append(np.concatenate([body(A, pt(0.25 * A["↑"])), body(A, pt(0.25 * A["→"]))]))

# 4. The mirror ------------------------------------------------------------------------------------
for k, (right, left) in answers.items():
    check("the mirror", f"{k}: the page-left drawing gives the same answer in the body's words", same(right, left))

# 5. Controls: wrong rules that must come out false -----------------------------------------------
A = arrows(+1); B = arrows(-1)
for claim, val in [("↓ × → = ↻", same(cross(A["↓"], A["→"]), A["↻"])),
                   ("→ · F · ← = → · F · →", same(dot(A["→"], 3 * X + Y) * A["←"], dot(A["→"], 3 * X + Y) * A["→"])),
                   ("a cross doesn't care about order", same(cross(A["↓"], A["→"]), cross(A["→"], A["↓"]))),
                   ("↺ is the page's counterclockwise whichever way forward is drawn", same(B["↺"], Z)),
                   ("the spool at rest at 45°", abs(dot(spool_at_rest(A, math.pi / 4)[3], A["↺"])) < 1e-9)]:
    check("controls (each must be false)", f"wrong: {claim}", not val, "false, as it should be" if not val else "TRUE: the checker is broken")

if __name__ == "__main__":
    group = None
    for g, claim, ok, got in rows:
        if g != group: print(f"\n{g}"); group = g
        print(f"  {'✓' if ok else '✗'} {claim}" + (f"   [{got}]" if got else ""))
    bad = sum(not ok for *_, ok, _ in rows)
    print(f"\n{len(rows) - bad} of {len(rows)} hold." + ("" if not bad else f"  {bad} FAIL: show doc and Codex exactly these lines."))
    sys.exit(1 if bad else 0)
