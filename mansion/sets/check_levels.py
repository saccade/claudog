"""Flags words a solution set uses before its level brings them in. Claude (Anthropic), 2026-10-21."""
import re
HIGHER = {
 2: r"\bheft|\bpunch|\bhook|\bprofile|\bpick(s|ing)? ?up\b|\bpickup|\bcrank|\bspin\b|\bcans\b|\bcanned|\ba can\b|\bthe can\b|\bcoils\b|\bcoiled",
 3: r"\bzip|\bzing|still point|\bchord|\btone|\bstripe|\bphase|\bshift|\bstretch|Ω|\btrade|mirror pair",
 4: r"\bzam|\bzlam|\bzlow|\bzow|\bzower|\bzlower|\bTEST\b|\bRUN\b|one machine|in step|at random|\btap",
}
for k in (1, 2, 3):
    lines = open(f"set{k}.txt").read().split("\n")
    for lev in range(k + 1, 5):
        for i, ln in enumerate(lines, 1):
            for m in re.finditer(HIGHER[lev], ln):
                print(f"set{k} L{lev} line {i}: …{ln[max(0,m.start()-50):m.end()+30]}…")


# American spelling (R-083): flag British forms in any set, so they get switched as we go
import re as _re
BRIT = _re.compile(r"\b\w*(centre|metre|litre|colour|grey|favour|behaviour|labour|honour|neighbour|organis|realis|recognis|analys|travell|modell|programme|whilst|amongst|aluminium|tyre|defence|licence)\w*\b", _re.I)
for _k in (1, 2, 3, 4):
    for _n, _ln in enumerate(open(f"set{_k}.txt"), 1):
        for _m in BRIT.finditer(_ln):
            print(f"set{_k} British line {_n}: {_m.group(0)}")
