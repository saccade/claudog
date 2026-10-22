"""Inserts a Claude entry into the Mansion doc's Goals tab after a given paragraph, colored per doc's 2026-10-22 recoloring.

Claude (Anthropic), 2026-10-22. Usage: python3 goals_append.py SPEC.json AT > reqs.json
SPEC: [[kind, text], ...]; kind H (Claude heading, bold orange), P (Claude, orange), Q (doc's chat quoted, red 0.6).
AT: the index to insert at (the start of the paragraph that should follow the entry).
"""
import json, sys
COL = {"H": {"red": 0.8, "green": 0.34901962, "blue": 0.0}, "P": {"red": 0.8, "green": 0.34901962, "blue": 0.0},
       "Q": {"red": 0.6, "green": 0.0, "blue": 0.0}}
G = "t.89r88yxpo4v3"
E = json.load(open(sys.argv[1])); at = int(sys.argv[2])
text = "".join(t + "\n" for k, t in E)
assert all(ord(ch) < 0x10000 for ch in text)
reqs = [{"insertText": {"text": text, "location": {"index": at, "tabId": G}}}]
pos = at
for k, t in E:
    end = pos + len(t)
    reqs.append({"updateParagraphStyle": {"range": {"startIndex": pos, "endIndex": end + 1, "tabId": G}, "paragraphStyle": {"namedStyleType": "NORMAL_TEXT"}, "fields": "namedStyleType"}})
    reqs.append({"updateTextStyle": {"range": {"startIndex": pos, "endIndex": end, "tabId": G}, "textStyle": {"bold": k == "H", "italic": False, "foregroundColor": {"color": {"rgbColor": COL[k]}}}, "fields": "bold,italic,foregroundColor"}})
    pos = end + 1
print(json.dumps(reqs, ensure_ascii=False))
