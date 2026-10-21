#!/usr/bin/env python3
# Written by Claude (Anthropic), 2026-10-21. Finds the Latin variable letters in the reading-draft tab so they can be italicised
# (doc: italics for variable names unless they are Greek). Prints a review table to stderr and the request list to stdout.
import json,re,sys,collections
from tab_tools import paras,TABID
COMB='̀-ͯ'
UNITS=set('mskgNJWVACHF')            # one-letter units (only when they follow a number or another unit)
PRODUCTS=set('mg mgh mgL mga mgR mL mR mb ms mv ma vt vT Vt wt ct cw cp kx rv uE ZI VI LC Li Mc CE CV DL Da Db'.split())
DIFFS=set('dt dx dq dI da dU dp dy dE dK dV'.split())   # d is upright, the letter after it is a variable
FUNCS={'sin','cos','tan','kg','rad','MHz','mJ','Hz','Pa','cm','nF','nJ'}
FRAMES={'S','H'}                      # frame names, left upright
def u16(s): return len(s.encode('utf-16-le'))//2
def classify(s):
    """yield (start,end,letter) character ranges (python offsets) to italicise in paragraph s"""
    labels=[m.start(1) for m in re.finditer(r'(?:^|(?<=\s))\(([a-g])\)(?=\s|$|\.)',s)]
    for m in re.finditer(r'[A-Za-z]+['+COMB+r']*',s):
        w=m.group(0); st=m.start(); en=m.end()
        base=re.sub('['+COMB+']','',w)
        prev=s[:st]; nxt=s[en:]
        if st>0 and s[st-1]=='_': continue                 # subscript label
        if st>0 and s[st-1] in "’'": continue            # possessive or contraction tail
        if nxt[:1] in "’'" and re.match(r"[’'][A-Za-z]",nxt): 
            if len(base)==1 and base not in 'sS': continue  # I’ll, A’s? (A’s handled below)
        if base in FUNCS: continue
        if base in DIFFS:
            for k,ch in enumerate(w):
                if k and ch.isalpha(): yield (st+k,st+k+1,ch)
            continue
        if base in PRODUCTS:
            for k,ch in enumerate(w): 
                if ch.isalpha(): yield (st+k,st+k+1,ch)
            continue
        if len(base)>1:
            continue                                        # English word or unit word
        c=base
        if st in labels: continue
        if c in ('o','d'): continue                           # own time, already italic
        if c in FRAMES and not re.search(r'\d\s*$',prev): continue
        # articles and the like
        if c in 'aA' and re.match(r"\s+(?:[a-z]|\d)",nxt) and not re.match(r"\s+(and|or)\s+[a-z]\b",nxt): continue
        if c in 'aA' and re.match(r"\s+(and|or)\s",nxt) and False: continue
        # units
        pl=prev.rstrip('  \xa0'); sp=len(prev)-len(pl)
        if c in UNITS:
            if sp<=1 and re.search(r'[\d)⁻⁰¹²³]$',pl) and not re.search(r'[A-Za-z]$',pl) and not (pl.endswith(')') and re.search(r'cos\([^)]*\)$',pl) is None and False):
                if re.search(r'\d$',pl) or (pl.endswith(')') and re.match(r'[.,;:\s]|$',nxt)): continue
            if re.search(r'(?:kg|rad|N|J|W|V|m|s|A|C|H|F)\s?$',pl) and re.search(r'\d\s*(?:kg|rad|N|J|W|V|m|s|A|C|H|F)\s?$',pl): continue   # chain: 3.0 N m, 1 kg m
            if nxt[:2] in ('/s','/m') or pl.endswith('/'): 
                if c in 'ms': continue
            if c=='s' and nxt[:1] in '⁻²': continue
            if c=='m' and nxt[:1]=='²' and re.search(r'(kg|N)\s$',prev): continue
        yield (st,st+len(c)+len(w)-len(base) if False else en,c)
if __name__=='__main__':
    rev,ps=paras(sys.argv[1]); out=[]
    for a,b,stl,s in ps:
        if stl.startswith('HEADING') or stl=='TITLE': continue
        for (x,y,c) in classify(s.rstrip('\n')):
            out.append((a+u16(s[:x]),a+u16(s[:y]),c,s[max(0,x-18):y+12].replace('\n',' ')))
    out.sort()
    print(rev,len(out),file=sys.stderr)
    cnt=collections.Counter(c for _,_,c,_ in out)
    print(sorted(cnt.items()),file=sys.stderr)
    json.dump(out,open(sys.argv[2],'w'),ensure_ascii=False)
