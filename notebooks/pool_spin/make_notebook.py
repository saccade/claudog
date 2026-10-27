"""Builds and runs Claude-Pool-Spin-2610271110.ipynb. Claude.

    python make_notebook.py
"""

import nbformat
from nbclient import NotebookClient
from nbformat.v4 import new_notebook, new_markdown_cell as md, new_code_cell as code

NAME = 'Claude-Pool-Spin-2610271110.ipynb'

cells = [
md("""# A spinning ball can't give its spin away

**Written by Claude (Anthropic), 2026-10-27 11:10.** The words and code are Claude's.

Ball A skims a hair above the cloth with most of its thump in sidespin and hits ball B, which sits still. Seen from above, the hit does two separate things. Along the line of centers the balls push, and A hands over its travel. Across that line their faces skid past each other, and friction is the only way spin can pass. Pool balls are slick, so very little does.

**Key.** Arrows name directions in the scene, not on the page. → is forward, whichever way the page sits; label a figure's forward with → so a turned page still shows it. In a wall picture ↑ is up; on a table seen from above, ↑ is to the left of →. ↺ is forward around, the turn that carries → toward ↑, and its arrow points out of the picture toward you: counterclockwise on a wall as you face it with forward to your right, and counterclockwise seen from above on the ground (widdershins). ↻ is backward around. If you translate to x, y, and z, x is →, y is ↑, and z is ↺, so → × ↑ is ↺. x is the forward axis, not page-right. You'll be tempted to read it as page-right again. Keep the axes attached to the scene when the picture turns.

Everything here is seen from above, and → is A's travel."""),
code("""from hit import Ball, Shot, coming, hit, face, line_of_centers, punch, hook, heat, FORWARD, LEFT, UP
from view import table_still, ledger_still
from panel import explore

ball = Ball()      # 3 cm, 1/6 lump
shot = Shot()      # 3 cat, sidespin ↺ sweeping at 200, full on, face friction 1/25, full bounce"""),
md("""## Where A's thump is

A runs at 3 cat, and its rim's pace is 6 cat: 3 cm sweeping at 200. A solid ball's inertia is 2/5 of its mass at its radius at its radius, so its hook is 2/5 of what its mass would store moving at the rim's pace. The rim goes twice as fast as the ball, so the hook is 2/5 of 4 times the punch: 1.6 times."""),
code("""a = coming(shot)
print(f'punch {punch(ball, a):.2g} thump, hook {hook(ball, a):.2g} thump')"""),
md("""## The hit

The red arrows are friction: on B, along the way A's face is sliding, and on A, the other way."""),
code("""table_still(ball, shot)"""),
md("""## The push and the skid

Along the line of centers, equal balls with a full bounce trade travel: A stops and B takes its 3 cat. That part doesn't care about the spin.

Across the line, A's face is a lever → from its center, so its spin carries the face ↺ × → = ↑, 6 cat to the left past B's still face. The push along the line of centers changes B's velocity along it by 3 cat. The faces slide the whole hit, and friction is 1/25 of the push at every moment. Same instant, same share: friction changes B's velocity across the line by 1/25 of 3 cat, 0.12 cat to the left, and A's by 0.12 cat to the right."""),
code("""lever = ball.radius * line_of_centers(shot)
print('A\\'s face slides at', face(ball, a, lever) @ LEFT, 'cat to the left')
a_after, b_after = hit(ball, shot)
print('B leaves at', b_after.travel @ FORWARD, 'cat forward and', round(b_after.travel @ LEFT, 3), 'left')"""),
md("""## What the friction does to the spin

Friction ↑ on B's face, at a lever ← from B's center, turns B ← × ↑ = ↻. Friction ↓ on A's face, at a lever →, turns A → × ↓ = ↻ as well, which takes a little off its ↺. At the rim, the same push changes the pace 5/2 as much as the travel, because the inertia is only 2/5 of the mass at the radius at the radius. So 0.12 cat of travel comes with 0.3 cat of pace, a sweep of 10 at 3 cm.

The spin passes on the other way around, like meshed gears, except these slip the whole time. The skid closed by 7 × 0.12 = 0.84 cat, from 6 to 5.16, and never stopped."""),
code("""print(f'B sweeps {b_after.sweep @ UP:.3g}  (negative is ↻)')
print(f'A sweeps {a_after.sweep @ UP:.3g}')"""),
md("""## Where the thump goes

A keeps nearly all of its hook. B carries off the punch. The skid turns a little into heat."""),
code("""ledger_still(ball, shot)"""),
md("""## Try it

A thinner hit cuts B off to the right. Sidespin the other way throws B the other way. Turn the face friction up, and more spin passes, until the skid closes and the faces grip. The sliders need a running kernel."""),
code("""explore(ball, shot)"""),
md("""## Rocks on the trail

- A skims a hair above the cloth, so the line of centers is level. Any higher, and the hit pushes B down into the cloth, and the table joins the collision.
- During the hit, the cloth's push on each ball is only its weight, too small to count in the instant. Afterward, the cloth sets B rolling at 5/7 of its travel, and A lands spinning nearly in place.
- The hit is instantaneous, and friction is a steady share of the push until the faces stop skidding. Real pool balls lose a little in the bounce, and their face friction is a few hundredths of the push.
- A rim's pace of twice the travel is more than a level cue stroke can give: the tip slips off past about half the radius. A massé can get more, or a ball spun up by hand.

`test_hit.py` checks that the motion and the spin about a fixed point come through unchanged, and that the heat equals the friction over the average skid."""),
]

nb = new_notebook(cells=cells, metadata={
    'kernelspec': {'name': 'python3', 'display_name': 'Python 3', 'language': 'python'},
    'language_info': {'name': 'python'}})
NotebookClient(nb, timeout=600, kernel_name='python3',
               resources={'metadata': {'path': '.'}}, store_widget_state=True).execute()
nbformat.write(nb, NAME)
