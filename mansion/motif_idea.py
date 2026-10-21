"""Appends one idea to the Phrases and motifs tab, in Claude's orange-brown. Also prints the Goals tail and the tab's paragraphs for checking.

Claude (Anthropic), 2026-10-21. Usage: python3 motif_idea.py SAVED_READ "idea text"
"""
import json, sys
d = json.load(open(sys.argv[1])); c = d.get("content", d)
BODY = {"red": 0.7058824, "green": 0.3254902, "blue": 0.03529412}
tabs = {t["tabProperties"]["tabId"]: t for t in c["tabs"]}
def paras(tid):
    out = []
    for s in tabs[tid]["documentTab"]["body"]["content"]:
        if "paragraph" in s:
            p = s["paragraph"]; els = [e for e in p["elements"] if "textRun" in e]
            out.append((s["startIndex"], s["endIndex"], p["paragraphStyle"].get("namedStyleType"),
                        "".join(e["textRun"]["content"] for e in els),
                        els[0]["textRun"]["textStyle"].get("foregroundColor", {}).get("color", {}).get("rgbColor") if els else None))
    return out
for row in paras("t.i5p9a4r26buw"):
    print("TAB", row[0], row[2], repr(row[3][:70]), row[4], file=sys.stderr)
for row in paras("t.89r88yxpo4v3")[-9:]:
    print("GOALS", row[0], repr(row[3][:70]), row[4], file=sys.stderr)
print(c["revisionId"], file=sys.stderr)
last = paras("t.i5p9a4r26buw")[-1]
at = last[1] - 1
idea = sys.argv[2]
text = "\n" + idea
reqs = [{"insertText": {"text": text, "location": {"index": at, "tabId": "t.i5p9a4r26buw"}}},
        {"updateParagraphStyle": {"range": {"startIndex": at + 1, "endIndex": at + 1 + len(idea) + 1, "tabId": "t.i5p9a4r26buw"},
                                  "paragraphStyle": {"namedStyleType": "NORMAL_TEXT"}, "fields": "namedStyleType"}},
        {"updateTextStyle": {"range": {"startIndex": at + 1, "endIndex": at + 1 + len(idea), "tabId": "t.i5p9a4r26buw"},
                             "textStyle": {"bold": False, "foregroundColor": {"color": {"rgbColor": BODY}}}, "fields": "bold,foregroundColor"}}]
assert all(ord(ch) < 0x10000 for ch in text)
print(json.dumps(reqs, ensure_ascii=False))
