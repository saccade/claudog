import re, itertools, sys
docs = {k: open(f"/root/archaeology/artifact_{k}.txt", encoding="utf-8").read() for k in "ABCD"}
def sh(t, n=6):
    w = re.findall(r"[a-zA-Z']+", t.lower())
    return set(tuple(w[i:i+n]) for i in range(len(w)-n+1))
S = {k: sh(v) for k, v in docs.items()}
for a, b in itertools.combinations("ABCD", 2):
    i = len(S[a] & S[b]); print(a, b, i, round(i/min(len(S[a]), len(S[b])), 3))
for k, v in docs.items():
    words = re.findall(r"[a-zA-Z']+", v.lower())
    print(k, "words", len(words), "lines", v.count("\n"),
          {w: len(re.findall(r"\b"+w+r"\b", v, re.I)) for w in
           ["we'll call","call","lagrange","kirchhoff","lorentz","telegrapher","mode","modes","potential","frequency","turn","turns","ledger","ledgers","centre","center","metre","meter","meters","travelling","traveling","moon","earth","fluxion","ghost","standard","textbook","book"]})
