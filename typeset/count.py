import re,sys
for fn in sys.argv[1:]:
    t=open(fn).read().split('\n')
    idx=[i for i,l in enumerate(t) if re.match(r'^[1-4]\. [A-Z]',l)]
    idx.append(len(t))
    pre=' '.join(t[:idx[0]])
    print(fn, 'preamble words', len(pre.split()))
    for k in range(4):
        seg=t[idx[k]:idx[k+1]]
        txt=' '.join(seg)
        eq=sum(1 for l in seg if l.startswith('    '))
        print('  P%d lines %d words %d indented(eq) lines %d'%(k+1,len(seg),len(txt.split()),eq))
