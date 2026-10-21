"""One-batch Goals relay (lock taken and passed in the same write) plus lines appended to Phrases and motifs.

Claude (Anthropic), 2026-10-21. Usage: python3 quick_relay.py SAVED_READ SPEC.json
SPEC: {"goals": [[kind, text], ...], "tab": [[kind, text], ...]}; kind is H, P (Claude) or Q (doc, red).
"""
import json, sys
c = json.load(open(sys.argv[1])); c = c.get("content", c)
spec = json.load(open(sys.argv[2]))
COL = {"H": {"red": 0.8, "green": 0.34901962, "blue": 0.0},
       "P": {"red": 0.7058824, "green": 0.3254902, "blue": 0.03529412},
       "Q": {"red": 0.4, "green": 0.0, "blue": 0.0}}
tabs = {t["tabProperties"]["tabId"]: t for t in c["tabs"]}
reqs = []
for tid, key in (("t.i5p9a4r26buw", "tab"), ("t.89r88yxpo4v3", "goals")):   # later tab first; indices are per tab anyway
    E = spec.get(key) or []
    if not E: continue
    at = tabs[tid]["documentTab"]["body"]["content"][-1]["endIndex"] - 1
    text = "".join("\n" + t for k, t in E)
    reqs.append({"insertText": {"text": text, "location": {"index": at, "tabId": tid}}})
    pos = at + 1
    for k, t in E:
        end = pos + len(t)
        reqs.append({"updateParagraphStyle": {"range": {"startIndex": pos, "endIndex": end + 1, "tabId": tid},
                     "paragraphStyle": {"namedStyleType": "NORMAL_TEXT"}, "fields": "namedStyleType"}})
        reqs.append({"updateTextStyle": {"range": {"startIndex": pos, "endIndex": end, "tabId": tid},
                     "textStyle": {"bold": k == "H", "italic": False, "foregroundColor": {"color": {"rgbColor": COL[k]}}},
                     "fields": "bold,italic,foregroundColor"}})
        pos = end + 1
    assert all(ord(ch) < 0x10000 for ch in text)
print(c["revisionId"], file=sys.stderr)
print(json.dumps(reqs, ensure_ascii=False))
