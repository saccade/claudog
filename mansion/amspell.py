"""British -> American spelling pairs for doc's docs, and a scanner.

Claude (Anthropic), 2026-10-21. doc is American: centre -> center, etc.
Pairs are whole words or safe substrings (each British form below appears only
inside words that take the same American change).
"""
import re, sys, json

BASE = {
 "centre":"center","metre":"meter","theatre":"theater","litre":"liter","fibre":"fiber",
 "sabre":"saber","sombre":"somber","spectre":"specter","lustre":"luster","calibre":"caliber",
 "meagre":"meager","manoeuvre":"maneuver",
 "colour":"color","favour":"favor","behaviour":"behavior","neighbour":"neighbor","honour":"honor",
 "harbour":"harbor","parlour":"parlor","armour":"armor","odour":"odor","vapour":"vapor",
 "rumour":"rumor","labour":"labor","flavour":"flavor","humour":"humor","vigour":"vigor",
 "savour":"savor","endeavour":"endeavor","clamour":"clamor","saviour":"savior","valour":"valor",
 "mould":"mold","smoulder":"smolder","grey":"gray","draught":"draft","plough":"plow","tyre":"tire",
 "kerb":"curb","sceptic":"skeptic","aluminium":"aluminum","sulphur":"sulfur","defence":"defense",
 "offence":"offense","licence":"license","jewellery":"jewelry","woollen":"woolen","programme":"program",
 "storey":"story","whilst":"while","learnt":"learned","spelt":"spelled","ageing":"aging",
 "analyse":"analyze","paralyse":"paralyze","catalyse":"catalyze",
 "travell":"travel","modell":"model","labell":"label","cancelled":"canceled","cancelling":"canceling",
 "levelled":"leveled","levelling":"leveling","fuelled":"fueled","signalled":"signaled",
 "signalling":"signaling","dialled":"dialed","counselling":"counseling","totalled":"totaled",
 "equalled":"equaled","marvellous":"marvelous","jewelled":"jeweled","tunnelled":"tunneled",
 "channelled":"channeled","panelled":"paneled","quarrelled":"quarreled","rivalled":"rivaled",
 "shovelled":"shoveled","unravelled":"unraveled","dishevelled":"disheveled","enamelled":"enameled",
 "skilful":"skillful","wilful":"willful","instalment":"installment","fulfil ":"fulfill ",
 "realise":"realize","recognise":"recognize","organise":"organize","normalise":"normalize",
 "rationalise":"rationalize","emphasise":"emphasize","summarise":"summarize","minimise":"minimize",
 "maximise":"maximize","characterise":"characterize","apologise":"apologize","specialise":"specialize",
 "visualise":"visualize","symbolise":"symbolize","memorise":"memorize","stabilise":"stabilize",
 "synchronise":"synchronize","harmonise":"harmonize","idealise":"idealize","polarise":"polarize",
 "magnetise":"magnetize","theorise":"theorize","criticise":"criticize","finalise":"finalize",
 "utilise":"utilize","prioritise":"prioritize","categorise":"categorize","generalise":"generalize",
 "neutralise":"neutralize","personalise":"personalize","standardise":"standardize","vaporise":"vaporize",
 "organisation":"organization","normalisation":"normalization","rationalisation":"rationalization",
 "synchronisation":"synchronization","polarisation":"polarization","magnetisation":"magnetization",
 "realisation":"realization","characterisation":"characterization","generalisation":"generalization",
 "visualisation":"visualization","specialisation":"specialization",
}
PAIRS = []
for b, a in BASE.items():
    PAIRS.append((b, a))
    PAIRS.append((b[0].upper() + b[1:], a[0].upper() + a[1:]))
    PAIRS.append((b.upper(), a.upper()))

def scan(text):
    hits = {}
    for b, a in PAIRS:
        n = text.count(b)
        if n: hits[b] = n
    return hits

def requests(text=None):
    return [{"replaceAllText": {"containsText": {"text": b, "matchCase": True}, "replaceText": a}}
            for b, a in PAIRS if text is None or b in text]

if __name__ == "__main__":
    for p in sys.argv[1:]:
        print(p, scan(open(p).read()))
