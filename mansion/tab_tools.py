#!/usr/bin/env python3
# Written by Claude (Anthropic), 2026-10-20. Helpers for the assembled-draft tab: locate paragraphs, build style fixes.
import json,sys
TABID='t.9kpjybvwfvl8'
BR={"red":0.19607843,"green":0.10588235,"blue":0.023529412}
H2={"Billiard room","Conservatory","Ballroom: the hoop","Ballroom: the ribbon"}
H3={"What the blow left","Who cocked the cue","Three further exhibits","The card","The basin keeps the beat","The beam that answers differently","The wheel that comes back","Something stands still","The ribbon through the floor"}
def paras(path):
    d=json.load(open(path))['content']
    t=[x for x in d['tabs'] if x['tabProperties']['tabId']==TABID][0]
    out=[]
    for e in t['documentTab']['body']['content']:
        p=e.get('paragraph')
        if p:
            s=''.join(r.get('textRun',{}).get('content','') for r in p['elements'])
            out.append((e['startIndex'],e['endIndex'],p['paragraphStyle']['namedStyleType'],s))
    return d['revisionId'],out
if __name__=='__main__':
    cmd,path=sys.argv[1],sys.argv[2]
    rev,ps=paras(path)
    if cmd=='info':
        print(rev)
        for a,b,st,s in ps:
            if s.startswith('Notes on the pilot'): print('NOTES',a)
        print('END',ps[-1][1])
    if cmd=='styles':
        start=int(sys.argv[3]); notes=[a for a,b,st,s in ps if s.startswith('Notes on the pilot')][0]
        rq=[{"updateParagraphStyle":{"range":{"startIndex":start,"endIndex":notes,"tabId":TABID},"paragraphStyle":{"namedStyleType":"NORMAL_TEXT"},"fields":"namedStyleType"}},
            {"updateTextStyle":{"range":{"startIndex":start,"endIndex":notes,"tabId":TABID},"textStyle":{},"fields":"bold,italic,fontSize,weightedFontFamily,foregroundColor"}},
            {"updateTextStyle":{"range":{"startIndex":start,"endIndex":notes,"tabId":TABID},"textStyle":{"foregroundColor":{"color":{"rgbColor":BR}}},"fields":"foregroundColor"}}]
        for a,b,st,s in ps:
            if a>=start and a<notes:
                h=s.rstrip('\n')
                k=2 if h in H2 else 3 if h in H3 else 0
                if k:
                    rq.append({"updateParagraphStyle":{"range":{"startIndex":a,"endIndex":b,"tabId":TABID},"paragraphStyle":{"namedStyleType":"HEADING_%d"%k},"fields":"namedStyleType"}})
                    rq.append({"updateTextStyle":{"range":{"startIndex":a,"endIndex":b-1,"tabId":TABID},"textStyle":{"bold":True,"foregroundColor":{"color":{"rgbColor":BR}}},"fields":"bold,foregroundColor"}})
        print(json.dumps(rq,ensure_ascii=False))
