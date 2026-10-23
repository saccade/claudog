"""Write a workbook tab from a small markup file. Claude (Anthropic), 2026-10-23, for the workbook move.

Usage: python3 md_tab.py FILE.md TAB_ID [--base orange|green|none] > batch.json   (the tab must be empty)
Lines (one paragraph each; blank lines are skipped):
  # / ## / ###   headings          ~ text   italic note          > text   doc's words, his red
  - text         bullet            -- text  nested bullet        + text   numbered item
  anything else  a plain paragraph, in the --base color
Inline: **bold**, [text](url), {r}doc's red{/r}. A url "tab:KEY" means this workbook's tab KEY (ids.py).
"""
import json, re, sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from ids import tab_url

RED = {"red": 0.6, "green": 0, "blue": 0}
COLORS = {"orange": {"red": 0.8, "green": 0.34901962, "blue": 0}, "green": {"red": 0.015686275, "green": 0.16470589, "blue": 0.05882353}}
u16 = lambda s: len(s.encode("utf-16-le")) // 2
INLINE = re.compile(r"\*\*(.+?)\*\*|\[(.+?)\]\((.+?)\)|\{r\}(.+?)\{/r\}")

def parse(line):
    """Returns plain text and a list of (start, end, style) in UTF-16 units within the line."""
    out = ""; marks = []; pos = 0
    for m in INLINE.finditer(line):
        out += line[pos:m.start()]; a = u16(out)
        if m.group(1) is not None: out += m.group(1); marks.append((a, u16(out), {"bold": True}))
        elif m.group(2) is not None:
            url = m.group(3); url = tab_url(url[4:]) if url.startswith("tab:") else url
            out += m.group(2); marks.append((a, u16(out), {"link": {"url": url}}))
        else: out += m.group(4); marks.append((a, u16(out), {"foregroundColor": {"color": {"rgbColor": RED}}}))
        pos = m.end()
    return out + line[pos:], marks

def build(lines, tab, base):
    paras = []
    for raw in lines:
        line = raw.rstrip("\n")
        if not line.strip(): continue
        for pre, kind in (("### ", "h3"), ("## ", "h2"), ("# ", "h1"), ("~ ", "note"), ("> ", "doc"), ("-- ", "li2"), ("- ", "li"), ("+ ", "num")):
            if line.startswith(pre): paras.append((kind, line[len(pre):])); break
        else: paras.append(("p", line))
    text = ""; spans = []
    for kind, t in paras:
        body, marks = parse(t)
        if kind == "li2": body = "\t" + body; marks = [(a + 1, b + 1, s) for a, b, s in marks]
        a = 1 + u16(text); text += body + "\n"
        spans.append((kind, a, a + u16(body), [(a + x, a + y, s) for x, y, s in marks]))
    reqs = [{"insertText": {"location": {"index": 1, "tabId": tab}, "text": text}}]
    named = {"h1": "HEADING_1", "h2": "HEADING_2", "h3": "HEADING_3"}
    for kind, a, b, marks in spans:
        reqs.append({"updateParagraphStyle": {"range": {"startIndex": a, "endIndex": b + 1, "tabId": tab},
                     "paragraphStyle": {"namedStyleType": named.get(kind, "NORMAL_TEXT")}, "fields": "namedStyleType"}})
        st = {}
        if kind == "doc": st["foregroundColor"] = {"color": {"rgbColor": RED}}
        elif base in COLORS and kind not in named: st["foregroundColor"] = {"color": {"rgbColor": COLORS[base]}}
        if kind == "note": st["italic"] = True
        if st and b > a: reqs.append({"updateTextStyle": {"range": {"startIndex": a, "endIndex": b, "tabId": tab}, "textStyle": st, "fields": ",".join(st)}})
        for x, y, s in marks:
            reqs.append({"updateTextStyle": {"range": {"startIndex": x, "endIndex": y, "tabId": tab}, "textStyle": s, "fields": ",".join(s)}})
    runs = []   # bullet runs, applied last to first: nesting tabs are removed and shift what follows
    i = 0
    while i < len(spans):
        k = spans[i][0]
        if k in ("li", "li2", "num"):
            j = i; group = ("num",) if k == "num" else ("li", "li2")
            while j + 1 < len(spans) and spans[j + 1][0] in group: j += 1
            runs.append((spans[i][1], spans[j][2], "NUMBERED_DECIMAL_ALPHA_ROMAN" if k == "num" else "BULLET_DISC_CIRCLE_SQUARE")); i = j
        i += 1
    for a, b, preset in reversed(runs):
        reqs.append({"createParagraphBullets": {"range": {"startIndex": a, "endIndex": b, "tabId": tab}, "bulletPreset": preset}})
    return reqs

if __name__ == "__main__":
    base = sys.argv[sys.argv.index("--base") + 1] if "--base" in sys.argv else "none"
    print(json.dumps(build(open(sys.argv[1]).readlines(), sys.argv[2], base), ensure_ascii=True, separators=(",", ":")))
