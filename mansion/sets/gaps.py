"""Where each term is used and glossed along each solution path, and how long the reader goes without it.

Claude (Anthropic), 2026-10-22, for doc's forgetting theory (R-117): a new thing gets a few uses in a row
so it settles; after a long gap it gets a nod; nothing re-glosses on a fixed beat. This measures the
solution text only (the paths are solutions now; statements live in the problem set), in reading order,
in characters. A "gloss" is a sentence that says what the term is (a heuristic: call / is the / that's /
means / we'll / read, near the term, or a colon right after it); the first use is always counted as one.
Usage: python3 gaps.py OUT.json
"""
import json, re, sys
import lineup_sets
import path_features

H = " "
TERMS = [  # name, regex, path where it first can appear
    ("↺ ↻ turning senses", r"[↺↻]", 1),
    ("→ ← straight arrows", r"[→←↑↓]", 1),
    ("the dot ·", r"·", 1),
    ("τ, the turn", r"τ", 1),
    ("stroke", r"\bstrokes?\b", 1),
    ("sweep", r"\bsweep", 1),
    ("χ, torque", r"χ", 1),
    ("heat-in, heat-out", r"heat-(?:in|out)", 1),
    ("own time", r"own time", 1),
    ("heft", r"\bheft", 2), ("punch", r"\bpunch", 2), ("hook", r"\bhook", 2),
    ("pickup", r"\bpick(?:up|s up|ing up| up)", 2), ("crank", r"\bcrank", 2), ("profile", r"\bprofile", 2),
    ("spin", r"\bspin\b", 2), ("can", r"\bcans\b|\b(?:the|a|its|this|one) can\b", 2), ("coil", r"\bcoil", 2),
    ("zip", r"\bzip", 3), ("zing", r"\bzing", 3), ("flip", r"\bflips?\b", 3), ("still point", r"still point", 3),
    ("tone, chord, beat", r"\b(?:tones?|chord|beats?)\b", 3), ("phase", r"\bphase", 3), ("trade", r"\btrad(?:e|ed|es)\b", 3),
    ("stripe", r"\bstripe", 3), ("shift, stretch", r"\bshift\b|\bthe stretch\b|\bstretch (?:is|of)\b", 3),
    ("zow, zlow", r"\bz[l]?ow(?:er)?s?\b", 4), ("zam, zlam", r"\bz[l]?am", 4), ("one machine", r"one machine", 4), ("tap", r"\btaps?\b", 4),
]
GLOSS = re.compile(r"\b(?:call(?:ed|s)?|is the|are the|that's the|that’s the|means|we'll|we’ll|is how|is what|stands for|its own sign|for short|the word|read)\b")
SENT = re.compile(r"(?<=[.?!])\s+(?=[A-Z(“0-9−√↺↻→←↑↓])")

WHOLE_PATH = True   # count the ending too: it's where the chorus pays a word off (Codex, 2026-10-22 15:05); False = workings only

def stream(k):
    """Solution sentences in reading order, then the path's ending: [(piece, sentence)]."""
    _, ps = lineup_sets.pieces(k)
    out = []
    for name, body in ps:   # the paths are solutions only since sweep 2: every p and eq is workings
        if name == "ending" and not WHOLE_PATH: continue
        for t, s in body:
            if t in ("p", "eq"):
                for x in SENT.split(re.sub(r"</?b>", "", s)): out.append((name, x))
    return out

def short(name):
    return (name.replace("problem ", "").replace("drawer ", "D").replace("funhouse ", "").replace("under the stage ", "")
            .split(",")[0])

def run(k):
    st = stream(k)
    pos, x, bounds = [], 0, []
    last = None
    for name, s in st:
        if name != last: bounds.append((x, short(name))); last = name
        pos.append(x); x += len(s) + 1
    total = x
    terms = []
    for tname, rx, lvl in TERMS:
        if lvl > k: continue
        r = re.compile(rx)
        hits = []
        for (name, s), p in zip(st, pos):
            for m in r.finditer(s):
                gm = [g.start() for g in GLOSS.finditer(s)]
                g = any(abs(a - m.start()) < 70 for a in gm) or s[m.end():m.end() + 3].startswith(":")
                hits.append({"at": p + m.start(), "piece": short(name), "gloss": g, "s": s[:220]})
        if not hits: continue
        hits[0]["gloss"] = True; hits[0]["first"] = True
        # collapse hits inside one sentence for gap purposes
        gaps = []
        for a, b in zip(hits, hits[1:]):
            d = b["at"] - a["at"]
            if d > 0: gaps.append({"from": a["at"], "to": b["at"], "len": d, "after": a["piece"], "back": b["piece"], "nod": b["gloss"]})
        terms.append({"name": tname, "level": lvl, "hits": hits, "gaps": gaps,
                      "glosses": sum(h["gloss"] for h in hits), "uses": len(hits)})
    return {"k": k, "total": total, "bounds": bounds, "terms": terms,
            "path_features": path_features.observe(lineup_sets.build_sets.build(k), k)}

if __name__ == "__main__":
    data = [run(k) for k in (1, 2, 3, 4)]
    json.dump(data, open(sys.argv[1], "w"), ensure_ascii=False)
    for d in data:
        print("path", d["k"], "chars", d["total"])
        for t in d["terms"]:
            long = [g for g in t["gaps"] if g["len"] > 4000]
            print(f"  {t['name']:22s} uses {t['uses']:3d} glosses {t['glosses']:2d} first {t['hits'][0]['piece']:>4s}  long gaps: "
                  + ", ".join(f"{g['after']}→{g['back']} {g['len']//1000}k{' nod' if g['nod'] else ''}" for g in long))
