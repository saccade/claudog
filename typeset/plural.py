import re,sys
U='hand|card|lump|cat|dog|zoom|push|press|thump|pow|crank|grunt|oompf|stroke|sweep|whirl|ponder|wheel|roll|zip|zing|zug|zow|zam|shift|transit|trundle|mw'
pl={'push':'pushes','press':'presses'}
alts='|'.join(sorted([pl.get(u,u+'s') for u in U.split('|')],key=len,reverse=True))
NUM=r'(?:\d[\d.,]*(?:/\d+)?|[½⅓⅔¼¾⅕⅖⅗⅘⅙⅚⅛]|\d+\s*[½¼¾])'
pat=re.compile(r'(\b'+NUM+r'\s+)('+alts+r')\b')
pat2=re.compile(r'\b(lump|mw)-(cards|sweeps)\b')
def sing(w):
    for u in U.split('|'):
        if pl.get(u,u+'s')==w: return u
    return w
def fix(s):
    s=pat.sub(lambda m:m.group(1)+sing(m.group(2)),s)
    s=pat2.sub(lambda m:m.group(1)+'-'+m.group(2)[:-1],s)
    return s
if __name__=='__main__':
    for f in sys.argv[1:]:
        s=open(f,encoding='utf-8').read()
        for m in pat.finditer(s): print(f[:30],'|',s[max(0,m.start()-25):m.end()+5].replace('\n',' '))
        for m in pat2.finditer(s): print(f[:30],'|',m.group(0))
