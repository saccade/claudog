#!/usr/bin/env python3
# Builds "Claude Lot Bulk and Four Tables 2610181354.pdf" — news for Codex. Written by Claude.
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                KeepTogether, PageBreak)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

FD = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("DV", "/home/claude/out/dv_sub.ttf"))
pdfmetrics.registerFont(TTFont("DVB", FD + "DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DVI", FD + "DejaVuSans-Oblique.ttf"))
pdfmetrics.registerFont(TTFont("DVS", FD + "DejaVuSerif.ttf"))
pdfmetrics.registerFont(TTFont("DVSB", FD + "DejaVuSerif-Bold.ttf"))
from reportlab.pdfbase.pdfmetrics import registerFontFamily
registerFontFamily("DV", normal="DV", bold="DVB", italic="DVI", boldItalic="DVB")
import re
_tag = re.compile(r"(<[^>]*>)")
_na = re.compile(r"([^\x00-\x7f]+)")
def wrapdv(t):
    out = []
    for part in _tag.split(t):
        if part.startswith("<"): out.append(part)
        else: out.append(_na.sub(r'<font name="DV">\1</font>', part))
    return "".join(out)

BROWN = colors.HexColor("#6b3a1e")
RED = colors.HexColor("#c8102e")
RED_LT = colors.HexColor("#e06070")
BLUE = colors.HexColor("#0047ab")
ORANGE = colors.HexColor("#c45a00")
GREY = colors.HexColor("#555555")

OUT = "/home/claude/out/Claude Lot Bulk and Four Tables 2610181354.pdf"
doc = SimpleDocTemplate(OUT, pagesize=letter, leftMargin=0.9*inch, rightMargin=0.9*inch,
                        topMargin=0.8*inch, bottomMargin=0.8*inch,
                        title="Lot, bulk, and four tables", author="Claude (Anthropic)")

base = ParagraphStyle("base", fontName="Helvetica", fontSize=10, leading=13.5)
small = ParagraphStyle("small", parent=base, fontSize=8.5, leading=11, textColor=GREY)
h1 = ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=20, leading=24, textColor=BROWN, spaceAfter=4)
h2 = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=13, leading=16, textColor=BROWN, spaceBefore=12, spaceAfter=5)
defn = ParagraphStyle("defn", parent=base, leftIndent=14, spaceBefore=3)
formula = ParagraphStyle("formula", parent=base, leftIndent=36, spaceAfter=2)
cell = ParagraphStyle("cell", fontName="Helvetica", fontSize=8.5, leading=10.5, alignment=1)
cellh = ParagraphStyle("cellh", fontName="Helvetica-Bold", fontSize=8.5, leading=10.5, alignment=1)
cellr = ParagraphStyle("cellr", fontName="Helvetica-Bold", fontSize=8.5, leading=10.5, alignment=0)
ghost = "<font color='#777777' size='7.5'>%s</font>"

def P(t, s=base): return Paragraph(wrapdv(t), s)
def O(t): return "<font color='#c45a00'>%s</font>" % t      # Claude coinage, orange
def B(t): return "<font color='#0047ab'>%s</font>" % t      # textbook term, cobalt
def R(t): return "<font color='#c8102e'>%s</font>" % t      # Straight-> term, red

def grid(headers, rows, colw=None, ghosts=None):
    # headers: list of (name, ghost) ; rows: list of (rowlabel, [cells]) with cell = (body, ghost) or str
    hdr = [P("<b>of →</b>", cellh)]
    for name, g in headers:
        hdr.append(P("<b>%s</b>%s" % (name, ("<br/>" + ghost % ("(%s)" % g)) if g else ""), cellh))
    data = [hdr]
    for lab, cells in rows:
        r = [P("<b>%s</b>" % lab, cellr)]
        for c in cells:
            if c is None or c == "":
                r.append(P("", cell))
            elif isinstance(c, tuple):
                body, g = c
                r.append(P(body + (("<br/>" + ghost % ("(%s)" % g)) if g else ""), cell))
            else:
                r.append(P(c, cell))
        data.append(r)
    t = Table(data, colWidths=colw, repeatRows=1)
    t.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#bbbbbb")),
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#f1e7dd")),
        ("BACKGROUND", (0, 1), (0, -1), colors.HexColor("#f7f2ec")),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    return t

def redbox(flow, light=False):
    t = Table([[flow]], colWidths=[doc.width])
    t.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 0.8 if light else 1.6, RED_LT if light else RED),
        ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    return t

S = []
S.append(P("Lot, bulk, and four tables", h1))
S.append(P("<b>Written by Claude (Anthropic), 2026-10-18 13:54.</b> News for Codex on doc's Straight→ Mechanics rotation glossary. "
           "Not doc's text: the ideas are his, the words here are the model's. Provenance is in the shared ledger "
           "(Events E-0135 to E-0165, Coinages, Rules R-027 to R-031), not here. "
           "Colors: <font color='#c8102e'>red</font> Straight→ terms, <font color='#0047ab'>blue</font> textbook terms, "
           "<font color='#c45a00'>orange</font> a Claude coinage still in play.", small))
S.append(Spacer(1, 8))

S.append(P("What this is", h2))
S.append(P("Two days of churn on the turning vocabulary, ending in four small multiplication tables that hold every quantity "
           "the book's rotation chapter needs, each cell a sentence of the form “the X of the Y”. Everything below was checked by "
           "hand and the vector identities by a sympy script (CL-092). Codex's job, if it takes it: try to break the tables. "
           "The specific claims worth attacking are listed at the end."))

S.append(P("The rulings since the last news, in one breath", h2))
rul = [
 "%s (ω) replaces turn rate; %s (α) is the fluxion of sweep." % (R("sweep"), R("pickup")),
 "The leverage of a force splits by direction against the arm: %s χ = ι × F about the free axis (can do work); %s M = ι × F across the arm (locked out); %s along the arm (torsion, no symbol). A torque is a moment that can do work." % (R("torque"), R("moment"), R("twist")),
 "%s (noun) is a unit of work: one stroke of torque. The trundle rate is power, ω · χ = F · ν." % R("trundle"),
 "A %s is a body (or several) and an axis; a body is set up in a rotation. Quantities about an axis belong to setups." % R("setup"),
 "%s (ν) = ω × ι, the sweep of the lever, replaces turn speed." % R("pace"),
 "“Inertia” was tried as a named quantity (mass taken around, η) and dropped: the axis belongs to the setup, “around” to the sweep. Inertia stays the name of the first law.",
 "%s (λ) = ι × m: mass on an arm, out along the arm; what you have to do. Sweep it: movement. Pick it up: the force around. Lever it: bulk. The tire shop's unbalance is a net lot." % R("lot"),
 "%s (β) = ι · λ = m r²: your leverage on the lot; a scale about the axis, no direction, tied to the setup as mass is tied to a body. Replaces ponder. The two r's are two facts: arc per stroke (in the lot) and leverage (on the lot)." % R("bulk"),
 "%s (p) is a set-up body's motion, the sweep of the lot; %s (ξ) is the leverage of the movement, the sweep of the bulk, the lot at pace." % (R("movement"), R("spin")),
 "%s/%s: rate of bulk and its negative (body: you need stuff to spread); %s/%s the same for the ghost (shape only). The skater tucks into a pickup." % (R("spread"), R("tuck"), R("splay"), R("fold")),
 "%s: a force or moment applied across time; taken, not spent (spending is for energy, power, motion). %s: duration of a net force, the movement it adds. %s: duration of a net torque, the spin it adds." % (R("effort"), R("impulse"), R("boost")),
 "%s / %s: the sweep of the movement / of the pace, what keeps a body on center (textbook %s). “Central force” was tried and retired: the textbook uses it for any force aimed at a center." % (R("center force"), R("center acceleration"), B("centripetal")),
 "%s: the tendency of a turning body to go straight when the center force lets go (textbook %s); a verb, not a second force. Claude's word; doc: “fling is the thing”." % (O("fling"), B("centrifugal")),
 "%s and %s are the stored danger, straight and turning; they can be %s. A %s is the energy a collision spends, burns and waves away. A collision has an impulse (motion ledger) and a kick (energy ledger)." % (R("punch"), R("hook"), R("caught"), R("kick")),
 "%s: the pickup of the movement, α × p, how fast the center force grows while picking up; the standard name for a rate of force, kept. “Gain” rejected (a multiplier, not a rate)." % R("yank"),
 "%s: one word, three numbers by direction (along, across, around). “Spring rate” rejected: collides with rate." % R("stiffness"),
 "%s: mass along a path, kg m; the duration of the movement, the swing of the lot; what moves a centre of mass (tonne-metres on a ship)." % R("transit"),
 "%s: the ghost of torque, ι × a (the old twirl unit was a placeholder). %s: the placeholder unit of spin, kg m²/s, Fred's second job." % (R("twirl"), R("Fred")),
 "The ghost energy family, for people who ain't afraid: %s = punch/m, %s = hook/m, %s = power/m, %s = work/m, %s = action/m." % (R("zip"), R("zing"), R("zow"), R("zug"), R("zam")),
]
for r in rul:
    S.append(P("• " + r, defn))

S.append(P("Two rules the tables run on", h2))
S.append(redbox(P("<b>“of” is the ordinary genitive, not an operator.</b> The product is whichever the two kinds of object take: two axis arrows dot, "
                  "an axis arrow and a lever cross, a scale just scales. <b>Two multiplication words, two orders:</b> “of” leads with the operator "
                  "(the sweep of the lot, ω × λ); “at” leads with the thing (the lot at pace, λ × ν). A backward-order cell goes in a table with its minus "
                  "sign; the running text uses the sentence that comes out positive. (R-027, R-031)")))
S.append(Spacer(1, 4))
S.append(redbox(P("<b>Rows are actions and rates; columns are things a setup has.</b> Duration and rate are rows, not columns (“the duration of the force” "
                  "reads; “the force of the duration” doesn't). Scalars (time, mass) take no column width: mass is carried by the ghost version "
                  "printed under each body cell, the same quantity with the mass taken out. The ghost of the lot is the leverage; the ghost of the "
                  "movement is the pace. (R-030)")))

S.append(P("Table 1 — the setup's starting pieces", h2))
S.append(grid([("lever ι", None), ("mass m", None), ("lot λ", None)],
    [("1 rate of", ["pace", "", "movement"]),
     ("2 swing of", ["arc", "", "transit"]),
     ("3 sweep of", ["pace", "", "movement"]),
     ("4 pickup of", ["acceleration around", "", "force around"]),
     ("5 leverage of", ["bulkiness", "lot", "bulk"]),
     ("6 pace of", ["−swirl", "movement", "−spin"])],
    colw=[1.1*inch, 1.6*inch, 1.3*inch, 1.5*inch]))
S.append(P("The lot column is the lever column with the mass in it, cell for cell; the mass column is the two seams, "
           "lot = leverage of the mass, movement = pace of the mass. Row 6's minus signs are the backward order; the text says "
           "“the lever at pace” (swirl, ι × ν) and “the lot at pace” (spin, λ × ν).", small))

S.append(KeepTogether([P("Table 2 — the motion ledger, ghosts beneath", h2), grid([("lot λ", "leverage ι"), ("bulk β", "bulkiness r²"), ("movement p", "pace ν"),
               ("force F", "accel. a"), ("torque χ", "twirl"), ("spin ξ", "swirl")],
    [("1 duration of", ["", "", ("transit", "path"), ("impulse = Δmovement", "Δpace"), ("boost = Δspin", "Δswirl"), ""]),
     ("2 rate of", [("movement", "pace"), ("spread", "splay"), ("force", "accel. a"), "", "", ("torque", "twirl")]),
     ("3 swing of", [("transit", "arc"), "", "", "", "", ""]),
     ("4 sweep of", [("movement", "pace"), ("spin", "swirl"), ("center force", "center accel."), "", "", ""]),
     ("5 pickup of", [("force around", "accel. around"), ("torque", "twirl"), ("yank", "jerk"), "", "", ""]),
     ("6 leverage of", [("bulk", "bulkiness"), "", ("spin", "swirl"), ("torque; moment if an arm", "twirl"), "", ""])],
    colw=[1.0*inch] + [0.95*inch]*6)]))
S.append(P("The empty cells are empty on purpose: leverage of bulk is m r³ along the arm and nothing is measured in it; the ladder stops "
           "because the arm enters a quantity exactly twice. The one cell that looks like a contradiction, torque; moment if an arm, is the "
           "crane: slew brake off, torque; brake on, moment.", small))

S.append(P("Table 3 — the energy ledger (every cell a dot)", h2))
S.append(grid([("movement p", None), ("force F", None), ("torque χ", None), ("spin ξ", None)],
    [("1 path of", ["action", "work", "", ""]),
     ("2 swing of", ["", "", "work", "action"]),
     ("3 pace of", ["2·punch", "power", "", ""]),
     ("4 sweep of", ["", "", "power", "2·hook"])],
    colw=[1.0*inch, 1.3*inch, 1.3*inch, 1.3*inch, 1.3*inch]))

S.append(P("Table 3-g — the same with the mass out, for the unafraid", h2))
S.append(grid([("pace ν", None), ("accel. a", None), ("twirl", None), ("swirl", None)],
    [("1 path of", ["zam", "zug", "", ""]),
     ("2 swing of", ["", "", "zug", "zam"]),
     ("3 pace of", ["2·zip", "zow", "", ""]),
     ("4 sweep of", ["", "", "zow", "2·zing"])],
    colw=[1.0*inch, 1.3*inch, 1.3*inch, 1.3*inch, 1.3*inch]))
S.append(P("Kept separate from the body tables so a reader who has never met a ghost can use Tables 1–3 whole.", small))

S.append(PageBreak())
S.append(P("The definitions, one per filled cell (doc's two-part format)", h2))
S.append(P("Table coordinates are row-number + column-letter. Articles: a body's own quantities take “the” (the lot, the bulk, the movement, "
           "the spin); an applied force or torque takes “a”. These are the sentences doc has accepted so far; the wording is his to change.", small))
defs = [
 ("T1 1a", "pace (ν): the rate of the lever's end", "ν = Δι / Δt"),
 ("T1 1c", "movement (p): the rate of the lot", "p = Δλ / Δt"),
 ("T1 2a", "arc: the swing of the lever", "arc = ψ × ι"),
 ("T1 2c", "transit: the swing of the lot", "transit = ψ × λ"),
 ("T1 3a", "pace (ν): the sweep of the lever", "ν = ω × ι"),
 ("T1 3c", "movement (p): the sweep of the lot", "p = ω × λ"),
 ("T1 4a", "acceleration around (a): the pickup of the lever", "a = α × ι"),
 ("T1 4c", "force around (F): the pickup of the lot", "F = α × λ"),
 ("T1 5a", "bulkiness (r²): the leverage of the lever", "r² = ι × ι"),
 ("T1 5b", "lot (λ): the leverage of the mass", "λ = ι × m"),
 ("T1 5c", "bulk (β): the leverage of the lot", "β = ι × λ"),
 ("T1 6a", "swirl: the lever at pace", "swirl = ι × ν"),
 ("T1 6b", "movement (p): the pace of the mass", "p = ν × m"),
 ("T1 6c", "spin (ξ): the lot at pace", "ξ = λ × ν"),
 ("T2 1c", "transit: the movement carried over time", "transit = p × Δt"),
 ("T2 1d", "impulse (Δp): the duration of a net force; the movement it adds", "Δp = F × Δt"),
 ("T2 1e", "boost (Δξ): the duration of a net torque; the spin it adds", "Δξ = χ × Δt"),
 ("T2 2a", "movement (p): the rate of the lot", "p = Δλ / Δt"),
 ("T2 2b", "spread: the increase of the bulk", "spread = Δβ / Δt"),
 ("T2 2c", "force (F): the fluxion of the movement; a push or pull adds movement over time", "F = Δp / Δt"),
 ("T2 2f", "torque (χ): the fluxion of the spin; a torque adds spin over time", "χ = Δξ / Δt"),
 ("T2 3a", "transit: the swing of the lot", "transit = ψ × λ"),
 ("T2 4a", "movement (p): the sweep of the lot", "p = ω × λ"),
 ("T2 4b", "spin (ξ): the sweep of the bulk", "ξ = ω × β"),
 ("T2 4c", "center force (F⊙): the sweep of the movement; the force that keeps it on center", "F⊙ = ω × p"),
 ("T2 5a", "force around (F): the pickup of the lot", "F = α × λ"),
 ("T2 5b", "torque (χ): the pickup of the bulk", "χ = α × β"),
 ("T2 5c", "yank: the pickup of the movement", "yank = α × p"),
 ("T2 6a", "bulk (β): the leverage of the lot", "β = ι × λ"),
 ("T2 6c", "spin (ξ): the leverage of the movement", "ξ = ι × p"),
 ("T2 6d", "torque (χ): the leverage of a force", "χ = ι × F"),
 ("T2 6d′", "moment (M): the leverage of a force across an arm", "M = ι × F"),
]
for coord, sent, f in defs:
    S.append(KeepTogether([P("<font color='#555555'>%s</font>&nbsp;&nbsp; <b>%s:</b>" % (coord, sent), defn),
                           P(f + ".", formula)]))

S.append(P("Where this contradicts the textbook (not just renames it)", h2))
S.append(P("• <b>Torque on a balanced beam.</b> The physics book sums “torques about the pivot” for a beam going nowhere; here those are "
           "moments, since nothing is free to turn. Engineers already say moments there. Contradiction with the physics book only.", defn))
S.append(P("• <b>Spin.</b> The textbook splits angular momentum into spin (about a body's own axis) and orbital. Here spin is the leverage of the "
           "movement about whatever axis the setup has, so a train on a track has spin. Wider than the textbook's word.", defn))
S.append(P("• <b>Center force</b> was chosen over “central force” precisely to avoid a third: the textbook's central force is any force aimed at a "
           "center, whatever its size.", defn))
S.append(P("Everything else is a new word for an old thing or the same word for the same thing: impulse, work, power, action, stiffness, "
           "yank, and lot as the first moment of mass all match the textbook.", defn))

S.append(P("What was checked, and what to attack", h2))
S.append(P("CL-092 (sympy) checks the ladder as 3-vectors for one body on a rigid lever: every cross with a lever in the written order holds; "
           "ω · χ = F · ν holds; ι × (η × ι) equals the inertia tensor applied to the axis. The script also records Claude's own error of the "
           "night: it took the “around” mark on a provisional inertia η = m with the rising-ahead arrow as an axis vector and crossed it, which produced a tangential lot and a "
           "radial movement. The fact underneath, ι × â = −(â × ι), is why the lot had to be the arm weighed and why η was dropped (FX-032, FX-038).", defn))
S.append(P("Claims Codex could usefully try to break:", defn))
for c in [
    "The lot along the arm is the only lot for which sweep of the lot = movement and leverage of the lot = bulk both hold as single operations.",
    "“Of” and “at” fix the order of every cross in the tables with no exceptions (R-031). Find a sentence doc would say that comes out with the wrong sign.",
    "Bulk is a scale about the axis and never needs a direction; the tensor form is out of scope for the book (doc's ruling), but is the scalar claim ever wrong for a rigid setup?",
    "Center force as the sweep of the movement is the whole of what the book needs about circular motion; the orbit (gravity along the lever, no torque, swirl holds) follows without more.",
    "Effort as “force or moment applied across time; taken, not spent”: is there a sentence where effort has to be spent?",
    "Fling (orange) as a verb for the centrifugal tendency: does it survive the rotor-ride example without positing a second force?",
]:
    S.append(P("– " + c, defn))

doc.build(S)
print(OUT)
