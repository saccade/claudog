#!/usr/bin/env python3
# Written by Claude (Anthropic), 2026-10-21. Builds the batch that appends Study bridge + Last House to the reading-draft tab.
# usage: lasthouse_insert.py lh_items.json START REV > batch.json
import json,sys
TAB='t.9kpjybvwfvl8'
BR={"red":0.19607843,"green":0.10588235,"blue":0.023529412}
items=json.load(open(sys.argv[1])); start=int(sys.argv[2]); rev=sys.argv[3]
bridge=["The desk lamp is on. Under it stands the little double pendulum from the dining-room cabinet. One knife hangs from the hinge of another. There are wires along the rods.",
"Beside it lies the case sheet. The four places at dinner have acquired four other names: VICTIM, KILLER, ACCOMPLICE, ACCUSER.",
"The folded scrap fits the corner missing from ATTENDANT. The cuff has kept the chalk. The ladder’s mark ends where the wall stopped pushing.",
"The paper runs beneath the sheet. The knife’s calibration comes first. A ruled line ends it. After that, the pen has followed a different point. The heading still reads POSITION; underneath, in smaller letters, SEAT.",
"Each entry has a time on the strip. The release, the preparation, the fall, the accusation: four accounts follow the same track. There is one space for the occupant’s name.",
"The chair isn’t in the study. Its record is.",
"You turn the case sheet over.",
"The instructions on the back are in your handwriting.",
"DO NOT GET UP."]
out=[]
for k,t in items:
    if k=='BRIDGE':
        out+= [('N',b) for b in bridge]; continue
    t=t.replace('from room 1','from problem 1').replace('from room 2','from problem 2')
    out.append((k,t))
# chorus: after H3 'The chorus', M lines -> plain lines, blank paragraphs at stanza breaks
ci=[i for i,(k,t) in enumerate(out) if k=='H3' and t=='The chorus'][0]
head=out[:ci+1]; ch=[t.strip() for k,t in out[ci+1:]]
stanza=[4,4,4,3,1,1,1,1]; lines=[];j=0
for si,n in enumerate(stanza):
    if si: lines.append('')
    lines+=ch[j:j+n]; j+=n
assert j==len(ch),(j,len(ch))
out=head+[('C',l) for l in lines]
assert out[-1][1]=='Something keeps your time.'
u=lambda s:len(s.encode('utf-16-le'))//2
pos=start; spans=[]
for k,t in out:
    spans.append((k,pos,pos+u(t)+1)); pos+=u(t)+1
text='\n'.join(t for k,t in out)   # no trailing newline: the doc's final newline closes the last line
end=pos-1+1  # last paragraph's newline is the document's own
R=lambda a,b:{"startIndex":a,"endIndex":b,"tabId":TAB}
rq=[{"insertText":{"location":{"index":start,"tabId":TAB},"text":text}},
 {"updateParagraphStyle":{"range":R(start,end),"paragraphStyle":{"namedStyleType":"NORMAL_TEXT"},"fields":"namedStyleType"}},
 {"updateTextStyle":{"range":R(start,end-1),"textStyle":{},"fields":"bold,italic,fontSize,weightedFontFamily,foregroundColor"}},
 {"updateTextStyle":{"range":R(start,end-1),"textStyle":{"foregroundColor":{"color":{"rgbColor":BR}}},"fields":"foregroundColor"}}]
runs=[]
for k,a,b in spans:
    b=min(b,end)
    if k in('H2','H3'):
        rq.append({"updateParagraphStyle":{"range":R(a,b),"paragraphStyle":{"namedStyleType":"HEADING_2" if k=='H2' else "HEADING_3"},"fields":"namedStyleType"}})
        rq.append({"updateTextStyle":{"range":R(a,b-1),"textStyle":{"bold":True,"foregroundColor":{"color":{"rgbColor":BR}}},"fields":"bold,foregroundColor"}})
    if k=='M':
        if runs and runs[-1][1]==a: runs[-1][1]=b
        else: runs.append([a,b])
for a,b in runs:
    rq.append({"updateTextStyle":{"range":R(a,b-1),"textStyle":{"weightedFontFamily":{"fontFamily":"Courier New"},"fontSize":{"magnitude":10,"unit":"PT"}},"fields":"weightedFontFamily,fontSize"}})
json.dump({"requests":rq,"writeControl":{"requiredRevisionId":rev}},open(sys.argv[4],'w'),ensure_ascii=False)
open(sys.argv[4]+'.txt','w').write('\n'.join(k+'|'+t for k,t in out))
print(len(rq),'requests',len(text),'chars',end)
