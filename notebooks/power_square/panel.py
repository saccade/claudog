"""Trim machine 2 and watch the power go around. Claude. Needs a running kernel."""

import io
from dataclasses import replace

import ipywidgets as w

from square import Machine, far_sweep, matched, current, torques, powers, roles
from view import square_still


def png(image):
    data = io.BytesIO()
    image.save(data, 'PNG')
    return data.getvalue()


def reading(square):
    p, t, i = powers(square), torques(square), current(square)
    one, two = roles(square)
    return (f'machine 2 sets up {square.two.capture*far_sweep(square):.3g} V against machine 1\'s '
            f'{square.one.capture*square.sweep:.3g} V; {abs(i):.3g} A around the wires.<br>'
            f'{one}; {two}.<br>'
            f'belt tension {abs(t.tension):.3g} push at {square.sweep*square.near:.3g} cat carries '
            f'{abs(p.belt):.3g} pow; the tractor pays {p.tractor:.3g} pow, all of it heat.<br>'
            f'matched capture for machine 2: {matched(square):.3g} catch')


def explore(square):
    image = w.Image(format='png', layout=w.Layout(width='100%', max_width='1100px'))
    readout = w.HTML()
    style = dict(description_width='150px')
    catch = w.FloatSlider(min=.5, max=.7, step=.01, value=square.two.capture,
                          description='machine 2 · catch', continuous_update=False, style=style)
    sweep = w.IntSlider(min=30, max=90, step=5, value=int(square.sweep),
                        description='tractor · sweep', continuous_update=False, style=style)
    winding = w.FloatSlider(min=.1, max=2, step=.1, value=square.one.resistance,
                            description='each winding · Ω', continuous_update=False, style=style)

    def show(change=None):
        now = replace(square, sweep=sweep.value,
                      one=Machine(square.one.capture, winding.value),
                      two=Machine(catch.value, winding.value))
        image.value = png(square_still(now))
        readout.value = f'<p style="font-family:monospace">{reading(now)}</p>'

    for control in (catch, sweep, winding):
        control.observe(show, names='value')
    show()
    return w.VBox([image, w.HBox([catch, sweep, winding]), readout])
