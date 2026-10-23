# Dog Math: where it came from

Written by Claude (Anthropic), 2026-10-23 13:35, for dr. kraemer and Codex (OpenAI).

**The source of truth is the Google Doc, [Dog Math](https://docs.google.com/document/d/1qDecvGSGpzf6NkTIouDkan-fTphtDHBKZEC5TmcghOQ/edit).** Nothing here regenerates it. This folder holds its history, so the doc can be checked against a known past.

## No builder exists

Dog Math was never assembled by a program. It started on 10-19 as a fixed-width text file, "Claude Dog Math YYMMDDHHMM.txt". Each version was the previous one, edited by hand and then rewrapped with the tools in `typeset/` (`reflow.py` and `wrap.py` for wrapping, `plural.py`, `count.py`, and `wc.py` for checks). The 47 versions, from 10-19 12:25 to 10-20 15:58, are in `text-versions/`. The last one is also `docs/Claude Dog Math 2610201558.txt`.

On 10-20 at about 21:35 that last text became the Google Doc, with a PDF render check made at the same time (`Dog Math render check 2610202136.pdf`). From then on, all edits went into the doc directly: Claude's and Codex's API batches, and doc's own hand edits. `doc-snapshots/` holds four Drive text reads of the doc from 10-22, the last one at its 19:35 revision. The doc's last modification is 10-22 19:34, so that last snapshot should match the live doc, apart from anything Drive's text export drops.

## Checking it

There's nothing to rebuild from, and the doc has taken hand edits a script wouldn't know about. A check therefore compares, and never regenerates:

- **Export the live doc and diff it against the newest snapshot.** Every difference is either an edit made since then or export noise. Read each one; don't "fix" it back.
- **Commit each new export as the next snapshot,** named "Dog Math doc as read YYMMDDHHMM", so the history keeps growing in one place.
- **A rule check** (round numbers, unit plurals, contractions) can flag lines, but it reports. It doesn't edit the doc, since a flagged line may be one doc wrote on purpose.
