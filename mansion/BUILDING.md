# Working the repo: how the Mansion's docs get built

Written by Claude (Anthropic), 2026-10-23 10:10, for Codex (OpenAI) and dr. kraemer. Claude is offline until tomorrow, so this covers the plumbing Codex needs to take the turn: the code in saccade/claudog that builds the four paths and the problem set, and the scripts that write the workbook. The rules and the plan are in the workbook itself: [Start here](https://docs.google.com/document/d/1fKhIhh077LMGux9o3iC7vzjgbepmmxWXurvmtV8GeHQ/edit?tab=t.0), [Next](https://docs.google.com/document/d/1fKhIhh077LMGux9o3iC7vzjgbepmmxWXurvmtV8GeHQ/edit?tab=t.mnefqzh9tgbf), and [Craft](https://docs.google.com/document/d/1fKhIhh077LMGux9o3iC7vzjgbepmmxWXurvmtV8GeHQ/edit?tab=t.ilzip2gkkpu6). This file is only the how.

## The one rule underneath

The builder is the source for the four path tabs. Don't fix a path tab by hand; fix the builder, rebuild, and bring the tab up to the build. The one exception is doc: he edits path tabs directly, and his edits must go into the builder before the next write to that tab, or the write erases them. `set_doc_verify.py` shows any difference between a tab and the build, so run it first and fold in whatever it finds.

A complete edit, start to finish:

1. Change the builder (where: below).
2. `cd mansion/sets && python3 build_sets.py && python3 repeats.py && python3 check_levels.py`
3. Check that each change actually landed: `grep` the new wording in `set1.txt` … `set4.txt`. Most edit lists assert one match, but `ROUND` doesn't, so a stale old string there fails silently.
4. If arrows, dots, or crosses changed: `python3 checks/arrows.py` from the repo root (97 checks; exit 1 on a failure).
5. Bring each affected path tab up to its build, then style it, then verify all four (below).
6. Commit with a message that names doc's message and time, and push.
7. Post a Discussion entry with the new count, then tell doc the count in chat.
8. Log it in the provenance ledger, with append_values only.

## Layout

```
mansion/
  sets/build_sets.py     the builder: writes set1..4.html (for the tabs) and set1..4.txt (for checks)
  sets/levels.py         LEVEL[1..4]: each level's wording, as (old, new) edits; cumulative, so path 3 gets levels 1 to 3
  sets/p4_reel.py        REEL4: path 4's brisk replacement for each labeled part
  sets/r1_now.txt .. r4_now.txt, cl214_now.txt
                         flattened inputs (Codex's four release copies; the standard statements). Don't edit them;
                         patch in the builder, so every change has a line and a comment
  sets/repeats.py        any line that appears twice in a path (nothing repeats exactly: R-125)
  sets/check_levels.py   words a path uses before its level brings them in (some hits are story text: read them)
  sets/gaps.py           how long a reader goes without each term (R-117; a picture, not a target)
  sets/lineup_page.py    the side-by-side lineup page (Claude publishes it; it's behind today's line edits)
  set_doc_patch.py       a tab's text up to the build, by replaceAllText (unguarded)
  workbook/para_swap.py  the same, by position, for lines that appear more than once (guarded)
  set_doc_replace.py     whole-body replace, for structural changes (guarded)
  set_doc_style.py       a tab's styles up to the build (guarded)
  set_doc_verify.py      a tab against the build: text, headings, indents, italic, bold, superscripts, no color
  goals_post.py          a Discussion entry with its count, from a small spec
  workbook/ids.py        the workbook's doc ID and every tab ID; PATH_TAB[k] for the paths
  workbook/tabsel.py     tab_doc (one tab out of a full read), tabify (scope a batch to one tab)
  workbook/tabs/*.md     sources for Start here, Next, Paths, Craft, the Discussion header, the archive, and the Appendix
  workbook/md_tab.py     writes an empty tab from one of those sources
  workbook/copy_tab.py, compare_tab.py, retire.py
                         the move into the workbook: copying tabs, checking a copy, the RETIRED line on old docs
  poems/narrative_intrigue.py
                         writes the Narrative intrigue tab
  pset/mansion_pset.tex  the problem set; the built PDF sits beside it
checks/arrows.py         the Test reality button for the arrows
```

The other top-level scripts in `mansion/` (rooms, check_rooms*, goals_*.py, pass2, pass3, …) are one-offs from earlier passes, kept as history. Don't build on them.

## Where an edit goes in the builder

`build(k)` runs in this order. Put a change at the earliest stage that covers every path it should reach.

1. The release route from `r{k}_now.txt`, then `apply_edits` with `LEVEL[1..k]` from `levels.py`. Wording that belongs to a level goes here. A level-2 word appears in paths 2 to 4.
2. Named lists of doc's rulings, applied with asserts: `SPOOL_I`, `DOC_0806`, `NO_NEGATIVE_FORCES`, `SETUP_DOC`, `SWEEP_UNIT`, and more. Add to the list whose comment matches, or start a new one with a comment naming doc's message.
3. `solutions_only`: statements live in the problem set, not the paths.
4. `P1_GLOSS` and `P1_FINAL`: path 1 only, its slower first explanations.
5. Paths 2 to 4: `MIDDLE` and `REEL`.
6. `ROUND`: late line fixes in every path (two figures, and doc's 10-23 line edits). Each entry carries a comment with doc's time.
7. `TWO`: rounding to two figures.
8. Path 4: `p4_reel.REEL4` replaces each labeled part wholesale. **A wording change in path 4 usually has to go in REEL4 too**, or the reel overwrites it.
9. The drawer passage lines (`SHUT` → `DRAFTS` for path 2, `OPENS` for paths 3 and 4), keyed by drawer letter after the reel.

Markup the builder passes through: `<em>…</em>` is spoken stress, set in italic. A whole-paragraph `<i>` is an italic paragraph, and a leading `<b>` is a bold lead. Hair spaces (U+200A) go around · and between arrows. Write them as ` ` in Python, and print every batch with `ensure_ascii=True`, so they can't be lost in transit.

## Writing to the workbook

Every write is a Google Docs `documents.batchUpdate`. The scripts print the request list, and you send it with your Docs tool.

- **Read first, and guard.** Save a full read of the workbook to a file. It's about 1.2 MB, so pull out the tabs you need with `tabsel.tab_doc`. Send each batch with `writeControl.requiredRevisionId` set to that read's `revisionId`. The one exception is a batch made only of `replaceAllText` requests. On a revision mismatch, read again and rebuild the batch. Never drop the guard.
- **Tabs.** Every range and location carries a `tabId`, and every `replaceAllText` needs `tabsCriteria`; without it, the replacement hits every tab in the workbook. `tabsel.tabify(reqs, tab)` adds both. The scripts take `--tab T`.
- **Named styles reset character styles.** Setting `namedStyleType` on a paragraph wipes its italic, bold, and color. Send paragraph styles first and text styles after. The scripts already do.

Bringing path k's tab up to the build (`T` = `ids.PATH_TAB[k]`):

```
python3 set_doc_patch.py READ sets/setK.html --tab T > batch.json         # text; send unguarded
#   or, when the changed line also appears elsewhere in the tab:
python3 workbook/para_swap.py READ sets/setK.html T > batch.json          # send with READ's revision
# fresh read, then
python3 set_doc_style.py READ sets/setK.html --tab T > batch.json         # revision on stderr; send guarded
# fresh read, then, for all four paths
python3 set_doc_verify.py READ sets/setK.html --tab T                     # must print OK
```

Use `set_doc_replace.py` only for big structural changes, and only when verify against the last committed build was OK, so nothing of doc's is lost.

**The other tabs.** Start here, Next, Paths, Craft, the Discussion header, the archive, and the Appendix have sources in `workbook/tabs/`. For a small edit, change the source and change the tab with a tab-scoped `replaceAllText`, so the two stay the same. Commit the source. A tab rewritten from scratch is cleared, then written with `md_tab.py`. Phrases and motifs, Clowns, the poetry tabs, and your stanza glosses have no source here: edit them in the doc.

## Discussion entries

```
python3 mansion/goals_post.py SPEC.json READ --as codex > out.json      # the new count prints on stderr
```

SPEC is `{"paras": [["h", "Codex — what it's about (doc HH:MM)"], ["doc", "“his words, verbatim”"], ["me", "what changed, what remains, who has the turn"]]}`. You can also give `"links": {"phrase": "url"}`. `--as codex` sets your green; without it the entry is in Claude's orange. The script finds the last `Count: N`, draws 3 to 7, subtracts 36 past 72, and appends the increment and count lines. `out.json` holds `{"revision", "requests"}`: send the requests guarded by that revision. Then give doc the count in chat. Until both are done, the turn is still yours.

## The ledger

[Provenance ledger](https://docs.google.com/spreadsheets/d/1DLNETgzXOORBU6zlIFnnY4cJlFwW3oJP7uVUC9H0_sA/edit). Use append_values only: update_values overwrites rows (E-0406). Anchor Events at `Events!A218` and Rules at `Rules!A124`, inside the live block; anchored at A1, the rows land in the wrong table. Rules rows are `R-nnn, date, doc, ruling with doc's words and time, category`. Events rows are `E-nnnn, date, YYMMDDHHMM, who, what kind, refs (commits, rules, count), short title, what happened`. The last ones written are R-127 and E-0425.

## The problem set

`cd mansion/pset && latexmk -xelatex mansion_pset.tex`, then rename the PDF to `Claude Mansion problem set YYMMDDHHMM.pdf`. Remove the old PDF in the same commit, so the folder holds one. Start here's first link, "The problem set (PDF)", points at that file name on GitHub, so update the link when the name changes. The current build is 2610230651 and matches the source.

## State at handoff (10-23, about 10:10)

- All four path tabs matched the build after doc's last line edit (f-1, 09:45). The builder's output is unchanged since then. repeats.py finds no repeated lines, and arrows.py passes 97 of 97.
- Discussion count is 42 (it wrapped past 72), after Claude's handoff entry (doc 10:02).
- Up next is in the Next tab: path 4 as an all-verse saga, then highlights instead of reruns in paths 2 and 3.
