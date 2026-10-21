#!/usr/bin/env python3
# Written by Claude (Anthropic), 2026-10-21. Builds italic requests for the own-time o in the reading-draft tab.
import json,re,sys
from tab_tools import paras,TABID
PATS=[r'γ d(o)\b', r'Δ(o) =', r'own time is (o) =', r'\((o)\)', r'ν(o)\)']
def u16(s): return len(s.encode('utf-16-le'))//2
rev,ps=paras(sys.argv[1])
rq=[]
for a,b,st,s in ps:
    for pat in PATS:
        for m in re.finditer(pat,s):
            i=a+u16(s[:m.start(1)])
            rq.append((i,s[max(0,m.start(1)-6):m.end(1)+4]))
rq.sort()
print(rev,len(rq),file=sys.stderr)
for i,c in rq: print(i,repr(c),file=sys.stderr)
print(json.dumps([{"updateTextStyle":{"range":{"startIndex":i,"endIndex":i+1,"tabId":TABID},"textStyle":{"italic":True},"fields":"italic"}} for i,_ in rq],ensure_ascii=False))
