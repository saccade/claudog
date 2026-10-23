"""IDs for The Mansion workbook, the project's one live doc (doc 07:51-08:37, 2026-10-23).

Claude (Anthropic), 2026-10-23. Everything that writes to the workbook takes its doc and tab IDs from here.
"""
DOC = "1fKhIhh077LMGux9o3iC7vzjgbepmmxWXurvmtV8GeHQ"
URL = f"https://docs.google.com/document/d/{DOC}/edit"
TAB = {
    "start": "t.0", "next": "t.mnefqzh9tgbf", "paths": "t.723tx4uvm5nl",
    "path1": "t.9gq9164tzjia", "path2": "t.n48yq7csgbx7", "path3": "t.5dyqu0kfwmvx", "path4": "t.q58y1fpf41q4",
    "craft": "t.ilzip2gkkpu6", "intrigue": "t.4zbsstxg7o9q", "phrases": "t.wmc1f4o7j736", "clowns": "t.7yb939w8cbdz",
    "poetry": "t.3ho7r8s8a9in", "loose": "t.tr1r5bdmnlxu", "fresh": "t.2idm4yr8vpnd", "verses": "t.d8p3ngjurwmn",
    "discussion": "t.cuwtjj1bqbsi", "archive": "t.o5qj7fwmxfl2", "appendix": "t.ukjm0svct28",
}
def tab_url(key): return f"{URL}?tab={TAB[key]}"
PATH_TAB = {1: TAB["path1"], 2: TAB["path2"], 3: TAB["path3"], 4: TAB["path4"]}

PLANNING = "1CsIlCADOka-OCrZ3YEX_74atll1nLo0Kf4tya6lgN24"   # the Mansion that did not Spin — planning (frozen; Goals log ends at the hand-back)
POETRY_NOTEBOOK = "17S5vLeBYNFWOxDcav9-Lm94OMX4NwYNgA-TIPzUPhLc"
