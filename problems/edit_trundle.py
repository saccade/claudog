import subprocess
p='/home/claude/out/build_dope2.py'; s=open(p,encoding='utf-8').read()
st=subprocess.run(['bash','-c','TZ=America/New_York date "+%y%m%d%H%M"'],capture_output=True,text=True).stdout.strip()
old=s.split('STAMP = "')[1][:10]
R=[
 ('S.append(D("%s: a setup\'s work per stroke, the work it takes to swing the setup through one stroke; the sweep of the trundle is the power (work per stroke times strokes per second)" % R("trundle"), "trundle = W per ζ"))',
  'S.append(D("%s: a setup\'s work per stroke, the work it takes to swing the setup through one stroke. At a steady torque, work counted in the setup\'s trundles is the swing counted in strokes, which is why a newton-metre of torque is a joule per stroke. The sweep of the trundle is the power (work per stroke times strokes per second)" % R("trundle"), "trundle = ζ · χ;  W / trundle = ψ / ζ"))'),
 ('STAMP = "%s"'%old,'STAMP = "%s"'%st),
 ('2026-10-19 %s:%s.</b>'%(old[6:8],old[8:]),'2026-10-19 %s:%s.</b>'%(st[6:8],st[8:])),
 ('Supersedes CL-115 (2610191303): "','Supersedes CL-119 (2610191315): "'),
 ('"forwardness and upwardness written with the arrows (section 7). Nothing here','"the trundle counts work in strokes, and gives torque its unit. Nothing here'),
 ('S.append(P("<b>Since 1303:</b>','S.append(P("<b>Since 1315:</b> a trundle is read relative to its setup; at a steady torque, work in trundles is swing in strokes, so a newton-metre of torque is a joule per stroke (E-0184).", defn))\nS.append(P("<b>Since 1303:</b>'),
 ('current: 2610191315 (CL-119, text only)','current: %s (CL-120, text only)'%st),
]
for a,b in R:
    assert a in s, a[:70]
    s=s.replace(a,b,1)
open(p,'w',encoding='utf-8').write(s); print(st)
