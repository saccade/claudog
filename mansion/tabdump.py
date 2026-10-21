"""Lists a saved Docs read's tabs (id, title, end index) and dumps chosen tabs' text, or the tail of one.

Claude (Anthropic), 2026-10-21. Usage: python3 tabdump.py SAVED_READ [TABID[:TAILCHARS] ...]
"""
import json, sys
c = json.load(open(sys.argv[1])); c = c.get("content", c)
def walk(ts):
    for t in ts:
        yield t; yield from walk(t.get("childTabs", []))
def text(t):
    return "".join(e["textRun"]["content"] for s in t["documentTab"]["body"]["content"] if "paragraph" in s
                   for e in s["paragraph"]["elements"] if "textRun" in e)
tabs = list(walk(c["tabs"]))
print(c["revisionId"])
for t in tabs:
    p = t["tabProperties"]; print(p["tabId"], "|", p["title"], "|", t["documentTab"]["body"]["content"][-1]["endIndex"])
for a in sys.argv[2:]:
    tid, _, tail = a.partition(":")
    t = next(t for t in tabs if t["tabProperties"]["tabId"] == tid)
    s = text(t); print("=====", tid); print(s[-int(tail):] if tail else s)
