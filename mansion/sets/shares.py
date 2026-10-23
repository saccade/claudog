"""No trailing zeros, and fractions wherever a fraction is the true value (doc, 10-23 10:23 and 10:42, R-129).
Claude (Anthropic), 2026-10-23. build_sets applies this last, to every path.
  - Two-figure padding goes: 6.0 N is 6 N, 0.040 is 0.04, 1.0 × 10⁸ is 10⁸.
  - An exact value standing alone as a quantity is written as a fraction: 0.50 m is 1/2 m, 0.040 kg m² is 1/25 kg m²,
    1.5 is 3/2, 0.75 N m is 3/4 N m. Exact means it was padded, or it's a half or a quarter, or it's listed in EXACT.
  - Other decimals (0.12 m, 2.4 m, rounded results like 0.32 m/s) and anything after "about" stay decimals.
  - Inside arithmetic (next to × or /) a fraction takes parentheses: 0.50 × 4.0/0.60 reads (1/2) × 4/(3/5).
Usage: python3 shares.py   (from mansion/sets: prints every change, in context, for review)
"""
import re
from fractions import Fraction

DENOMS = {2, 4, 5, 8, 10, 20, 25, 50}
PRE = [   # sentences whose arithmetic reads better said than divided out
    ("Here I/R² = 0.040/0.040 = 1.0 kg.", "Here I/R² is 1/25 kg m² over 1/25 m², 1 kg."),
    ("The profile over R² is 0.020/0.040 = 1/2,", "The profile, 1/50 m², is half of R², 1/25 m²,"),
    ("Setting that to 0.080 J gives", "Setting that to 80 mJ gives"),
    ("q₀²/(2C) = 0.080 J with", "q₀²/(2C) = 80 mJ with"),
]
EXACT = {"0.38": "3/8", "0.05": "1/20"}   # 0.375 N m shown rounded; the conductance 1/R of 20 Ω
NUM = re.compile(r"(?<![\d.⁰¹²³⁴⁵⁶⁷⁸⁹])(\d+)\.(\d+)(?![\d])")

def convert(text, log=None):
    """Two-figure padding goes; a value that's exact becomes a fraction when it stands alone as a quantity.
    Exact means: it carried a padding zero (0.40, 6.0), or it's a half or a quarter (1.5, 0.75), or it's in EXACT.
    Other decimals (0.12, 2.4, 0.32) are measurements or roundings and stay. Inside arithmetic (next to × or /)
    a value only loses its padding, so 0.50 × 4.0/0.60 reads 0.5 × 4/0.6."""
    for a0, b0 in PRE: text = text.replace(a0, b0)
    out = []; pos = 0
    for m in NUM.finditer(text):
        a, b = m.span(); s = m.group(0); whole, dec = m.groups()
        before = text[max(0, a - 7):a]
        approx = "about" in before or "≈" in before or "near" in before
        stripped = dec.rstrip("0")
        padded = stripped != dec
        new = whole if not stripped else f"{whole}.{stripped}"
        prev = text[:a].rstrip()[-1:]; nxt = text[b:].lstrip()[:1]
        in_math = prev in "×/" or nxt in "×/" or text[b:b + 1] == "/"
        mantissa = re.match(r"\s*×\s*10", text[b:]) is not None
        exact = padded or stripped in ("5", "25", "75") or s in EXACT
        if not approx and not mantissa and exact and stripped:
            f = EXACT.get(s) or (lambda F: f"{F.numerator}/{F.denominator}" if F.denominator in DENOMS else None)(Fraction(new))
            if f:
                new = f
                if in_math or text[b:b + 1].isalpha() or text[b:b + 1] in "²√(":
                    new = f"({new})"
        if new == "1" and mantissa:   # 1 × 10⁸ is 10⁸
            new = ""; b = b + len(re.match(r"\s*×\s*", text[b:]).group(0))
        if new == s: continue
        out.append(text[pos:a]); out.append(new); pos = b
        if log is not None: log.append((s, new, text[max(0, a - 50):b + 30]))
    out.append(text[pos:])
    return "".join(out)

def apply(items, log=None):
    return [(t, convert(x, log) if isinstance(x, str) else x) for t, x in items]

if __name__ == "__main__":
    import build_sets
    for k in (1, 2, 3, 4):
        log = []
        apply(build_sets.build(k, shares=False), log)
        print(f"== path {k}: {len(log)} changes")
        for s, new, ctx in log: print(f"  {s} -> {new or '(dropped)'}   | {ctx}")
