"""Replaces a path doc's whole body with a built set's text, for big structural changes (the sweep).

Claude (Anthropic), 2026-10-22. Usage: python3 set_doc_replace.py SAVED_READ setK.html > batch.json
Only when the doc matches the last committed build (set_doc_verify against it says OK), so nothing of doc's is lost.
One guarded batch: delete everything but the final newline, insert the text. Then run set_doc_style.py on a fresh read.
"""
import json, re, html, sys
c = json.load(open(sys.argv[1])); c = c.get("content", c)
body = c["tabs"][0]["documentTab"]["body"]["content"]
end = body[-1]["endIndex"]
h = open(sys.argv[2]).read()
b = [x for x in (html.unescape(re.sub("<[^>]+>", "", m.group(2))).strip() for m in re.finditer(r"<(h1|h2|h3|p)[^>]*>(.*?)</\1>", h, re.S)) if x]
reqs = [{"deleteContentRange": {"range": {"startIndex": 1, "endIndex": end - 1}}},
        {"insertText": {"location": {"index": 1}, "text": "\n".join(b)}}]
print(json.dumps({"revision": c["revisionId"], "requests": reqs}, ensure_ascii=False))
