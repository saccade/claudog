"""Check a copied tab against its source: every paragraph's text, paragraph style, bullet, and character styles.

Claude (Anthropic), 2026-10-23. Usage: python3 compare_tab.py SRC_READ SRC_TAB DST_READ DST_TAB [--relink OLD=NEW ...]
Empty paragraphs right before a table are ignored (inserting a table adds one). Exit 1 on any difference.
"""
import json, sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from copy_tab import tab, body_items, textstyle, relinks, PS

def flat(dt, rl, img_ok=True):
    out = []
    def paras(items, where):
        for el in items:
            if "table" in el:
                if out and out[-1][1] == "" : out.pop()
                for r, row in enumerate(el["table"]["tableRows"]):
                    for c, cell in enumerate(row["tableCells"]):
                        paras([p for p in cell["content"] if "paragraph" in p], f"{where}cell{r},{c} ")
                continue
            p = el["paragraph"]; t = ""; chars = []
            for e in p["elements"]:
                if "textRun" in e:
                    s = e["textRun"]["content"]; st = json.dumps(textstyle(e["textRun"].get("textStyle", {}), rl), sort_keys=True)
                    t += s; chars += [st] * len(s)
                elif "inlineObjectElement" in e: t += "￼"; chars.append("img")
            ps = {k: v for k, v in p.get("paragraphStyle", {}).items() if k in PS}
            if "bullet" in p: ps = {k: v for k, v in ps.items() if not k.startswith("indent")}
            # a newline's own style is invisible; drop it from the comparison
            out.append((where, t.rstrip("\n"), json.dumps(ps, sort_keys=True), bool(p.get("bullet")), chars[:len(t.rstrip("\n"))]))
    paras(body_items(dt), "")
    while out and out[-1][1] == "": out.pop()
    return out

if __name__ == "__main__":
    rl = relinks()
    a = flat(tab(sys.argv[1], sys.argv[2]), rl); b = flat(tab(sys.argv[3], sys.argv[4]), {})
    bad = []
    if len(a) != len(b): bad.append(f"paragraph count {len(a)} vs {len(b)}")
    for x, y in zip(a, b):
        if x[1] != y[1]: bad.append(f"text: {x[0]}{x[1][:50]!r} vs {y[1][:50]!r}"); continue
        if x[2] != y[2]: bad.append(f"para style: {x[1][:40]!r} {x[2]} vs {y[2]}")
        if x[3] != y[3]: bad.append(f"bullet: {x[1][:40]!r}")
        if x[4] != y[4]:
            i = next(i for i in range(min(len(x[4]), len(y[4]))) if x[4][i] != y[4][i]) if any(p != q for p, q in zip(x[4], y[4])) else 0
            bad.append(f"char style at {i} of {x[1][:40]!r}: {x[4][i] if i < len(x[4]) else ''} vs {y[4][i] if i < len(y[4]) else ''}")
    print(sys.argv[4], "|", len(b), "paragraphs |", "OK" if not bad else bad[:12])
    sys.exit(1 if bad else 0)
