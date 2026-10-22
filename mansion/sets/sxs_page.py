"""Side-by-side page: set 1's passages written with trig and signs, and with arrows.

Claude (Anthropic), 2026-10-22. Usage: python3 sxs_page.py PAIRS.json FINDINGS.html OUT.html
PAIRS: [{"title", "statement": [..], "old": [..], "new": [..]}]; FINDINGS: an HTML fragment (the readers' report).
"""
import html, json, re, sys
P = json.load(open(sys.argv[1])); F = open(sys.argv[2]).read()

def para(s):
    e = html.escape(s, quote=False).replace("†", "<sup>†</sup>")
    cls = ' class="eq"' if (s.startswith("    ") or re.match(r"^(\(H − R\) ↑ ×|\(2/5\) m|½ \(|\(m \+ I)", s)) else ""
    return f"<p{cls}>{e.strip()}</p>"

cards = []
for i, p in enumerate(P, 1):
    cards.append(f"""<section class="pair" id="p{i}">
<h2>{html.escape(p['title'])}</h2>
<details><summary>Problem statement</summary>{''.join(para(s) for s in p['statement'])}</details>
<div class="cols">
<div class="col old"><div class="tag">Trig and signs</div>{''.join(para(s) for s in p['old'])}</div>
<div class="col new"><div class="tag">Arrows</div>{''.join(para(s) for s in p['new'])}</div>
</div></section>""")

page = f"""<title>Trig Beside Arrows</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Literata:opsz,wght@7..72,400;7..72,600&family=IBM+Plex+Sans:wght@400;600&display=swap">
<style>
/* two ruled columns per problem, like a teacher's answer key held beside a student's page */
:root {{
  --bg: #fbf9f6; --fg: #2a211b; --muted: #6d625a; --rule: #e2dad2;
  --brown: #5a3a22; --cobalt: #1f4fa3; --red: #b3261e; --panel: #f3efe9;
  --body: "Literata", Georgia, serif; --ui: "IBM Plex Sans", system-ui, sans-serif;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg: #1c1814; --fg: #ece5dc; --muted: #a99c90; --rule: #3a322b;
  --brown: #d2a57c; --cobalt: #8fb0ee; --red: #f08a7e; --panel: #252019; color-scheme: dark }} }}
:root[data-theme="dark"] {{
  --bg: #1c1814; --fg: #ece5dc; --muted: #a99c90; --rule: #3a322b;
  --brown: #d2a57c; --cobalt: #8fb0ee; --red: #f08a7e; --panel: #252019; color-scheme: dark }}
body {{ background: var(--bg); color: var(--fg); font: 16px/1.6 var(--body); }}
.wrap {{ max-width: 72rem; margin: 0 auto; padding-block: 2rem 4rem;
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }}
h1 {{ font: 600 2rem/1.2 var(--body); color: var(--brown); margin: 0 0 .5rem; text-wrap: balance; }}
h2 {{ font: 600 1.25rem/1.3 var(--body); color: var(--brown); margin: 0 0 .5rem; text-wrap: balance; }}
.by {{ font: 600 .9rem/1.4 var(--ui); color: var(--muted); margin: 0 0 1.25rem; }}
.lede {{ max-width: 44rem; margin: 0 0 2rem; }}
.pair {{ border-top: 1px solid var(--rule); padding-block: 1.5rem; display: grid; gap: .75rem; }}
details {{ font-size: .92rem; color: var(--muted); }}
summary {{ font: 600 .8rem/1.4 var(--ui); letter-spacing: .04em; text-transform: uppercase; cursor: pointer; }}
summary:focus-visible {{ outline: 2px solid var(--brown); outline-offset: 2px; }}
.cols {{ display: grid; grid-template-columns: 1fr 1fr; gap: 1.25rem; }}
.col {{ min-width: 0; padding: .25rem 0 .25rem 1rem; border-left: 3px solid; }}
.col.old {{ border-color: var(--cobalt); }} .col.new {{ border-color: var(--red); }}
.tag {{ font: 600 .75rem/1.4 var(--ui); letter-spacing: .06em; text-transform: uppercase; margin-bottom: .25rem; }}
.old .tag {{ color: var(--cobalt); }} .new .tag {{ color: var(--red); }}
.col p {{ margin: 0 0 .6rem; overflow-wrap: anywhere; }}
p.eq {{ padding-left: 1.5rem; }}
.findings {{ border-top: 2px solid var(--brown); margin-top: 1rem; padding-top: 1.5rem; max-width: 46rem; }}
.findings h3 {{ font: 600 1rem/1.4 var(--ui); color: var(--brown); margin: 1.25rem 0 .25rem; }}
.findings p, .findings li {{ margin: 0 0 .6rem; }}
.findings blockquote {{ margin: .25rem 0 .75rem; padding-left: 1rem; border-left: 2px solid var(--rule); color: var(--muted); }}
@media (max-width: 760px) {{ .cols {{ grid-template-columns: 1fr; }} }}
</style>
<div class="wrap">
<h1>Trig beside arrows</h1>
<p class="by">Written by Claude (Anthropic), 2026-10-22, for dr. kraemer. The passages are from solution set 1; the readers' notes are from two fresh model readers.</p>
<p class="lede">Six places in set 1, each written the earlier way (sines, cosines and signed torques) and the way it reads now (arrows, dots and crosses). Same physics, same numbers. Below the pairs: what two newcomer readers made of them, read blind, A and B shuffled.</p>
{''.join(cards)}
<section class="findings">{F}</section>
</div>"""
open(sys.argv[3], "w").write(page)
print("wrote", sys.argv[3], len(page))
