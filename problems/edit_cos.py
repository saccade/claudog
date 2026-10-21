import subprocess
p = '/home/claude/out/build_dope2.py'; s = open(p, encoding='utf-8').read()
st = subprocess.run(['bash', '-c', 'TZ=America/New_York date "+%y%m%d%H%M"'], capture_output=True, text=True).stdout.strip()
old = s.split('STAMP = "')[1][:10]
OLD_ENTRY = 'S.append(D("cosine and sine: how much of a direction is forward, and how much is up, each written as a fraction of the whole. The cosine is also the forwardness of the angle, the product of forward and the direction; the fraction reads more easily", "cos θ = → / θ = → · θ;  sin θ = ↑ / θ = ↑ · θ"))'
NEW_ENTRY = ('S.append(D("cosine and sine: what fraction of forward a direction is, and what fraction of up. Physically it is the direction\'s forwardness '
             '(or upwardness), and mathematically a dot product; it is often more useful to read it as the fraction: dividing by a direction counts it, '
             'the way 30 metres over a metre counts metres. The other order fails at first approach as soon as the thing divided has a size", '
             '"cos θ = θ / → = → · θ;  sin θ = θ / ↑ = ↑ · θ"))\n'
             'S.append(D("the heft of a bulk: the bulk under gravitation, as many ups as its direction is worth; with β the bulk\'s size and θ its direction", '
             '"U = g β (↑ · θ) = g β (θ / ↑)"))')
R = [
 (OLD_ENTRY, NEW_ENTRY),
 ('STAMP = "%s"' % old, 'STAMP = "%s"' % st),
 ('2026-10-19 %s:%s.</b>' % (old[6:8], old[8:]), '2026-10-19 %s:%s.</b>' % (st[6:8], st[8:])),
 ('Supersedes CL-111 (2610191227): "', 'Supersedes CL-113 (2610191245): "'),
 ('"the body entry says any letter can name a body (section 7). Nothing here', '"cosine and sine read as fractions of forward and up, θ / → and θ / ↑, with the heft of a bulk (section 7). Nothing here'),
 ('S.append(P("<b>Since 1227:</b>', 'S.append(P("<b>Since 1245:</b> cosine and sine back to θ / → and θ / ↑, what fraction of forward or up a direction is; the 1227 flip to → / θ was wrong. A direction over a direction gives the same number either way, but dividing anything with a size by a direction gives its component, and the other order doesn\'t. Heft of a bulk: U = g β (θ / ↑) (FX-067).", defn))\nS.append(P("<b>Since 1227:</b>'),
 ('S.append(P("<b>Since 1208:</b> cosine and sine written the right way up, the part over the whole: → / θ and ↑ / θ (FX-065).", defn))\n', ''),
 ('current: 2610191245 (CL-113)', 'current: %s (CL-114)' % st),
]
miss = 0
for a, b in R:
    if a not in s: print("MISSING", a[:70]); miss += 1
    s = s.replace(a, b, 1)
if miss == 0: open(p, 'w', encoding='utf-8').write(s)
print(st, miss)
