#!/usr/bin/env python3
# Written by Claude (Anthropic), 2026-10-21. Prints (start,end) of the assembled-tab paragraphs to edit, by text prefix.
import sys
sys.path.insert(0,'/home/claude/claudog/mansion')
import tab_tools as T
rev,ps=T.paras(sys.argv[1])
print('REV',rev)
pref=[l.rstrip('\n') for l in open(sys.argv[2]) if l.strip()]
for p in pref:
    hits=[(a,b,s) for a,b,st,s in ps if s.startswith(p)]
    print(len(hits),p[:50].ljust(50),[(a,b) for a,b,s in hits])
