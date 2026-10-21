#!/usr/bin/env python3
# Written by Claude (Anthropic), 2026-10-21. Compare the reading-draft tab text with an expected text file.
import sys,difflib
sys.path.insert(0,'/home/claude/claudog/mansion')
import tab_tools as T
rev,ps=T.paras(sys.argv[1])
cur=''.join(s for a,b,st,s in ps)
exp=open(sys.argv[2]).read()+'\n'
print(rev,len(cur),len(exp),cur==exp)
if cur!=exp:
    sm=difflib.SequenceMatcher(None,cur,exp,autojunk=False)
    n=0
    for tag,i1,i2,j1,j2 in sm.get_opcodes():
        if tag!='equal':
            n+=1
            if n<=60: print(tag,i1,repr(cur[max(0,i1-15):i2+15]),'->',repr(exp[max(0,j1-15):j2+15]))
    print('diffs',n)
