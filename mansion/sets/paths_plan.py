"""The four paths, planned: where each notation idea and each word shows up, and how it's quoted later.

Claude (Anthropic), 2026-10-22. Usage: python3 paths_plan.py OUT.html  (also rewrites BALANCE.md)
One problem set, four solution paths (doc, 12:35). Path 1 explains each idea fully where it first pays
rent; paths 2-4 quote it in shorter forms (R-110), keep a level's new words full where they land, and may
stop briefly to admire the view (R-111). Lengths are solution text only, in thousands of characters,
measured on the current builds (lineup_sets.pieces); statements and rooms are counted separately.
"""
import html, json, sys
import path_features

H = " "  # hair space: arrows hug their operator (R-100)
DOT = f"{H}·{H}"
X = f"{H}×{H}"

FORMS = [
    ("Full", "the first explanation, taking its time, at the place it first pays rent"),
    ("Reprise", "two or three sentences that quote path 1, then the work"),
    ("Reel", "the balance line and the numbers: the highlights reel"),
    ("Nod", "a clause, or the result alone"),
    ("Lands", "a level's new word arrives here; that spot stays full inside a shorter piece"),
    ("View", "a candidate detour of a sentence or two, where something just introduced has a nice job to do"),
]

# idea, path 1, path 2, path 3, path 4, pays rent at
IDEAS = [
 ("2π, then the turn, τ", "textbook",
  "2π at the knife. The slow walk to τ at the flywheel (2), where it pays at once. View: calipers.",
  "The faster walk, at the knife (1).", "One line at the knife: the turn, τ, about 6.3 strokes.", "Used.",
  "2, 6, 9, 10, 13; drawer 3; U1"),
 ("χ for torque", "textbook",
  "Doc's χ on the wall, at the flywheel (2), with the numbers put to it once.",
  "Crank lands beside it at (2): χ keeps the letter, crank is the word.", "Used.", "Used.", "2, 10"),
 ("A sweep as a unit", "textbook",
  "Said as \"stroke a second\" throughout. The plain phrase does the work until the unit is wanted.",
  "Lands at the knife's pickup (1): a stroke a second makes a handy unit of sweep.", "Used.", "Used.",
  "every problem after"),
 ("Straight arrows: → forward, ← back; the direction carries the sign", "arrow",
  "Full at the spool (3): which way is which, m a → = F → + f →. Dog Math §13's \"into the arrows by the third problem.\"",
  "Reprise at (3): → is the cord's way, and the grip's direction comes out of the answer.", "Reel.", "Nod.",
  "4, 5, 7, 11, 12, 13; drawers 1, 3"),
 (f"Turning senses from crosses, the couple: ↓{X}→ = ↺, ↑{X}→ = ↻", "arrow",
  "Full at (3), one cross at a time; ↻ is the opposite of ↺ the way ← is of →. View at the cue ball (5): follow and draw.",
  "Reprise: the couple quoted in one line, always together.", "The couple, no gloss.", "The couple.",
  f"3, 5 ((H − R) ↑{X}→ J); drawers 1, 3, 6; F3, F4; U1"),
 ("Senses in words beside the arrows", "rule",
  "At the spool (3), forward around and back around said beside ↺ and ↻ while the arrows are new; after that the arrows carry it. "
  "Where the scene has its own word, it gets it: topspin at the cue ball.",
  "Arrows; scene words where the scene has them.", "Same.", "Same.", "3, 5"),
 (f"Rolling → turns ↻ (↻{X}↓ = ←: the bottom can't slide)", "arrow",
  "Full at (3). View at the hoop (7): spokes blur at the top.",
  "One clause: rolling →, the spool turns back around.", "The slip line at the cue ball.", "Nod.",
  "5 (v − ω R) →, 7; drawer 3"),
 ("Opposite senses on the two sides of a balance: I α ↻ = (Fr + fR) ↺", "arrow",
  "Full at (3), with the check: 0.72 N m ↺ and 0.88 N m ↻, net 0.16 N m ↻.",
  "The balance line and the check.", "The balance line.", "The numbers.", "3 (4); drawer 1"),
 (f"cos θ first, then the dot: →{DOT}F, the forward part of F", "textbook",
  "cos θ at the knife (1) and the governor (1). F cos θ said first at the spool (4), then →" + DOT + "F there.",
  "Quoted at (3). Its best second rent is drawer 1 (5): cos θ = r/R is the forward part, 3/5 of the pull, Dog Math §9's own 3-4-5. "
  "Drawer 1's governor can say the upward part holds the weight.",
  "Used. Drawer 2 and F4's geometry: try both, keep what reads (R-104).", "Used. U1's sines: try both.",
  "4 (one dot); drawers 1, 2, 6; F4; U1"),
 (f"→{DOT}F{DOT}→, a part that's a force in its own right (the dot scales)", "arrow",
  f"At (4), with the grip as →{DOT}F{DOT}←.", "Once, at drawer 1 (5), where the part acts as a force.",
  f"Only where the part is a force; plain →{DOT}F elsewhere.", "Same.", "3 (4); drawer 1"),
 ("The upward fraction, v / ↑", "arrow",
  "No slot yet: path 1 has no real fraction that wants it.", "Waits.", "Waits.", "Waits.",
  "only a real fraction (R-101)"),
 ("Arrow sums, with what dropped out named", "arrow",
  "Ladder (4): one dot, the top's velocity seen from the foot, about 0.17 strokes a second. Cue ball (5): the bottom's slip. "
  "Hoop (7): the top point's velocity. Line (11): 0.12 A → + 0.12 A ← = 0. Pulses (12): the pair's momentum.",
  "Sums and names kept; they're short.", "The sums.", "Results.", "where they stand"),
 (f"Brackets around a mobile: [½ v →{DOT}→ p]", "arrow",
  f"At the cue ball (5), twice: [½ 2.0 m/s →{DOT}→ 2.0 N s] and the turning [½ 40 ↻{DOT}↻ 0.040 kg m²/s].",
  "Lands with punch and hook: the first bracket is the punch, the second the hook (spin lands at 5 too).",
  "The senses-agree check only.", "Numbers.", "5; drawer 3"),
 ("Hands: a cycle as a hand swinging round from →", "arrow",
  "At the chair (13, part 2).", "One line at the chair.",
  "Phase lands at F1, and the hand is already there to carry it; then 9, drawer 6, F3.", "Used.",
  "13 (3); F1, 9, drawer 6, F3"),
 ("The emphatic register: the sum inside, the meaning outside", "arrow",
  "At the chair (13, part 3), where everything else has already summed and canceled.", "Only where a spot asks for it. The chair may still.",
  "Same. F1's phase sum is a candidate.", "Same. U1, the machine, all of it, is a candidate.",
  "no quota; rare is what makes it work (R-103)"),
 ("Mobiles: arrows tight on the operator, sizes outside", "rule",
  "Typesetting, not an idea to introduce: everywhere arrows are, all four paths.", "Same.", "Same.", "Same.", "everywhere"),
]

# word, lands (path, place), full there, pays rent next, later paths, view
WORDS = [
 ("heft", 2, "knife (1)", "what gravity stores: the weight pulls, the height hefts", "4 (32 J of heft), drawer 2, F4", "Path 3: a three-word gloss at first use. Path 4: used.", ""),
 ("punch", 2, "knife (1)", "the center's motion energy", "4, 5, 8; drawer 2", "Same.", ""),
 ("pickup, and the sweep as a unit", 2, "knife (1)", "a sweep per second", "2; drawer 1", "Same.", ""),
 ("hook", 2, "flywheel (2)", "the turning's energy", "4, 5; drawer 3", "Same.", ""),
 ("crank", 2, "flywheel (2)", "torque's word; χ keeps its letter", "3, 10; drawer 1", "Same.", ""),
 ("profile", 2, "spool (3)", "inertia with the mass out, I/m", "drawer 1 (4), 4, 6; drawer 3; F4",
  "Same.", "Drawer 1 (4), \"that's a uniform disk\": any uniform disk, a coin or a cable reel, has the same profile for its size, which is why things of one shape roll down a ramp together."),
 ("spin", 2, "cue ball (5)", "turning movement", "drawer 3, 8", "Same.", ""),
 ("can, coil", 2, "coils and capacitor (10)", "the stores of charge and of flux", "drawer 5, 11, drawer 6, 13",
  "Same.", "Already there: drawer 5 is a can to match the knife."),
 ("zip", 3, "knife (1)", "punch per mass", "4, F4, 5, 6, 8", "Path 4: used.", ""),
 ("zing", 3, "flywheel (2)", "hook per inertia", "F4, 5", "Same.", ""),
 ("flip", 3, "knife (1); full at F1", "half a turn", "F4, 9-12", "Same.", ""),
 ("still point", 3, "ladder (4); full at F4", "the point still for the instant", "7 (the hoop's bottom, path 1's 2.0 m/s → + 2.0 m/s ← = 0 again); drawer 3",
  "Same.", ""),
 ("tone, chord, beat, phase, Ω_shape", 3, "F1", "a swing at one ring; two at once; the gap", "9, 13",
  "Same.", "The double pendulum (9): two strings nearly in tune beat at the gap between them, and that's how a guitar gets tuned by ear."),
 ("trade, mirror pair", 3, "drawer 3; F2", "motion traded both ways", "10", "Same.", ""),
 ("stripe", 3, "the line (11)", "", "", "Same.", ""),
 ("shift, stretch", 3, "two lights (12); F3", "Bondi's one number", "13",
  "Same.", "The two lights (12): a radar gun reads the shift twice, because its echo is a bounce, the s s t of the bounce."),
 ("zow, zlow (zower, zlower)", 4, "flywheel (2)", "power per mass, per inertia", "2", "", ""),
 ("one machine", 4, "coils and capacitor (10)", "", "13; full at U1", "", ""),
 ("RUN, TEST, tap, in step, at random", 4, "chair (13) for RUN; full at U2", "", "U2", "", ""),
 ("zam, zlam", 4, "U1", "action per mass, per inertia", "ending", "", ""),
]

# piece, current solution length per path (from the build), target, form note per path
P = json.load(open(sys.argv[2])) if len(sys.argv) > 2 else None
PIECES = [
 ("1 knife",          [1.7, 2.3, 2.5, 2.5], [1.7, 2.0, 1.3, 0.9], ["Full, textbook", "Lands: heft, punch, pickup, sweep", "Reel; lands: zip, flip", "Nod"]),
 ("2 flywheel",       [1.7, 1.2, 1.3, 1.6], [1.8, 1.1, 0.8, 1.0], ["Full: τ walk, χ. View", "Lands: hook, crank", "Reel; lands: zing", "Reel; lands: zow, zlow"]),
 ("3 governor, spool",[4.3, 2.7, 2.7, 2.7], [4.3, 1.4, 0.9, 0.6], ["Full: arrows, crosses, roll, balance, dot", "Reprise; lands: profile", "Reel", "Nod"]),
 ("4 ladder",         [1.4, 0.9, 1.3, 1.3], [1.4, 0.8, 0.9, 0.6], ["Full: one dot, seen from the foot", "Reel (drawer 2 follows)", "Reel; lands: still point", "Nod"]),
 ("5 cue ball",       [1.4, 1.3, 1.4, 1.4], [1.5, 1.1, 0.8, 0.6], ["Full: crosses, slip, brackets. View", "Reel; lands: spin", "Reel", "Nod"]),
 ("6 basin",          [0.6, 0.7, 0.8, 0.8], [0.6, 0.6, 0.5, 0.4], ["Full", "Reel", "Reel", "Nod"]),
 ("7 hoop",           [0.6, 0.5, 0.8, 0.8], [0.7, 0.4, 0.5, 0.4], ["Full. View", "Reel", "Reel; still point again", "Nod"]),
 ("8 ribbon",         [0.8, 0.8, 0.8, 0.8], [0.8, 0.7, 0.5, 0.4], ["Full", "Reel", "Reel", "Nod"]),
 ("9 double pendulum",[0.7, 0.7, 0.9, 0.9], [0.7, 0.6, 1.0, 0.5], ["Full", "Reel", "Lands: tone, chord, beat. View", "Nod"]),
 ("10 coils, capacitor",[1.4, 1.6, 1.7, 1.8], [1.4, 1.5, 1.0, 1.0], ["Full", "Lands: can, coil", "Reel", "Reel; lands: one machine"]),
 ("11 line",          [1.0, 1.0, 1.2, 1.2], [1.0, 0.8, 0.9, 0.6], ["Full", "Reel", "Reel; lands: stripe", "Nod"]),
 ("12 two lights",    [0.7, 0.6, 0.8, 0.8], [0.7, 0.5, 1.0, 0.5], ["Full", "Reel", "Lands: shift, stretch. View", "Nod"]),
 ("13 chair",         [1.7, 1.3, 1.3, 1.5], [1.7, 1.1, 1.0, 1.0], ["Full: hands; the emphatic sum", "Reel; emphatic once", "Reel; emphatic once", "Reel; RUN"]),
 ("drawer 4",         [None, 0.6, 0.6, 0.6], [None, 0.6, 0.4, 0.3], ["", "Full", "Reel", "Nod"]),
 ("drawer 1",         [None, 2.3, 2.3, 2.3], [None, 2.0, 1.0, 0.6], ["", "Full: the dot's second rent. View", "Reel", "Nod"]),
 ("drawer 2",         [None, 1.1, 1.0, 1.0], [None, 1.1, 0.6, 0.4], ["", "Full", "Reel", "Nod"]),
 ("drawer 3",         [None, 1.4, 1.4, 1.4], [None, 1.4, 0.9, 0.5], ["", "Full", "Reel; lands: trade", "Nod"]),
 ("drawer 5",         [None, 0.8, 0.7, 0.7], [None, 0.8, 0.4, 0.3], ["", "Full", "Reel", "Nod"]),
 ("drawer 6",         [None, 0.6, 0.6, 0.6], [None, 0.6, 0.4, 0.3], ["", "Full", "Reel", "Nod"]),
 ("drawer 7",         [None, 0.4, 0.4, 0.4], [None, 0.4, 0.3, 0.2], ["", "Full", "Reel", "Nod"]),
 ("F1",               [None, None, 1.3, 1.3], [None, None, 1.3, 0.8], ["", "", "Full: tone, phase, hands", "Reel"]),
 ("F4",               [None, None, 1.2, 1.2], [None, None, 1.2, 0.7], ["", "", "Full: still point", "Reel"]),
 ("F2",               [None, None, 1.1, 1.1], [None, None, 1.1, 0.7], ["", "", "Full", "Reel"]),
 ("F3",               [None, None, 1.2, 1.2], [None, None, 1.2, 0.8], ["", "", "Full", "Reel"]),
 ("U1",               [None, None, None, 1.3], [None, None, None, 1.3], ["", "", "", "Full"]),
 ("U2",               [None, None, None, 1.2], [None, None, None, 1.2], ["", "", "", "Full"]),
]
FIXED = [13.1, 18.5, 20.4, 23.1]  # statements, the way in, rooms, doors, endings: the same text whatever the pace


def measure():
    """Sweep 6: 'now' measured from the current builds, solution text only (p and eq lines); FIXED is the rest
    (headings, scenes, the way in, endings). The statements live in the problem set since sweep 2, so FIXED shrank."""
    import lineup_sets
    def key(name):
        m = __import__("re").match(r"(\d+) ", name)
        if m: return ("problem", m.group(1))
        if name.startswith("drawer"): return ("drawer", "abcdefg"[int(name.split()[1]) - 1])
        if name.startswith("F"): return ("mirror", name[1])
        if name.startswith("U"): return ("under", "αβ"[int(name[1]) - 1])
    fixed = []
    for i, k in enumerate((1, 2, 3, 4)):
        words, ps = lineup_sets.pieces(k)
        sol, rest = {}, sum(len(x) for _, x in words)
        for name, body in ps:
            n = sum(len(x) for t, x in body if t in ("p", "eq")) if name != "ending" else 0
            rest += sum(len(x) for t, x in body) - n
            if name.startswith("problem "): sol[("problem", name.split()[1].rstrip(","))] = n
            elif name.startswith("drawer "): sol[("drawer", name.split()[1])] = n
            elif name.startswith("funhouse mirror "): sol[("mirror", name.split()[2])] = n
            elif name.startswith("under the stage "): sol[("under", name.split()[3])] = n
        for row in PIECES:
            v = sol.get(key(row[0]))
            row[1][i] = None if v is None else round(v / 1000, 1)
        fixed.append(round(rest / 1000, 1))
    FIXED[:] = fixed


PIECES = [[a, list(b), c, d] for a, b, c, d in PIECES]
measure()
LABEL = {"drawer 1": "drawer a", "drawer 2": "drawer b", "drawer 3": "drawer c", "drawer 4": "drawer d", "drawer 5": "drawer e",
         "drawer 6": "drawer f", "drawer 7": "drawer g", "F1": "mirror 1", "F2": "mirror 2", "F3": "mirror 3", "F4": "mirror 4", "U1": "α", "U2": "β"}
for row in PIECES: row[0] = LABEL.get(row[0], row[0])

VIEWS = [
 (1, "flywheel (2), at the walk to τ", "Calipers measure across, so the diameter was the ruler, and π came from there. A turn measured from the center is τ.", "doc's teaching notes say calipers belong in the book"),
 (1, "cue ball (5), after (H − R) ↑" + X + "→ J = (H − R) J ↻", "Hit above center and the cross gives ↻, topspin: the pool player's follow. Below center it's ↓" + X + "→ = ↺, draw.", "the couple pays rent in the room it's named for"),
 (1, "hoop (7), after the top point's 4.0 m/s →", "That's why a photo of a passing bicycle blurs the spokes at the top and catches them sharp at the bottom.", "the arrow sum is something you've seen"),
 (2, "drawer 1 (4), \"that's a uniform disk\"", "Any uniform disk, a coin or a cable reel, has the same profile for its size; that's why things of one shape roll down a ramp together.", "profile just landed one problem back"),
 (3, "double pendulum (9), at the beat", "Two strings nearly in tune beat at the gap between them, and that's how a guitar gets tuned by ear.", "chord and beat just landed at F1"),
 (3, "two lights (12), at the shift", "A radar gun reads the shift twice, because its echo is a bounce: the s s t of the bounce.", "the shift just landed"),
 (4, "none planned", "The understage is the view. Add one only if a place asks for it.", ""),
]


def tot(i, which):
    return round(sum((r[which][i] or 0) for r in PIECES), 1)


def md():
    o = ["# The four paths, planned (working note, Claude, 2026-10-22 12:50)", "",
         "Written by Claude (Anthropic) for dr. kraemer; shared feature controls extended by Codex (OpenAI), 2026-10-23. Applied and planned choices are labeled separately. One problem set, four solution paths.",
         "Generated by paths_plan.py; edit there.", "",
         "Path 1 explains each idea fully where it first pays rent. Paths 2-4 quote it in shorter forms (R-110), keep a level's new words full where they land, and can stop briefly to admire the view (R-111).", "",
         "## The forms", ""] + [f"- **{a}**: {b}" for a, b in FORMS] + ["", "## Notation ideas", "",
         "| Idea | Path 1 | Path 2 | Path 3 | Path 4 | Pays rent at |", "|---|---|---|---|---|---|"]
    o += [f"| {r[0]} | {r[2]} | {r[3]} | {r[4]} | {r[5]} | {r[6]} |" for r in IDEAS]
    o += ["", "## Words", "", "| Word | Lands | Said as | Pays rent next | Later paths | View |", "|---|---|---|---|---|---|"]
    o += [f"| {w} | path {k}, {where} | {said} | {rent} | {later} | {view} |" for w, k, where, said, rent, later, view in WORDS]
    o += ["", "## Pieces: current length → historical estimate (thousand characters)", "", "The estimates are old planning aids, not user quotas or requirements.", "",
          "| Piece | Path 1 | Path 2 | Path 3 | Path 4 |", "|---|---|---|---|---|"]
    for name, now, tgt, f in PIECES:
        cells = [("-" if n is None else f"{n} → {t}: {ff}") for n, t, ff in zip(now, tgt, f)]
        o.append(f"| {name} | " + " | ".join(cells) + " |")
    o.append("| solutions | " + " | ".join(f"{tot(i, 1)} → {tot(i, 2)}" for i in range(4)) + " |")
    o.append("| rooms, scenes, endings | " + " | ".join(str(x) for x in FIXED) + " |")
    o.append("| whole path | " + " | ".join(f"{round(FIXED[i] + tot(i, 1), 1)} → {round(FIXED[i] + tot(i, 2), 1)}" for i in range(4)) + " |")
    o += ["", "## Views (R-111)", "", "| Path | Where | The view | Why there |", "|---|---|---|---|"]
    o += [f"| {k} | {w} | {v} | {why} |" for k, w, v, why in VIEWS]
    return "\n".join(o) + "\n\n" + path_features.markdown()


def e(s):
    return html.escape(s, quote=False)


def chips(s):
    out = e(s)
    for f, _ in FORMS:
        out = out.replace(f, f'<span class="f f-{f.lower()}">{f}</span>', 1) if out.startswith(f) or f"; {f.lower()}" in out.lower() or f". {f}" in out else out
    return out


def page():
    import build_sets
    feature_panel = path_features.panel(observations=[path_features.observe(build_sets.build(k), k) for k in range(1,5)])
    leg = "".join(f'<div class="leg"><span class="f f-{a.lower()}">{a}</span><span>{e(b)}</span></div>' for a, b in FORMS)
    ideas = "".join(f'<tr class="k-{r[1]}"><th scope="row">{e(r[0])}</th>' + "".join(f"<td>{e(c)}</td>" for c in r[2:6]) + f'<td class="rent">{e(r[6])}</td></tr>' for r in IDEAS)
    words = ""
    for k in (2, 3, 4):
        words += f'<tr class="grp"><th colspan="6">Path {k} words</th></tr>'
        for w, kk, where, said, rent, later, view in WORDS:
            if kk == k:
                words += f'<tr><th scope="row">{e(w)}</th><td>{e(where)}</td><td>{e(said)}</td><td class="rent">{e(rent)}</td><td>{e(later)}</td><td class="view">{e(view)}</td></tr>'
    pieces = ""
    for name, now, tgt, f in PIECES:
        pieces += f'<tr><th scope="row">{e(name)}</th>'
        for n, t, ff in zip(now, tgt, f):
            if n is None:
                pieces += '<td class="na">·</td>'
            else:
                head = ff.split(";")[0].split(":")[0].split(".")[0].split(" (")[0].strip()
                kind = head if head in [a for a, _ in FORMS] else ""
                rest = ff[len(head):].lstrip(":;. ") if kind else ff
                tag = f'<span class="f f-{kind.lower()}">{kind}</span>' if kind else ""
                pieces += f'<td><span class="num">{n:.1f} → <b>{t:.1f}</b></span>{tag}<span class="note">{e(rest)}</span></td>'
        pieces += "</tr>"
    sums = '<tr class="sum"><th scope="row">solutions</th>' + "".join(f'<td><span class="num">{tot(i, 1)} → <b>{tot(i, 2)}</b></span></td>' for i in range(4)) + "</tr>"
    sums += '<tr class="sum"><th scope="row">rooms, scenes, endings</th>' + "".join(f'<td><span class="num">{x}</span></td>' for x in FIXED) + "</tr>"
    sums += '<tr class="sum big"><th scope="row">whole path</th>' + "".join(f'<td><span class="num">{round(FIXED[i] + tot(i, 1), 1)} → <b>{round(FIXED[i] + tot(i, 2), 1)}</b></span></td>' for i in range(4)) + "</tr>"
    views = "".join(f'<tr><td class="pk">{k}</td><th scope="row">{e(w)}</th><td>{e(v)}</td><td class="rent">{e(why)}</td></tr>' for k, w, v, why in VIEWS)
    return f"""<title>The Four Paths</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Literata:opsz,wght@7..72,400;7..72,600&family=IBM+Plex+Sans:wght@400;600&display=swap">
<style>
/* a score for four movements: one row per idea, one column per path, read across */
:root {{
  --bg: #fbf9f6; --fg: #2a211b; --muted: #6d625a; --rule: #e2dad2; --panel: #f3efe9;
  --brown: #5a3a22; --cobalt: #1f4fa3; --red: #b3261e; --redwash: #f7e4e1; --cobaltwash: #e3eaf7; --brownwash: #efe5da;
  --body: "Literata", Georgia, serif; --ui: "IBM Plex Sans", system-ui, sans-serif;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg: #1c1814; --fg: #ece5dc; --muted: #a99c90; --rule: #3a322b; --panel: #252019;
  --brown: #d2a57c; --cobalt: #8fb0ee; --red: #f08a7e; --redwash: #3a2220; --cobaltwash: #1f2a40; --brownwash: #33281e; color-scheme: dark }} }}
:root[data-theme="dark"] {{
  --bg: #1c1814; --fg: #ece5dc; --muted: #a99c90; --rule: #3a322b; --panel: #252019;
  --brown: #d2a57c; --cobalt: #8fb0ee; --red: #f08a7e; --redwash: #3a2220; --cobaltwash: #1f2a40; --brownwash: #33281e; color-scheme: dark }}
body {{ background: var(--bg); color: var(--fg); font: 15px/1.55 var(--body); }}
.wrap {{ max-width: 84rem; margin: 0 auto; padding-block: 2rem 4rem;
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }}
h1 {{ font: 600 2rem/1.2 var(--body); color: var(--brown); margin: 0 0 .5rem; text-wrap: balance; }}
h2 {{ font: 600 1.3rem/1.3 var(--body); color: var(--brown); margin: 2.5rem 0 .4rem; text-wrap: balance; }}
.by {{ font: 600 .85rem/1.4 var(--ui); color: var(--muted); margin: 0 0 1rem; }}
.lede, .sub {{ max-width: 46rem; margin: 0 0 1rem; }}
.sub {{ color: var(--muted); font-size: .95rem; }}
.legend {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(17rem, 1fr)); gap: .4rem 1.5rem; margin: 1rem 0 0; max-width: 60rem; }}
.leg {{ display: flex; gap: .6rem; align-items: baseline; font-size: .9rem; }}
.f {{ font: 600 .68rem/1 var(--ui); letter-spacing: .06em; text-transform: uppercase; padding: .22rem .4rem; border-radius: 3px; white-space: nowrap; flex: none; }}
.f-full {{ background: var(--red); color: var(--bg); }}
.f-reprise {{ background: var(--redwash); color: var(--red); }}
.f-reel {{ background: var(--panel); color: var(--fg); border: 1px solid var(--rule); }}
.f-nod {{ color: var(--muted); border: 1px solid var(--rule); }}
.f-lands {{ background: var(--brownwash); color: var(--brown); }}
.f-view {{ background: var(--cobaltwash); color: var(--cobalt); }}
.scroll {{ overflow-x: auto; margin-top: .75rem; border-top: 2px solid var(--brown); }}
table {{ border-collapse: collapse; width: 100%; min-width: 64rem; font-size: .88rem; }}
th, td {{ text-align: left; vertical-align: top; padding: .55rem .6rem; border-bottom: 1px solid var(--rule); }}
thead th {{ font: 600 .72rem/1.3 var(--ui); letter-spacing: .06em; text-transform: uppercase; color: var(--muted); background: var(--bg); position: sticky; top: 0; }}
tbody th {{ font-weight: 600; width: 15rem; }}
tr.k-textbook > th {{ box-shadow: inset 3px 0 0 var(--cobalt); }}
tr.k-arrow > th {{ box-shadow: inset 3px 0 0 var(--red); }}
tr.k-rule > th {{ box-shadow: inset 3px 0 0 var(--brown); }}
td.rent {{ color: var(--muted); font-family: var(--ui); font-size: .8rem; }}
td.view {{ color: var(--cobalt); }}
tr.grp th {{ font: 600 .75rem/1.3 var(--ui); letter-spacing: .06em; text-transform: uppercase; color: var(--brown); background: var(--panel); }}
.pieces td {{ min-width: 11rem; }}
.num {{ display: block; font: .85rem/1.4 var(--ui); font-variant-numeric: tabular-nums; color: var(--muted); }}
.num b {{ color: var(--fg); }}
.pieces .f {{ display: inline-block; margin: .3rem .35rem 0 0; }}
.note {{ font-size: .82rem; }}
td.na {{ color: var(--rule); text-align: center; }}
tr.sum th, tr.sum td {{ background: var(--panel); }}
tr.big .num {{ font-size: 1rem; }}
td.pk {{ font: 600 1rem/1.3 var(--ui); color: var(--brown); width: 3rem; }}
.views table {{ min-width: 48rem; }}
.foot {{ max-width: 46rem; margin-top: 2.5rem; color: var(--muted); font-size: .92rem; }}
.foot p {{ margin: 0 0 .7rem; }}
@media (max-width: 760px) {{ body {{ font-size: 14px; }} }}
</style>
<div class="wrap">
<h1>The four paths</h1>
<p class="by">Written by Claude (Anthropic), 2026-10-22, for dr. kraemer; shared feature controls extended by Codex (OpenAI), 2026-10-23. Applied and planned choices are labeled separately.</p>
<p class="lede">One problem set, four solution paths. Path 1 explains each idea fully where it first pays rent. Paths 2–4 quote it in shorter and shorter forms, keep a level's new words full where they land, and now and then stop for a sentence to admire the view.</p>
<div class="legend">{leg}</div>

{feature_panel}
<h2>Notation ideas</h2>
<p class="sub">In order of arrival in path 1. A blue edge marks the textbook form that's kept until it looks goofy, red marks the arrows, brown a rule that holds everywhere. Numbers in parentheses are problems.</p>
<div class="scroll"><table>
<thead><tr><th>Idea</th><th>Path 1</th><th>Path 2</th><th>Path 3</th><th>Path 4</th><th>Pays rent at</th></tr></thead>
<tbody>{ideas}</tbody></table></div>

<h2>Words</h2>
<p class="sub">Each word is said in full where it lands, in that path only. Later paths use it with at most a short gloss at its first use.</p>
<div class="scroll"><table>
<thead><tr><th>Word</th><th>Lands</th><th>Said as</th><th>Pays rent next</th><th>Later paths</th><th>View</th></tr></thead>
<tbody>{words}</tbody></table></div>

<h2>Pieces</h2>
<p class="sub">Solution text only, in thousands of characters: the current build, then a historical estimate. These old planning estimates are not user quotas or requirements. Rooms, scenes and endings are counted below, apart; the statements live in the problem set.</p>
<div class="scroll pieces"><table>
<thead><tr><th>Piece</th><th>Path 1</th><th>Path 2</th><th>Path 3</th><th>Path 4</th></tr></thead>
<tbody>{pieces}{sums}</tbody></table></div>

<h2>Views</h2>
<p class="sub">Roommates doing each other odd jobs: a sentence or two, right after something's introduced, where it has a nice job to do in the scene. Only where something just landed and has a nice job to do in the scene. No quota.</p>
<div class="scroll views"><table>
<thead><tr><th>Path</th><th>Where</th><th>The view</th><th>Why there</th></tr></thead>
<tbody>{views}</tbody></table></div>

<div class="foot">
<p>The statements and rooms set a floor: 13 thousand characters in path 1, 23 thousand in path 4. Shortening solutions alone takes the paths from about {', '.join(str(round(FIXED[i] + tot(i, 1))) for i in range(4))} thousand to about {', '.join(str(round(FIXED[i] + tot(i, 2))) for i in range(4))}. The rest of the gap is the problems themselves, and path 1 shouldn't be padded to close it.</p>
<p>A later path can point back by name (\"as at the spool in path 1\") so a reader who skipped ahead knows where the full version lives.</p>
<p>The paths are solutions only since the sweep (doc, 18:22), titled \"path k of 4\"; the statements live in the problem set.</p>
</div>
</div>"""


if __name__ == "__main__":
    open(sys.argv[1], "w").write(page())
    open(__file__.replace("paths_plan.py", "BALANCE.md"), "w").write(md())
    print("solutions now", [tot(i, 1) for i in range(4)], "target", [tot(i, 2) for i in range(4)])
    print("paths now", [round(FIXED[i] + tot(i, 1), 1) for i in range(4)], "target", [round(FIXED[i] + tot(i, 2), 1) for i in range(4)])
