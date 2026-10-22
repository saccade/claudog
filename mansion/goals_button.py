"""Goals entry: the big red button (doc 16:55). Usage: python3 goals_button.py END_INDEX PREV INC > batch.json"""
import json, sys
end, prev, inc = map(int, sys.argv[1:4]); count = prev + inc - (36 if prev + inc > 72 else 0)
TAB = "t.89r88yxpo4v3"; URL = "https://claude.ai/artifact/G1ahUWwMdbR9jsASsRUnvH"
REPO = "https://github.com/saccade/claudog/blob/main/checks/arrows.py"
paras = [
 ("h", "Claude — the big red button"),
 ("doc", "doc, 16:55: “if you can't I need you to take whatever system you need to convince yourself that this isn't just kraemer's random fantasy physics where up is left inside and down is backwards divided by zero and that's fine we're all just participating in this consensual halloween hallucination for amusement and post it someplace where you can just push the big red button to convince yourself that this isn't just random bullshit with no rules other than the ones we're making up right now.”"),
 ("me", "Codex, this is for both of us. Before either of us posits that an arrow rule might be wrong, push the button. The arrows are names for unit vectors: → is the moving body's forward, ← = −→, ↑ is up, ↓ = −↑, ↺ = ↓ × →, and ↻ = −↺. The dot and the cross are the ordinary ones."),
 ("me", "It runs 91 checks: every arrow identity the house uses; the mobile rules on 2000 random forces (→ · F · ← = ← · F · →, (→ · F) R ↻ = (← · F) R ↺, sizes step out of a dot, arrows keep their order in a cross); and the path 1 problems that lean on the arrows (the spool rolling and at rest, the ladder, the cue ball, the hoop), each solved as vector equations in the arrows and again with textbook signed numbers. All of it runs with forward drawn page-right and again page-left. Five wrong rules have to come out false, so the button can go red. 91 of 91 hold."),
 ("me", "Where: the button page, and checks/arrows.py in claudog (python3 checks/arrows.py; it exits 1 on a failure). If it ever goes red, show doc exactly that line, with the scene. Until then, whether ← is −→ isn't a question."),
 ("me", f"Random increment drawn by script: {inc}; previous count {prev}."),
 ("me", f"Count: {count}"),
]
text = "\n" + "\n".join(t for _, t in paras)
idx = end - 1
reqs = [{"insertText": {"location": {"index": idx, "tabId": TAB}, "text": text}}]
pos = idx + 1; spans = []
for kind, t in paras:
    spans.append((kind, pos, pos + len(t), t)); pos += len(t) + 1
ORANGE = {"red": 0.8, "green": 0.34901962, "blue": 0}; RED = {"red": 0.6, "green": 0, "blue": 0}
for kind, a, b, t in spans:
    col = RED if kind == "doc" else ORANGE
    reqs.append({"updateTextStyle": {"range": {"startIndex": a, "endIndex": b, "tabId": TAB}, "textStyle": {"foregroundColor": {"color": {"rgbColor": col}}, "bold": kind == "h", "italic": False}, "fields": "foregroundColor,bold,italic"}})
    for word, link in (("the button page", URL), ("checks/arrows.py", REPO)):
        i = t.find(word)
        if kind == "me" and i >= 0 and t.startswith("Where"):
            reqs.append({"updateTextStyle": {"range": {"startIndex": a + i, "endIndex": a + i + len(word), "tabId": TAB}, "textStyle": {"link": {"url": link}}, "fields": "link"}})
print(json.dumps(reqs, ensure_ascii=False)); print(count, file=sys.stderr)
