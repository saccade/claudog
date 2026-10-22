"""Page for gaps.py: each term as a staff across a path, uses as notes, glosses as stems, long gaps shaded.

Claude (Anthropic), 2026-10-22. Usage: python3 gaps_page.py GAPS.json OUT.html
"""
import json, sys
data = json.load(open(sys.argv[1]))
page = """<title>Forgetting Gaps</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Literata:opsz,wght@7..72,400;7..72,600&family=IBM+Plex+Sans:wght@400;600&display=swap">
<style>
/* a score: one staff per term, read left to right along a path; notes are uses, stems are glosses */
:root {
  --bg: #fbf9f6; --fg: #2a211b; --muted: #6d625a; --rule: #e2dad2; --panel: #f3efe9;
  --brown: #5a3a22; --cobalt: #1f4fa3; --red: #b3261e; --amber: #a86400; --gapwash: #efe5da; --coldwash: #f6e3c8;
  --body: "Literata", Georgia, serif; --ui: "IBM Plex Sans", system-ui, sans-serif;
}
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
  --bg: #1c1814; --fg: #ece5dc; --muted: #a99c90; --rule: #3a322b; --panel: #252019;
  --brown: #d2a57c; --cobalt: #8fb0ee; --red: #f08a7e; --amber: #e0a24a; --gapwash: #2c241c; --coldwash: #3a2a14; color-scheme: dark } }
:root[data-theme="dark"] {
  --bg: #1c1814; --fg: #ece5dc; --muted: #a99c90; --rule: #3a322b; --panel: #252019;
  --brown: #d2a57c; --cobalt: #8fb0ee; --red: #f08a7e; --amber: #e0a24a; --gapwash: #2c241c; --coldwash: #3a2a14; color-scheme: dark }
body { background: var(--bg); color: var(--fg); font: 15px/1.55 var(--body); }
.wrap { max-width: 90rem; margin: 0 auto; padding-block: 2rem 4rem;
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }
h1 { font: 600 2rem/1.2 var(--body); color: var(--brown); margin: 0 0 .4rem; text-wrap: balance; }
h2 { font: 600 1.2rem/1.3 var(--body); color: var(--brown); margin: 2rem 0 .4rem; text-wrap: balance; }
.by { font: 600 .85rem/1.4 var(--ui); color: var(--muted); margin: 0 0 1rem; }
.lede { max-width: 48rem; margin: 0 0 1.2rem; }
.controls { display: flex; flex-wrap: wrap; gap: .75rem 1.5rem; align-items: center; font: .9rem/1.3 var(--ui); margin: 0 0 .5rem; }
.tabs { display: flex; gap: .3rem; }
.tabs button { font: 600 .85rem/1 var(--ui); padding: .5rem .8rem; border: 1px solid var(--rule); background: var(--bg); color: var(--fg); border-radius: 3px; cursor: pointer; }
.tabs button[aria-pressed="true"] { background: var(--brown); color: var(--bg); border-color: var(--brown); }
button:focus-visible, input:focus-visible { outline: 2px solid var(--cobalt); outline-offset: 2px; }
.slider { display: flex; gap: .5rem; align-items: center; }
.slider output { font-variant-numeric: tabular-nums; min-width: 6.5rem; }
.legend { display: flex; flex-wrap: wrap; gap: .4rem 1.2rem; font: .82rem/1.3 var(--ui); color: var(--muted); margin: .25rem 0 .75rem; }
.legend svg { vertical-align: middle; margin-right: .3rem; }
.score { overflow-x: auto; border-top: 2px solid var(--brown); padding-top: .25rem; }
.score svg { display: block; }
.score text { font-family: var(--ui); }
.lists { display: grid; grid-template-columns: repeat(auto-fit, minmax(22rem, 1fr)); gap: 1rem 2rem; }
.lists > div { min-width: 0; }
.lists h3 { font: 600 .78rem/1.3 var(--ui); letter-spacing: .06em; text-transform: uppercase; color: var(--muted); margin: 0 0 .4rem; }
.item { border-top: 1px solid var(--rule); padding: .5rem 0; font-size: .9rem; }
.item b { font-family: var(--ui); font-size: .85rem; }
.item .where { font: .8rem/1.3 var(--ui); color: var(--muted); font-variant-numeric: tabular-nums; }
.item q { display: block; margin-top: .2rem; color: var(--muted); quotes: none; }
.none { color: var(--muted); font-size: .9rem; }
.foot { max-width: 48rem; color: var(--muted); font-size: .9rem; margin-top: 2rem; }
.foot p { margin: 0 0 .6rem; }
</style>
<div class="wrap">
<h1>Forgetting gaps</h1>
<p class="by">Written by Claude (Anthropic), 2026-10-22, for dr. kraemer. Measured on the current builds.</p>
<p class="lede">Each staff is one term, read left to right through a path's solutions. A note is a use. A red stem is a gloss, a sentence that says what the term is. A shaded stretch is a gap longer than the dial, and the mark where the term comes back shows whether it came back with a nod or cold.</p>
<div class="controls">
  <div class="tabs" role="group" aria-label="Path">
    <button type="button" id="p1" data-k="1" aria-pressed="true">Path 1</button>
    <button type="button" id="p2" data-k="2" aria-pressed="false">Path 2</button>
    <button type="button" id="p3" data-k="3" aria-pressed="false">Path 3</button>
    <button type="button" id="p4" data-k="4" aria-pressed="false">Path 4</button>
  </div>
  <label class="slider" for="th">Long gap at <input type="range" id="th" min="2000" max="12000" step="500" value="4000"> <output id="thv"></output></label>
</div>
<div class="legend">
  <span><svg width="14" height="14" aria-hidden="true"><circle cx="7" cy="7" r="3" fill="currentColor"></circle></svg>use</span>
  <span><svg width="14" height="18" aria-hidden="true"><line x1="7" y1="2" x2="7" y2="16" stroke="var(--red)" stroke-width="2"></line><circle cx="7" cy="12" r="3" fill="var(--red)"></circle></svg>gloss</span>
  <span><svg width="16" height="16" aria-hidden="true"><circle cx="8" cy="8" r="5.5" fill="var(--red)"></circle></svg>first use</span>
  <span><svg width="16" height="16" aria-hidden="true"><circle cx="8" cy="8" r="5" fill="none" stroke="var(--cobalt)" stroke-width="2"></circle></svg>back after a long gap, with a nod</span>
  <span><svg width="16" height="16" aria-hidden="true"><rect x="2" y="2" width="12" height="12" fill="none" stroke="var(--amber)" stroke-width="2"></rect></svg>back after a long gap, cold</span>
</div>
<div class="score" id="score"></div>
<h2 id="h-lists">What the dial picks out</h2>
<div class="lists">
  <div><h3>Comes back cold: candidates for a nod</h3><div id="cold"></div></div>
  <div><h3>Glossed at most uses: candidates for hammering</h3><div id="hammer"></div></div>
</div>
<div class="foot">
<p>The distance is solution text in characters, in reading order, statements left out. Path 1's solutions run about 18 thousand characters, so 4 thousand is roughly three problems.</p>
<p>A gloss is found by its wording (call, is the, that's the, means, read, we'll, or a colon right after the term), so it misses some and catches some that aren't. Hover a mark for its sentence. Arrow counts include every arrow on the page, so their staves are dense by nature.</p>
<p>Built by gaps.py and gaps_page.py in the repo; rerun after the sweep to see the new paths.</p>
</div>
</div>
<script>
const DATA = __DATA__;
const LABEL = 190, W = 1150, ROW = 30, TOP = 46;
let K = 1, TH = 4000;
try { const s = JSON.parse(localStorage.getItem("gaps") || "{}"); if (s.k) K = s.k; if (s.th) TH = s.th; } catch (e) {}
const esc = s => s.replace(/[&<>"]/g, c => ({"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;"}[c]));
function draw() {
  const d = DATA[K - 1], x = a => LABEL + a / d.total * (W - LABEL - 10);
  const H = TOP + d.terms.length * ROW + 10;
  let s = `<svg width="${W}" height="${H}" viewBox="0 0 ${W} ${H}" role="img" aria-label="Uses and glosses of each term along path ${K}">`;
  d.bounds.forEach(([a, n], i) => {
    s += `<line x1="${x(a)}" y1="${TOP - 8}" x2="${x(a)}" y2="${H - 6}" stroke="var(--rule)" stroke-width="1"></line>`;
    s += `<text x="${x(a) + 2}" y="${i % 2 ? 26 : 14}" font-size="10" fill="var(--muted)">${esc(n)}</text>`;
  });
  d.terms.forEach((t, r) => {
    const y = TOP + r * ROW + ROW / 2;
    s += `<text x="${LABEL - 10}" y="${y + 4}" font-size="12" text-anchor="end" fill="var(--fg)">${esc(t.name)}</text>`;
    s += `<line x1="${LABEL}" y1="${y}" x2="${W - 10}" y2="${y}" stroke="var(--rule)" stroke-width="1"></line>`;
    t.gaps.filter(g => g.len > TH).forEach(g => {
      s += `<rect x="${x(g.from)}" y="${y - 9}" width="${x(g.to) - x(g.from)}" height="18" fill="${g.nod ? "var(--gapwash)" : "var(--coldwash)"}"><title>${Math.round(g.len / 100) / 10}k characters without it, ${esc(g.after)} to ${esc(g.back)}</title></rect>`;
    });
    t.hits.forEach(h => {
      const cx = x(h.at), tip = `<title>${esc(h.piece)}: ${esc(h.s)}</title>`;
      if (h.first) s += `<circle cx="${cx}" cy="${y}" r="5.5" fill="var(--red)">${tip}</circle>`;
      else if (h.gloss) s += `<g><line x1="${cx}" y1="${y - 11}" x2="${cx}" y2="${y}" stroke="var(--red)" stroke-width="2"></line><circle cx="${cx}" cy="${y}" r="3" fill="var(--red)">${tip}</circle></g>`;
      else s += `<circle cx="${cx}" cy="${y}" r="2.6" fill="var(--fg)" fill-opacity=".7">${tip}</circle>`;
    });
    t.gaps.filter(g => g.len > TH).forEach(g => {
      const cx = x(g.to);
      s += g.nod ? `<circle cx="${cx}" cy="${y}" r="6" fill="none" stroke="var(--cobalt)" stroke-width="2"></circle>`
                 : `<rect x="${cx - 6}" y="${y - 6}" width="12" height="12" fill="none" stroke="var(--amber)" stroke-width="2"></rect>`;
    });
  });
  document.getElementById("score").innerHTML = s + "</svg>";
  const cold = [], ham = [];
  d.terms.forEach(t => {
    t.gaps.filter(g => g.len > TH && !g.nod).forEach(g => {
      const back = t.hits.find(h => h.at === g.to);
      cold.push({t: t.name, len: g.len, after: g.after, back: g.back, s: back ? back.s : ""});
    });
    if (t.uses >= 4 && t.glosses / t.uses >= 0.6) ham.push(t);
  });
  cold.sort((a, b) => b.len - a.len);
  document.getElementById("cold").innerHTML = cold.length ? cold.map(c =>
    `<div class="item"><b>${esc(c.t)}</b> <span class="where">${Math.round(c.len / 100) / 10}k without it, ${esc(c.after)} to ${esc(c.back)}</span><q>${esc(c.s)}</q></div>`).join("")
    : `<p class="none">Nothing comes back cold at this setting.</p>`;
  document.getElementById("hammer").innerHTML = ham.length ? ham.map(t =>
    `<div class="item"><b>${esc(t.name)}</b> <span class="where">${t.glosses} glosses in ${t.uses} uses</span><q>${esc(t.hits.filter(h => h.gloss).map(h => h.piece).join(", "))}</q></div>`).join("")
    : `<p class="none">No term is glossed at most of its uses.</p>`;
  document.getElementById("thv").textContent = (TH / 1000).toFixed(1) + "k characters";
  document.getElementById("th").value = TH;
  document.querySelectorAll(".tabs button").forEach(b => b.setAttribute("aria-pressed", String(+b.dataset.k === K)));
  try { localStorage.setItem("gaps", JSON.stringify({k: K, th: TH})); } catch (e) {}
}
document.querySelectorAll(".tabs button").forEach(b => b.addEventListener("click", () => { K = +b.dataset.k; draw(); }));
document.getElementById("th").addEventListener("input", e => { TH = +e.target.value; draw(); });
draw();
</script>"""
open(sys.argv[2], "w").write(page.replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/")))
print("wrote", sys.argv[2])
