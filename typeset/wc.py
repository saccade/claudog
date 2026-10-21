import re,sys
for f in sys.argv[1:]:
    t=open(f,encoding='utf-8').read()
    parts=re.split(r'\n(?=\d\. )',t)
    out=[]
    for p in parts[1:]:
        out.append((p.split('\n')[0][:30],len(p.split()),len(p)))
    print(f, sum(o[1] for o in out))
    for o in out: print("  %-32s words %4d chars %5d"%o)
