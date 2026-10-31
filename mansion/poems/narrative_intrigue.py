"""The 'Narrative intrigue' tab of the poetry notebook: how the Mansion keeps surprising, as worked out 2026-10-22/23.

Claude (Anthropic), 2026-10-23, for doc (07:34: "put the stuff you did with the foreshadowing and the deja vu and
the surprise and the fibonacci mobiles in another tab, call it narrative intrigue").
Usage: python3 narrative_intrigue.py TAB_ID > batch.json
Kinds: h1, note (italic), h2, p (Claude's prose), q (doc's words, his red), li (bullet).
"""
import json, sys

T = [
("h1", "Narrative intrigue"),
("note", "Written by Claude (Anthropic), 2026-10-23, for dr. kraemer. How the Mansion keeps the reader from seeing it coming: the mobiles, the third thing, the key change, the crown move, and path 4's déjà vu. The ideas are dr. kraemer's (his words in red, from chat on 2026-10-22 and 23); the summary is Claude's. Moved into the workbook on 2026-10-23 with two amendments from Codex's review: the mobile clarification, and a softer rule for the déjà vu touches."),

("h2", "The mobiles: as unsymmetric as balance allows"),
("q", "“look at the mobiles I posted earlier. there's a pattern to their structure to make them sort of maximally un-symmetric” · “never let em see it coming. that's the point of having four paths too.”"),
("p", "His beaded twig mobile is a Fibonacci tree: 8 hangs as 3 + 5, the 5 as 2 + 3, the 3 as 1 + 2, the 2 as 1 + 1. Every split is uneven and close to the golden ratio, with the heavier side on the shorter arm, so it balances without ever repeating a symmetry. For the paths: no two do the same thing at the same depth, and no gap between surprises is the same as the last one."),
("img", ""),
("p", "Once the reader understands the mobile, the whole structure becomes predictable without becoming matchy (doc's clarification, as Codex reported it on 10-23). Knowing how it hangs doesn't tell you where the next bead is. So the rule isn't that a kind of surprise can never come back: it's that nothing comes back in step, at the same depth, or at an even spacing."),

("h2", "The third thing"),
("q", "“you give people three things, increasingly surprising and then you say now I'd like to show you a third thing and people are wait like that was three things, and I'm like oh that first one was just standard stuff, think of it as a well-constructed baseline, I just needed to establish some context first. now *this* was what I came here to show you...”"),
("p", "Path 1 is the baseline: the thirteen, said plainly and fully. Paths 2 to 4 each bring something new, of a different kind and at an uneven depth. Path 4's reveal should change what came before, the way the third thing turns the first one into context."),

("h2", "The crown move: openings that differ in kind"),
("q", "“I like the way you're distinguishing this from the other one by pulling in heft right away, that's the kind of thing I'm looking for, that kind of unpredictability. like opening my fourth book with the crown scene, bam look the crown doesn't matter it's there it's gone look now it's in the hut where it sat all through the third book (think progressive flashbacks, not time travel)” · “but it's not unpredictable if you do it the same every time, you know?”"),
("p", "Path 2 surprises right out of the gate, pulling in heft at the knife. That isn't a template for the other paths: a surprise done the same way every time stops being one, so no path owes an opening move."),
("p", "Path 4's big turn comes under the stage: the upper rod's bob is the dining room's knife, a kilogram a meter out from the same silver pivot. You've been watching one end of this machine since the roast went cold."),

("h2", "The key change: same openings, new endings"),
("q", "“the top of every line is the same while the back ends progressively reveal that this is not in the key you thought you were in. but all the notes were right there on the staff.”"),
("p", "His Mary had a little lamb: every line starts E D C D, and the endings walk from C down to B and on to A, the relative minor that was sitting in C's key signature the whole time. The same trick runs through the Prime Directive, where the rhythm turns upside down at the low point (“Nothing doing! / I won't have it!”) and leaps into its longest lines. Dog Math's stealth mode uses it for vocabulary: start each problem in the textbook's terms and end each part a little further in. Harlequin Clockwork uses it for verse: the head “Knife goes over, knife comes back” never changes, and the tails walk from “the paper takes the bend” down to “the tock was always you.”"),
("p", "The physics has its own version. At the chair's halfway point the can holds the least it ever will, 25 parts in 169, and that's exactly when the rods are flying fastest. The low point of one store is the high point of the other, which is where the verse jumps back up."),

("h2", "Déjà vu: the narrator half-remembers"),
("q", "“by the 4th path the narrator can also have some unstructured unexamined awareness that this seems to have happened before. ‘grab the chi off the wall for torque like usual, no time to slow down here.’ (like Señor Featherboots here seems to be experiencing as he lives through the same events over and over for Nell's edification)”"),
("p", "In the Fox and the Fisher, Señor Featherboots never stops to look: “Again.” “(This kept happening...)” “Because at last… (or… again?...)”. Path 4's narrator does the same, in six touches of different kinds, spaced unevenly and growing:"),
("li", "2-c: “Grab the χ off the wall like usual, no time to slow down here: P = ωχ.” (his line)"),
("li", "b-3: the ladder “lets go, right on schedule.”"),
("li", "6-a: the basin keeps “exactly the knife's time, on a 5/7 m arc. Again.”"),
("li", "10-a: the conductance litany, “by now it says itself.”"),
("li", "12-b: “the 3–4–5, twenty times over. (How many is that now? Never mind. Keep moving.)”"),
("li", "13-b: at the chair's return, “It was 16 s last time, too.”"),
("p", "Two lines already there do the same work: “No stray 2 this time” at the knife, and “Its other end has been in your hand” at the ribbon. Keep it from becoming a system. A kind of touch can come back once the reader knows the shape, the way the mobile's splits do, but never in step, never at an even spacing, and never explained."),

("h2", "The haunted house"),
("p", "From Dog Math's first page: no ghostly hullabaloo at the door, or there'd be no guests. At first things seem the tiniest bit odd; it builds at the right moments, and it keeps not quite going back down all the way. The notation follows the same rule, arriving where it pays rent, and so do the house's reveals: the hand-mending, the maker's kit, one wearer behind the costumes, then the unfinished work of squaring the circle. The route begins in third person, and “you” creeps in: the chalk is on your cuff, the ribbon is already in your hand, and the chair is where you left it. You never left it."),
]

RED = {"red": 0.6, "green": 0, "blue": 0}
IMG = None; IMG_SIZE = {"height": {"magnitude": 324, "unit": "PT"}, "width": {"magnitude": 468, "unit": "PT"}}

def batch(tab):
    text = ""; spans = []
    for kind, t in T:
        start = len(text.encode("utf-16-le")) // 2
        text += t + "\n"
        spans.append((kind, start + 1, start + 1 + len(t.encode("utf-16-le")) // 2))
    reqs = [{"insertText": {"location": {"index": 1, "tabId": tab}, "text": text}}]
    named = {"h1": "HEADING_1", "h2": "HEADING_2"}
    for kind, a, b in spans:
        reqs.append({"updateParagraphStyle": {"range": {"startIndex": a, "endIndex": b + 1, "tabId": tab},
                     "paragraphStyle": {"namedStyleType": named.get(kind, "NORMAL_TEXT")}, "fields": "namedStyleType"}})
        if kind == "note":
            reqs.append({"updateTextStyle": {"range": {"startIndex": a, "endIndex": b, "tabId": tab},
                         "textStyle": {"italic": True}, "fields": "italic"}})
        if kind == "q":
            reqs.append({"updateTextStyle": {"range": {"startIndex": a, "endIndex": b, "tabId": tab},
                         "textStyle": {"foregroundColor": {"color": {"rgbColor": RED}}}, "fields": "foregroundColor"}})
    i = 0
    while i < len(spans):   # one bullet range per run of li paragraphs
        if spans[i][0] == "li":
            j = i
            while j + 1 < len(spans) and spans[j + 1][0] == "li": j += 1
            reqs.append({"createParagraphBullets": {"range": {"startIndex": spans[i][1], "endIndex": spans[j][2], "tabId": tab},
                         "bulletPreset": "BULLET_DISC_CIRCLE_SQUARE"}})
            i = j
        i += 1
    for kind, a, b in spans:   # last, since it adds one index: doc's mobile photo, from the planning tab's copy (Google must be able to fetch the URL)
        if kind == "img" and IMG:
            reqs.append({"insertInlineImage": {"location": {"index": a, "tabId": tab}, "uri": IMG, "objectSize": IMG_SIZE}})
    return reqs

if __name__ == "__main__":
    if len(sys.argv) > 2: IMG = sys.argv[2]   # usage: TAB_ID [IMAGE_URL]
    print(json.dumps(batch(sys.argv[1]), ensure_ascii=True))
