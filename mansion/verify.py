import json,sys,glob
f=sorted(glob.glob('/root/.claude/projects/-home-claude/*/tool-results/mcp-Google_Docs-read_doc-*.txt'),key=lambda p:__import__('os').path.getmtime(p))[-1]
d=json.load(open(f))['content']
body=d['tabs'][0]['documentTab']['body']['content']
txt='';runs=[]
for el in body:
    p=el.get('paragraph')
    if not p: continue
    for e in p['elements']:
        tr=e.get('textRun')
        if tr: runs.append((e['startIndex'],tr['content'],tr.get('textStyle',{}),p['paragraphStyle'].get('namedStyleType'))); txt+=tr['content']
print("revision",d['revisionId'],"len",len(txt))
open('doc_text.txt','w').write(txt)
srcs=sys.argv[1:]
exp=''
import os
for s in srcs:
    exp+=open(s).read()
# check each source occurs contiguous in doc text
pos=0
for s in srcs:
    t=open(s).read()
    k=txt.find(t)
    print(os.path.basename(s)[:50], "FOUND at",k if k>=0 else "MISSING")
