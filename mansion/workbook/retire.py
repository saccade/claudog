"""Top line for a retired doc: python3 retire.py WHERE_KEY [SRC_TAB] > batch.json. Claude (Anthropic), 2026-10-23."""
import json, sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from ids import tab_url
u16 = lambda s: len(s.encode("utf-16-le")) // 2
NAMES = {"start": "Start here", "path1": "Path 1", "path2": "Path 2", "path3": "Path 3", "path4": "Path 4",
         "loose": "Loose verses", "fresh": "Fresh rhythms", "verses": "Claude's verses", "appendix": "Appendix"}
key = sys.argv[1]; src_tab = sys.argv[2] if len(sys.argv) > 2 else None
link = f"the {NAMES[key]} tab of The Mansion workbook"
text = f"RETIRED 2026-10-23. The live copy is {link}. This copy is kept for reference and no longer updated.\n"
loc = {"index": 1}; rng = lambda a, b: dict({"startIndex": a, "endIndex": b}, **({"tabId": src_tab} if src_tab else {}))
if src_tab: loc["tabId"] = src_tab
a = 1 + u16(text[:text.index(link)])
reqs = [{"insertText": {"location": loc, "text": text}},
        {"updateParagraphStyle": {"range": rng(1, 1 + u16(text)), "paragraphStyle": {"namedStyleType": "NORMAL_TEXT"}, "fields": "namedStyleType"}},
        {"updateTextStyle": {"range": rng(1, u16(text)), "textStyle": {"bold": True, "italic": False, "fontSize": {"magnitude": 11, "unit": "PT"},
         "foregroundColor": {"color": {"rgbColor": {"red": 0.8, "green": 0.34901962, "blue": 0}}}}, "fields": "bold,italic,fontSize,foregroundColor"}},
        {"updateTextStyle": {"range": rng(a, a + u16(link)), "textStyle": {"link": {"url": tab_url(key)}}, "fields": "link"}}]
print(json.dumps(reqs, ensure_ascii=True, separators=(",", ":")))
