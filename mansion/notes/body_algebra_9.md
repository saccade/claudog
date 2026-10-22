# Body algebra on the double pendulum (problem 9), a working note

Written by Claude (Anthropic), 2026-10-22 17:20, for doc. Not in any path; shown to doc in chat first.

The book's demo (end of Straight→ Mechanics): quantities are written body by body, m = 2 kg × A + 5 kg × B,
F = 10 N → × B, and applied to the model [A + B]. Dividing distributes over the bodies with B/B = 1 and B/A = 0,
so a × [A + B] = 5 × B/A + 2 × B/B = 2 m/s² → × B: the pull on B moves B and only B.

Problem 9, model [U + L], upper and lower masses, ℓ = 1 m, g = 10 m/s². Upper rod swung 0.10 rad →.
m = 1 kg × U + 1 kg × L. The upper rod carries both weights (20 N); the lower rod carries one (10 N).
A rod leaning by a swing pulls its weight-load times the swing sideways, back toward the pivot.
The lower rod pulls both ends: the same size, opposite arrows on L and on U.

Slow mode (lower rod 0.14 rad →):
  places:  0.10 m → × U + 0.24 m → × L
  pulls:   upper rod 2.0 N ← × U;  lower rod 1.41 N ← × L + 1.41 N → × U
  F × [U + L] = 0.59 N ← × U + 1.41 N ← × L
  a × [U + L] = 0.59 m/s² ← × U + 1.41 m/s² ← × L   = 5.86 per s² of each place, pointed back (ω_a²)
Fast mode (lower rod 0.14 rad ←):
  places:  0.10 m → × U + 0.041 m ← × L
  pulls:   upper rod 2.0 N ← × U;  lower rod 1.41 N → × L + 1.41 N ← × U
  F × [U + L] = 3.41 N ← × U + 1.41 N → × L
  a × [U + L] = 3.41 m/s² ← × U + 1.41 m/s² → × L   = 34.1 per s² of each place, pointed back (ω_b²)
Joint body (U + L): the lower rod's two pulls cancel inside it; only the upper rod's 2.0 N ← acts from outside,
1 m/s² ← for the center in both modes (center at 0.17 m and 0.029 m: 5.86 and 34.1 of them).

Finding for 9-3: path 1 says the lower *angle* is ±√2 the upper; the statement asks how the lower *mass* moves.
The lower mass rides on the upper: slow, 1 + √2 ≈ 2.4 as far, same way; fast, √2 − 1 ≈ 0.41 as far, the other way.
Checked numerically 2026-10-22 (small-angle tensions 2mg and mg).
