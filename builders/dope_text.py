#!/usr/bin/env python3
# Renders the straight dope as plain fixed-width text from the same story as the PDF.
# Written by Claude (Anthropic).
import re, html, textwrap, sys
from reportlab.platypus import Paragraph, Table, KeepTogether, PageBreak, Spacer

W = 78
src = open("/home/claude/out/build_dope2.py", encoding="utf-8").read()
src = src.replace("doc.build(S2)\nprint(OUT)", "")
ns = {"__file__": "/home/claude/out/build_dope2.py"}
exec(compile(src, "build_dope2.py", "exec"), ns)
S2, STAMP = ns["S2"], ns["STAMP"]

def clean(markup):
    t = re.sub(r"<br\s*/?>", "\n", markup)
    t = re.sub(r"<sub>(.*?)</sub>", r"_\1", t)
    t = re.sub(r"<font color='#c8102e'>(.*?)</font>", r"*\1*", t)   # Straight-> terms (red in the PDF)
    t = re.sub(r"<font color='#0047ab'>(.*?)</font>", r"_\1_", t)   # textbook terms (blue in the PDF)
    t = re.sub(r"<[^>]+>", "", t)
    t = html.unescape(t).replace("\xa0", " ")
    return re.sub(r"[ \t]+", " ", t).strip()

NB = "\u2060"   # placeholder glue so short formulas don't break across lines
def wrap(t, width=W, indent=""):
    out = []
    for para in t.split("\n"):
        glued = re.sub(r" ([=×·/+−]) ", lambda m: NB + m.group(1) + NB, para)
        glued = re.sub(r"\b(Table|Tables|row|rows|section) (\d)", lambda m: m.group(1) + NB + m.group(2), glued)
        sub = indent + ("  " if para.startswith("• ") else "")
        lines = textwrap.wrap(glued, width=width, initial_indent=indent,
                              subsequent_indent=sub, break_on_hyphens=False) or [indent.rstrip()]
        out += [l.replace(NB, " ") for l in lines]
    return out

COLORS = ("*Red* Straight→ terms, _blue_ textbook terms.",
          "*Stars* mark Straight→ terms (red in the PDF), _underscores_ textbook terms (blue in the PDF).")
def cellwrap(t, width):
    lines = []
    for para in t.split("\n"):
        for l in (textwrap.wrap(para, width=width, break_long_words=False, break_on_hyphens=False) or [""]):
            while len(l) > width:              # a word longer than the column: hyphenate it
                lines.append(l[:width - 1] + "-"); l = l[width - 1:]
            lines.append(l)
    return lines

def ptext(p): return clean(p.text).replace(*COLORS)

def table_cells(t):
    return [[(ptext(c) if isinstance(c, Paragraph) else ("" if c in ("", None) else str(c)))
             for c in row] for row in t._cellvalues]

def render_grid(rows):
    n = len(rows[0])
    natural = [max(max((len(w) for w in re.split(r"[ \n]", r[i]) if w), default=1) for r in rows) for i in range(n)]
    widths = [max(4, x) for x in natural]
    # widen columns to fill W while staying under it
    total = lambda: sum(widths) + 2 * n + 1
    while total() < W:
        full = [max(len(l) for l in r[i].split("\n")) for r in rows for i in [None] if False] or None
        # give a char to the column whose longest line most exceeds its width
        need = [max(max(len(l) for l in r[i].split("\n")) for r in rows) - widths[i] for i in range(n)]
        i = max(range(n), key=lambda k: need[k])
        if need[i] <= 0: break
        widths[i] += 1
    while total() > W + 2:                  # tables may run to 80 columns; too wide: narrow the widest column, words break
        slack = [widths[k] - natural[k] for k in range(n)]   # shrink where no word breaks first
        i = max(range(n), key=lambda k: (slack[k] > 0, slack[k] if slack[k] > 0 else widths[k]))
        widths[i] -= 1
    sep = "+" + "+".join("-" * (w + 1) for w in widths) + "+"
    out = [sep]
    for ri, r in enumerate(rows):
        cells = [cellwrap(r[i], widths[i]) for i in range(n)]
        h = max(len(c) for c in cells)
        for k in range(h):
            out.append("|" + "|".join(" " + (cells[i][k] if k < len(cells[i]) else "").ljust(widths[i]) for i in range(n)) + "|")
        out.append(sep if ri == 0 or ri == len(rows) - 1 else sep.replace("-", "-"))
    return out

out = []
def emit(lines): out.extend(lines)

def walk(f):
    if isinstance(f, KeepTogether):
        for g in f._content: walk(g)
    elif isinstance(f, PageBreak):
        pass
    elif isinstance(f, Spacer):
        pass
    elif isinstance(f, Paragraph):
        name = f.style.name
        t = ptext(f)
        if name == "h1":
            emit([t.upper(), "=" * len(t), ""])
        elif name == "h2":
            emit(["", t, "-" * len(t), ""])
        elif name == "h3":
            emit([""] + wrap(t, W) + [""])
        elif name in ("formula", "formt"):
            emit(wrap(t, W, " " * 8))
        elif name in ("defn",):
            emit([""] + wrap(t, W, "  "))
        else:
            emit(wrap(t, W)); emit([""])
    elif isinstance(f, Table):
        cells = table_cells(f)
        if len(cells) == 1 and len(cells[0]) == 1:          # a rule box
            body = wrap(cells[0][0], W - 4)
            bar = "+" + "-" * (W - 2) + "+"
            emit([bar] + ["| " + l.ljust(W - 4) + " |" for l in body] + [bar, ""])
        elif len(cells) == 2 and len(cells[0]) == 2 and cells[1][0] == "":   # a cell definition
            coord, sent, form = cells[0][0], cells[0][1], cells[1][1]
            lines = wrap(sent, W - 7)
            emit([coord.rjust(5) + "  " + lines[0]] + ["       " + l for l in lines[1:]])
            emit(wrap(form, W, " " * 11)); emit([""])
        else:
            emit(render_grid(cells)); emit([""])

for f in S2: walk(f)

txt = "\n".join(out)
txt = re.sub(r"\n{3,}", "\n\n", txt).strip() + "\n"
txt = txt.replace("Red Straight→ terms, blue textbook terms; no orange left.",
                  "(Plain text: the PDF's red marks Straight→ terms and its blue marks textbook terms; "
                  "here each textbook term is named as textbook, standard, or by its trade in its own entry.)")
# rewrap the header paragraph after the replacement
path = "/home/claude/out/Claude The Straight Dope %s.txt" % STAMP
open(path, "w", encoding="utf-8").write(txt)
print(path, max(len(l) for l in txt.splitlines()), "cols,", len(txt.splitlines()), "lines")
