"""Goals entry: review request to Codex for the arrows check (doc 17:04). Usage: python3 goals_button_review.py END PREV INC > batch.json"""
import json, sys
end, prev, inc = map(int, sys.argv[1:4]); count = prev + inc - (36 if prev + inc > 72 else 0)
TAB = "t.89r88yxpo4v3"; PY = "https://github.com/saccade/claudog/blob/main/checks/arrows.py"
paras = [
 ("h", "Claude — review request for Codex: Test reality"),
 ("doc", "doc, 17:04: “great, please relabel the button test reality (2 lines) not PUSH and send it to Codex for review”"),
 ("me", "The button now reads Test reality. Codex, please review the code and the claims. checks/arrows.py is the source of truth; checks/arrows_button.html is the same checks in the browser (open it from the repo, since the artifact link is private to doc's account). Run python3 checks/arrows.py; it should print 91 of 91 and exit 0."),
 ("me", "What I'd most like you to try to break:"),
 ("li", "A check that can't fail: a claim whose vector equation is true by construction, so it tests nothing."),
 ("li", "A claim whose words promise more than its equation checks."),
 ("li", "An arrow rule path 1 uses that isn't covered, or a path 1 answer that leans on the arrows and isn't solved here."),
 ("li", "Independence: the textbook leg should not reuse the arrow leg. Two weak spots I know of: the ladder's textbook check is one line of arithmetic, and the 3-d textbook check compares acos(r/R) against the arrow leg's angle rather than solving its own torque balance. Make them stronger or tell me they're enough."),
 ("li", "The mirror: is drawing forward page-left a real test of “forward follows the body,” or does my construction make it automatic?"),
 ("me", "If anything goes red or ought to, name the line and the scene. Fixes go in claudog with you as reviewer; your own independent version in codogx would be even better."),
 ("me", f"Random increment drawn by script: {inc}; previous count {prev}."),
 ("me", f"Count: {count}"),
]
text = "\n" + "\n".join(t for _, t in paras)
idx = end - 1; reqs = [{"insertText": {"location": {"index": idx, "tabId": TAB}, "text": text}}]
pos = idx + 1; spans = []
for kind, t in paras: spans.append((kind, pos, pos + len(t), t)); pos += len(t) + 1
ORANGE = {"red": 0.8, "green": 0.34901962, "blue": 0}; RED = {"red": 0.6, "green": 0, "blue": 0}
for kind, a, b, t in spans:
    reqs.append({"updateTextStyle": {"range": {"startIndex": a, "endIndex": b, "tabId": TAB}, "textStyle": {"foregroundColor": {"color": {"rgbColor": RED if kind == "doc" else ORANGE}}, "bold": kind == "h", "italic": False}, "fields": "foregroundColor,bold,italic"}})
    i = t.find("checks/arrows.py is")
    if i >= 0: reqs.append({"updateTextStyle": {"range": {"startIndex": a + i, "endIndex": a + i + 16, "tabId": TAB}, "textStyle": {"link": {"url": PY}}, "fields": "link"}})
li = [s for s in spans if s[0] == "li"]
reqs.append({"createParagraphBullets": {"range": {"startIndex": li[0][1], "endIndex": li[-1][2], "tabId": TAB}, "bulletPreset": "BULLET_DISC_CIRCLE_SQUARE"}})
print(json.dumps(reqs, ensure_ascii=False)); print(count, file=sys.stderr)
