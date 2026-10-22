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
