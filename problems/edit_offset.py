import subprocess
p = '/home/claude/out/build_dope2.py'; s = open(p, encoding='utf-8').read()
st = subprocess.run(['bash', '-c', 'TZ=America/New_York date "+%y%m%d%H%M"'], capture_output=True, text=True).stdout.strip()
hhmm = st[6:8] + ":" + st[8:]
old_st = s.split('STAMP = "')[1][:10]
old_hhmm = old_st[6:8] + ":" + old_st[8:]

R = [
 ('"Claude The Straight Dope %s.pdf" (CL-099)' % old_st, '"Claude The Straight Dope %s.pdf" (CL-100)' % st),
 ('STAMP = "%s"' % old_st, 'STAMP = "%s"' % st),
 ('2026-10-19 %s.</b>' % old_hhmm, '2026-10-19 %s.</b>' % hhmm),
 ('Supersedes CL-098 (2610191009): "\n           "Codex\'s review of 1009 is worked in (section 7).',
  'Supersedes CL-099 (2610191025): "\n           "Codex\'s second review is worked in, and the offset is assigned (section 7).'),
 # work as a sum of steps
 ('S.append(D("work (W): a force along a path", "W = F · Δx"))',
  'S.append(D("work (W): a force along a path, added up step by step", "W = Σ F · Δx"))'),
 # kick counts each energy once
 ('kick = every body\'s punch and hook before − after − what was caught',
  'kick = every body\'s punch and hook before − after − what was caught, each energy counted once'),
 # offset entry after radius
 ('S.append(D("radius (r): the length of a lever; distance from the axis", "r = |ι|"))',
  'S.append(D("radius (r): the length of a lever; distance from the axis", "r = |ι|"))\n'
  'S.append(D("%s: the part of a lever that runs across the member; the part along it is the reach. A load on the member\'s own line has no offset" % R("offset"), "ι = reach + offset"))'),
 # twist through the offset
 ('S.append(D("%s: the part of a leverage that points along the arm, torsion; no symbol" % R("twist"), ""))',
  'S.append(D("%s: the leverage of a force through the offset, about the member\'s own line; torsion. A crane\'s jib twists only when the load hangs off its line; a wrench on a shaft is all offset; no symbol" % R("twist"), ""))'),
 # trundle sweep
 ('the work it takes to swing the setup through one stroke; the trundle rate is the power" % R("trundle")',
  'the work it takes to swing the setup through one stroke; the sweep of the trundle is the power (work per stroke times strokes per second)" % R("trundle")'),
 # action
 ('(standard: the abbreviated action, not the time sum of the Lagrangian)", "action = p · path = ξ · ψ"',
  '(standard: the abbreviated action, not the time sum of the Lagrangian); it adds up step by step, so it builds all the way around a closed circle", "action = Σ p · Δx = ξ · ψ (steady spin)"'),
 ('("13j", "action: the movement along the path (the abbreviated action)", "action = p · path")',
  '("13j", "action: the movement along the path (the abbreviated action)", "action = Σ p · Δx")'),
 ('("13k", "work (W): a force along a path", "W = F · path")',
  '("13k", "work (W): a force along a path", "W = Σ F · Δx")'),
 # global convention in the rule box
 ('"Products through the lever\'s direction (lever, bulk, movement) hold moment to moment only: arc, transit and shift add up step by step.")))',
  '"Products through the lever\'s direction (lever, bulk, movement) hold moment to moment only: arc, transit and shift add up step by step. "\n'
  '               "<b>Path products add up step by step:</b> work is the force along each step, action the movement along each step, exact as the steps get small.")))'),
 # triangle qualifiers
 ('"The average velocity being half the final is the same triangle. Hook is half the sweep of the spin the same way.", small))',
  '"That holds with the mass fixed; hook is half the sweep of the spin the same way, with the inertia fixed. The average velocity here is the average over the motion added, "\n'
  '           "which equals the time average for a steady push from rest: the same triangle.", small))'),
 # change note
 ('S.append(P("<b>Since 1009 (Codex\'s review):</b>',
  'S.append(P("<b>Since 1025:</b> <b>offset</b> is the part of a lever across the member, and twist comes through it (FX-058); the sweep of the trundle is the power (FX-057); "\n'
  '           "work and action add up step by step (FX-059); kick counts each energy once, the triangle holds mass or inertia fixed, and its average is over the motion added (FX-060).", defn))\n'
  'S.append(P("<b>Since 1009 (Codex\'s review):</b>'),
]
miss = 0
for a, b in R:
    if a not in s: print("MISSING:", a[:90]); miss += 1
    s = s.replace(a, b)
if miss == 0:
    open(p, 'w', encoding='utf-8').write(s)
print(st, "missing", miss)
