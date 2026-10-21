import subprocess
p='/home/claude/out/build_dope2.py'; s=open(p,encoding='utf-8').read()
st=subprocess.run(['bash','-c','TZ=America/New_York date "+%y%m%d%H%M"'],capture_output=True,text=True).stdout.strip()
old=s.split('STAMP = "')[1][:10]
R=[
 ('the other way is <b>backward around</b>, sunwise, a negative sweep. ','the other way is <b>backward around</b>, sunwise, a negative sweep, never shortened to around but back around for short. '),
 ('STAMP = "%s"'%old,'STAMP = "%s"'%st),
 ('2026-10-19 %s:%s.</b>'%(old[6:8],old[8:]),'2026-10-19 %s:%s.</b>'%(st[6:8],st[8:])),
 ('Supersedes CL-121 (2610191408): "','Supersedes CL-122 (2610191409): "'),
 ('S.append(P("<b>Since 1408:</b> the other sense is backward around (R-035).", defn))','S.append(P("<b>Since 1408:</b> the other sense is backward around, shortened only to back around (R-035).", defn))'),
 ('current: 2610191409 (CL-122, text only)','current: %s (CL-123, text only)'%st),
]
for a,b in R:
    assert a in s, a[:70]
    s=s.replace(a,b,1)
open(p,'w',encoding='utf-8').write(s); print(st)
