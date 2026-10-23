"""Claude's verses for the Mansion: text and a Docs batch for the 'Claude's verses' tab of the poetry notebook.

Claude (Anthropic), 2026-10-23, for doc (07:26: put the harlequin poem where the poems go, then some
Poe, Dickinson, Gorman, Heaney, Angelou, Cummings, and Eliot). Usage: python3 claude_verses.py TAB_ID > batch.json
Kinds: h1 title, note (italic), h2 poem title, after (italic byline under a title), v verse line.
"""
import json, sys

V = [
("h1", "Claude's verses"),
("note", "Written by Claude (Anthropic), 2026-10-23, for dr. kraemer. Verse for the Mansion, in the manner of the poets named; the Eliot borrows Prufrock's frame on purpose. The house, its physics, and its vocabulary are dr. kraemer's; the words are Claude's."),

("h2", "Harlequin Clockwork"),
("v", "Knife goes over, knife comes back, back and forth, back and forth.\nKnife goes over, knife comes back; the paper takes the bend.\nKnife goes over, knife comes back, back and forth, back and forth.\nKnife goes over, knife comes back: two seconds, then again...\nAnd every turn it comes back home, comes back home, comes back home?\nAnd every turn it comes back home to find the roast gone cold...\n\nTick, says the clock, and tick, and tick.\nThe tock's a thing the ear puts in.\nEach tick's as level as the last;\nyou lean, and there the tocks begin.\n\nHarlequin, harlequin, diamonds and pins,\nlock and let go where the scape-wheel begins:\nred diamond, black diamond, red diamond, red,\none patch sewn on with the flowers turned in.\nLock, and a drop, and a lock, and a — drop —\nthe beat comes in late, and the late's on top.\n\nLow voice counting one to four,\nhigh voice one to nine;\nneither hears the other count,\nand both come home on time.\n\nHalfway round, the low one's home,\nthe high one's upside down;\nthe can lets go, and lets go, and lets\ngo:\nfive\nin thirteen\nleft,\nno current\nin the wire.\nThe clock says\nstop.\n\nStop? Not likely! Not a moment! Bottom's where it all gets going!\nBoth the rods are through the vertical and flying, flat-out flying,\nhundred forty-four of every hundred sixty-nine in motion;\nwhat the can let go of didn't leave, it's swinging through the middle,\nfive and twelve and thirteen out of two and three, and nothing missing!\n\nKnife goes over, knife comes back, back and forth, back and forth.\nKnife goes over, knife comes back; the paper takes the bend.\nKnife goes over, knife comes back, back and forth (again?) and forth.\nKnife goes over, knife comes back: two seconds, like last time...\nAnd every turn it comes back home: home to what? home to whom?\nEvery turn it came back home. The tock was always you."),

("h2", "The Carving Knife"),
("after", "after Poe"),
("v", "In the dining room I lingered, and the cold roast lay unfingered,\nwhile above it swung a carving knife as patient as the slain;\nto and fro it went, unhurried, with its measure never worried,\ntwo full seconds, never flurried, never faster for the strain;\nand I whispered, “Knife, how long now?” and it answered, “Once again.”\n        Just the beat, and once again.\n\nThen I hung a heavier cleaver, sure the weight would make it eager,\nsure a doubled pull would hurry it and snap the cycle's chain;\nbut the double weight came double in its loathing to be hurried,\nand the two of them were canceled, pull on pull and grain for grain,\nand it whispered as it passed me, “Two full seconds. Once again.”\n        Just the beat, and once again.\n\nSo I sat, and I am sitting, while the pen beneath is knitting\nall the curve of every crossing on a ribbon without stain,\nand the clock inside the paneling has stopped its idle channeling,\nfor it needs no other counting than the blade above my brain;\nand the knife says, as it passes, as it passes, “Once again.”\n        Just the beat — and once again."),

("h2", "A Ghost"),
("after", "after Dickinson"),
("v", "A Ghost is Body — with the Mass\nLifted — like a Lid —\nIt keeps the Place — the Pace — the Swirl —\nOf all the Body did —\n\nIt cannot Punch — it cannot Heft —\nIt only Zips — and Runs —\nAnd walks through Walls — as Ghosts are let —\nUntil the Body comes —\n\nInside the Walls — ’tis Algebra —\nNo Lamp — no Door — no Floor —\nAnd Those who followed — lost the Way —\nWho left the Mass — before —\n\nThe Way is out — the Way it came —\nPut Body — back — across —\nThen Half a Wheel — steps out — and Hooks —\nNine Thump — and not a Loss —"),

("h2", "What We Keep"),
("after", "after Gorman"),
("v", "We are the guests the house was waiting for,\nnot because we knocked, but because we kept count.\nWe have learned that a turn is not a trap,\nthat coming round is not the same as coming back,\nthat what returns is not what repeats.\nWe carry the knife's time in our pockets\nand the can's quiet in our coats.\nWe are not lost in these walls;\nwe are the mass the ghosts were missing.\nSo let us lift. Let us heft.\nLet us not merely swing, but sing;\nnot merely hang, but hum;\nfor every store we keep is a promise\nthat what we put in, we can take back out,\nthat in a loop with no resistor\nnothing given is burned.\nThe house is not just what grew around the work.\nThe house is the work, and we are its hands.\nAnd when the clock comes home at last,\nfour turns low and nine turns high,\nlet it find us in our chairs:\nnot waiting, but ready;\nnot left, but here."),

("h2", "Spool"),
("after", "after Heaney"),
("v", "My grandmother's kitchen, the range banked low,\nand on the oilcloth a spool of black thread\nshe'd tug across the board to make me laugh.\nPull low, and it came to her, rolling, biddable;\npull high, and it ran from her hand\nlike a calf that won't be led to the byre.\nSomewhere between, an angle she found\nby feel, not figure: the thread's line\nlaid dead through the place the rim met board,\nand the spool stood, the thread taut,\nthe whole kitchen holding its breath.\nI have that angle now in numbers,\nthree and four and the long five,\nits cosine the hub over the rim.\nBut the numbers came after the hand,\nthe way the name comes after the field,\nand I keep her pull in my wrist\nthe way a spade keeps its heft in the shaft."),

("h2", "Governor"),
("after", "after Angelou"),
("v", "You may turn me on your spindle,\nspin me harder, spin me higher;\nevery sweep you lay upon me\nlifts me nearer to the fire.\n\nDoes my rising put you out, sir?\nDid you think that I would cling\nstraight down by the shaft forever,\nlike a plumb bob on a string?\n\nWhen the shaft went slow, I hung there.\nThat was arithmetic, not shame.\nTurn me past the root of twenty,\nand I'll never hang the same.\n\nOut I go, and up I'm going,\ntill the drop and reach agree:\nnot because I fight the pulling;\n'cause the pulling's bending me.\n\nWatch me climbing.\nWatch me climbing\nto the height the turning knows.\nAnd the faster that you spin me,\nthe higher, honey, the governor goes."),

("h2", "hoop"),
("after", "after cummings"),
("v", "what does the hoop say\nwhen it(rolling)\ntouches the floor? it\nsays\n\nnothing:\n          for one\n                    not even a moment\nthe bottom of the moving\nis the still\n                    est thing in the\nworld(\nand then it isn't)\n                    and then the next one is\n\ntop goes twice\nas fast as anything;bottom\ngoes\n     not\n          at\n               all\n& the hoop,who\nis all of its points at once,\n                    goes\n                         on"),

("h2", "The Love Song of the Visitor in the Chair"),
("after", "after Eliot"),
("v", "Let us go down, then, you and I,\nbeneath the stage, where the rods hang by\nlike a breath held between one tick and the next;\nlet us go, through certain half-lit halls,\nthe muttering returns\nof tones that never meet, and never quite\ncome round together, though they try,\nfour low, nine high,\nto lead you to a question you won't ask...\nOh, do not ask, “What is it for?”\nLet us go down, and through the door.\n\nIn the hall the lamps come and go,\ntalking of how slow is slow.\n\nAnd indeed there will be time\nto wonder, “Is it sixteen?” and, “Is it twenty?”,\ntime to count it on my clock and then on theirs,\nand find four seconds lost only in the counting;\ntime for you and time for me,\nand time yet for a hundred calculations,\nand for a hundred checks and recalculations,\nbefore the carving of a roast gone cold.\n\nIn the hall the lamps come and go,\ntalking of how slow is slow.\n\nI have measured out my evening with a carving knife,\ntwo seconds to a swing;\nI know the hum beneath the floorboards, never louder than a breath,\nunder the whispering in the understage.\n        So how should I begin?\n\nShall I sit a little forward? Is the carving out of reach?\nI shall wear the chalk upon my cuff, and practice what they teach.\nI have heard the capacitors humming, each to each.\n\nI do not think that they will hum for me.\n\nWe have lingered in the chambers of the house\nby lamps that came level, neither of them stopped,\ntill the clock comes home, and we have never left."),
]

def batch(tab):
    text = ""; spans = []
    for kind, t in V:
        start = len(text.encode("utf-16-le")) // 2
        text += t + "\n"
        spans.append((kind, start, start + len(t.encode("utf-16-le")) // 2))
    reqs = [{"insertText": {"location": {"index": 1, "tabId": tab}, "text": text}}]
    named = {"h1": "HEADING_1", "h2": "HEADING_2"}
    for kind, a, b in spans:
        a += 1; b += 1
        reqs.append({"updateParagraphStyle": {"range": {"startIndex": a, "endIndex": b + 1, "tabId": tab},
                     "paragraphStyle": {"namedStyleType": named.get(kind, "NORMAL_TEXT")}, "fields": "namedStyleType"}})
        if kind in ("note", "after"):
            reqs.append({"updateTextStyle": {"range": {"startIndex": a, "endIndex": b, "tabId": tab},
                         "textStyle": {"italic": True}, "fields": "italic"}})
    return reqs

if __name__ == "__main__":
    print(json.dumps(batch(sys.argv[1]), ensure_ascii=True))
