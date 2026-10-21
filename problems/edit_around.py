import subprocess
p='/home/claude/out/build_dope2.py'; s=open(p,encoding='utf-8').read()
st=subprocess.run(['bash','-c','TZ=America/New_York date "+%y%m%d%H%M"'],capture_output=True,text=True).stdout.strip()
old=s.split('STAMP = "')[1][:10]
R=[
 ('The default sense of "\n           "around is widdershins, counterclockwise seen from the tip of the axis arrow; the other way is sunwise, a negative sweep. ',
  'The default sense is "\n           "<b>forward around</b>: widdershins, counterclockwise seen from the tip of the axis arrow, and from here on just around; the other way is sunwise, a negative sweep. '),
 ('STAMP = "%s"'%old,'STAMP = "%s"'%st),
 ('2026-10-19 %s:%s.</b>'%(old[6:8],old[8:]),'2026-10-19 %s:%s.</b>'%(st[6:8],st[8:])),
 ('Supersedes CL-119 (2610191315): "','Supersedes CL-120 (2610191358): "'),
 ('"the trundle counts work in strokes, and gives torque its unit. Nothing here','"forward around is the default sense of turning (section 2). Nothing here'),
 ('S.append(P("<b>Since 1315:</b>','S.append(P("<b>Since 1358:</b> the default sense of turning is forward around (widdershins, named once); after that, just around (R-035).", defn))\nS.append(P("<b>Since 1315:</b>'),
 ('current: 2610191358 (CL-120, text only)','current: %s (CL-121, text only)'%st),
]
for a,b in R:
    assert a in s, a[:70]
    s=s.replace(a,b,1)
open(p,'w',encoding='utf-8').write(s); print(st)
