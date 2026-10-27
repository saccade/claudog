# Dog Math: the working copy

Written by Claude (Anthropic), 2026-10-27 10:50, for dr. kraemer and Codex (OpenAI).

**The source of truth is the Google Doc, [Dog Math](https://docs.google.com/document/d/1qDecvGSGpzf6NkTIouDkan-fTphtDHBKZEC5TmcghOQ/edit).** Nothing here regenerates it.

## What's here

`Dog Math working copy.md` is the only file. On `main` it's the live doc's text as last read (10-26 12:35). Git keeps every earlier read, so there's no folder of old versions.

The older history (the 47 fixed-width text versions from 10-19 and 10-20 that became the doc, the PDF render check, and the 10-22 reads of the doc) was cleared out of the active view on 10-27. It's all still under the tag `dog-math-history-2610271050` (commit `97d4325`): `git checkout dog-math-history-2610271050 -- docs/dog-math` brings it back.

## Checking it

There's nothing to rebuild from, and the doc takes hand edits a script wouldn't know about, so a check compares and never regenerates:

- **Export the live doc and diff it against the working copy on `main`.** Every difference is either an edit made since then or export noise. Read each one; don't "fix" it back.
- **Commit the new export over the working copy on `main`.** The commit is the snapshot.
- **A rule check** (round numbers, unit plurals, contractions) can flag lines, but it reports. It doesn't edit the doc, since a flagged line may be one doc wrote on purpose.

## Proposing changes

Branch, edit the working copy, and open a pull request: the diff shows exactly what would change in the doc. Once doc approves, the changes go into the Google Doc by hand or by API batch, and a fresh read of the doc is committed over the working copy on `main`. The working copy is never the source of truth; the Google Doc is.

## Queued for the next pass

- The WRITING IN DOG MATH block says "'On' and 'over' divide." Too strong (doc, 10-27): "on" can lay one thing across another, so a 0.1 mm coat on 40 m² of wall is 4 liters of paint, a product. Say that "on" divides when a rate is spread on a lever (5 cat on 1 hand sweeps at 50), lays one thing across another when it's a coat on an area, and that the units tell you which.
- Pool notebook and Spin Hit: "Friction ↑ on B's face, at a lever ← from B's center" → "Friction ↑ on B's face acts on a lever ← from B's center and turns B ← × ↑ = ↻."
- Parabola of Safety SxS: "upward part", not "up part" (doc, 10-27), matching the forward part and the downward part. Every use in the arrows column and the names.
- Parabola of Safety SxS, arrows column: where a sentence is just an equation read aloud, write the equation (doc, 10-27). The boundary row becomes h = (20 m − d) − d(s − 40 m/x)², with words kept only for the physics: the top sits the straight-up height above the horizontal-shot curve. The same goes for the two-shots row (h = 15 m − 5 m (s − 2)², then "it's a hill in the slope") and the drop-at-a-slope row (h = 20 m s − 5 m (1 + s²)).
