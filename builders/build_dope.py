#!/usr/bin/env python3
# Builds "Claude The Straight Dope 2610181506.pdf". Written by Claude (Anthropic).
import re
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                KeepTogether, PageBreak)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

STAMP = "2610181506"
OUT = "/home/claude/out/Claude The Straight Dope %s.pdf" % STAMP

# tiny DejaVu subset for Greek and symbols; Helvetica for everything else
SRC = open(__file__, encoding="utf-8").read()
CH = "".join(sorted(set(c for c in SRC if ord(c) > 127)))
open("/home/claude/out/chars2.txt", "w").write(CH)
import subprocess
subprocess.run(["pyftsubset", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
                "--text-file=/home/claude/out/chars2.txt", "--no-hinting", "--desubroutinize",
                "--output-file=/home/claude/out/dv_sub2.ttf", "--layout-features=",
                "--name-IDs=1,2,3,4,6", "--drop-tables+=FFTM,GSUB,GPOS,GDEF"], check=True,
               stderr=subprocess.DEVNULL)
pdfmetrics.registerFont(TTFont("DV", "/home/claude/out/dv_sub2.ttf"))
_tag = re.compile(r"(<[^>]*>)")
_na = re.compile(r"([^\x00-\x7f]+)")
def wrapdv(t):
    out = []
    for part in _tag.split(t):
        out.append(part if part.startswith("<") else _na.sub(r'<font name="DV">\1</font>', part))
    return "".join(out)

BROWN = colors.HexColor("#6b3a1e"); RED = colors.HexColor("#c8102e"); RED_LT = colors.HexColor("#e06070")
BLUE = colors.HexColor("#0047ab"); ORANGE = colors.HexColor("#c45a00"); GREY = colors.HexColor("#555555")

doc = SimpleDocTemplate(OUT, pagesize=letter, leftMargin=0.9*inch, rightMargin=0.9*inch,
                        topMargin=0.8*inch, bottomMargin=0.8*inch,
                        title="The straight dope: Straight-> Mechanics glossary and tables", author="Claude (Anthropic)")
base = ParagraphStyle("base", fontName="Helvetica", fontSize=10, leading=13.5)
small = ParagraphStyle("small", parent=base, fontSize=8.5, leading=11, textColor=GREY)
h1 = ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=20, leading=24, textColor=BROWN, spaceAfter=4)
h2 = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=13, leading=16, textColor=BROWN, spaceBefore=12, spaceAfter=5)
h3 = ParagraphStyle("h3", fontName="Helvetica-Bold", fontSize=10.5, leading=13, textColor=BROWN, spaceBefore=8, spaceAfter=2)
defn = ParagraphStyle("defn", parent=base, leftIndent=14, spaceBefore=3)
formula = ParagraphStyle("formula", parent=base, leftIndent=36, spaceAfter=2)
cell = ParagraphStyle("cell", fontName="Helvetica", fontSize=8.5, leading=10.5, alignment=1)
cellh = ParagraphStyle("cellh", fontName="Helvetica-Bold", fontSize=8.5, leading=10.5, alignment=1)
cellr = ParagraphStyle("cellr", fontName="Helvetica-Bold", fontSize=8.5, leading=10.5, alignment=0)
ghost = "<font color='#777777' size='7.5'>%s</font>"

def P(t, s=base): return Paragraph(wrapdv(t), s)
def O(t): return "<font color='#c45a00'>%s</font>" % t
def B(t): return "<font color='#0047ab'>%s</font>" % t
def R(t): return "<font color='#c8102e'>%s</font>" % t

def grid(headers, rows, colw=None):
    hdr = [P("<b>of →</b>", cellh)]
    for name, g in headers:
        hdr.append(P("<b>%s</b>%s" % (name, ("<br/>" + ghost % ("(%s)" % g)) if g else ""), cellh))
    data = [hdr]
    for lab, cells in rows:
        r = [P("<b>%s</b>" % lab, cellr)]
        for c in cells:
            if not c: r.append(P("", cell))
            elif isinstance(c, tuple):
                body, g = c
                r.append(P(body + (("<br/>" + ghost % ("(%s)" % g)) if g else ""), cell))
            else: r.append(P(c, cell))
        data.append(r)
    t = Table(data, colWidths=colw, repeatRows=1)
    t.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#bbbbbb")),
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#f1e7dd")),
        ("BACKGROUND", (0, 1), (0, -1), colors.HexColor("#f7f2ec")),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
    return t

def box(flow, light=False):
    t = Table([[flow]], colWidths=[doc.width])
    t.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.8 if light else 1.6, RED_LT if light else RED),
        ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6)]))
    return t

def D(sent, f): return KeepTogether([P("<b>%s%s</b>" % (sent, ":" if f else "."), defn)] + ([P(f + ".", formula)] if f else []))
def DC(coord, sent, f): return KeepTogether([P("<font color='#555555'>%s</font>&nbsp;&nbsp; <b>%s:</b>" % (coord, sent), defn), P(f + ".", formula)])

S = []
S.append(P("The straight dope", h1))
S.append(P("<b>Written by Claude (Anthropic), 2026-10-18 15:06.</b> The Straight→ Mechanics glossary and tables as they stand this afternoon, "
           "for Codex and for doc's reconciliation pass: straight-line mechanics first, then the turning vocabulary, the rules, the four "
           "tables and one definition per cell. Not doc's text; the ideas are his, the words are the model's, and the sentences in the "
           "definitions are the ones he has accepted in chat so far. Supersedes CL-093 (1354). Nothing here about electricity, flow or the rotor. "
           "<font color='#c8102e'>Red</font> Straight→ terms, <font color='#0047ab'>blue</font> textbook terms, "
           "No orange left: fling went into the glossary this afternoon.", small))

# ---------------- Part 1: straight mechanics ----------------
S.append(P("1. The straight line", h2))
S.append(P("Words that are already operators", h3))
S.append(P("Multiplication has four kinds of factor: <b>scale</b> (a bare number, can be negative), <b>type</b> (units), <b>direction</b>, "
           "and <b>body</b> (whose property). The English word for multiplication is <b>of</b> (four boxes of ten cookies), or <b>at</b> "
           "(28 studs at 4 nails per stud); the words for division are <b>per</b> and <b>over</b>. <b>And</b> adds. A direction follows "
           "the quantity it modifies (3 km north). The four directions of the cartoon universe are ↑ ↓ → ←, with → forward; two directions "
           "multiply to a number: 1 identical, 0 perpendicular, −1 opposite, the forwardness of the angle between them.", defn))
S.append(D("body (<b>B</b>)", "a model of an object holding only its physics-relevant properties; applying a symbol to a body gives that body's quantity, and the body stays in the product: <b>m</b> × <b>B</b> = 5 kg × <b>B</b>; <b>B</b> × <b>B</b> = <b>B</b>, <b>B</b> / <b>B</b> = <b>B</b>"))
S.append(D("ghost", "a body-like thing of no mass that appears to be somewhere: a laser dot, a projected image, a theoretical point"))
S.append(P("Quantities", h3))
S.append(D("mass (m): how much matter a body has", "m × <b>B</b>"))
S.append(D("speed (s): distance over time", "s = d / Δt"))
S.append(D("velocity (v): directed speed", "v = direction × speed"))
S.append(D("fluxion", "a directed rate of change over time; acceleration is the fluxion of velocity, velocity the fluxion of position"))
S.append(D("acceleration (a): the fluxion of velocity", "a = Δv / Δt"))
S.append(D("%s (p): the velocity of mass; the capacity to move other bodies (textbook %s; a unit, the %s, 1 o = 1 kg m/s)" % (R("motion"), B("momentum"), R("oompf")), "p = v × m"))
S.append(D("%s: the motion gained by a body over a span of time; the duration of a net force (standard)" % B("impulse"), "Δp = F × Δt"))
S.append(D("force (F): the fluxion of the motion; a push or pull adds motion over time (1 N = 1 oompf/s)", "F = Δp / Δt"))
S.append(D("weight: the gravitation of a body's mass, pulling down", "F<sub>g</sub> = g × m"))
S.append(D("gravitation (g): the free fall of bodies in a rest frame; Earth's is about 10 N↓/kg", "g = F<sub>g</sub> / m"))
S.append(D("%s: a force or moment applied across time; taken, not spent. Holding a load up takes effort and does no work" % R("effort"), "effort = F × Δt (a push) or M × Δt (a moment)"))
S.append(D("work (W): a force along a path", "W = F · Δx"))
S.append(D("power (P): the force of the velocity; the rate of work", "P = F · v"))
S.append(D("%s: the energy a body's motion stores, the measure of how dangerous it is (textbook %s); the velocity of added motion is stored as punch" % (R("punch"), B("kinetic energy")), "punch = ½ v · p"))
S.append(D("%s: the energy a collision spends, burns and waves away; what punch or hook delivers when it isn't %s. A spring catches punch and returns it; a generator catches it and hands it on; a climb catches it as %s (weight's stored energy, transformed)" % (R("kick"), R("caught"), R("heft")), "kick = punch before − punch after"))
S.append(D("stiffness: how hard a thing pushes back per how far you moved it. One word, three numbers, because a member is long one way: <b>along</b>, stretch it and it pulls back, force per length (coil springs; the spring maker's number); <b>across</b>, bend it and it pushes back, moment per bend (leaf springs, diving boards, beams; the structural engineer's number); <b>around</b>, twist it and it twists back, twist per stroke (torsion bars, mainsprings, drive shafts; the clockmaker's and the drivetrain engineer's number). Engineers say axial, bending, torsional", "F = stiffness × Δx"))
S.append(P("The laws", h3))
S.append(box(P("<b>Inertia:</b> a body can't change its own motion.<br/><b>Reaction:</b> bodies trade motion by pushing or pulling; the joint motion is conserved: "
               "Δp × <b>A</b> + Δp × <b>B</b> = 0.<br/><b>Force:</b> a push or pull adds motion over time: F = Δp / Δt.")))
S.append(P("Energy is transformed; work is performed; punch and hook are delivered, or land, or are caught; a spring returns what was put into it; "
           "fuel is burned; motion is traded or added over time; a force does work along a path (the body's path). Energy can be stored, spent, "
           "waved away, or burned. Effort is taken, never spent.", small))

# ---------------- Part 2: turning ----------------
S.append(P("2. Turning", h2))
S.append(P("Directions against an axis: <b>along</b> (the axis), <b>across</b> (the arm), <b>around</b> (the circle). The default sense of "
           "around is widdershins, counterclockwise seen from the tip of the axis arrow; the other way is sunwise, a negative sweep. "
           "On the page, rising ahead is ⤷ with its axis out of the page at the reader; it works the same with the book flat or on the wall.", defn))
S.append(P("Angles and actions", h3))
S.append(D("angle (θ): a difference between directions, as distance around the unit circle", ""))
S.append(D("swing (ψ): an action that continuously carries a direction through an angle; its amount keeps counting past a full turn", ""))
S.append(D("stroke (ζ): a swing of one unit (textbook %s)" % B("radian"), ""))
S.append(D("turn (τ): a swing of ~6.283 strokes, all the way round; flip (π): half a turn; quadrant (φ): half a flip", ""))
S.append(D("%s (ω): the rate of swing; how fast a direction is changing (textbook %s; unit: strokes per second)" % (R("sweep"), B("angular velocity")), "ω = Δψ / Δt"))
S.append(D("%s (α): the fluxion of sweep (textbook %s; unit: the %s, one sweep per second)" % (R("pickup"), B("angular acceleration"), R("whirl")), "α = Δω / Δt"))
S.append(P("Setups", h3))
S.append(D("%s: a body (or several) and an axis. A body is set up in a rotation. Quantities taken about an axis belong to setups" % R("setup"), ""))
S.append(D("%s (ι): a rigid arm that turns a force at its far end into a torque about the axis; a lever applies torque, transmits power and sweeps force" % R("lever"), ""))
S.append(D("%s (also ι): a lever that can't move; an arm does no work, carries a load and resists a moment" % R("arm"), ""))
S.append(D("radius (r): the length of a lever; distance from the axis", "r = |ι|"))
S.append(D("%s (ν): the rate at the lever's end; the sweep of the lever (textbook %s)" % (R("pace"), B("tangential velocity")), "ν = ω × ι"))
S.append(D("%s (λ): mass on an arm, out along the arm; what you have to do (textbook %s; the balancer's unbalance is a net lot)" % (R("lot"), B("first moment of mass")), "λ = ι × m"))
S.append(D("%s (β): your leverage on the lot; a scale about the axis with no direction, tied to the setup as mass is tied to a body (textbook %s; a body's bulk is each bit's lot levered, then added)" % (R("bulk"), B("moment of inertia")), "β = ι · λ = m r²"))
S.append(D("%s: the ghost of bulk, r²; %s, %s: the rate of bulk and its negative (body); %s, %s: the same for a ghost" % (R("bulkiness"), R("spread"), R("tuck"), R("splay"), R("fold")), "spread = Δβ / Δt"))
S.append(D("%s (p): a set-up body's motion; the sweep of the lot, the pace of the mass" % R("movement"), "p = ω × λ = ν × m"))
S.append(D("%s (ξ): the leverage of the movement; the sweep of the bulk; the lot at pace (textbook %s, orbital included; unit: the %s, 1 kg m²/s)" % (R("spin"), B("angular momentum"), R("roll")), "ξ = ι × p = ω × β = λ × ν"))
S.append(D("%s: the ghost of spin, the lever at pace; what an orbit does around its primary (textbook %s)" % (R("swirl"), B("specific angular momentum")), "swirl = ι × ν"))
S.append(P("Forces on a setup", h3))
S.append(D("%s (χ): the leverage of a force, about the axis the setup is free on; a moment that can do work (textbook %s)" % (R("torque"), B("torque")), "χ = ι × F"))
S.append(D("%s (M): the leverage of a force across an arm; crossed up and locked out, it can't do work (engineers' %s)" % (R("moment"), B("bending moment, load moment")), "M = ι × F"))
S.append(D("%s: the leverage of a force along the arm, torsion; no symbol" % R("twist"), ""))
S.append(D("%s: the ghost of torque, the leverage of an acceleration" % R("twirl"), "twirl = ι × a"))
S.append(D("%s (F⊙): the sweep of the movement; the force that keeps a body on center (textbook %s; a textbook %s is any force aimed at a center)" % (R("center force"), B("centripetal"), B("central force")), "F⊙ = ω × p"))
S.append(D("%s: the tendency of a turning body to go straight when the center force lets go; a verb, not a second force (textbook %s). A rock on a string gets flung around and out" % (R("fling"), B("centrifugal")), ""))
S.append(D("%s: the duration of a net torque; the spin it adds" % R("boost"), "Δξ = χ × Δt"))
S.append(D("%s: the fluxion of the force (ghost: jerk); %s: the pickup of the movement, the growing part of the yank" % (R("yank"), R("yerk")), "yank = ΔF / Δt;  yerk = α × p"))
S.append(D("%s: the duration of the movement, mass times displacement; what moves a centre of mass (naval architects' weight shift)" % R("shift"), "shift = p × Δt"))
S.append(D("%s: the swing of the lot, mass along the arc; keeps counting past a turn, like distance (merchants' goods in transit)" % R("transit"), "transit = ψ × λ"))
S.append(P("Work and energy, turning", h3))
S.append(D("work: a torque through a swing", "W = ψ · χ"))
S.append(D("%s: a unit of work, one stroke of torque; the trundle rate is the power" % R("trundle"), "1 trundle = ζ χ"))
S.append(D("power: the sweep of the torque; the same number as the force of the pace", "P = ω · χ = F · ν"))
S.append(D("%s: the turning punch, the energy a spin stores (textbook %s); the sweep of added spin is stored as hook" % (R("hook"), B("rotational kinetic energy")), "hook = ½ ω · ξ"))
S.append(D("action: the movement along the whole path; the spin through the whole swing (standard)", "action = p · path = ξ · ψ"))
S.append(D("the ghosts of punch, hook, power, work and action: %s, %s, %s, %s, %s, each the body quantity per mass; kept in their own table" % (R("zip"), R("zing"), R("zow"), R("zug"), R("zam")), "zip = ½ ν · ν"))

# ---------------- Part 3: rules ----------------
S.append(P("3. The rules the tables run on", h2))
S.append(box(P("<b>“Of” is the ordinary genitive, not an operator.</b> The product is whichever the two kinds of object take: two axis arrows dot, "
               "an axis arrow and a lever cross, a scale just scales. <b>Two multiplication words, two orders:</b> “of” leads with the operator "
               "(the sweep of the lot, ω × λ); “at” leads with the thing (the lot at pace, λ × ν). A backward-order cell goes in a table with its "
               "minus sign; the running text uses the sentence that comes out positive.")))
S.append(Spacer(1, 4))
S.append(box(P("<b>Rows are actions and rates; columns are things a setup has.</b> Duration and rate are rows, not columns. Scalars (time, mass) take no "
               "column width: mass is carried by the ghost printed under each body cell, the same quantity with the mass out. The ghost of the lot "
               "is the leverage; the ghost of the movement is the pace.")))
S.append(Spacer(1, 4))
S.append(box(P("<b>A product cell holds the other factor stable.</b> Torque is the pickup of <i>stable</i> bulk; let the bulk change and the rate of spin "
               "picks up a second term, the sweep of the spread, so with no torque the pickup of the bulk equals the sweep of the tuck (the skater). "
               "Yerk is the growing part of the yank; the center force also turns. The fluxion cells in the rate row carry the whole; the product cells carry one term.")))
S.append(Spacer(1, 4))
S.append(box(P("<b>Words mean what they mean or they can't do what they do.</b> Effort is taken; energy is spent. A body's own quantities take “the” "
               "(the lot, the bulk, the movement, the spin); an applied force or torque takes “a”. One name per thing. Operators first: if a trade "
               "already has the word, it wins (shift, transit, unbalance, slew, load moment).")))

# ---------------- Part 4: tables ----------------
S.append(P("4. The tables", h2))
S.append(P("Row number plus column letter names a cell; each filled cell has a definition in section 5. Ghost versions in grey beneath.", small))
S.append(KeepTogether([P("Table 1 — the setup's starting pieces", h3),
    grid([("a  lever ι", None), ("b  mass m", None), ("c  lot λ", None)],
    [("1 rate of", ["pace", "", "movement"]),
     ("2 swing of", ["arc", "", "transit"]),
     ("3 sweep of", ["pace", "", "movement"]),
     ("4 pickup of", ["acceleration around", "", "force around"]),
     ("5 leverage of", ["bulkiness", "lot", "bulk"]),
     ("6 pace of", ["−swirl", "movement", "−spin"])],
    colw=[1.1*inch, 1.6*inch, 1.3*inch, 1.5*inch])]))
S.append(P("The lot column is the lever column with the mass in it; the mass column is the two seams. Row 6's minus signs are the backward "
           "order; the text says “the lever at pace” (swirl) and “the lot at pace” (spin).", small))
S.append(KeepTogether([P("Table 2 — the motion ledger", h3),
    grid([("a  lot λ", "leverage ι"), ("b  bulk β", "bulkiness r²"), ("c  movement p", "pace ν"),
          ("d  force F", "accel. a"), ("e  torque χ", "twirl"), ("f  spin ξ", "swirl")],
    [("1 duration of", ["", "", ("shift", "displacement"), ("impulse = Δmovement", "Δpace"), ("boost = Δspin", "Δswirl"), ""]),
     ("2 rate of", [("movement", "pace"), ("spread", "splay"), ("force", "accel. a"), ("yank", "jerk"), "", ("torque", "twirl")]),
     ("3 swing of", [("transit", "arc"), "", "", "", "", ""]),
     ("4 sweep of", [("movement", "pace"), ("spin", "swirl"), ("center force", "center accel."), "", "", ""]),
     ("5 pickup of", [("force around", "accel. around"), ("torque, stable bulk", "twirl"), ("yerk", "ghost yerk"), "", "", ""]),
     ("6 leverage of", [("bulk", "bulkiness"), "", ("spin", "swirl"), ("torque; moment if an arm", "twirl"), "", ""])],
    colw=[1.0*inch] + [0.95*inch]*6)]))
S.append(P("Empty cells are empty on purpose: the leverage of bulk is m r³ along the arm and nothing is measured in it; the arm enters a "
           "quantity exactly twice. Torque; moment if an arm is the crane: slew brake off, torque; brake on, moment.", small))
S.append(KeepTogether([P("Table 3 — the energy ledger (every cell a dot)", h3),
    grid([("a  movement p", None), ("b  force F", None), ("c  torque χ", None), ("d  spin ξ", None)],
    [("1 path of", ["action", "work", "", ""]),
     ("2 swing of", ["", "", "work", "action"]),
     ("3 pace of", ["2·punch", "power", "", ""]),
     ("4 sweep of", ["", "", "power", "2·hook"])],
    colw=[1.0*inch, 1.3*inch, 1.3*inch, 1.3*inch, 1.3*inch])]))
S.append(KeepTogether([P("Table 3-g — the same with the mass out, for the unafraid", h3),
    grid([("a  pace ν", None), ("b  accel. a", None), ("c  twirl", None), ("d  swirl", None)],
    [("1 path of", ["zam", "zug", "", ""]),
     ("2 swing of", ["", "", "zug", "zam"]),
     ("3 pace of", ["2·zip", "zow", "", ""]),
     ("4 sweep of", ["", "", "zow", "2·zing"])],
    colw=[1.0*inch, 1.3*inch, 1.3*inch, 1.3*inch, 1.3*inch])]))

# ---------------- Part 5: defs per cell ----------------
S.append(P("5. One definition per filled cell", h2))
defs = [
 ("T1 1a", "pace (ν): the rate at the lever's end", "ν = Δι / Δt"),
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
 ("T2 1c", "shift: the movement carried over time", "shift = p × Δt"),
 ("T2 1d", "impulse (Δp): the duration of a net force; the movement it adds (standard word)", "Δp = F × Δt"),
 ("T2 1e", "boost (Δξ): the duration of a net torque; the spin it adds", "Δξ = χ × Δt"),
 ("T2 2a", "movement (p): the rate of the lot", "p = Δλ / Δt"),
 ("T2 2b", "spread: the increase of the bulk", "spread = Δβ / Δt"),
 ("T2 2c", "force (F): the fluxion of the movement; a push or pull adds movement over time", "F = Δp / Δt"),
 ("T2 2d", "yank: the fluxion of the force", "yank = ΔF / Δt"),
 ("T2 2f", "torque (χ): the fluxion of the spin; a torque adds spin over time", "χ = Δξ / Δt"),
 ("T2 3a", "transit: the swing of the lot", "transit = ψ × λ"),
 ("T2 4a", "movement (p): the sweep of the lot", "p = ω × λ"),
 ("T2 4b", "spin (ξ): the sweep of the bulk", "ξ = ω × β"),
 ("T2 4c", "center force (F⊙): the sweep of the movement; the force that keeps it on center", "F⊙ = ω × p"),
 ("T2 5a", "force around (F): the pickup of the lot", "F = α × λ"),
 ("T2 5b", "torque (χ): the pickup of stable bulk", "χ = α × β"),
 ("T2 5c", "yerk: the pickup of the movement", "yerk = α × p"),
 ("T2 6a", "bulk (β): the leverage of the lot", "β = ι × λ"),
 ("T2 6c", "spin (ξ): the leverage of the movement", "ξ = ι × p"),
 ("T2 6d", "torque (χ): the leverage of a force", "χ = ι × F"),
 ("T2 6d′", "moment (M): the leverage of a force across an arm", "M = ι × F"),
 ("T3 1a", "action: the movement along the path", "action = p · path"),
 ("T3 1b", "work (W): a force along a path", "W = F · path"),
 ("T3 2c", "work (W): a torque through a swing", "W = ψ · χ"),
 ("T3 2d", "action: the spin through the swing", "action = ξ · ψ"),
 ("T3 3a", "punch: half the movement at pace", "punch = ½ ν · p"),
 ("T3 3b", "power (P): the force of the pace", "P = F · ν"),
 ("T3 4c", "power (P): the sweep of the torque", "P = ω · χ"),
 ("T3 4d", "hook: half the sweep of the spin", "hook = ½ ω · ξ"),
]
for c, s_, f in defs: S.append(DC(c, s_, f))

# ---------------- Part 6: contradictions ----------------
S.append(P("6. Where this contradicts the textbook, not just renames it", h2))
S.append(P("• <b>Torque on a balanced beam.</b> The physics book sums “torques about the pivot” for a beam going nowhere; here those are moments. "
           "Engineers already say moments there.", defn))
S.append(P("• <b>Spin.</b> The textbook splits angular momentum into spin (about a body's own axis) and orbital; here spin is the leverage of the "
           "movement about whatever axis the setup has, so a train on a track has spin.", defn))
S.append(P("• <b>Center force</b> is the textbook's centripetal force; the textbook's “central force” (any force aimed at a center) keeps its own meaning.", defn))
S.append(P("Everything else is a new word for an old thing or the same word for the same thing.", defn))

S.append(P("7. Changed since 1354", h2))
S.append(P("Codex's four catches, all of one kind, a product cell standing in for a whole it only partly covered: (1) a body's bulk is each bit's lot "
           "levered, then added; (2) torque is the pickup of <i>stable</i> bulk; (3) yank is the whole fluxion of the force, yerk the pickup part; "
           "(4) shift (displacement) and transit (arc) are different after one full turn. Also: roll is the unit of spin (Fred retired again); "
           "pace is “the rate at the lever's end”; the third rule box is new.", defn))

doc.build(S)
print(OUT)
