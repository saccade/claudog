"""Flattens a saved Docs read (all tabs) to text, with heading marks and link targets; optionally lists runs in a given color family.

Claude (Anthropic), 2026-10-21. Usage: python3 flatten.py SAVED_READ [--red]
"""
import json, sys
c = json.load(open(sys.argv[1])); c = c.get("content", c)
def walk(ts):
    for t in ts:
        yield t; yield from walk(t.get("childTabs", []))
red = "--red" in sys.argv
print(c["title"], c["revisionId"])
for t in walk(c["tabs"]):
    p = t["tabProperties"]; print("\n######## TAB", p["tabId"], p["title"])
    for s in t["documentTab"]["body"]["content"]:
        if "paragraph" not in s: continue
        txt = ""
        for e in s["paragraph"]["elements"]:
            if "textRun" not in e: continue
            r = e["textRun"]; col = r["textStyle"].get("foregroundColor", {}).get("color", {}).get("rgbColor", {})
            seg = r["content"].rstrip("\n")
            if red and col and col.get("red", 0) > 0.3 and col.get("green", 0) < 0.15 and col.get("blue", 0) < 0.15:
                seg = "<<RED:" + seg + ">>"
            txt += seg
        st = s["paragraph"]["paragraphStyle"].get("namedStyleType", "")
        if txt.strip(): print(("## " if "HEADING" in st else "") + txt)
