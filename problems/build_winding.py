import sys, re, textwrap
stamp, date = sys.argv[1], sys.argv[2]
OUT="/home/claude/out/"
SP="/tmp/claude-0/-home-claude/703a9c19-4a4f-5d49-a5f7-811fca7a3452/scratchpad/"
def W66(s,i="",j=""):
    s=" ".join(s.split())
    for g in [" × "," · "," / ","5 kg","12 V","3.0 A","150 Ω","10 Ω","2000 µF","0.40 H","24 mC","1.2 Wb"]: s=s.replace(g,g.replace(" ","\x00"))
    return textwrap.fill(s,66,initial_indent=i,subsequent_indent=j,break_long_words=False,break_on_hyphens=False).replace("\x00"," ")

def rewrap(lines):
    ind=lambda l: len(l)-len(l.lstrip(" "))
    paras=[]; cur=[]
    for l in lines:
        if l.strip()=="" :
            if cur: paras.append(cur); cur=[]
            paras.append(None)
        else: cur.append(l)
    if cur: paras.append(cur)
    out=[]
    for p in paras:
        if p is None: out.append(""); continue
        if p[0].startswith("+") or p[0].startswith("|") or any(re.match(r"^[=-]{3,}$",x) for x in p):
            out.extend(p); continue
        k=len(p)
        while k>0 and ind(p[k-1])>=8: k-=1
        prose, form = p[:k], p[k:]
        if k==1 and len(p[0].strip())<=25 and p[0].rstrip().endswith(":") and form and not re.search(r"^\s*\S+ = ", form[0]):
            # term line, then prose at indent 8
            out.append(p[0])
            body=form
            if all(len(x)<=66 for x in body): out.extend(body)
            else: out.append(W66(" ".join(x.strip() for x in body)," "*8," "*8))
            continue
        if prose and any(len(x)>66 for x in prose):
            first=prose[0]
            m=re.match(r"^(\s*(?:\d+[a-z]′?\s+|•\s+))",first)
            if m:
                lab=m.group(1); sub=" "*ind(prose[1]) if len(prose)>1 else " "*len(lab)
                text=" ".join(first[len(lab):].split()+[w for x in prose[1:] for w in x.split()])
                out.append(W66(text,lab,sub))
            else:
                sub=" "*ind(prose[1]) if len(prose)>1 else " "*ind(first)
                out.append(W66(" ".join(x.strip() for x in prose)," "*ind(first),sub))
        else:
            out.extend(prose)
        out.extend(form)
    return out

dope_raw=open(OUT+"Claude The Straight Dope 2610191640.txt").read()
g_old="""  ghost:
        a body-like thing of no mass that appears to be somewhere: a laser
        dot, a projected image, a theoretical point."""
g_new="""  ghost:
        a body-like thing of no mass. It needs something, a place to be or some other property, though not necessarily a place: a laser dot, a projected image, a theoretical point, a centre of mass; one can have only a velocity and a swirl. Its properties are the ghost quantities: velocity, swirl, zip. With no place and no properties at all, it is the ghost of a ghost, and gone."""
assert dope_raw.count(g_old)==1
dope=dope_raw.replace(g_old,g_new).split("\n")
a=dope.index("1. The straight line")
dope_body="\n".join(rewrap(dope[a:])).rstrip()
dope_body=dope_body.replace("Straight→","straight→")
dope_body=dope_body.replace("        kick = every body's punch and hook before − after − what was caught,\n        each energy counted once.","        kick = every body's punch and hook before − after\n               − what was caught, each energy counted once.")

dog=open(OUT+"Claude Dog Math 2610200859.txt").read().split("\n")
b=dog.index("1. What dog math is")
dog_body="\n".join(dog[b:]).rstrip()

el=open(SP+"winding_elec.txt").read()
def table(widths, head, body):
    def rows(cells):
        cols=[textwrap.wrap(c,w,break_on_hyphens=False) or [""] for c,w in zip(cells,widths)]
        n=max(map(len,cols)); [c.extend([""]*(n-len(c))) for c in cols]
        return "\n".join("| "+" | ".join("%-*s"%(w,c[k]) for c,w in zip(cols,widths))+" |" for k in range(n))
    sep="+"+"+".join("-"*(w+2) for w in widths)+"+"
    return "\n".join([sep,rows(head),sep]+[rows(r) for r in body]+[sep])
mirror=table([33,33],["The can","The coil"],[
 ["cans charge, Q","coils linked flux, λ"],
 ["at a voltage, V","at a current, I"],
 ["capacitance, C","inductance, L"],
 ["current is charge's fluxion","voltage is flux's fluxion"],
 ["cans the capacitance of its voltage: Q = C V","coils the inductance of its current: λ = L I"],
 ["stores the voltage of added charge: dE = V dQ","stores the current of added flux: dE = I dλ"],
 ["holds ½ Q V","holds ½ λ I"]])
blocks=el.split("\n\n"); outb=[]
for bl in blocks:
    if bl.strip()=="TABLE_MIRROR": outb.append(mirror)
    elif bl.startswith("    ") or re.match(r"^.+\n[=-]+$",bl): outb.append(bl.rstrip("\n"))
    elif bl.startswith("  - "): outb.append(W66(bl[4:],"  - ","    "))
    else: outb.append(W66(bl))
el_body="\n\n".join(outb).rstrip()

head=W66(f"Written by Claude (Anthropic), {date}. The straight dope and dog math together, as they stand this morning, with dr. kraemer's electricity rules added and two problems that verb the new quantities: a snapshot of a draft that is still winding. Not doc's text; the ideas and rules are his, these words are the model's.")
note=W66("Part one is the straight→ mechanics glossary and tables. Part two is dog math: the rules, units, ghosts and stealth mode. Part three is electricity. *Stars* mark straight→ terms, _underscores_ textbook terms.")
doc=("CURRENTLY WINDING\n=================\n\n"+head+"\n\n"+note+"\n\n"
     "PART ONE: THE STRAIGHT DOPE\n===========================\n\n"+dope_body+"\n\n\n"
     "PART TWO: DOG MATH\n==================\n\n"+dog_body+"\n\n\n"+el_body+"\n")
open(OUT+f"Claude Currently Winding {stamp}.txt","w").write(doc)
