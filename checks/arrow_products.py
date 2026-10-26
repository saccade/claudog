"""The arrow product table, and the hidden-arrow cases that lean on it. Claude, 2026-10-26.

Wall picture: → forward, ↑ up, and ↺ (forward around, counterclockwise on the wall)
points out of the wall, so ↓ × → = ↺ as in the book. Run it: python arrow_products.py
"""

import numpy as np

ARROWS = {'→': (1, 0, 0), '←': (-1, 0, 0), '↑': (0, 1, 0), '↓': (0, -1, 0),
          '↺': (0, 0, 1), '↻': (0, 0, -1)}
A = {k: np.array(v) for k, v in ARROWS.items()}


def name(v):
    if not np.any(v):
        return '0'
    for k, a in A.items():
        if np.array_equal(v, a):
            return k
    return str(v)


# The book's anchor: the lever first, the leverage second.
assert name(np.cross(A['↓'], A['→'])) == '↺'

# Dot: the forward part of backward is the opposite of 1; backward of backward is 1.
flat = ['→', '←', '↑', '↓']
six = flat + ['↺', '↻']
print('dot   ' + ' '.join(f'{b:>3}' for b in six))
for a in six:
    print(f'{a:>5} ' + ' '.join(f'{int(A[a] @ A[b]):>3}' for b in six))
assert A['←'] @ A['←'] == 1 and A['←'] @ A['→'] == -1 and A['↑'] @ A['→'] == 0

print('\ncross ' + ' '.join(f'{b:>3}' for b in six))
for a in six:
    print(f'{a:>5} ' + ' '.join(f'{name(np.cross(A[a], A[b])):>3}' for b in six))
# Two at right angles cross to the third; a sweep about → carries ↑ toward ↺.
assert name(np.cross(A['↺'], A['→'])) == '↑' and name(np.cross(A['→'], A['↑'])) == '↺'

# The opposite of ← is →.
assert name(-A['←']) == '→'

# No product of two wall arrows turns one arrow into its opposite:
# the dot gives a number and the cross gives a turning (or nothing), never a wall arrow.
for a in flat:
    for b in flat:
        assert np.ndim(A[a] @ A[b]) == 0
        assert name(np.cross(A[a], A[b])) in ('↺', '↻', '0')

# Where it shows: electrons running ←, field out of the wall (↺), charge the opposite way.
e, v, B = 1.0, A['←'], A['↺']
q = -e
push = q * np.cross(v, B)
assert name(push) == '↓'
# The electrons' velocity turns from ← toward ↓: forward around (↺).
assert name(np.cross(v, push)) == '↺'
# The current points → and turns toward ↑, the same sense, like the far end of a clock hand.
j = q * v
assert name(j) == '→' and name(np.cross(j, -push)) == '↺'
# The current answers the push the opposite way: dj/dt runs along the opposite of the push.
assert name(q * push) == '↑'
# If the hidden ← were an arrow dotted in, the current would come out a number with no arrow.
assert np.ndim(A['←'] @ v) == 0
print('\nall checks pass')
