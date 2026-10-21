import subprocess
p = '/home/claude/out/build_dope2.py'; s = open(p, encoding='utf-8').read()
st = subprocess.run(['bash', '-c', 'TZ=America/New_York date "+%y%m%d%H%M"'], capture_output=True, text=True).stdout.strip()
old = s.split('STAMP = "')[1][:10]
lines = s.split('\n')
for i, l in enumerate(lines):
    if l.startswith('S.append(D("cosine and sine:'):
        lines[i] = ('S.append(D("forwardness and upwardness: how much of a direction is forward, or up; what fraction of a forward or an up it is worth '
                    '(textbook %s and %s)" % (B("cosine"), B("sine")), "→ · θ = θ / →;  ↑ · θ = θ / ↑"))')
    if l.startswith('S.append(D("the identity: a direction is its forward part plus its up part.'):
        lines[i] = ('S.append(D("a direction is its forward part plus its up part. Its reflex is one, since a direction is one long; forward and up are square '
                    'to each other, so the cross terms drop out and the reflex is the reflexes of the two parts", '
                    '"θ = (θ / →) → + (θ / ↑) ↑<br/>1 = θ · θ = (θ / →)² + (θ / ↑)²"))')
    if l.startswith('S.append(P("<b>Since 1302:</b>'):
        lines[i] = ('S.append(P("<b>Since 1303:</b> forwardness and upwardness lead, written with the arrows; cosine and sine are the textbook\'s names (R-034).", defn))\n' + l)
s = '\n'.join(lines)
R = [
 ('STAMP = "%s"' % old, 'STAMP = "%s"' % st),
 ('2026-10-19 %s:%s.</b>' % (old[6:8], old[8:]), '2026-10-19 %s:%s.</b>' % (st[6:8], st[8:])),
 ('Supersedes CL-114 (2610191302): "', 'Supersedes CL-115 (2610191303): "'),
 ('"cosine and sine read as fractions of forward and up, θ / → and θ / ↑, with the heft of a bulk (section 7). Nothing here',
  '"forwardness and upwardness written with the arrows (section 7). Nothing here'),
 ('with the identity cos²θ + sin²θ = 1 from the reflex', 'with the identity from the reflex'),
 ('current: 2610191303 (CL-115, text only)', 'current: %s (CL-119, text only)' % st),
]
miss = 0
for a, b in R:
    if a not in s: print("MISSING", a[:70]); miss += 1
    s = s.replace(a, b, 1)
open(p, 'w', encoding='utf-8').write(s)
print(st, miss, s.count('cos'), s.count('sin²'))
