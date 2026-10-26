"""Change the shot and hit again. Claude. Needs a running kernel."""

import io
from dataclasses import replace

import numpy as np
import ipywidgets as w

from hit import UP, coming, hit, punch, hook, heat, line_of_centers, across
from view import table_still, ledger_still

FULLNESS = [('full on', 1.0), ('3/4 ball', .75), ('1/2 ball', .5), ('1/4 ball', .25)]


def png(image):
    data = io.BytesIO()
    image.save(data, 'PNG')
    return data.getvalue()


def reading(ball, shot):
    """The hit in a few lines of dog math."""
    a, b = hit(ball, shot)
    line = line_of_centers(shot)
    throw = across(b.travel, line)
    side = 'left' if np.cross(line, throw) @ UP > 0 else 'right'
    return (f'B leaves at {np.linalg.norm(b.travel):.3g} cat, thrown {np.linalg.norm(throw):.2g} cat '
            f'{side} of the line of centers, sweeping {"↺" if b.sweep @ UP > 0 else "↻"} at '
            f'{abs(b.sweep @ UP):.3g}.<br>'
            f'A keeps {"↺" if a.sweep @ UP > 0 else "↻"} at {abs(a.sweep @ UP):.3g} and travels '
            f'{np.linalg.norm(a.travel):.2g} cat.<br>'
            f'Thump: A came in with {punch(ball, coming(shot)):.2g} punch and '
            f'{hook(ball, coming(shot)):.2g} hook; A keeps {hook(ball, a):.2g} hook, '
            f'B carries {punch(ball, b):.2g} punch, {heat(ball, shot):.2g} goes to heat.')


def explore(ball, shot):
    table, ledger = (w.Image(format='png', layout=w.Layout(width='100%', max_width='1100px'))
                     for _ in range(2))
    readout = w.HTML()
    style = dict(description_width='120px')
    speed = w.FloatSlider(min=1, max=5, step=.5, value=shot.speed, description='travel · cat',
                          continuous_update=False, style=style)
    sweep = w.IntSlider(min=-300, max=300, step=10, value=int(shot.sweep),
                        description='sidespin · ↺', continuous_update=False, style=style)
    fullness = w.Dropdown(options=FULLNESS, value=shot.fullness, description='hit', style=style)
    friction = w.FloatSlider(min=.01, max=.3, step=.01, value=shot.friction,
                             description='face friction', continuous_update=False, style=style)
    bounce = w.FloatSlider(min=.8, max=1, step=.01, value=shot.bounce, description='bounce',
                           continuous_update=False, style=style)

    def show(change=None):
        now = replace(shot, speed=speed.value, sweep=sweep.value, fullness=fullness.value,
                      friction=friction.value, bounce=bounce.value)
        table.value = png(table_still(ball, now))
        ledger.value = png(ledger_still(ball, now))
        readout.value = f'<p style="font-family:monospace">{reading(ball, now)}</p>'

    controls = (speed, sweep, fullness, friction, bounce)
    for control in controls:
        control.observe(show, names='value')
    show()
    return w.VBox([table, w.HBox(controls[:3]), w.HBox(controls[3:]), readout, ledger])
