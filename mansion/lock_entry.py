"""Replaces Claude's Goals lock line with a finished entry, and appends lines to Phrases and motifs, in one batch.

Claude (Anthropic), 2026-10-21. Usage: python3 lock_entry.py SAVED_READ SPEC.json
SPEC: {"goals": [[kind, text], ...], "tab": [[kind, text], ...]}; kind H (heading), P (Claude), Q (doc, red).
"""
import json, sys
c = json.load(open(sys.argv[1])); c = c.get("content", c)
spec = json.load(open(sys.argv[2]))
COL = {"H": {"red": 0.8, "green": 0.34901962, "blue": 0.0},
       "P": {"red": 0.7058824, "green": 0.3254902, "blue": 0.03529412},
       "Q": {"red": 0.4, "green": 0.0, "blue": 0.0}}
GOALS, TAB = "t.89r88yxpo4v3", "t.i5p9a4r26buw"
tabs = {t["tabProperties"]["tabId"]: t for t in c["tabs"]}
def styled(tid, pos, E, reqs):
    for k, t in E:
        end = pos + len(t)
        reqs.append({"updateParagraphStyle": {"range": {"startIndex": pos, "endIndex": end + 1, "tabId": tid},
                     "paragraphStyle": {"namedStyleType": "NORMAL_TEXT"}, "fields": "namedStyleType"}})
        reqs.append({"updateTextStyle": {"range": {"startIndex": pos, "endIndex": end, "tabId": tid},
                     "textStyle": {"bold": k == "H", "italic": False, "foregroundColor": {"color": {"rgbColor": COL[k]}}},
                     "fields": "bold,italic,foregroundColor"}})
        pos = end + 1
reqs = []
E = spec.get("tab") or []
if E:   # tab first: separate tab, independent indices
    at = tabs[TAB]["documentTab"]["body"]["content"][-1]["endIndex"] - 1
    reqs.append({"insertText": {"text": "".join("\n" + t for k, t in E), "location": {"index": at, "tabId": TAB}}})
    styled(TAB, at + 1, E, reqs)
paras = [s for s in tabs[GOALS]["documentTab"]["body"]["content"] if "paragraph" in s]
def ptext(x): return "".join(e["textRun"]["content"] for e in x["paragraph"]["elements"] if "textRun" in e)
last = next(x for x in reversed(paras) if ptext(x).startswith("This is a lock. Claude"))
assert all(not ptext(x).strip() for x in paras[paras.index(last) + 1:]), "text after the lock"
s0, s1 = last["startIndex"], last["endIndex"] - 1
E = spec["goals"]
text = "\n".join(t for k, t in E)
reqs += [{"deleteContentRange": {"range": {"startIndex": s0, "endIndex": s1, "tabId": GOALS}}},
         {"insertText": {"text": text, "location": {"index": s0, "tabId": GOALS}}}]
styled(GOALS, s0, E, reqs)
assert all(ord(ch) < 0x10000 for ch in json.dumps(spec, ensure_ascii=False))
print(c["revisionId"], file=sys.stderr)
print(json.dumps(reqs, ensure_ascii=False))
