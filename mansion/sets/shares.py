"""Path-aware choices for exact relationships, not universal fraction conversion.
Claude (Anthropic), 2026-10-23; extended and corrected by Codex (OpenAI).
R-130 removes padding; R-131 keeps rounded results decimal and uses useful units.
"""
import re
from decimal import Decimal
from fractions import Fraction
import path_features

NUM = re.compile(r"(?<![\d.⁰¹²³⁴⁵⁶⁷⁸⁹])(\d+)\.(\d+)(?![\d])")
PRE = [
    ("Here I/R² = 0.040/0.040 = 1.0 kg.",
     "Here I/R² is 40 g m² over 0.04 m², 1 kg."),
    ("The profile over R² is 0.020/0.040 = 1/2,",
     "The profile is 0.02 m², half of R², 0.04 m²,"),
    ("Setting that to 0.080 J gives", "Setting that to 80 mJ gives"),
    ("q₀²/(2C) = 0.080 J with", "q₀²/(2C) = 80 mJ with"),
    ("The loop on its own rings at the slow tone, 2.4 sweep, exactly.",
     "The loop on its own rings exactly at the slow tone, about 2.4 sweep."),
    ("ω² = 10(2 − √2) = 5.9 and 10(2 + √2) = 34",
     "ω² = 10(2 − √2) ≈ 5.9 and 10(2 + √2) ≈ 34"),
    ("The slow one takes τ/2.4 = 2.6 s and the fast one τ/5.8 = 1.1 s.",
     "The slow one takes τ/ω_a ≈ 2.6 s and the fast one τ/ω_b ≈ 1.1 s."),
    ("(2/3) × 2.4 = 1.6 and (3/2) × 2.4 = 3.6 sweep.",
     "(2/3)ω₀ ≈ 1.6 and (3/2)ω₀ ≈ 3.6 sweep."),
    ("ω_b − ω_a = 3.4 sweep", "ω_b − ω_a ≈ 3.4 sweep"),
    ("q₀ = √(2 × 1.7 × 0.080) = 0.52 C", "q₀ = √(2C × 80 mJ) ≈ 0.52 C"),
    ("q₀/C = 0.31 V", "q₀/C ≈ 0.31 V"),
    ("10(2 − √2) = 5.9 s⁻²", "10(2 − √2) ≈ 5.9 s⁻²"),
    ("u/9 = 1.1 × 10⁷", "u/9 ≈ 1.1 × 10⁷"),
]

def decimal(value):
    """Finite rationals only; choosing a unit does not create a rounding."""
    n = Decimal(value.numerator) / Decimal(value.denominator)
    return format(n, "f").rstrip("0").rstrip(".") if n % 1 else str(int(n))

def compact_units(text):
    # A base of grams makes 40 and 500 visible; kilo absorbs 1000 and above.
    rx = r"(?<![\w./])(\d+/\d+|\d+(?:\.\d+)?)\s+(kg|g) m²(?P<spin>/s)?"
    def inertia(m):
        grams = Fraction(m[1]) * (1000 if m[2] == "kg" else 1)
        value, unit = (grams / 1000, "kg") if grams >= 1000 else (grams, "g")
        d = value.denominator
        for prime in (2, 5):
            while d % prime == 0:
                d //= prime
        if d != 1:
            return m[0]   # Do not round an exact third merely to change the unit.
        return decimal(value) + " " + unit + " m²" + (m["spin"] or "")
    text = re.sub(rx, inertia, text)
    def distance(m):
        mm = Fraction(m[1]) * 1000
        return f"{mm.numerator} mm" if mm.denominator == 1 and mm < 10 else m[0]
    return re.sub(r"(?<![\w./])(0\.\d+) m(?![²\w/])", distance, text)

def rounded(s, part, before, precision):
    if s in precision["rounded_literals"]:
        return True
    ctx = precision["contextual_roundings"].get(s)
    if ctx:
        if "exact_parts" in ctx:
            return part not in ctx["exact_parts"] or bool(re.search(ctx.get("rounded_after", r"(?!)"), before))
        return part in ctx.get("rounded_parts", [])
    return False

def convert(text, log=None, mode="fractions", part="", plan=None):
    """Keep authored approximation wording. Only selected exact relationships change."""
    assert mode in {"decimals", "fractions"}, mode
    config = path_features.feature("number-form", plan)
    precision = config["precision"]
    corrections = {Fraction(k): Fraction(v) for k,v in precision["corrected_exact"].items()}
    chosen = {Fraction(v) for rule in config["fraction_choices"] if part in rule["parts"] for v in rule["values"]}
    for old, new in PRE:
        text = text.replace(old, new)
    text = compact_units(text)
    def number(m):
        s = m[0]; value = Fraction(s)
        if value in corrections:
            value = corrections[value]
        new = decimal(value)
        before, after = text[:m.start()], text[m.end():]
        approximate = bool(re.search(r"(?:about|near|≈)\s*$", before)) or rounded(s, part, before, precision)
        use_fraction = mode == "fractions" and not approximate and value in chosen and value.denominator <= config["maximum_denominator"]
        if use_fraction:
            new = str(value)
            prev, nxt = before.rstrip()[-1:], after.lstrip()[:1]
            if (prev and prev in "×/") or (nxt and nxt in "×/") or after[:1] in "²√(":
                new = f"({new})"
        if log is not None and new != s:
            log.append((s, new, text[max(0,m.start()-50):m.end()+30]))
        return new
    return NUM.sub(number, text)

def apply(items, log=None, path=4, plan=None):
    plan = plan or path_features.load()
    reached, part, out = set(), "", []
    for tag, text in items:
        if isinstance(text, str):
            if tag in {"h1", "h2", "h3"}:
                part = ""
            m = re.match(r"^\((\d+-[a-zαβγ]|[a-gαβγ]-\d+)\)", text)
            if m:
                part = m[1]; reached.add(part)
            mode = path_features.mode_at("number-form", path, reached, plan)
            text = convert(text, log, mode, part, plan)
        out.append((tag, text))
    return out

if __name__ == "__main__":
    import build_sets
    for k in (1,2,3,4):
        log=[]
        apply(build_sets.build(k, shares=False), log, path=k)
        print(f"== path {k}: {len(log)} changes")
        for s,new,ctx in log:
            print(f"  {s} -> {new} | {ctx}")
