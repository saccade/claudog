"""Turn the knobs and tap the cone again. Claude. Needs a running kernel."""

import io
from dataclasses import replace

import ipywidgets as w

from speaker import bl, wire, drag, q_electrical, OPEN, SHORT
from view import ringdown_still


def png(image):
    data = io.BytesIO()
    image.save(data, 'PNG')
    return data.getvalue()


def explore(speaker):
    """Field, windings, and what's across the leads; the tap follows."""
    image = w.Image(format='png', layout=w.Layout(width='100%', max_width='1100px'))
    readout = w.HTML()
    style = dict(description_width='110px')
    field = w.FloatSlider(min=.4, max=1.6, step=.1, value=speaker.field,
                          description='field · T', continuous_update=False, style=style)
    turns = w.IntSlider(min=21, max=89, value=speaker.turns,
                        description='windings', continuous_update=False, style=style)
    across = w.Dropdown(options=[('leads shorted', SHORT), ('8 Ω across', 8.0),
                                 ('100 Ω across', 100.0)],
                        value=SHORT, description='compare with', style=style)

    def show(change=None):
        now = replace(speaker, field=field.value, turns=turns.value)
        image.value = png(ringdown_still(now, across=(OPEN, across.value)))
        readout.value = ('<p style="font-family:monospace">'
                         f'wire {wire(now):.3g} m · Bl {bl(now):.3g} T·m · '
                         f'drag {drag(now, across.value):.3g} N per m/s · '
                         f'Qes {q_electrical(now):.2g}</p>')

    for control in (field, turns, across):
        control.observe(show, names='value')
    show()
    return w.VBox([image, w.HBox([field, turns, across]), readout])
