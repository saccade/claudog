"""Replaces a set doc's whole body with a built set (setK.html), daggers as superscripts, in one guarded batch.

Claude (Anthropic), 2026-10-22. Usage: python3 set_doc_batch.py SAVED_READ setK.html > batch.json
"""
import json, subprocess, sys
c = json.load(open(sys.argv[1])); c = c.get("content", c)
end = c["tabs"][0]["documentTab"]["body"]["content"][-1]["endIndex"]
ins = json.loads(subprocess.check_output([sys.executable, __file__.replace("set_doc_batch.py", "html_to_batch.py"), sys.argv[2]]))
text = ins[0]["insertText"]["text"]
assert all(ord(ch) < 0x10000 for ch in text)
reqs = [{"deleteContentRange": {"range": {"startIndex": 1, "endIndex": end - 1}}}] if end > 2 else []
reqs.append(ins[0])
n = len(text)   # clear whatever style the old body leaves on the new text, then style it
reqs.append({"updateTextStyle": {"range": {"startIndex": 1, "endIndex": 1 + n}, "textStyle": {}, "fields": "bold,italic,underline,strikethrough,baselineOffset,foregroundColor,backgroundColor,link"}})
reqs.append({"updateParagraphStyle": {"range": {"startIndex": 1, "endIndex": 1 + n}, "paragraphStyle": {"indentStart": {"magnitude": 0, "unit": "PT"}, "indentFirstLine": {"magnitude": 0, "unit": "PT"}}, "fields": "indentStart,indentFirstLine"}})
reqs += ins[1:]
for i, ch in enumerate(text):
    if ch == "†":
        reqs.append({"updateTextStyle": {"range": {"startIndex": 1 + i, "endIndex": 2 + i}, "textStyle": {"baselineOffset": "SUPERSCRIPT"}, "fields": "baselineOffset"}})
print(c["revisionId"], file=sys.stderr)
print(json.dumps(reqs, ensure_ascii=False))
