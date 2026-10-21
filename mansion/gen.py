import json,sys
BROWN={"red":0.329,"green":0.18,"blue":0.039}   # #542E0A
GREEN={"red":0.031,"green":0.29,"blue":0.11}    # #084A1C
def u16(s): return len(s.encode('utf-16-le'))//2
def col(a): return {"color":{"rgbColor":BROWN if a=='claude' else GREEN}}
def build(start, segs):
    """segs: list of dict(text, role, author, pb) ; returns styles list, total len"""
    reqs=[];i=start
    for s in segs:
        t=s['text'];n=u16(t);a,b=i,i+n;r=s['role']
        if r=='title':
            reqs.append(dict(updateTextStyle=dict(range=dict(startIndex=a,endIndex=b),textStyle=dict(foregroundColor=col(s['author']),bold=True),fields="foregroundColor,bold")))
            reqs.append(dict(updateParagraphStyle=dict(range=dict(startIndex=a,endIndex=b),paragraphStyle=dict(namedStyleType="TITLE"),fields="namedStyleType")))
        elif r=='h1':
            reqs.append(dict(updateParagraphStyle=dict(range=dict(startIndex=a,endIndex=b),paragraphStyle=dict(namedStyleType="HEADING_1",pageBreakBefore=bool(s.get('pb'))),fields="namedStyleType,pageBreakBefore")))
            reqs.append(dict(updateTextStyle=dict(range=dict(startIndex=a,endIndex=b),textStyle=dict(foregroundColor=col(s['author']),bold=True,weightedFontFamily=dict(fontFamily="Arial",weight=700),fontSize=dict(magnitude=20,unit="PT")),fields="foregroundColor,bold,weightedFontFamily,fontSize")))
        elif r=='prose':
            reqs.append(dict(updateParagraphStyle=dict(range=dict(startIndex=a,endIndex=b),paragraphStyle=dict(namedStyleType="NORMAL_TEXT",lineSpacing=115,spaceBelow=dict(magnitude=0,unit="PT")),fields="namedStyleType,lineSpacing,spaceBelow")))
            reqs.append(dict(updateTextStyle=dict(range=dict(startIndex=a,endIndex=b),textStyle=dict(foregroundColor=col(s['author']),bold=False,weightedFontFamily=dict(fontFamily="Arial",weight=400),fontSize=dict(magnitude=11,unit="PT")),fields="foregroundColor,bold,weightedFontFamily,fontSize")))
            for sub,au in s.get('marks',[]):
                k=t.index(sub);ka=a+u16(t[:k]);kb=ka+u16(sub)
                reqs.append(dict(updateTextStyle=dict(range=dict(startIndex=ka,endIndex=kb),textStyle=dict(foregroundColor=col(au),bold=True),fields="foregroundColor,bold")))
            for sub in s.get('heads',[]):
                k=t.index(sub);ka=a+u16(t[:k]);kb=ka+u16(sub)
                reqs.append(dict(updateTextStyle=dict(range=dict(startIndex=ka,endIndex=kb),textStyle=dict(bold=True),fields="bold")))
        elif r=='mono':
            reqs.append(dict(updateParagraphStyle=dict(range=dict(startIndex=a,endIndex=b),paragraphStyle=dict(namedStyleType="NORMAL_TEXT",lineSpacing=100,spaceAbove=dict(magnitude=0,unit="PT"),spaceBelow=dict(magnitude=0,unit="PT")),fields="namedStyleType,lineSpacing,spaceAbove,spaceBelow")))
            reqs.append(dict(updateTextStyle=dict(range=dict(startIndex=a,endIndex=b),textStyle=dict(foregroundColor=col(s['author']),bold=False,weightedFontFamily=dict(fontFamily="Roboto Mono",weight=400),fontSize=dict(magnitude=9.5,unit="PT")),fields="foregroundColor,bold,weightedFontFamily,fontSize")))
            first=t.index('\n')+1
            if not s.get('notitle'): reqs.append(dict(updateTextStyle=dict(range=dict(startIndex=a,endIndex=a+first-1),textStyle=dict(bold=True),fields="bold")))
            if s.get('pb'):
                reqs.append(dict(updateParagraphStyle=dict(range=dict(startIndex=a,endIndex=a+first),paragraphStyle=dict(pageBreakBefore=True),fields="pageBreakBefore")))
        i=b
    return reqs,i
if __name__=='__main__':
    spec=json.load(open(sys.argv[1]))
    start=int(sys.argv[2])
    for s in spec:
        if 'file' in s: s['text']=open(s['file']).read()
    reqs,end=build(start,spec)
    json.dump(reqs,open(sys.argv[3],'w'),separators=(',',':'))
    print("end index",end,"(next insert at",end,")")
