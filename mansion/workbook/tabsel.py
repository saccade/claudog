"""Tab selection and tab-scoping for Docs reads and request batches.

Claude (Anthropic), 2026-10-23, for the workbook move: every set_doc script takes an optional tab ID.
tab_doc(content, tab) finds the documentTab (children included); tabify(reqs, tab) scopes every range and
location to that tab, and every replaceAllText to that tab only (unscoped, it would hit every tab in the doc).
"""
def walk(tabs):
    for t in tabs:
        yield t
        yield from walk(t.get("childTabs", []))

def tab_doc(c, tab=None):
    tabs = list(walk(c["tabs"]))
    t = tabs[0] if tab is None else next(t for t in tabs if t["tabProperties"]["tabId"] == tab)
    return t["documentTab"]

def tabify(reqs, tab):
    if not tab: return reqs
    def fix(x):
        if isinstance(x, dict):
            for k, v in x.items():
                if k in ("range", "location", "tableStartLocation") and isinstance(v, dict): v["tabId"] = tab
                fix(v)
            if "replaceAllText" in x: x["replaceAllText"]["tabsCriteria"] = {"tabIds": [tab]}
        elif isinstance(x, list):
            for v in x: fix(v)
    fix(reqs); return reqs
