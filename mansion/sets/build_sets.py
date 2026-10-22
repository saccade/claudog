"""Builds the four end-to-end Mansion solution sets, one per level, as simple HTML.

Claude (Anthropic), 2026-10-21. Sources (flattened copies in this folder): Codex's four release
reading copies r1..r4 (main route, ending, and the appendix tabs open at that release) and
CL-214's standard statements. Set k = the mansion route of release k with every mansion solution
re-said in level-k words (levels.py), the problem statements put back in, and the optional
problems open at level k interleaved in the problem set's order:
  1 knife, drawer 4, F1 | 2, 3, drawer 1 | 4, drawer 2, F4 | 5 | 6 | 7, drawer 3 | 8 |
  9, 10, drawer 5, F2 | 11, drawer 6 | 12, drawer 7, F3 | 13, U1, U2 | ending k.
Usage: python3 build_sets.py   (writes set1.html .. set4.html and set*.txt beside it)
"""
import html, re
from levels import LEVEL

STAMP = "2610212230"
DATE = {1: "2026-10-22", 2: "2026-10-21", 3: "2026-10-21", 4: "2026-10-21"}   # set 1 fixed 2026-10-22 08:16; 2-4 marked outdated
WORDS = {
 1: "the turn and τ, π for the flip, the cycle (it cycles), the sweep and the stroke, χ for torque, sentences the right way round (current is the conductance of the voltage; power is the voltage of the current, and the sweep of the torque), own time",
 2: "level 1's, plus heft, punch and hook; profile; pickup, and crank as a verb; spin; can and coil",
 3: "level 2's, plus zip and zing; the still point; flips and mirror pairs; tone, chord, beat and the shape Ω_shape; the trade (a belt, not a battery); the stripe and phase, for ghosts; shift and stretch",
 4: "level 3's, plus the one machine; zam and zlam; in step, at random, the tap; TEST and RUN; and doc's zow and zlow, with their verbs zower and zlower",
}
NAMES = {1: "the base game", 2: "with the cabinet", 3: "with the cabinet and the funhouse", 4: "the whole house"}

def read(path):
    lines = open(path, encoding="utf-8").read().split("\n")
    tabs, cur = {}, None
    for ln in lines[1:]:
        if ln.startswith("######## TAB"):
            cur = ln.split(" ", 3)[3]; tabs[cur] = []; continue
        if cur is not None and ln.strip():
            tabs[cur].append(ln)
    return tabs

def blocks(lines):
    """Split into [(heading, [lines])], heading None for anything before the first heading."""
    out, head, body = [], None, []
    for ln in lines:
        if ln.startswith("## "):
            out.append((head, body)); head, body = ln[3:], []
        else:
            body.append(ln)
    out.append((head, body))
    return out

def statements():
    tabs = read("cl214_now.txt"); bl = blocks(next(iter(tabs.values())))
    st = {}
    for h, body in bl:
        m = re.match(r"(\d+)\. ", h or "")
        if not m: continue
        n = int(m.group(1)); parts = []
        for ln in body:
            if ln.startswith("candle") or ln.startswith("the clown"): continue
            parts.append(ln)
        st[n] = parts
    return st

def apply_edits(text, k):
    for lev in range(1, k + 1):
        for old, new in LEVEL[lev]:
            c = text.count(old)
            assert c == 1, (lev, c, old[:80])
            text = text.replace(old, new)
    return text

NAV = [(re.compile(r" \(Appendix 1, drawer \d\.\)"), ""),
       (re.compile(r"Passage: from Appendix 1, drawers? [\d and]+, and back (the same way|either way)\. "), ""),
       (re.compile(r"Passage: the back of this drawer opens on Appendix b, F\d\. The passage is open\."), "The back of this drawer opens into the funhouse."),
       (re.compile(r"Passage: the back of this drawer opens on Appendix b, F\d\. Painted shut until patch 2\."), "Behind this drawer there's a draft; the panel at its back is painted shut."),
       (re.compile(r" \(Appendix γ\. The trapdoor is open\.\)"), " The trapdoor is open."),
       (re.compile(r" \(Appendix γ\. Nailed down until patch 3\.\)"), " It's nailed down."),
       (re.compile(r"Service entrance: any of the three trapdoors\. They all come down here, and any of them takes you back up\."), "Any of the three trapdoors comes down here."),
       (re.compile(r"Take the coupled machine of funhouse problem 2"), "Take the coupled machine of F2")]
SKIP = re.compile(r"^(Return to |Return the |Optional problems and worked route|each drawer opens)")
# words a set reaches before its level brings them in (set 2 only)
SET2_FIX = [("and a moment later a different point is: the still point keeps changing.", "and a moment later a different point is."),
            ("It carries nothing: that's the hall's stripe.", "It carries nothing.")]
TIMES = [("and the center speeds up at R times that:", "and the center speeds up at R of that:"),
         ("In a mode both rods pick up at −ω² times their angle.", "In a mode both rods pick up at ω² of their angle, back toward vertical."),
         ("In a mode both rods pick up at −ω² times their angle, and the lower rod leans Ω_shape times as far as the upper.", "In a mode both rods pick up at ω² of their angle, back toward vertical, and the lower rod leans Ω_shape of the upper's lean."),
         ("One tone is ω₀ times a factor and the other is ω₀ over it: a mirror pair.", "One tone is ω₀ at a factor and the other is ω₀ on it: a mirror pair.")]

SPOOL_I = [("(3) Write the statement’s moment of inertia as η. With the mass taken out, inertia is the profile: η on", "(3) With the mass taken out, inertia is the profile: I on"),
           ("(3) Write the statement’s moment of inertia as η. ", "(3) "),
           ("ηα = −Fr − fR", "Iα = −Fr − fR"), ("(m + η/R²)a", "(m + I/R²)a"), ("Here η/R²", "Here I/R²")]

# doc's set-1 edits of 2026-10-22 08:06, as discussed: arrows start at the governor, the spool's
# signs become senses (→ ← straight, ↻ ↺ turning), the grip is taken positive → and comes out ←,
# the hoop's eighth of a turn, the powdered clown. Each entry lists the level variants of one spot.
DOC_0806 = [
 [("(2) The cosine can't go over 1, so g/(ℓω²) has to stay under 1. Below a sweep of √(g/ℓ) = √20, about 4.5 stroke a second, hanging straight down is the only answer.",
   "(2) The ball hangs g/ω² below the hinge: 10/25 = 0.40 m here. A drop can't be longer than the arm. Below a sweep of √(g/ℓ) = √20, about 4.5 strokes a second, g/ω² would be longer than the 0.50 m arm, so hanging straight down is all that's left.")],
 [("Take forward, the way the cord pulls, as positive, and let f be the counter's grip on the spool, positive forward too. The center of mass speeds up as if both forces acted there: ma = F + f. For the turning, take the way the spool turns when it rolls forward as positive. The cord pulls forward 0.12 m below the axle and the grip acts 0.20 m below it, and a forward push below the axle turns the spool backward.",
   "The cord pulls forward (→). Take the counter's grip on the spool, f, as positive → too; the answer will say which way it really goes. The center of mass speeds up as if both forces acted on it directly: ma = F + f. For turning, call the way the spool turns when it rolls → positive: ↻. The cord pulls → 0.12 m below the axle and the grip acts 0.20 m below it, and a → push below the axle turns the spool ↺.")],
 [("So the torques about the axle are −Fr and −fR, and Iα = −Fr − fR.", "So the torques about the axle are Fr ↺ and fR ↺, and Iα ↻ = [Fr + fR] ↺."),
  ("So the cord cranks the spool backward about the axle with −Fr, the grip cranks it with −fR, and Iα = −Fr − fR.", "So the cord cranks the spool ↺ about the axle with Fr, the grip cranks it ↺ with fR, and Iα ↻ = [Fr + fR] ↺.")],
 [("The center speeds up at 0.80 m/s², forward: the spool rolls toward the pull", "The center speeds up at 0.80 m/s² →: the spool rolls toward the pull")],
 [("The grip is f = 1.6 − 6.0 = −4.4 N. It pulls back, and about the axle it turns the spool forward harder than the cord turns it back.",
   "The grip is f = 1.6 − 6.0 = −4.4 N: 4.4 N ←. It pulls back, and about the axle it turns the spool ↻ harder than the cord turns it ↺."),
  ("The grip is f = 1.6 − 6.0 = −4.4 N. It pulls back, and about the axle it cranks the spool forward harder than the cord cranks it back.",
   "The grip is f = 1.6 − 6.0 = −4.4 N: 4.4 N ←. It pulls back, and about the axle it cranks the spool ↻ harder than the cord cranks it ↺.")],
 [("Forward 2.0 m/s and down 2.0 m/s make 2√2, about 2.8 m/s, 45° below forward.", "2.0 m/s → and 2.0 m/s ↓ make 2√2, about 2.8 m/s, 45° (τ/8) below →.")],
 [("a whiteface in damask", "a powdered clown in damask")],
 # doc 08:40-08:41: a hair space keeps ℓ and θ apart; the definite description, not the pronoun (only one thing has weight)
 [("lifts a point at distance ℓ by ℓ(1 − cos θ). For this small lean, that’s ℓθ²/2", "lifts a point ℓ away by ℓ(1 − cos θ). For this small lean, that’s ℓ\u200aθ²/2")],
 [("Its 10 N weight lifted through 5 mm", "The 10 N weight lifted through 5 mm")],
 [("the whiteface has gloves", "the powdered clown has gloves")],
]
# The 2π is lugged around and noticed: the knife's rule and numbers (2nd and 3rd sightings, the 2 noticed),
# the flywheel's sweeps in turns (4th, 5th, noticed again), a torque through a whole turn (6th), and there
# the turn takes τ and torque takes χ, with doc's sentences.
SLOW_WALK = [
 ("The usual small-swing rule gives T = 2π√(ℓ/g). A whole turn has arrived wearing two flips. Give the full turn its own sign, τ.\nCall a radian a stroke. A whole turn is τ, about 6.3 strokes. Half a turn is π, the flip. A turn of the knife’s cycle brings it back to the same end; a flip of the cycle takes it to the opposite end.\nCount strokes each second and call that the sweep. The cycle’s sweep is ω. The small-swing rule balances as\n    ℓω² = g,\n     Tω = τ.\nHere the cycle sweeps at √10, about 3.2 strokes a second. Its turn takes T = τ/√10 = 1.99 s, about two seconds.",
  "Call a radian a stroke. All the way round is a turn, about 6.3 strokes, and half of that is π, the flip. A flip of the knife’s cycle takes it to the opposite end; a turn brings it back.\nCount strokes each second and call that the sweep. The cycle’s sweep is ω. The usual small-swing rule balances as\n    ℓω² = g,\n    Tω = 2π.\nHere the cycle sweeps at √10, about 3.2 strokes a second. Its cycle takes T = 2π/√10 = 1.99 s, about two seconds. There's a 2 riding along with that π."),
 ("The height, bottom speed and time for a turn stay the same.", "The height, bottom speed and time for a cycle stay the same."),
 ("At 4.0 strokes a second, half of 0.50 kg m² at 16 is 4.0 J. Four seconds at a net 3.0 W add 12 J, for 16 J, and 16 J on the same wheel needs the squared sweep to be 64. The wheel ends up sweeping at 8.0 strokes a second.",
  "At 4.0 strokes a second, half of 0.50 kg m² at 16 is 4.0 J. Counted in turns, 4.0 strokes a second is 4.0/2π, about 0.64 of a turn a second. Four seconds at a net 3.0 W add 12 J, for 16 J, and 16 J on the same wheel needs the squared sweep to be 64. The wheel ends up sweeping at 8.0 strokes a second: 8.0/2π, about 1.3 turns a second. The 2 again: every sweep we count in turns gets divided by it."),
 ("(3) Torque usually gets the letter τ, but the turn has it now. An χ hung on the wall could apply a twist to something—use that for torque. The power a torque delivers is the sweep of the torque: P = ωχ. Put numbers to it once: 0.75 N m at 4.0 strokes a second delivers 3.0 W. So at the start the engine's 3.0 W takes χ = 0.75 N m, and at the end, at 8.0, it takes 0.38 N m.\nWhen the wheel goes twice as fast, applying the same power takes just half the torque.",
  "(3) The power a torque delivers is the sweep of the torque. Put numbers to it once: 0.75 N m at 4.0 strokes a second delivers 3.0 W. So at the start the engine's 3.0 W takes 0.75 N m, and at the end, at 8.0, it takes 0.38 N m.\nWhen the wheel goes twice as fast, applying the same power takes just half the torque.\nThrough one whole turn, 0.75 N m does 2π of itself: 4.7 J, and 0.64 of a turn a second at 4.7 J a turn is the engine's 3.0 W. There's the 2π again, two flips standing in for one turn. π only covers half of what the knife does, one swing across; the cycle is the whole of it. Give the whole turn its own sign, τ. The knife's rule is then Tω = τ, and the wheel's 4.0 strokes a second is 4.0/τ of a turn a second.\nTorque usually gets the letter τ, but the turn has it now. An χ hung on the wall could apply a twist to something—use that for torque: P = ωχ, with χ = 0.75 N m at the start."),
]

STATEMENT_FIX = [("A spool of mass 2.0 kg, outer radius R = 0.20 m and hub radius r = 0.12 m has moment of inertia 0.040 kg m²† about its axle. It rests on a level counter.",
                  "A spool rests on a level counter. It has mass 2.0 kg, outer radius R = 0.20 m, hub radius r = 0.12 m, and moment of inertia 0.040 kg m²† about its axle.")]
# turn-family units are count nouns and take a plural (doc, 08:06); dog park units stay bare (R-041)
STROKES = re.compile(r"(?<=[0-9√τ]) stroke\b")
LEGEND = "A value marked † is supplied: chosen so the house works, with the reason somewhere below the mansion."

def clean(ln, k):
    for rx, rep in NAV: ln = rx.sub(rep, ln)
    for old, new in TIMES: ln = ln.replace(old, new)
    if k == 2:
        for old, new in SET2_FIX: ln = ln.replace(old, new)
    return ln

def number_parts(lines):
    """Statement lines: first is setup; later bare lines become numbered parts unless they already are."""
    out, n = [], 0
    for i, ln in enumerate(lines):
        if i == 0 or ln.startswith("Use g"):
            out.append(("p", ln)); continue
        m = re.match(r"(\d+)\.\s+(.*)", ln)
        n = int(m.group(1)) if m else n + 1
        out.append(("p", f"{n}. {m.group(2) if m else ln}"))
    return out

def appendix_items(tabs, k):
    """Drawer/funhouse/understage problems as {key: [(kind, text)]}, plus scenery lines per appendix."""
    items, scenery = {}, {}
    for title, lines in tabs.items():
        if not title.startswith("Appendix"): continue
        bl = blocks(lines); app = title.split(" ")[1]
        pre = []
        for h, body in bl:
            if h is None: continue
            if h.startswith("Appendix"):
                pre = [ln for ln in body if not SKIP.match(ln)]; scenery[app] = pre; continue
            if h == "Solution":
                items[key] += [("b", "Solution")] + [("p", clean(ln, k)) for ln in body if not SKIP.match(ln)]
                continue
            if h == "The four voices": continue
            key = h.split(":")[0]
            if k == 2: h = h.replace("the second knife's two tones", "the second knife's two motions")
            body = [clean(ln, k) for ln in body if not SKIP.match(ln)]
            intro = [ln for ln in body if ln.startswith(("Door", "Doors", "Passage", "A long", "Two facing", "A hall", "A tilted", "Any of", "On the chassis"))]
            rest = [ln for ln in body if ln not in intro]
            items[key] = [("h3", h)] + [("i", ln) for ln in intro] + number_parts(rest)
    return items, scenery

def build(k):
    tabs = read(f"r{k}_now.txt")
    main = tabs["The mansion"]
    i0 = main.index("## The way in"); iE = next(i for i, l in enumerate(main) if l.startswith("## Ending"))
    route = "\n".join(main[i0:iE])
    # doc's own corrections in release 4 (21:4x) are what LEVEL[1] applies everywhere; undo them here so one edit list fits all four
    route = route.replace("needs the squared sweep to be 64.", "needs the square of the sweep to be 64.")
    route = route.replace("is the the sweep of the torque [ see how this means something and the other one is not English? ]  torque times the sweep:", "is the torque times the sweep:")
    route = apply_edits(route, k)
    # doc 2026-10-22: a letter moves when it's needed. Nothing needs I for anything else at the spool,
    # so it keeps the statement's I; inertia moves to η only where current has taken I (F2, U1).
    route = route.replace("a page somebody has already used", "a page someone has already used")   # doc, set 1, 07:31
    for old, new in SPOOL_I:
        if old in route: route = route.replace(old, new)
    assert "η" not in route, "η left in the mansion route"
    for alts in DOC_0806:   # each entry: one or more (old, new) variants; at least one must apply
        hit = False
        for old, new in alts:
            if old in route: route = route.replace(old, new); hit = True
        assert hit, alts[0][0][:70]
    if k == 1:
        route = STROKES.sub(" strokes", route)
    if k == 1:   # doc 2026-10-22 08:29: the slow walk to τ, in set 1 first; sets 2-4 get it at the sweep
        for old, new in SLOW_WALK:
            assert route.count(old) == 1, old[:70]
            route = route.replace(old, new)
    ending = main[iE:]
    items, scen = appendix_items(tabs, k)
    st = statements()
    out = [("h1", f"The Mansion, solution set {k} of 4: {NAMES[k]}")]
    out.append(("p", f"<b>Written by Claude (Anthropic), {DATE[k]}, for dr. kraemer.</b> Set {k} of four: the whole problem set done through, end to end, the way a reader at level {k} would do it, with every optional problem open at that level placed right after the room it belongs to. Assembled from Codex's (OpenAI) release copies and the checked drafts; the thirteen mansion solutions are re-said in this level's words. The ideas and vocabulary are dr. kraemer's; the words are the models'. Statements stay in standard language."))
    out.append(("i", f"Words this set uses: {WORDS[k]}."))
    out.append(("i", LEGEND))
    after = {"1. The knife": ["Drawer 4", "F1"], "3. The governor and the spool": ["Drawer 1"],
             "4. The ladder": ["Drawer 2", "F4"], "7. The hoop": ["Drawer 3"],
             "10. The coils and the capacitor": ["Drawer 5", "F2"], "11. The line": ["Drawer 6"],
             "12. The two lights": ["Drawer 7", "F3"], "13. The chair": ["U1", "U2"]}
    shown = set()
    for h, body in blocks(route.split("\n")):
        if h is None: continue
        m = re.match(r"(\d+)\. ", h)
        hold = []
        if h.startswith("12."):
            hold = [ln for ln in body if ln.startswith("In the chair’s frame")]
            body = [ln for ln in body if ln not in hold]
        body = [clean(ln, k) for ln in body]
        if m:
            n = int(m.group(1))
            out.append(("h3", h))
            sl = [x for x in st[n]]
            for old, new in STATEMENT_FIX: sl = [x.replace(old, new) for x in sl]
            sl = [x.replace("problem 12(c)", "problem 12, part 3").replace("problem 10(d)", "problem 10, part 4") for x in sl]
            if n == 10: sl = ["Four parts."] + sl
            out += [(t, s) for t, s in number_parts(sl)][1 if n == 10 else 0:]
            out.append(("b", "Solution"))
            out += [("eq" if ln.startswith("    ") or ln.startswith("(m + η") or ln.startswith("a = F(1") else "p", ln.strip()) for ln in body]
            for key in after.get(h, []):
                if key in items:
                    if key.startswith("F") and "b" not in shown and "b" in scen:
                        out.append(("h2", "Into the funhouse")); out += [("i", s) for s in scen["b"]]; shown.add("b")
                    if key.startswith("Drawer") and "1" not in shown and "1" in scen:
                        out.append(("h2", "Into the cabinet")); out += [("i", s) for s in scen["1"]]; shown.add("1")
                    if key.startswith("U") and "γ" not in shown and "γ" in scen:
                        out.append(("h2", "Under the stage")); out += [("i", s) for s in scen["γ"]]; shown.add("γ")
                    out += items[key]
            if hold:
                out += [("i", s) for s in hold]
        else:
            out.append(("h2", h)); out += [("i", ln) for ln in body]
    # the chair paragraph held from 12 goes before 13: move it
    for idx, (t, s) in enumerate(out):
        if t == "h3" and s.startswith("13."):
            j = next(j for j, (tt, ss) in enumerate(out) if tt == "i" and ss.startswith("In the chair’s frame"))
            if j > idx:
                para = out.pop(j); out.insert(idx, para)
            break
    eh = ending[0][3:]
    out.append(("h2", eh))
    for ln in ending[1:]:
        if ln.startswith("## "): out.append(("h3", ln[3:]))
        else: out.append(("p", ln))
    return [(t, STROKES.sub(" strokes", x)) for t, x in out]

def to_html(items):
    h = ['<html><head><meta charset="utf-8"></head><body>']
    for t, s in items:
        e = html.escape(s, quote=False).replace("&lt;b&gt;", "<b>").replace("&lt;/b&gt;", "</b>").replace("†", "<sup>†</sup>")
        if t in ("h1", "h2", "h3"): h.append(f"<{t}>{e}</{t}>")
        elif t == "i": h.append(f"<p><i>{e}</i></p>")
        elif t == "b": h.append(f"<p><b>{e}</b></p>")
        elif t == "eq": h.append(f'<p style="margin-left:36pt">{e}</p>')
        else: h.append(f"<p>{e}</p>")
    h.append("</body></html>")
    return "\n".join(h)

if __name__ == "__main__":
    for k in (1, 2, 3, 4):
        items = build(k)
        open(f"set{k}.html", "w").write(to_html(items))
        open(f"set{k}.txt", "w").write("\n".join(("## " if t.startswith("h") else "") + re.sub("</?b>", "", s) for t, s in items))
        print(k, len(items), sum(len(s) for _, s in items))
