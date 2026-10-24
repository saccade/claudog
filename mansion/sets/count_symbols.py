"""Symbols per solution: the four paths against a standard solutions-manual write-up of the same 44 main parts.
Claude (Anthropic), 2026-10-24, for doc (11:42): "the solution sets have a lot more characters in them than a standard
textbook set, but do they have more symbols? like, if zinging is one symbol, it's doing a fair bit of work there."
Usage: python3 count_symbols.py   (from mansion/sets, after build_sets.py)

A symbol is one token, counted the same way in words and in math:
  a word (hyphenated or with an apostrophe, still one), a number (2.4, 1×10⁸, ½), a variable with its subscript or
  prime (ω₀, T_a, L′), a unit (m, J, rad), an operator or relation (= + − × / · √ ≈ ⇒ ≤ < > :), an exponent (² ⁻¹),
  an arrow (→ ↑ ↺). Punctuation and brackets aren't counted, in either kind of text: commas and parentheses both group.
Function words (the, of, is, …) are counted, and also reported separately, since they do the gluing that brackets
and operators do in algebra.
A path's solution to a part is its labeled paragraph plus the paragraphs after it, up to the next label or heading,
leaving out the story: whole-italic paragraphs and paragraphs that echo a scene of the problem set.
"""
import difflib, html, re

MAIN = [f"{p}-{s}" for p, n in zip(range(1, 14), (4, 3, 4, 3, 3, 3, 3, 3, 3, 4, 3, 4, 4)) for s in "abcd"[:n]]
FUNC = set("""a an the of to in on at by for from with as and or but nor so if then than that this these those it its
it's is are was were be been being has have had do does did not no there here what which who whom whose where when
why how all each every both either any some one's into onto out up down over under about against between through
same other just only also too very can can't could would should will won't must may might isn't aren't doesn't
don't that's there's here's let's""".split())

TOKEN = re.compile(r"""
   \d+(?:\.\d+)?(?:\s?×\s?10[⁻⁰¹²³⁴⁵⁶⁷⁸⁹]+)?      # number, with scientific notation as one value
 | [½⅓¼⅔¾]                                        # vulgar fractions are numbers
 | [A-Za-zΑ-Ωα-ωϑϕℓħ∂Δȧẋẏ][A-Za-zΑ-Ωα-ω]*(?:[’'][a-z]+)*(?:-[A-Za-z]+)*(?:_[A-Za-z0-9]+|[₀-₉₊₋ₐ-ₜ]+)?[′]?[̇]?  # word or variable
 | [⁻]?[⁰¹²³⁴⁵⁶⁷⁸⁹]+                              # exponent
 | [=+−×/·√≈⇒≤≥<>:%∝]                              # operators and relations
 | [→←↑↓↺↻]                                       # arrows
""", re.X)

UNITS = set("J mJ nJ kg g m mm s W N rad Hz MHz V A C F H Ω ohm mho amp".split())
FUNCS = {"cos", "sin", "gcd", "emf"}
GLUED = set("Fr fR mv LC pc vt CV Mc mg ma mvr RC dt gh mL mR mgh GV VI dx dy Li CU Pt".split())   # products, written run together
PIECE = re.compile(r"Δ|[A-Za-zα-ωΑ-Ωℓȧẋẏ](?:_[A-Za-z0-9]+|[₀-₉₊₋]+)?[′]?[̇]?")

def tokens(text):
    out = []
    for x in TOKEN.findall(text):
        base = re.sub(r"(_[A-Za-z0-9]+|[₀-₉₊₋]+|′|̇)", "", x)
        if x in GLUED or (len(base) > 1 and re.search(r"[α-ωΑ-ΩℓΔ]", base) and base not in FUNCS):
            out += PIECE.findall(x)
        else:
            out.append(x)
    return out

def count(text):
    t = tokens(text)
    words = []
    for i, x in enumerate(t):
        nxt = t[i + 1] if i + 1 < len(t) else ""; prv = t[i - 1] if i else ""
        if x in UNITS or x in FUNCS: continue
        if re.fullmatch(r"[A-Za-z]{2,}(?:[’'][a-z]+)*(?:-[A-Za-z]+)*", x) or (x in ("a", "A", "I") and nxt not in "=+−×/·" and prv not in "=+−×/·"):
            words.append(x)
    func = [x for x in words if x.lower().replace("’", "'") in FUNC]
    return len(t), len(words), len(func)

def scenes():
    tex = open("../pset/mansion_pset.tex").read()
    return [re.sub(r"\\[a-z]+|[{}`']", "", s) for s in re.findall(r"\\scene\{([^}]*)\}", tex)]

def path_parts(k, sc):
    paras = re.findall(r"<(p|h2|h3)[^>]*>(.*?)</\1>", open(f"set{k}.html").read(), re.S)
    out, cur = {}, None
    for tag, body in paras:
        plain = html.unescape(re.sub(r"<[^>]+>", "", body)).strip()
        if tag != "p": cur = None; continue
        m = re.match(r"\(([^)]+)\)", plain)
        if m: cur = m.group(1); out[cur] = [plain[m.end():]]; continue
        if cur is None: continue
        if re.fullmatch(r"\s*<i>.*</i>\s*", body, re.S): continue
        if any(difflib.SequenceMatcher(None, plain[:80], s[:80]).ratio() > 0.6 for s in sc): continue
        out[cur].append(plain)
    return out

std = {}
for line in open("standard_solutions.txt"):
    m = re.match(r"\(([^)]+)\)\s*(.*)", line)
    if m: std[m.group(1)] = m.group(2)
sc = scenes()
paths = {k: path_parts(k, sc) for k in (1, 2, 3, 4)}
assert all(p in std for p in MAIN), [p for p in MAIN if p not in std]

rows = [("standard", {p: std[p] for p in MAIN})] + [(f"path {k}", {p: " ".join(paths[k].get(p, [])) for p in MAIN}) for k in (1, 2, 3, 4)]
print(f"{'':10} {'symbols':>8} {'words':>6} {'glue':>5} {'math':>5} {'chars':>7}  symbols/part")
for name, d in rows:
    T = W = F = C = 0
    for p in MAIN:
        t, w, f = count(d[p]); T += t; W += w; F += f; C += len(d[p])
    print(f"{name:10} {T:8d} {W:6d} {F:5d} {T - W:5d} {C:7d}  {T / len(MAIN):6.0f}")
print("\nper problem (symbols): " + "  ".join(f"{n}" for n in range(1, 14)))
for name, d in rows:
    per = [sum(count(d[p])[0] for p in MAIN if p.split("-")[0] == str(n)) for n in range(1, 14)]
    print(f"{name:10} " + " ".join(f"{x:5d}" for x in per))
