import sys, textwrap
src, dst, tm = sys.argv[1], sys.argv[2], sys.argv[3]
import re
NB='\u00a0'
text = open(src, encoding='utf-8').read().replace('@@TIME@@', tm)
text = re.sub(r'(\d) (?=(s|m|J|kg|mw|card|hand|cat|thump|zoom|zlow|rad|C|V|F|kg m²|g cm²|m²|percent|lines?)\b)', lambda m: m.group(1)+NB, text)
text = re.sub(r'\b([XY]) (?=\d)', lambda m: m.group(1)+NB, text)
text = text.replace(' = ', NB+'='+NB).replace('kg m²', 'kg'+NB+'m²')
paras = text.split('\n\n')
out = []
for p in paras:
    p = p.strip('\n')
    lines = p.split('\n')
    if all(l.startswith('|') for l in lines):
        out.append('\n'.join(l[1:] for l in lines))
    elif p.startswith('- '):
        out.append(textwrap.fill(' '.join(lines)[2:], 66, initial_indent='- ', subsequent_indent='  ', break_on_hyphens=False))
    else:
        out.append(textwrap.fill(' '.join(lines), 66, break_on_hyphens=False))
res = ('\n\n'.join(out) + '\n').replace(NB, ' ')
open(dst, 'w', encoding='utf-8').write(res)
bad = [(i+1, len(l)) for i, l in enumerate(res.split('\n')) if len(l) > 66]
print('lines', res.count('\n'), 'too long', bad)
