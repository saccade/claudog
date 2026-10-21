#!/usr/bin/env python3
# Builds "Claude The Straight Dope <STAMP>.pdf"; current: 2610191409 (CL-135, text only). Written by Claude (Anthropic).
import re
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                KeepTogether, PageBreak)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

STAMP = "2610191640"
OUT = "/home/claude/out/Claude The Straight Dope %s.pdf" % STAMP

# tiny DejaVu subset for Greek and symbols; Helvetica for everything else
SRC = open(__file__, encoding="utf-8").read()
CH = "".join(sorted(set(c for c in SRC if ord(c) > 127)))
open("/home/claude/out/chars3.txt", "w").write(CH)
import subprocess
subprocess.run(["pyftsubset", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
                "--text-file=/home/claude/out/chars3.txt", "--no-hinting", "--desubroutinize",
                "--output-file=/home/claude/out/dv_sub3.ttf", "--layout-features=",
                "--name-IDs=1,2,3,4,6", "--drop-tables+=FFTM,GSUB,GPOS,GDEF"], check=True,
               stderr=subprocess.DEVNULL)
pdfmetrics.registerFont(TTFont("DV", "/home/claude/out/dv_sub3.ttf"))
# DejaVu Sans has no U+2937 (the widdershins arrow); DejaVu Serif does
open("/home/claude/out/chars_arrow.txt", "w").write("\u2937")
subprocess.run(["pyftsubset", "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
                "--text-file=/home/claude/out/chars_arrow.txt", "--no-hinting", "--desubroutinize",
                "--output-file=/home/claude/out/dvs_arrow.ttf", "--layout-features=",
                "--name-IDs=1,2,3,4,6", "--drop-tables+=FFTM,GSUB,GPOS,GDEF"], check=True,
               stderr=subprocess.DEVNULL)
pdfmetrics.registerFont(TTFont("DVS", "/home/claude/out/dvs_arrow.ttf"))
_tag = re.compile(r"(<[^>]*>)")
_na = re.compile(r"([^\x00-\x7f]+)")
def wrapdv(t):
    out = []
    for part in _tag.split(t):
        if part.startswith("<"): out.append(part); continue
        part = _na.sub(r'<font name="DV">\1</font>', part)
        out.append(part.replace("\u2937", '</font><font name="DVS">\u2937</font><font name="DV">'))
    return "".join(out)

BROWN = colors.HexColor("#6b3a1e"); RED = colors.HexColor("#c8102e"); RED_LT = colors.HexColor("#e06070")
BLUE = colors.HexColor("#0047ab"); GREY = colors.HexColor("#555555")

doc = SimpleDocTemplate(OUT, pagesize=letter, leftMargin=0.9*inch, rightMargin=0.9*inch,
                        topMargin=0.7*inch, bottomMargin=0.7*inch,
                        title="The straight dope: Straight-> Mechanics glossary and tables", author="Claude (Anthropic)")
base = ParagraphStyle("base", fontName="Helvetica", fontSize=10, leading=13.5)
small = ParagraphStyle("small", parent=base, fontSize=8.5, leading=11, textColor=GREY)
h1 = ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=20, leading=24, textColor=BROWN, spaceAfter=4)
h2 = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=13, leading=16, textColor=BROWN, spaceBefore=12, spaceAfter=5, keepWithNext=1)
h3 = ParagraphStyle("h3", fontName="Helvetica-Bold", fontSize=10.5, leading=13, textColor=BROWN, spaceBefore=8, spaceAfter=2, keepWithNext=1)
defn = ParagraphStyle("defn", parent=base, leftIndent=14, spaceBefore=3)
formula = ParagraphStyle("formula", parent=base, leftIndent=36, spaceAfter=2)
cell = ParagraphStyle("cell", fontName="Helvetica", fontSize=8.5, leading=10.5, alignment=1)
cellh = ParagraphStyle("cellh", fontName="Helvetica-Bold", fontSize=8.5, leading=10.5, alignment=1)
cellr = ParagraphStyle("cellr", fontName="Helvetica-Bold", fontSize=8.5, leading=10.5, alignment=0)
ghost = "<font color='#777777' size='7.5'>%s</font>"

def P(t, s=base): return Paragraph(wrapdv(t), s)
def B(t): return "<font color='#0047ab'>%s</font>" % t
def R(t): return "<font color='#c8102e'>%s</font>" % t

def grid(headers, rows, colw=None, corner="of →"):
    hdr = [P("<b>%s</b>" % corner, cellh)]
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
coordc = ParagraphStyle("coordc", parent=base, textColor=GREY, alignment=2)
deft = ParagraphStyle("deft", parent=base)
formt = ParagraphStyle("formt", parent=base, leftIndent=22)
def DC(coord, sent, f):
    # coordinate in a fixed-width gutter so the definitions share one left margin
    t = Table([[P(coord, coordc), P("<b>%s:</b>" % sent, deft)], ["", P(f + ".", formt)]],
              colWidths=[0.42*inch, doc.width - 0.42*inch])
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (0, -1), 8),
        ("TOPPADDING", (0, 0), (-1, 0), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 1)]))
    return KeepTogether([t])

S = []
S.append(P("The straight dope", h1))
S.append(P("<b>Written by Claude (Anthropic), 2026-10-19 16:40.</b> The Straight→ Mechanics glossary and tables as they stand today, "
           "for Codex and for doc's reconciliation pass: straight-line mechanics first, then the turning vocabulary, the rules, the five "
           "tables on one coordinate scheme (rows 1–17, columns a–u) and one definition per filled cell. Not doc's text; the ideas are his, "
           "the words are the model's, and the sentences in the definitions are the ones he has accepted in chat so far. "
           "Nothing here about electricity, flow or the rotor. "
           "<font color='#c8102e'>Red</font> Straight→ terms, <font color='#0047ab'>blue</font> textbook terms.", small))

# ---------------- Part 1: straight mechanics ----------------
S.append(P("1. The straight line", h2))
S.append(P("Words that are already operators", h3))
S.append(P("Multiplication has four kinds of factor: <b>scale</b> (a bare number, can be negative), <b>type</b> (units), <b>direction</b>, "
           "and <b>body</b> (whose property). The English word for multiplication is <b>of</b> (four boxes of ten cookies), or <b>at</b> "
           "(28 studs at 4 nails per stud); the words for division are <b>per</b> and <b>over</b>. <b>And</b> adds. A direction follows "
           "the quantity it modifies (3 km north). The four directions of the cartoon universe are ↑ ↓ → ←, with → forward; two directions "
           "multiply to a number: 1 identical, 0 perpendicular, −1 opposite, the forwardness of the angle between them.", defn))
S.append(D("body", "a model of an object holding only its physics-relevant properties. Any letter can name a body: take apple <b>A</b>, and <b>A</b> is a body. Applying a symbol to a body gives that body's quantity, and the body stays in the product: <b>m</b> × <b>A</b> = 5 kg × <b>A</b>; <b>A</b> × <b>A</b> = <b>A</b>, <b>A</b> / <b>A</b> = <b>A</b>"))
S.append(D("ghost", "a body-like thing of no mass that appears to be somewhere: a laser dot, a projected image, a theoretical point"))
S.append(P("Quantities", h3))
S.append(D("mass (m): how much matter a body has; the mass of apple A", "m × <b>A</b>"))
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
S.append(D("work (W): a force along a path, added up step by step", "W = Σ F · Δx"))
S.append(D("power (P): the velocity of force; the rate of work", "P = v · F"))
S.append(D("%s: the energy a body's motion stores, the measure of how dangerous it is (textbook %s); the velocity of added motion is stored as punch" % (R("punch"), B("kinetic energy from linear motion")), "punch = ½ v · p"))
S.append(D("%s: the energy a collision spends, burns and waves away; what punch or hook delivers when it isn't %s. A spring catches punch and returns it; a generator catches it and hands it on; a climb catches it as %s (weight's stored energy, transformed)" % (R("kick"), R("caught"), R("heft")), "kick = every body's punch and hook before − after − what was caught, each energy counted once"))
S.append(D("stiffness: how hard a thing pushes back per how far you moved it. One word, three numbers, because a member is long one way: <b>along</b>, stretch it and it pulls back, force per length (coil springs; the spring maker's number); <b>across</b>, bend it and it pushes back, moment per bend (leaf springs, diving boards, beams; the structural engineer's number); <b>around</b>, twist it and it twists back, twist per stroke (torsion bars, mainsprings, drive shafts; the clockmaker's and the drivetrain engineer's number). Engineers say axial, bending, torsional", "F = stiffness × Δx"))
S.append(P("The laws", h3))
S.append(box(P("<b>Inertia:</b> a body can't change its own motion.<br/><b>Reaction:</b> bodies trade motion by pushing or pulling; the joint motion is conserved: "
               "Δp × <b>A</b> + Δp × <b>B</b> = 0.<br/><b>Force:</b> a push or pull adds motion over time: F = Δp / Δt.")))
S.append(P("Energy is transformed; work is performed; punch and hook are delivered, or land, or are caught; a spring returns what was put into it; "
           "fuel is burned; motion is traded or added over time; a force does work along a path (the body's path). Energy can be stored, spent, "
           "waved away, or burned. Effort is taken, never spent.", small))

# ---------------- Part 2: turning ----------------
S.append(P("2. Turning", h2))
S.append(P("Directions against an axis: <b>along</b> (the axis), <b>across</b> (the arm), <b>around</b> (the circle). The default sense is "
           "<b>forward around</b>: widdershins, counterclockwise seen from the tip of the axis arrow, and from here on just around; the other way is <b>backward around</b>, sunwise, a negative sweep, never shortened to around but back around for short. "
           "On the page, rising ahead is ⤷ with its axis out of the page at the reader; it works the same with the book flat or on the wall.", defn))
S.append(P("Angles and actions", h3))
S.append(D("angle (θ): a difference between directions, as distance around the unit circle", ""))
S.append(D("forwardness and upwardness: how much of a direction is forward, or up; what fraction of a forward or an up it is worth (textbook %s and %s)" % (B("cosine"), B("sine")), "→ · θ = θ / →;  ↑ · θ = θ / ↑"))
S.append(D("the heft of a bulk: the bulk under gravitation, as many ups as its direction is worth; with β the bulk's size and θ its direction", "U = g β (↑ · θ) = g β (θ / ↑)"))
S.append(D("a direction is its forward part plus its up part. Its reflex is one, since a direction is one long; forward and up are square to each other, so the cross terms drop out and the reflex is the reflexes of the two parts", "θ = (θ / →) → + (θ / ↑) ↑<br/>1 = θ · θ = (θ / →)² + (θ / ↑)²"))
S.append(D("swing (ψ): an action that continuously carries a direction through an angle; its amount keeps counting past a full turn", ""))
S.append(D("stroke (ζ): a swing of one unit (textbook %s)" % B("radian"), ""))
S.append(D("turn (τ): a swing of ~6.283 stroke, all the way round; flip (π): half a turn; quadrant (φ): half a flip", ""))
S.append(D("%s (ω): the rate of swing; how fast a direction is changing (textbook %s; unit: the %s, one stroke per second)" % (R("sweep"), B("angular velocity"), R("sweep")), "ω = Δψ / Δt"))
S.append(D("%s (α): the fluxion of sweep (textbook %s; unit: the %s, one sweep per second)" % (R("pickup"), B("angular acceleration"), R("whirl")), "α = Δω / Δt"))
S.append(P("Setups", h3))
S.append(D("%s: a body (or several) and an axis. A body is set up in a rotation. Quantities taken about an axis belong to setups" % R("setup"), ""))
S.append(D("%s (ι): a rigid arm that turns a force at its far end into a torque about the axis; a lever applies torque, transmits power and sweeps force" % R("lever"), ""))
S.append(D("%s (also ι): a lever that can't move; an arm does no work, carries a load and resists a moment" % R("arm"), ""))
S.append(D("radius (r): the length of a lever; distance from the axis", "r = |ι|"))
S.append(D("%s: the part of a lever that runs across the member; the part along it is the reach. A load on the member's own line has no offset" % R("offset"), "ι = reach + offset"))
S.append(D("%s: a thing's product with itself; out to the end, turn, and back. The reflex of the lever is r²; the reflex of the sweep on the bulk is the center force; the diagonal cells of the energy tables are reflexes, and the energy stored is half the reflex (under Table 3-g)" % R("reflex"), "reflex of x = x · x  or  x × x"))
S.append(D("the closure: going out, the sweep of the lever gives pace; acting there, the mass at that pace gives movement; coming back, the leverage of that movement gives spin. The same arm appears twice because it does two jobs: taking the sweep out to the moving mass, then bringing the movement back into spin about the axis. The two crosses are two quarter turns, and they land back on the axis, facing the way the sweep faced; reverse either and the spin lands backward, the minus sign of Table 1. Take the mass away and what is left of the trip is the profile. This closure uses the lever square to the axis; general three-dimensional rotation is outside the scope here", "ξ = ι × (m (ω × ι)) = m r² ω"))
S.append(D("%s (ν): the rate at the lever's end; the sweep of the lever (textbook %s)" % (R("pace"), B("tangential velocity")), "ν = ω × ι"))
S.append(D("%s (β): the leverage of the mass; mass on an arm, out along the arm; what you have to do (textbook %s; unit: the %s, 1 kg m, a ponderous bulk). A body's bulk is each bit's bulk, added; a balanced wheel's add to nothing, and the balancer's unbalance is a net bulk" % (R("bulk"), B("first moment of mass"), R("ponder")), "β = ι × m"))
S.append(D("%s (η): the leverage of the bulk; your leverage on what you have to do. A scale about the axis with no direction, tied to the setup as mass is tied to a body (textbook %s, the book's own second name for it; unit: the %s, 1 kg m²; a millstone has a few hundred of them). A body's inertia: lever each bit's bulk, then add. The first law stays the law of inertia, as in the textbook" % (R("inertia"), B("rotational inertia, moment of inertia"), R("wheel")), "η = ι · β = m r²"))
S.append(D("%s: the ghost of inertia, inertia per mass; how the mass is laid out about the axis, whatever it weighs. For a point it is the reflex of the lever, r²; for a body, each bit's reflex averaged over the mass (textbook: the square of the %s; a hoop R², a disc ½ R², a rod about its end ⅓ L²; dog math: the card, one square hand). %s, %s: the rate of inertia and its negative (body); %s, %s: the same for a ghost" % (R("profile"), B("radius of gyration"), R("spread"), R("tuck"), R("splay"), R("fold")), "spread = Δη / Δt"))
S.append(D("%s (p): a set-up body's motion; the sweep of the bulk, the pace of the mass" % R("movement"), "p = ω × β = ν × m"))
S.append(D("%s (ξ): the leverage of the movement; the sweep of the inertia; the bulk at pace (textbook %s, orbital included; unit: the %s, 1 kg m²/s)" % (R("spin"), B("angular momentum"), R("roll")), "ξ = ι × p = ω × η = β × ν"))
S.append(D("%s: the ghost of spin, the lever at pace; what an orbit does around its primary (textbook %s)" % (R("swirl"), B("specific angular momentum")), "swirl = ι × ν"))
S.append(P("Forces on a setup", h3))
S.append(D("%s (χ): the leverage of a force, about the axis the setup is free on; a moment that can do work (textbook %s)" % (R("torque"), B("torque")), "χ = ι × F"))
S.append(D("%s (M): the leverage of a force across an arm; crossed up and locked out, it does no work around the axle; a springy arm takes work through its bend, around the moment's own axis (engineers' %s). The bulk under gravitation is the load moment" % (R("moment"), B("bending moment, load moment")), "M = ι × F"))
S.append(D("%s: the leverage of a force through the offset, about the member's own line; torsion. A crane's jib twists only when the load hangs off its line; a wrench on a shaft is all offset; no symbol" % R("twist"), ""))
S.append(D("%s: the ghost of torque, the leverage of an acceleration" % R("twirl"), "twirl = ι × a"))
S.append(D("%s (F⊙): the sweep of the movement; the force that keeps a body on center (textbook %s; a textbook %s is any force aimed at a center)" % (R("center force"), B("centripetal"), B("central force")), "F⊙ = ω × p"))
S.append(D("%s: the tendency of a turning body to go straight when the center force lets go; a verb, not a second force (textbook %s). A rock on a string gets flung around and out" % (R("fling"), B("centrifugal")), ""))
S.append(D("%s: the duration of a net torque; the spin it adds" % R("boost"), "Δξ = χ × Δt"))
S.append(D("%s: the fluxion of the force (ghost: jerk); %s: the pickup of the movement, the growing part of the yank" % (R("yank"), R("yerk")), "yank = ΔF / Δt;  yerk = α × p"))
S.append(D("%s: the duration of the movement, mass times displacement; what moves a centre of mass (naval architects' weight shift). Steady movement only; a turning body's shift adds up step by step" % R("shift"), "Δshift = p × Δt"))
S.append(D("%s: the swing of the bulk, mass along the arc; keeps counting past a turn, like distance (merchants' goods in transit)" % R("transit"), "transit = ψ m r"))
S.append(P("Work and energy, turning", h3))
S.append(D("work: a torque through a swing", "W = ψ · χ"))
S.append(D("%s: a setup's work per stroke, the work it takes to swing the setup through one stroke. At a steady torque, work counted in the setup's trundles is the swing counted in strokes, which is why a newton-metre of torque is a joule per stroke. The sweep of the trundle is the power (work per stroke times strokes per second)" % R("trundle"), "trundle = ζ · χ;  W / trundle = ψ / ζ"))
S.append(D("power: the sweep of the torque; the same number as the pace of the force", "P = ω · χ = ν · F"))
S.append(D("%s: the turning punch, the energy a spin stores (textbook %s); the sweep of added spin is stored as hook. The sweep of the spin is the reflected hook, twice the hook. A body set up about an axis has one energy, counted as hook about the axis or as punch on its own path, never both: a train on a circular track. They add only when the spin is about the body's own centre: a rolling wheel has the punch of its centre and the hook about it, the same as its hook about the contact point. Hook is the zing of the inertia; at constant spin, the power into hook is the zing of the tuck" % (R("hook"), B("rotational kinetic energy")), "hook = ½ ω · ξ"))
S.append(D("action: the movement along the whole path; the spin through the whole swing (standard: the abbreviated action, not the time sum of the Lagrangian); it adds up step by step, so it builds all the way around a closed circle", "action = Σ p · Δx = ξ · ψ (steady spin)"))
S.append(D("the ghosts of punch, hook, power, work and action: %s, %s, %s, %s, %s, each the energy per mass for straight motion and per inertia for turning; kept in their own table. Every quantity has a one-word unit: its own name unless one exists (1 zip, 1 zing, 1 shift, 1 swirl; a ponder of bulk, a wheel of inertia, a roll of spin)" % (R("zip"), R("zing"), R("zow"), R("zug"), R("zam")), "zip = ½ v · v;  zing = ½ ω · ω"))

# ---------------- Part 3: rules ----------------
S.append(P("3. The rules the tables run on", h2))
S.append(box(P("<b>“Of” is the ordinary genitive, not an operator.</b> The product is whichever the two kinds of object take: two axis arrows dot, "
               "an axis arrow and a lever cross, a scale just scales. <b>Two multiplication words, two orders:</b> “of” leads with the operator "
               "(the sweep of the bulk, ω × β); “at” leads with the thing (the bulk at pace, β × ν). A backward-order cell goes in a table with its "
               "minus sign; the running text uses the sentence that comes out positive. The bulk sits between: operators lead it, things follow it.")))
S.append(Spacer(1, 4))
S.append(box(P("<b>Rows are actions and rates; columns are things a setup has.</b> Duration and rate are rows, not columns. Scalars (time, mass) take no "
               "column width: mass is carried by the ghost printed under each body cell, the same quantity with the mass out. The ghost of the bulk "
               "is the lever; the ghost of the movement is the pace; the ghost of the inertia is the profile. The five tables share one coordinate scheme, "
               "rows 1–17 and columns a–u, so a cell's address needs no table number.")))
S.append(Spacer(1, 4))
S.append(box(P("<b>A product cell holds the other factor stable.</b> Torque is the pickup of <i>stable</i> inertia; let the inertia change and the rate of spin "
               "picks up a second term, the sweep of the spread, so with no torque the pickup of the inertia equals the sweep of the tuck (the skater). "
               "Yerk is the growing part of the yank; the center force also turns. The fluxion cells in the rate row carry the whole; the product cells carry one term.")))
S.append(Spacer(1, 4))
S.append(box(P("<b>Lever each bit, then add.</b> Inertia, spin and torque are taken bit by bit and then added; never lever a bulk or a movement that is already a sum. "
               "A balanced wheel's bulks and movements add to nothing while its inertia and spin are whole. "
               "<b>A finite swing turns the lever.</b> Products along the axis (swing, sweep, torque, spin) hold through a whole swing while they are steady: work and action through a swing. "
               "Products through the lever's direction (lever, bulk, movement) hold moment to moment only: arc, transit and shift add up step by step. "
               "<b>Path products add up step by step:</b> work is the force along each step, action the movement along each step, exact as the steps get small.")))
S.append(Spacer(1, 4))
S.append(box(P("<b>Words mean what they mean or they can't do what they do.</b> Effort is taken; energy is spent. A body's own quantities take “the” "
               "(the bulk, the inertia, the movement, the spin); an applied force or torque takes “a”. One name per thing, and every quantity "
               "has a one-word unit: its own name unless one already exists (roll, whirl, ponder, wheel, oompf). No new words here, only old ones assigned to quantities that were always there. Operators first: if a trade "
               "already has the word, it wins (shift, transit, unbalance, slew, load moment).")))

# ---------------- Part 4: tables ----------------
S.append(PageBreak())
S.append(P("4. The tables", h2))
S.append(P("Row number plus column letter names a cell; each filled cell has a definition in section 5. Ghost versions in grey beneath. "
           "The diagonal is the reflex: always a dot, out and back.", small))
S.append(KeepTogether([P("Table 1 — the setup's starting pieces (rows 1–6, columns a–c)", h3),
    grid([("a  lever ι", None), ("b  mass m", None), ("c  bulk β", None)],
    [("1 rate of", ["pace", "", "movement"]),
     ("2 swing of", ["arc", "", "transit"]),
     ("3 sweep of", ["pace", "", "movement"]),
     ("4 pickup of", ["acceleration around", "", "force around"]),
     ("5 leverage of", ["profile (reflex)", "bulk", "inertia"]),
     ("6 pace of", ["−swirl", "movement", "−spin"])],
    colw=[1.1*inch, 1.6*inch, 1.3*inch, 1.5*inch]), P("The bulk column is the lever column with the mass in it; the mass column is the two seams. Row 5a and 5c are reflexes (the lever "
           "twice), so they dot. Row 6's minus signs are the backward order; the text says “the lever at pace” (swirl) and “the bulk at pace” (spin).", small)]))

S.append(KeepTogether([P("Table 2 — the motion ledger (rows 7–12, columns d–i)", h3),
    grid([("d  bulk β", "lever ι"), ("e  inertia η", "profile"), ("f  movement p", "pace ν"),
          ("g  force F", "accel. a"), ("h  torque χ", "twirl"), ("i  spin ξ", "swirl")],
    [("7 duration of", ["", "", ("shift", "displacement"), ("impulse = Δmovement", "Δpace"), ("boost = Δspin", "Δswirl"), ""]),
     ("8 rate of", [("movement", "pace"), ("spread", "splay"), ("force", "accel. a"), ("yank", "jerk"), "", ("torque", "twirl")]),
     ("9 swing of", [("transit", "arc"), "", "", "", "", ""]),
     ("10 sweep of", [("movement", "pace"), ("spin", "swirl"), ("center force", "center accel."), "", "", ""]),
     ("11 pickup of", [("force around", "accel. around"), ("torque, stable inertia", "twirl"), ("yerk", "ghost yerk"), "", "", ""]),
     ("12 leverage of", [("inertia", "profile"), "", ("spin", "swirl"), ("torque; moment if an arm", "twirl"), "", ""])],
    colw=[1.0*inch] + [0.95*inch]*6)]))
S.append(P("Empty cells are empty on purpose: the leverage of inertia is m r³ along the arm and nothing is measured in it; the arm enters a "
           "quantity exactly twice. Torque; moment if an arm is the crane: slew brake off, torque; brake on, moment.", small))
S.append(KeepTogether([P("Table 3 — the energy ledger (rows 13–16, columns j–m; every cell a dot)", h3),
    grid([("j  movement p", None), ("k  force F", None), ("l  torque χ", None), ("m  spin ξ", None)],
    [("13 path of", ["action", "work", "", ""]),
     ("14 swing of", ["", "", "work", "action"]),
     ("15 pace of", ["reflected punch", "power", "", ""]),
     ("16 sweep of", ["", "", "power", "reflected hook"])],
    colw=[1.0*inch, 1.3*inch, 1.3*inch, 1.3*inch, 1.3*inch])]))
S.append(KeepTogether([P("Table 3-g — the same per mass (straight) and per inertia (turning), for the unafraid (rows 13–16, columns n–q)", h3),
    grid([("n  pace ν", None), ("o  accel. a", None), ("p  pickup α", None), ("q  sweep ω", None)],
    [("13 path of", ["zam", "zug", "", ""]),
     ("14 swing of", ["", "", "zug", "zam"]),
     ("15 pace of", ["reflected zip", "zow", "", ""]),
     ("16 sweep of", ["", "", "zow", "reflected zing"])],
    colw=[1.0*inch, 1.3*inch, 1.3*inch, 1.3*inch, 1.3*inch])]))
S.append(P("The reflected cells are reflexes: the pace of the movement, ν · p. Punch is half of it because the velocity of added motion is stored as punch: "
           "each bit of motion goes in at the velocity the body has then, so from rest the store fills the triangle under the line, half the rectangle. "
           "That holds with the mass fixed; hook is half the sweep of the spin the same way, with the inertia fixed. The average velocity here is the average over the motion added, "
           "which equals the time average for a steady push from rest: the same triangle.", small))
S.append(KeepTogether([P("Table 4 — the bulk meeting things (row 17, columns r–u)", h3),
    grid([("r  lever ι", None), ("s  pace ν", None), ("t  accel. around a", None), ("u  gravitation g", None)],
    [("17 bulk of / at / under", [("inertia", "profile"), ("spin", "swirl"), ("torque", "twirl"), ("load moment", "")])],
    colw=[1.5*inch, 1.2*inch, 1.2*inch, 1.3*inch, 1.3*inch], corner="bulk →")]))
S.append(P("The bulk is the one quantity that goes both ways: operators lead it (the sweep of the bulk, row 10) and things follow it "
           "(the bulk at pace, 17s). The bulk of the lever is a dot (both along the arm); the other three cross.", small))

# ---------------- Part 5: defs per cell ----------------
S.append(P("5. One definition per filled cell", h2))
defs = [
 ("1a", "pace (ν): the rate at the lever's end", "ν = Δι / Δt"),
 ("1c", "movement (p): the rate of the bulk", "p = Δβ / Δt"),
 ("2a", "arc: the swing of the lever; its length is ψ r, and moment to moment its step is Δψ × ι", "Δx = Δψ × ι"),
 ("2c", "transit: the swing of the bulk, mass along the arc", "transit = ψ m r"),
 ("3a", "pace (ν): the sweep of the lever", "ν = ω × ι"),
 ("3c", "movement (p): the sweep of the bulk", "p = ω × β"),
 ("4a", "acceleration around (a): the pickup of the lever", "a = α × ι"),
 ("4c", "force around (F): the pickup of the bulk", "F = α × β"),
 ("5a", "profile: the reflex of the lever; the leverage of the lever", "profile = ι · ι = r²"),
 ("5b", "bulk (β): the leverage of the mass", "β = ι × m"),
 ("5c", "inertia (η): the leverage of the bulk", "η = ι · β"),
 ("6a", "−swirl: the pace of the lever, read as the lever at pace (swirl)", "ν × ι = −swirl"),
 ("6b", "movement (p): the pace of the mass", "p = ν × m"),
 ("6c", "−spin: the pace of the bulk, read as the bulk at pace (spin)", "ν × β = −ξ"),
 ("7f", "shift: the movement carried over time, steady movement only", "Δshift = p × Δt"),
 ("7g", "impulse (Δp): the duration of a net force; the movement it adds (standard word)", "Δp = F × Δt"),
 ("7h", "boost (Δξ): the duration of a net torque; the spin it adds", "Δξ = χ × Δt"),
 ("8d", "movement (p): the rate of the bulk", "p = Δβ / Δt"),
 ("8e", "spread: the increase of the inertia", "spread = Δη / Δt"),
 ("8f", "force (F): the fluxion of the movement; a push or pull adds movement over time", "F = Δp / Δt"),
 ("8g", "yank: the fluxion of the force", "yank = ΔF / Δt"),
 ("8i", "torque (χ): the fluxion of the spin; a torque adds spin over time", "χ = Δξ / Δt"),
 ("9d", "transit: the swing of the bulk, mass along the arc", "transit = ψ m r"),
 ("10d", "movement (p): the sweep of the bulk", "p = ω × β"),
 ("10e", "spin (ξ): the sweep of the inertia", "ξ = ω × η"),
 ("10f", "center force (F⊙): the sweep of the movement; the force that keeps it on center", "F⊙ = ω × p"),
 ("11d", "force around (F): the pickup of the bulk", "F = α × β"),
 ("11e", "torque (χ): the pickup of stable inertia", "χ = α × η"),
 ("11f", "yerk: the pickup of the movement", "yerk = α × p"),
 ("12d", "inertia (η): the leverage of the bulk", "η = ι · β"),
 ("12f", "spin (ξ): the leverage of the movement", "ξ = ι × p"),
 ("12g", "torque (χ): the leverage of a force", "χ = ι × F"),
 ("12g′", "moment (M): the leverage of a force across an arm", "M = ι × F"),
 ("13j", "action: the movement along the path (the abbreviated action)", "action = Σ p · Δx"),
 ("13k", "work (W): a force along a path", "W = Σ F · Δx"),
 ("14l", "work (W): a torque through a swing", "W = ψ · χ"),
 ("14m", "action: the spin through the swing", "action = ξ · ψ"),
 ("15j", "reflected punch: the pace of the movement, twice the punch", "ν · p = 2 punch"),
 ("15k", "power (P): the pace of the force", "P = ν · F"),
 ("16l", "power (P): the sweep of the torque", "P = ω · χ"),
 ("16m", "reflected hook: the sweep of the spin, twice the hook", "ω · ξ = 2 hook"),
 ("17r", "inertia (η): the bulk of the lever", "η = β · ι"),
 ("17s", "spin (ξ): the bulk at pace", "ξ = β × ν"),
 ("17t", "torque (χ): the bulk of the acceleration around", "χ = β × a"),
 ("17u", "load moment (M): the bulk under gravitation", "M = β × g"),
]
for c, s_, f in defs: S.append(DC(c, s_, f))

# ---------------- Part 6: contradictions ----------------
S.append(P("6. Where this contradicts the textbook, not just renames it", h2))
S.append(P("• <b>Torque on a balanced beam.</b> The physics book sums “torques about the pivot” for a beam going nowhere; here those are moments. "
           "Engineers already say moments there.", defn))
S.append(P("• <b>Spin.</b> The textbook splits angular momentum into spin (about a body's own axis) and orbital; here spin is the leverage of the "
           "movement about whatever axis the setup has, so a train on a track has spin.", defn))
S.append(P("• <b>Center force</b> is the textbook's centripetal force; the textbook's “central force” (any force aimed at a center) keeps its own meaning.", defn))
S.append(P("• <b>Inertia</b> is the textbook's rotational inertia, the same m r² under its own second name; the book keeps the word for the first law too, as the textbook does. "
           "Bulk, m r, is the textbook's first moment of mass, which it has but never uses in sentences.", defn))
S.append(P("Everything else is an old word assigned to a quantity that was always there, or the textbook's own word for it.", defn))

# glue each heading to the block after it (flattened: nested KeepTogether misbehaves)
def ishead(f): return isinstance(f, Paragraph) and f.style.name in ("h2","h3")
S2=[]; i=0
while i < len(S):
    if ishead(S[i]):
        grp=[S[i]]; i+=1
        while i < len(S) and ishead(S[i]): grp.append(S[i]); i+=1
        if i < len(S):
            nxt=S[i]; i+=1
            grp += list(nxt._content) if isinstance(nxt, KeepTogether) else [nxt]
        S2.append(KeepTogether(grp))
    else: S2.append(S[i]); i+=1
doc.build(S2)
print(OUT)
