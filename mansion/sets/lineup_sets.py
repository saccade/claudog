"""Lays the four Mansion solution sets out as four folders of matching pieces, for lineup.

Claude (Anthropic), 2026-10-22. Each set (build_sets.build) is cut at its room and problem
headings into one Markdown file per piece. A piece has the same file name in every set it
appears in, numbered in the whole house's order, so lineup's side-by-side view lines the same
part up across the four levels. Prose is one sentence per line, so a change highlights the
sentence that changed rather than the whole paragraph.
Usage: python3 lineup_sets.py OUTDIR   (writes OUTDIR/set1 .. set4 and OUTDIR/overview.md)
"""
import os, re, shutil, sys
import build_sets

def key(t, s):
    """A name for the piece that's the same in every set."""
    if t == "h2":
        if s.startswith("Ending"): return "ending"
        return s.lower()
    m = re.match(r"(\d+)\. (.*)", s)
    if m: return f"problem {m.group(1)}, {m.group(2).lower()}"
    m = re.match(r"(Drawer [a-g]|Mirror \d|[αβγ]):", s)   # the problem set's labels since sweep 2
    tag = m.group(1)
    if tag.startswith("Mirror"): return f"funhouse {tag.lower()}"
    if tag in "αβγ": return f"under the stage {tag}"
    return tag.lower()

def pieces(k):
    items = build_sets.build(k)
    out, cur, words = [], None, []
    pending = []          # the chair paragraph leads into problem 13 in every set
    for t, s in items:
        if t == "h1": continue
        if cur is None and t != "h2":
            words.append((t, s)); continue
        if t == "i" and s.startswith("In the chair’s frame"):
            pending.append((t, s)); continue
        if t in ("h2", "h3"):
            cur = [key(t, s), [(t, s)] + pending]; pending = []
            out.append(cur)
        else:
            cur[1].append((t, s))
    return words, out

SPLIT = re.compile(r"(?<=[.?!”])\s+(?=[A-Z(“\"0-9−√])")

def md(t, s):
    s = re.sub(r"</?b>", "**", s)
    if t == "h2": return f"# {s}"
    if t == "h3": return f"## {s}"
    if t == "b": return f"**{s}**"
    if t == "eq": return f"    {s}"
    lines = []
    for x in SPLIT.split(s):   # keep a part's number on its line: "1. Find ..."
        if lines and re.fullmatch(r"\d+\.", lines[-1]): lines[-1] += " " + x
        else: lines.append(x)
    if t == "i": lines = [f"*{x}*" for x in lines]
    return "\n".join(lines)

def main(outdir):
    sets = {k: pieces(k) for k in (1, 2, 3, 4)}
    order = {name: i for i, (name, _) in enumerate(sets[4][1], start=1)}
    for k, (words, ps) in sets.items():
        d = os.path.join(outdir, f"set{k}")
        shutil.rmtree(d, ignore_errors=True); os.makedirs(d)
        with open(os.path.join(d, "00 header.md"), "w") as f:
            f.write("\n\n".join(md(t, s) for t, s in words) + "\n")
        for name, body in ps:
            n = order[name] if name != "ending" else 99
            with open(os.path.join(d, f"{n:02d} {name}.md"), "w") as f:
                f.write("\n\n".join(md(t, s) for t, s in body) + "\n")
        print(k, len(ps) + 1, "files")

if __name__ == "__main__":
    main(sys.argv[1])
