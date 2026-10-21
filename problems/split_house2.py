import sys,re,textwrap
src_file,s,d=sys.argv[1:4]
blocks=open(src_file).read().split("\n\n")
W=lambda x: textwrap.fill(" ".join(x.split()),66)
out_sol=[]; out_prob=[]; st=False
for k,b in enumerate(blocks):
    if re.match(r"^[1-5]\. .+\n-+$",b): out_prob.append(b); out_sol.append(b); st=True; continue
    if st and b.startswith("    "): out_prob.append(b); continue
    st=False
    if k<2: continue
    out_sol.append(b)
src_par=[b for b in blocks if b.startswith("Source:")][0]
hp=W(f"Written by Claude (Anthropic), {d}. The five problems of The Second House, statements only; the worked solutions are in The Second House: Solutions {s}. Not doc's text.")
hs=W(f"Written by Claude (Anthropic), {d}. Worked solutions to the five problems in The Second House: Problems {s}, in stealth mode: each one starts in the textbook's terms and ends a little further into dr. kraemer's straight-> mechanics vocabulary. Not doc's manuscript text; the ideas and vocabulary are his, these words are the model's.")
open(f"Claude The Second House Problems {s}.txt","w").write("THE SECOND HOUSE: PROBLEMS\n==========================\n\n"+hp+"\n\n"+"\n\n".join(out_prob)+"\n\n"+src_par.rstrip()+"\n")
open(f"Claude The Second House Solutions {s}.txt","w").write("THE SECOND HOUSE: SOLUTIONS\n===========================\n\n"+hs+"\n\n"+"\n\n".join(out_sol).rstrip()+"\n")
