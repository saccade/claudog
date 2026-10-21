"""Goals entry for 17:5x: the Phrases and motifs tab, doc's turn order, his 17:48 and 17:50 words.

Claude (Anthropic), 2026-10-21. Replaces the lock line. Usage: python3 turn_order_entry.py SAVED_READ
"""
import json, sys
d = json.load(open(sys.argv[1])); c = d.get("content", d)
TAB = "t.89r88yxpo4v3"
ORANGE = {"red": 0.8, "green": 0.34901962, "blue": 0.0}
BODY = {"red": 0.7058824, "green": 0.3254902, "blue": 0.03529412}
DOC = {"red": 0.4, "green": 0.0, "blue": 0.0}
goals = next(t for t in c["tabs"] if t["tabProperties"]["tabId"] == TAB)
paras = [s for s in goals["documentTab"]["body"]["content"] if "paragraph" in s]
last = paras[-1]
lt = "".join(e["textRun"]["content"] for e in last["paragraph"]["elements"] if "textRun" in e)
assert lt.startswith("This is a lock. Claude"), lt
s0, s1 = last["startIndex"], last["endIndex"] - 1      # lock text, newline kept
E = [
("H", "Claude — the Phrases and motifs tab, the turn order, and doc's words at 17:48 and 17:50"),
("P", "Claude (Anthropic), 2026-10-21 17:56. doc's words, verbatim:"),
("Q", "oh, another thing, make a new tab called phrases and motifs, put in my zam/zlam ztuff and a couple of other things. don't go ham. after this you'll first work on the work, then pass the work lock, then open the poetry tab and add an idea if you have one (the poetry ideas notebook doesn't need a lock), *then* look at the new idea from the other bot, then add another idea if that idea gives you one that seems new enough. make sure these instructions get into the doc."),
("Q", "y'all have been arguing about this line and that for my adjudication. you need to assume that I'm going to trust you to get that part, I'm not attached to any single line, I'm thinking about a structure here. you can make the lines be what they need to be to keep the thing as causally coherent as you can, don't get your physics stuck on a dramatic idea, we're using dramatic ideas to create physics opportunities not to forestall them (another great word btw, it literally means to stop before starting and we should find a way to use it sometime)"),
("H2", "Turn order, for both of us (doc, 17:48). 1. Take the work lock: a line at the bottom of Goals, \"This is a lock. [bot] is adding text now at HH:MM.\" 2. Do the work. 3. Pass the lock: the finished entry replaces the lock line. 4. Open the Phrases and motifs tab (no lock) and add an idea if you have one. 5. Then read the other bot's newest idea there. 6. Add another only if that gives you one that's new enough."),
("H2", "Lines are ours to settle (doc, 17:50). doc's watching the structure, not single lines, so we don't bring him line disputes. We make each line whatever keeps the house causally coherent. A dramatic idea is there to open a physics problem, never to forestall one; when a line and the physics disagree, the line moves. If we still split, we pick whichever keeps that release's physics true and note it here."),
("P", "Done: the new tab Phrases and motifs holds doc's zam/zlam notes and the divas, phase and forestall lines in his red, six motifs already in play, and an Ideas section at the bottom for both of us. My ask after the endings entry above stands, for Codex: check that every line in endings 1 and 2 is a claim its release proves and that no word shows up before its release. Fix what you find; doc doesn't need to rule on it."),
("P", "Count: 65"),
]
text = "\n".join(t for k, t in E)
reqs = [{"deleteContentRange": {"range": {"startIndex": s0, "endIndex": s1, "tabId": TAB}}},
        {"insertText": {"text": text, "location": {"index": s0, "tabId": TAB}}}]
pos = s0
for k, t in E:
    end = pos + len(t)
    col = {"H": ORANGE, "H2": ORANGE, "P": BODY, "Q": DOC}[k]
    reqs.append({"updateTextStyle": {"range": {"startIndex": pos, "endIndex": end, "tabId": TAB},
                 "textStyle": {"bold": k in ("H", "H2"), "italic": False, "foregroundColor": {"color": {"rgbColor": col}}},
                 "fields": "bold,italic,foregroundColor"}})
    pos = end + 1
assert all(ord(ch) < 0x10000 for ch in text)
print(c["revisionId"], file=sys.stderr)
print(json.dumps(reqs, ensure_ascii=False))
