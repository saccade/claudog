"""Claude's independent recomputation of codogx's three harness cases, for the 2026-10-22 review.

Claude (Anthropic), 2026-10-22. Written from the case files' stated inputs and assumptions only,
without importing or copying Codex's implementations. Closed forms where they exist; for the
two-store sweater, eigen-decomposition and a hand-written RK4. Usage: python3 codogx_review.py CASES_DIR
"""
import json, math, sys
import numpy as np
D = sys.argv[1]
case = lambda n: json.load(open(f"{D}/{n}.json"))
def report(c, got):
    bad = []
    for k, r in c["observables"].items():
        if k not in got: bad.append(f"{k}: not computed"); continue
        if not math.isclose(got[k], r["expected"], rel_tol=max(r["rtol"], 1e-6), abs_tol=max(r["atol"], 1e-6)):
            bad.append(f"{k}: mine {got[k]:.9g}, case {r['expected']:.9g}")
    print(c["case_id"], "agree" if not bad else "DIFFER", *bad, sep="\n  ")

# valves: momentum from net force over the onset; energy split; governor roll/hook; diaphragm; loop poles
c = case("valves"); p = c["inputs"]; g = {}
cap = p["cap"]; F = cap["gauge"] * cap["area"]; net = F - cap["weight"]; dt = cap["duration"]
g["cap_movement"] = net * dt
x = net * dt**2 / (2 * cap["mass"])                    # rise under constant net force from rest
g["cap_punch"] = (net * dt)**2 / (2 * cap["mass"]); g["cap_heft"] = cap["weight"] * x; g["cap_pressure_work"] = F * x
gv = p["governor"]; I0 = 2 * gv["mass_each"] * gv["r0"]**2; I1 = 2 * gv["mass_each"] * gv["r1"]**2; w = gv["omega"]
g["governor_roll0"], g["governor_roll1"] = I0 * w, I1 * w
g["governor_hook0"], g["governor_hook1"] = I0 * w * w / 2, I1 * w * w / 2
g["governor_engine_work"] = w * (I1 - I0) * w           # torque through angle = sweep times added roll
g["governor_link_work"] = g["governor_engine_work"] - (g["governor_hook1"] - g["governor_hook0"])
dp = p["diaphragm"]
g["diaphragm_gauge0"] = dp["absolute0"] - dp["ambient"]
g["diaphragm_gauge1"] = dp["absolute0"] * dp["mass1"] / dp["mass0"] - dp["ambient"]   # isothermal, fixed volume
fa, fb = dp["spring_force"], dp["spring_force"] - dp["stiffness"] * dp["travel"]
g["diaphragm_spring_work"] = (fa + fb) / 2 * dp["travel"]
for K in p["loop_gains"]:                               # s (s + 1)^2 + K = 0
    g[f"loop_gain{int(K)}_max_real"] = max(r.real for r in np.roots([1, 2, 1, K]))
report(c, g)
print("  spring force at end of travel equals the new gauge on the area:", math.isclose(fb, g["diaphragm_gauge1"] * dp["area"]))

# sweater, equal lags: two cascaded first-order lags (cold), one remaining lag (hot)
c = case("sweater_equal"); p = c["inputs"]; g = {}
for t in p["times_s"]:
    n = t / p["lag_s"]
    g[f"cold_{t}_fraction"] = 1 - (1 + n) * math.exp(-n); g[f"hot_{t}_fraction"] = 1 - math.exp(-n)
g["balance_residual"] = 0.0
report(c, g)

# sweater, two stores: skin and bulk; dryer air on the skin; carry with the room on the skin
c = case("sweater_two_store"); p = c["inputs"]; g = {}
cs, cb, gh, gi, gr = (p[k] for k in ("skin_capacity", "bulk_capacity", "hot_conductance", "inner_conductance", "room_conductance"))
A = np.array([[-(gh + gi) / cs, gi / cs], [gi / cb, -gi / cb]]); Bv = np.array([gh / cs, 0.0])
Cm = np.array([[-(gr + gi) / cs, gi / cs], [gi / cb, -gi / cb]])
def ex(M, t):
    lam, V = np.linalg.eig(M); return (V @ np.diag(np.exp(lam * t)) @ np.linalg.inv(V)).real
def hot(t):  # from room temperature, dryer air already at the plateau
    return np.linalg.solve(A, (ex(A, t) - np.eye(2)) @ Bv * p["plateau_K"])
def cold(t, h=0.01):  # dryer air ramps to the plateau; RK4
    f = lambda s, x: A @ x + Bv * min(s * p["ramp_K_per_s"], p["plateau_K"])
    x, s = np.zeros(2), 0.0
    while s < t - 1e-12:
        k = min(h, t - s); a = f(s, x); b = f(s + k/2, x + k/2*a); cc = f(s + k/2, x + k/2*b); d = f(s + k, x + k*cc)
        x = x + k / 6 * (a + 2*b + 2*cc + d); s += k
    return x
hold = np.array([cs, cb]); carry = ex(Cm, p["carry_s"])
x = hot(10); y = carry @ x
g.update(skin_door=x[0], bulk_door=x[1], skin_neck=y[0], bulk_neck=y[1], heat_lost=hold @ (x - y), net_heat_inward=cb * (y[1] - x[1]))
for t in p["cold_times_s"]: g[f"cold_{t}_retained_K"] = hold @ (carry @ cold(t)) / hold.sum()
for t in p["hot_times_s"]: g[f"hot_{t}_retained_K"] = hold @ (carry @ hot(t)) / hold.sum()
internal = np.array([[-gi / cs, gi / cs], [gi / cb, -gi / cb]])
g["redistribution_residual_J"] = abs(hold @ (ex(internal, 15) @ x - x))
report(c, g)
