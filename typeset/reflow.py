import unicodedata,sys,re
p=sys.argv[1]
W=66
def dw(s): return sum(0 if unicodedata.combining(c) else 1 for c in s)
lines=open(p,encoding='utf-8').read().split('\n')
units={'s','m','J','mJ','W','N','C','V','A','F','%','kg','rad','rad/s','m/s','s⁻²','s⁻³','m²','kg','m²:','s,','m,','J,','J.','s.','m.','C,','V.','A','F,','°','%,','%)','rad,','rad/s,','rad/s.','m/s,','m/s.','m/s²','m/s²,','m/s²:','rad/s²','s⁻²,','s⁻³,','J:','J;','m;','s;','C;','A;','rad;','rad/s;','(rightward),','kg.','kg),'}
out=[];i=0
def flush(par):
    toks=' '.join(par).split()
    # glue units
    g=[]
    for t in toks:
        if g and (t in units or t.rstrip('.,;:)') in units) and len(t)<=12:
            g[-1]=g[-1]+'\x00'+t
        else: g.append(t)
    res=[];cur=''
    for t in g:
        if not cur: cur=t
        elif dw(cur)+1+dw(t)<=W: cur+=' '+t
        else: res.append(cur);cur=t
    if cur: res.append(cur)
    return [r.replace('\x00',' ') for r in res]
par=[]
for n,l in enumerate(lines):
    para_line = n>=2 and l and not l[0].isspace() and not l.startswith('====')
    if para_line: par.append(l)
    else:
        if par: out+=flush(par);par=[]
        out.append(l.replace('='*70,'='*66))
if par: out+=flush(par)
open(p,'w',encoding='utf-8').write('\n'.join(out))
for n,l in enumerate(out,1):
    if dw(l)>W: print('LONG',n,dw(l),l)
