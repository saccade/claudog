"""Shared notation, narrative, and poetry plan.
Codex (OpenAI), 2026-10-23. Extends Claude's planners; editorial features describe
choices, not a claim that regex can judge a poem. The numeric formatter reads the
same data the planning view displays.
"""
import copy, html, json, re
from pathlib import Path

MANIFEST = Path(__file__).with_name("path_features.json")

def load(path=None):
    data = json.loads(Path(path or MANIFEST).read_text())
    assert data["schema_version"] == 1
    ids = [f["id"] for f in data["features"]]
    assert len(ids) == len(set(ids)), "duplicate feature ID"
    for f in data["features"]:
        assert set(f["paths"]) == {"1", "2", "3", "4"}, f["id"]
        assert f["implementation"] in {"automatic", "editorial"}
        if f.get("allowed_modes"):
            for state in f["paths"].values():
                assert state["mode"] in f["allowed_modes"], f["id"]
                if state.get("then"):
                    assert state["then"]["mode"] in f["allowed_modes"], f["id"]
        if f["id"] == "number-form":
            for state in f["paths"].values():
                for anchor in (state["starts_at"], state.get("then", {}).get("starts_at", "start")):
                    assert anchor == "start" or re.fullmatch(r"\d+-[a-zαβγ]|[a-gαβγ]-\d+", anchor), anchor
    return data

def feature(fid, data=None):
    return next(f for f in (data or load())["features"] if f["id"] == fid)

def mode_at(fid, path, reached=(), data=None):
    state = feature(fid, data)["paths"][str(path)]
    later = state.get("then")
    return later["mode"] if later and later["starts_at"] in reached else state["mode"]

def observe(items, path, data=None):
    data = data or load()
    reached, numbers = set(), []
    for tag, raw in items:
        text = re.sub(r"</?[^>]+>", "", raw)
        part = re.match(r"^\((\d+-[a-zαβγ]|[a-gαβγ]-\d+)\)", text)
        if part: reached.add(part.group(1))
        mode = mode_at("number-form", path, reached, data)
        ds = re.findall(r"(?<![\d.])\d+\.\d+(?!\d)", text)
        fs = re.findall(r"(?<![\d/])\d+/\d+(?![\d/])", text)
        if ds or fs:
            numbers.append({"part": part.group(1) if part else "", "mode": mode,
                            "decimals": len(ds), "fractions": len(fs),
                            "text": text[:220]})
    return {"path": path, "features": [
        {"id": f["id"], "kind": f["kind"], "title": f["title"],
         "implementation": f["implementation"], "status": f["status"],
         "priority": f["priority"], "state": f["paths"][str(path)]}
        for f in data["features"]],
        "numbers": numbers,
        "decimal_count": sum(n["decimals"] for n in numbers),
        "fraction_count": sum(n["fractions"] for n in numbers),
        "mixed_number_passages": [n for n in numbers if n["decimals"] and n["fractions"]]}

def markdown(data=None):
    data = data or load()
    lines = ["## Path features: notation, form, and poetic choices", "",
             "One plan shared with the builder. Automatic means a presentation policy can be checked; "
             "editorial means a choice to read and assess. Planned verse is not reported as applied.", "",
             "| Feature | Kind / priority | State | Path 1 | Path 2 | Path 3 | Path 4 |",
             "|---|---|---|---|---|---|---|"]
    for f in data["features"]:
        cells = []
        for k in range(1,5):
            s = f["paths"][str(k)]
            cell = s["mode"] + " @ " + s["starts_at"]
            if s.get("then"): cell += " → " + s["then"]["mode"] + " @ " + s["then"]["starts_at"]
            if s.get("note"): cell += ": " + s["note"]
            cells.append(cell.replace("|", "\\|"))
        lines.append("| " + " | ".join([f["title"], f["kind"]+" / "+f["priority"],
                                         f["status"]+" ("+f["implementation"]+")"]+cells) + " |")
    return "\n".join(lines)+"\n"

def panel(data=None, observations=None):
    data = data or load()
    payload = json.dumps({"plan": data, "observed": observations or []}, ensure_ascii=False).replace("</", "<\\/")
    return r'''<section id="path-feature-plan">
<h2>Notation, form, and poetic changes</h2>
<p class="sub">The same plan drives number formatting and displays editorial choices.
Changing a control previews a plan; Export saves it. Nothing here writes to Google Docs.
Observations describe the current build, not the preview. Poetry has no automatic correctness score.</p>
<p><label>Show <select id="feature-kind"><option value="">all kinds</option>
<option>notation</option><option>structure</option><option>poetry</option><option>narrative</option></select></label>
<button id="features-export" type="button">Export plan JSON</button>
<button id="features-reset" type="button">Reset preview</button></p>
<div class="scroll"><table><thead><tr><th>Feature</th><th>Path 1</th><th>Path 2</th><th>Path 3</th><th>Path 4</th></tr></thead>
<tbody id="feature-rows"></tbody></table></div>
<p id="feature-observed" class="sub"></p>
<script id="feature-data" type="application/json">''' + payload + r'''</script>
<script>
(() => {
const data=JSON.parse(document.getElementById("feature-data").textContent);
let plan=structuredClone(data.plan);
const esc=s=>String(s).replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const modes=["off","decimals","fractions","full","reprise","reel","verse","introduce","use","full-range","selective","prose","chorus-ending","interleaving","slow-burn","deeper","hurry","deja-vu","ad-rhythm","keep","preserve-verbatim"];
function select(value, attr, choices) {
  return '<select '+attr+'>'+choices.map(x=>'<option'+(x===value?' selected':'')+'>'+esc(x)+'</option>').join('')+'</select>';
}
function render(){
 const kind=document.getElementById("feature-kind").value;
 document.getElementById("feature-rows").innerHTML=plan.features.filter(f=>!kind||f.kind===kind).map(f=>{
 let row='<tr><th scope="row">'+esc(f.title)+'<br><small>'+esc(f.kind+' · '+f.priority+' · '+f.implementation)+'<br>'+esc(f.status)+'</small></th>';
 for(let k=1;k<=4;k++){ const s=f.paths[k], a='data-feature="'+esc(f.id)+'" data-path="'+k+'"';
 row+='<td>'+select(s.mode,a+' data-field="mode"',f.allowed_modes||Array.from(new Set([s.mode,...modes])))+
 '<br><label>Begins <input '+a+' data-field="starts_at" value="'+esc(s.starts_at)+'" size="9"></label>';
 if(s.then) row+='<br>'+select(s.then.mode,a+' data-field="then.mode"',f.allowed_modes||modes)+
 '<br><label>Switch at '+select(s.then.starts_at,a+' data-field="then.starts_at"',["start",...Array.from({length:13},(_,i)=>(i+1)+"-a")])+'</label>';
 row+='<p>'+esc(s.note||'')+'</p></td>';
 }return row+'</tr>';
 }).join("");
 document.getElementById("feature-observed").textContent=data.observed.map(o=>
 'Built path '+o.path+': '+o.decimal_count+' decimal literals, '+o.fraction_count+
 ' fraction literals. Counts describe the forms, not a target to maximize.').join(' ');
}
document.getElementById("feature-kind").addEventListener("change",render);
document.getElementById("feature-rows").addEventListener("change",e=>{
 const a=e.target.dataset;if(!a.feature)return;
 const feature=plan.features.find(f=>f.id===a.feature),s=feature.paths[a.path];
 if(a.field.startsWith("then."))s.then[a.field.slice(5)]=e.target.value;else s[a.field]=e.target.value;
 feature.status="planned";
});
document.getElementById("features-reset").addEventListener("click",()=>{plan=structuredClone(data.plan);render();});
document.getElementById("features-export").addEventListener("click",()=>{
 const blob=new Blob([JSON.stringify(plan,null,2)+"\n"],{type:"application/json"});
 const u=URL.createObjectURL(blob),a=document.createElement("a");a.href=u;a.download="path_features.json";a.click();URL.revokeObjectURL(u);
});
render();
})();
</script></section>'''
