import json,difflib,sys
base='/root/.claude/projects/-home-claude/703a9c19-4a4f-5d49-a5f7-811fca7a3452/tool-results/'
def load(p):
    d=json.load(open(base+p))['content']
    tabs=[]
    for t in d['tabs']:
        s=''
        for el in t['documentTab']['body']['content']:
            para=el.get('paragraph')
            if para: s+=''.join(e.get('textRun',{}).get('content','') for e in para['elements'])
        tabs.append(s.split('\n'))
    return d,tabs
d0,a=load(sys.argv[1]); d1,b=load(sys.argv[2])
print('rev',d1['revisionId'][:24],'tabs',[t['tabProperties']['title'] for t in d1['tabs']],[len(x) for x in a],[len(x) for x in b])
for el in d1['tabs'][0]['documentTab']['body']['content'][:2]:
    p=el.get('paragraph')
    if p:
        for e in p['elements']:
            t=e['textRun'];print(repr(t['content'][:40]),t['textStyle'].get('foregroundColor',{}).get('color',{}).get('rgbColor'))
for i in range(len(b)):
    old=a[i] if i<len(a) else []
    for l in difflib.unified_diff(old,b[i],lineterm='',n=0):
        print(i,l[:400])
