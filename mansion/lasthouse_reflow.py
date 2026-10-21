#!/usr/bin/env python3
# Written by Claude (Anthropic), 2026-10-21. Turns the Last House source (Tab 1 text) into reading-draft paragraphs:
# prose lines reflowed, indented lines kept one per paragraph (monospace), problems interleaved with their solutions,
# wrappers dropped, inertia I_a/I_b -> eta_a/eta_b (current I stays). Content otherwise verbatim.
import re,json,sys
src=open(sys.argv[1]).read().split('\n')
def sect(lo,hi): return src[lo-1:hi]     # 1-based inclusive line numbers
def paras(lines):
    out=[];buf=[]
    def flush():
        nonlocal buf
        if buf: out.append(('N',' '.join(s.strip() for s in buf))); buf=[]
    for ln in lines:
        if not ln.strip(): flush(); continue
        if ln.startswith('    '):
            flush(); out.append(('M',ln.rstrip()))
        elif re.fullmatch(r'-{3,}|={3,}',ln.strip()): flush()
        else: buf.append(ln)
    flush(); return out
def swap(items):
    r=[]
    for k,t in items:
        t=t.replace('I_a','η_a').replace('I_b','η_b'); r.append((k,t))
    return r
# segment by "N. Title" + dashes headings
def segments(lo,hi):
    segs={};cur=None
    for i in range(lo-1,hi):
        ln=src[i]
        m=re.match(r'^(\d)\. ',ln)
        if m and i+1<len(src) and re.fullmatch(r'-{3,}',src[i+1].strip()):
            cur=int(m.group(1)); segs[cur]=[]; continue
        if cur is not None: segs[cur].append(ln)
    return segs
pre=sect(11,24)
probs=segments(26,258)
sols=segments(279,len(src))
solpre=sect(268,276)
titles={1:'Something hanging from something',2:'The wires under the skin',3:'The corridor that gets there first',4:'The two lights disagree',5:'The chair at the end'}
rooms={1:'Study',3:'Hall',5:'Lounge'}
items=[]
pp=paras(pre)
pp=[(k,t.replace('Plain text, fixed columns. ','')) for k,t in pp]
for n in range(1,6):
    if n in rooms: items.append(('H2',rooms[n]))
    if n==1: items.append(('BRIDGE',''))
    items.append(('H3',titles[n]))
    if n==1: items+=pp
    items+=paras(probs[n])
    if n==1: items+=paras(solpre)
    items+=paras(sols[n])
items=[('H3',t) if (k=='N' and t=='The chorus') else (k,t) for k,t in items]
items=swap(items)
json.dump(items,open(sys.argv[2],'w'),ensure_ascii=False)
for k,t in items: print(k+'|'+t)
