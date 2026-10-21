import subprocess
p = '/home/claude/out/build_dope2.py'; s = open(p, encoding='utf-8').read()
st = subprocess.run(['bash', '-c', 'TZ=America/New_York date "+%y%m%d%H%M"'], capture_output=True, text=True).stdout.strip()
hhmm = st[6:8] + ":" + st[8:]
old_st = s.split('STAMP = "')[1][:10]
old_hhmm = old_st[6:8] + ":" + old_st[8:]

CHANGE_NOTE = '''S.append(P("<b>Since 1009 (Codex's review):</b> the half in punch comes from the velocity of added motion being stored as punch (the triangle), not from legs out and back; "
           "a rule box says lever each bit, then add, and that a finite swing turns the lever; arc, transit and shift say moment to moment; kick counts every body and what was caught; "
           "a moment does no work around the axle; twist is the part of a leverage along the arm; trundle is a setup's work per stroke, a quantity in joules, not a unit; "
           "action is the abbreviated action; cells 6a and 6c are defined as they stand, with their minus signs (FX-049 to FX-056).", defn))
S.append(P("<b>Since 0953:</b>'''

NEW_BOX = '''"Yerk is the growing part of the yank; the center force also turns. The fluxion cells in the rate row carry the whole; the product cells carry one term.")))
S.append(Spacer(1, 4))
S.append(box(P("<b>Lever each bit, then add.</b> Inertia, spin and torque are taken bit by bit and then added; never lever a bulk or a movement that is already a sum. "
               "A balanced wheel's bulks and movements add to nothing while its inertia and spin are whole. "
               "<b>A finite swing turns the lever.</b> Products along the axis (swing, sweep, torque, spin) hold through a whole swing while they are steady: work and action through a swing. "
               "Products through the lever's direction (lever, bulk, movement) hold moment to moment only: arc, transit and shift add up step by step.")))'''

NOTE_OLD = '''S.append(P("The reflected cells are round trips: the pace of the movement is ν · p, two legs, and the punch is the leg out, ½ ν · p. "
           "That is where the half in punch and hook comes from.", small))'''
NOTE_NEW = '''S.append(P("The reflected cells are reflexes: the pace of the movement, ν · p. Punch is half of it because the velocity of added motion is stored as punch: "
           "each bit of motion goes in at the velocity the body has then, so from rest the store fills the triangle under the line, half the rectangle. "
           "The average velocity being half the final is the same triangle. Hook is half the sweep of the spin the same way.", small))'''

R = [
 ('"Claude The Straight Dope %s.pdf" (CL-098)' % old_st, '"Claude The Straight Dope %s.pdf" (CL-099)' % st),
 ('STAMP = "%s"' % old_st, 'STAMP = "%s"' % st),
 ('2026-10-19 %s.</b>' % old_hhmm, '2026-10-19 %s.</b>' % hhmm),
 ('Supersedes CL-097 (2610190953): "\n           "punch is kinetic energy from linear motion, punch and hook are one energy for a set-up body, and the last line of section 6 no longer claims new words.',
  'Supersedes CL-098 (2610191009): "\n           "Codex\'s review of 1009 is worked in (section 7).'),
 ('"kick = punch before − punch after"', '"kick = every body\'s punch and hook before − after − what was caught"'),
 ('the diagonal cells of the energy tables are reflexes, and the energy is the leg out" % R("reflex")',
  'the diagonal cells of the energy tables are reflexes, and the energy stored is half the reflex (under Table 3-g)" % R("reflex")'),
 ('The sweep of the spin is the reflected hook, out and back; the hook is the leg out. A body', 'The sweep of the spin is the reflected hook, twice the hook. A body'),
 ("crossed up and locked out, it can't do work (engineers'",
  "crossed up and locked out, it does no work around the axle; a springy arm takes work through its bend, around the moment's own axis (engineers'"),
 ('"%s: the leverage of a force along the arm, torsion; no symbol" % R("twist")', '"%s: the part of a leverage that points along the arm, torsion; no symbol" % R("twist")'),
 ("what moves a centre of mass (naval architects' weight shift)\" % R(\"shift\"), \"shift = p × Δt\"",
  "what moves a centre of mass (naval architects' weight shift). Steady movement only; a turning body's shift adds up step by step\" % R(\"shift\"), \"Δshift = p × Δt\""),
 ("(merchants' goods in transit)\" % R(\"transit\"), \"transit = ψ × β\"", "(merchants' goods in transit)\" % R(\"transit\"), \"transit = ψ m r\""),
 ('S.append(D("%s: a unit of work, one stroke of torque; the trundle rate is the power" % R("trundle"), "1 trundle = ζ χ"))',
  'S.append(D("%s: a setup\'s work per stroke, the work it takes to swing the setup through one stroke; the trundle rate is the power" % R("trundle"), "trundle = W per ζ"))'),
 ('"action: the movement along the whole path; the spin through the whole swing (standard)"',
  '"action: the movement along the whole path; the spin through the whole swing (standard: the abbreviated action, not the time sum of the Lagrangian)"'),
 ('(roll, whirl, trundle, ponder, wheel, oompf)', '(roll, whirl, ponder, wheel, oompf)'),
 (NOTE_OLD, NOTE_NEW),
 ('("2a", "arc: the swing of the lever", "arc = ψ × ι")', '("2a", "arc: the swing of the lever; its length is ψ r, and moment to moment its step is Δψ × ι", "Δx = Δψ × ι")'),
 ('("2c", "transit: the swing of the bulk", "transit = ψ × β")', '("2c", "transit: the swing of the bulk, mass along the arc", "transit = ψ m r")'),
 ('("9d", "transit: the swing of the bulk", "transit = ψ × β")', '("9d", "transit: the swing of the bulk, mass along the arc", "transit = ψ m r")'),
 ('("6a", "swirl: the lever at pace", "swirl = ι × ν")', '("6a", "−swirl: the pace of the lever, read as the lever at pace (swirl)", "ν × ι = −swirl")'),
 ('("6c", "spin (ξ): the bulk at pace", "ξ = β × ν")', '("6c", "−spin: the pace of the bulk, read as the bulk at pace (spin)", "ν × β = −ξ")'),
 ('("7f", "shift: the movement carried over time", "shift = p × Δt")', '("7f", "shift: the movement carried over time, steady movement only", "Δshift = p × Δt")'),
 ('("13j", "action: the movement along the path", "action = p · path")', '("13j", "action: the movement along the path (the abbreviated action)", "action = p · path")'),
 ('("15j", "reflected punch: the pace of the movement, out and back; the punch is the leg out", "ν · p = 2 punch")', '("15j", "reflected punch: the pace of the movement, twice the punch", "ν · p = 2 punch")'),
 ('("16m", "reflected hook: the sweep of the spin, out and back; the hook is the leg out", "ω · ξ = 2 hook")', '("16m", "reflected hook: the sweep of the spin, twice the hook", "ω · ξ = 2 hook")'),
 ('"Yerk is the growing part of the yank; the center force also turns. The fluxion cells in the rate row carry the whole; the product cells carry one term.")))', NEW_BOX),
 ('S.append(P("<b>Since 0953:</b>', CHANGE_NOTE),
 ("The half in punch: Codex's product rule says why the reflex is twice the energy \"\n           \"(a push grows v · p from both ends, v · F and p · a, each at the power); the explanation-sized version is the average velocity, W = v̄ · Δp. \"",
  "The half in punch: the product rule checks it \"\n           \"(a push grows v · p from both ends, v · F and p · a, each at the power); the reason is that the velocity of added motion is stored as punch. \""),
]
miss = 0
for a, b in R:
    if a not in s: print("MISSING:", a[:90]); miss += 1
    s = s.replace(a, b)
if miss == 0:
    open(p, 'w', encoding='utf-8').write(s)
print(st, "missing", miss)
