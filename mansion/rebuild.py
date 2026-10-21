#!/usr/bin/env python3
# Written by Claude (Anthropic), 2026-10-21. Rebuilds the reading-draft tab from clean sources after a bad replaceAllText.
import sys,json
sys.path.insert(0,'/home/claude/claudog/mansion')
import tab_tools as T
S='/tmp/claude-0/-home-claude/703a9c19-4a4f-5d49-a5f7-811fca7a3452/scratchpad/mansion/'
clean='/root/.claude/projects/-home-claude/703a9c19-4a4f-5d49-a5f7-811fca7a3452/tool-results/mcp-Google_Docs-read_doc-1792555946262.txt'
rev,ps=T.paras(clean)
out=[]
for a,b,st,s in ps[:-1]:
    k={'HEADING_1':'H1','HEADING_2':'H2','HEADING_3':'H3'}.get(st,'N'); out.append((k,s.rstrip('\n')))
assert ps[-1][3]=='\n'
out[0]=('N','Written by Claude (Anthropic), 2026-10-21 00:20.')
for line in open(S+'lh_batch.json.txt').read().split('\n'):
    k,t=line.split('|',1); out.append((k,t))
assert out[-1][1]=='Something keeps your time.'
u=lambda s:len(s.encode('utf-16-le'))//2
pos=1;spans=[]
for k,t in out: spans.append((k,pos,pos+u(t)+1)); pos+=u(t)+1
end=pos           # includes the doc's own final newline
text='\n'.join(t for k,t in out)
TAB=T.TABID;BR=T.BR
R=lambda a,b:{"startIndex":a,"endIndex":b,"tabId":TAB}
ins=[{"insertText":{"location":{"index":1,"tabId":TAB},"text":text}}]
sty=[{"updateParagraphStyle":{"range":R(1,end),"paragraphStyle":{"namedStyleType":"NORMAL_TEXT"},"fields":"namedStyleType"}},
 {"updateTextStyle":{"range":R(1,end-1),"textStyle":{},"fields":"bold,italic,fontSize,weightedFontFamily,foregroundColor"}},
 {"updateTextStyle":{"range":R(1,end-1),"textStyle":{"foregroundColor":{"color":{"rgbColor":BR}}},"fields":"foregroundColor"}}]
runs=[]
for k,a,b in spans:
    if k in('H1','H2','H3'):
        n={'H1':1,'H2':2,'H3':3}[k]
        sty.append({"updateParagraphStyle":{"range":R(a,b),"paragraphStyle":{"namedStyleType":"HEADING_%d"%n},"fields":"namedStyleType"}})
        sty.append({"updateTextStyle":{"range":R(a,b-1),"textStyle":{"bold":True,"foregroundColor":{"color":{"rgbColor":BR}}},"fields":"bold,foregroundColor"}})
    if k=='M':
        if runs and runs[-1][1]==a: runs[-1][1]=b
        else: runs.append([a,b])
for a,b in runs:
    sty.append({"updateTextStyle":{"range":R(a,b-1),"textStyle":{"weightedFontFamily":{"fontFamily":"Courier New"},"fontSize":{"magnitude":10,"unit":"PT"}},"fields":"weightedFontFamily,fontSize"}})
curend=int(sys.argv[1])
dele=[{"deleteContentRange":{"range":R(1,curend-1)}}]
json.dump(dele+ins,open(S+'rb_ins.json','w'),ensure_ascii=True,separators=(',',':'))
json.dump(sty,open(S+'rb_sty.json','w'),ensure_ascii=True,separators=(',',':'))
open(S+'rb_expected.txt','w').write(text)
print(len(text),end,len(sty),len(out))
