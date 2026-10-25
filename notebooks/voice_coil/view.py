"""Pictures of the voice coil, drawn with one Manim camera. Claude.

still() calls return a PIL image, so a notebook cell shows it directly.
Forward is to the right: the way the cone pushes air out of the box.
"""

import numpy as np
from manim import (Camera, VGroup, VMobject, Rectangle, Square, Line, Arrow,
                   Dot, Cross, Text)

from speaker import bl, ring, OPEN, SHORT
from tap import tap

PAPER = '#f8f7f2'
INK = '#2b2b2b'
STEEL = '#bec2bb'
COPPER = '#9a6241'
FORCE = '#a85147'
FIELD = '#528b7b'
TEXT = '#626860'


def label(words, point, size=18, color=TEXT):
    return Text(words, font_size=size, color=color).move_to(point)


def camera(pixels=1100):
    return Camera(pixel_width=pixels, pixel_height=round(pixels*9/16),
                  frame_width=14.2, frame_height=14.2*9/16, background_color=PAPER)


def snap(cam, objects):
    cam.reset()
    cam.capture_mobjects([objects])
    return cam.get_image().copy()


def block(left, bottom, width, height):
    return Rectangle(width=width, height=height, color=STEEL, fill_color=STEEL,
                     fill_opacity=.55, stroke_width=1).move_to(
                         [left + width/2, bottom + height/2, 0])


def coil_side(center, into_page):
    """One side of the coil, cut through: current into the page (×) or out of it (•)."""
    box = Square(.42, color=COPPER, fill_color=COPPER, fill_opacity=.25,
                 stroke_width=2).move_to(center)
    mark = (Cross(box, stroke_color=COPPER, stroke_width=3, scale_factor=.55) if into_page
            else Dot(center, radius=.07, color=COPPER))
    return VGroup(box, mark)


def motor(current=1.0):
    """The magnet and coil cut in half along the axis, with the push on the coil.
    A positive current runs into the page at the top: around one way."""
    top, gap = 1.25, .5                       # coil's height off the axis, gap's width
    drawing = VGroup(
        Line([-6.4, 0, 0], [6.6, 0, 0], color=STEEL, stroke_width=1.2),
        block(-5.2, -top + gap/2, 1.4, 2*(top - gap/2)),            # center pole
        block(-6.0, -2.6, .8, 5.2),                                 # back plate
        block(-5.2, top + gap/2, 1.4, 1.1),                         # top plate, above
        block(-5.2, -top - gap/2 - 1.1, 1.4, 1.1),                  # and below
        label('magnet', [-4.5, 2.95, 0], 16),
        label('axis', [6.3, -.25, 0], 14),
    )
    for side in (1, -1):
        y = side*top
        for x in (-4.95, -4.05):         # field across the gap, out from the axis
            drawing.add(Arrow([x, y - side*gap/2, 0], [x, y + side*gap/2, 0],
                              color=FIELD, buff=0, stroke_width=2.5,
                              max_tip_length_to_length_ratio=.35))
        drawing.add(coil_side([-4.5, y, 0], into_page=(side > 0) == (current > 0)))
        drawing.add(Line([-4.2, y, 0], [-1.6, y, 0], color=COPPER, stroke_width=2))  # former
        drawing.add(Line([-1.6, y, 0], [4.2, side*3.0, 0], color=INK, stroke_width=2.5))  # cone
    if current:
        sense = np.sign(current)
        for side in (1, -1):
            start = np.array([-2.95 - .65*sense, side*top + side*.55, 0])   # beside the former
            drawing.add(Arrow(start, start + [1.3*sense, 0, 0], color=FORCE, buff=0,
                              stroke_width=4, max_tip_length_to_length_ratio=.3))
    drawing.add(
        label('field B, out from the axis', [-1.2, 3.55, 0], 18, FIELD),
        label('coil: current into the page at the top, out at the bottom' if current >= 0 else
              'coil: current out of the page at the top, into it at the bottom',
              [0, -3.55, 0], 18, COPPER),
        label('push along the axis', [-1.9, 2.1, 0], 18, FORCE) if current else VGroup(),
        label('cone', [3.4, 1.6, 0], 18, INK),
    )
    return drawing


def motor_still(current=1.0, pixels=1100):
    return snap(camera(pixels), motor(current))


class Graph:
    """Time across, the cone's place up the side."""
    left, right, middle, height = -5.6, 6.2, 0.0, 2.4

    def __init__(self, duration, top):
        self.duration, self.top = duration, top

    def point(self, time, value):
        return [self.left + (self.right - self.left)*time/self.duration,
                self.middle + self.height*value/self.top, 0]

    def axes(self, unit):
        objects = VGroup(Line(self.point(0, 0), self.point(self.duration, 0),
                              color=STEEL, stroke_width=1.2),
                         Line(self.point(0, -self.top), self.point(0, self.top),
                              color=STEEL, stroke_width=1.2))
        for ms in range(0, round(1000*self.duration) + 1, 25):
            x, y = self.point(ms/1000, 0)[:2]
            objects.add(Line([x, y - .06, 0], [x, y + .06, 0], color=STEEL, stroke_width=1.2),
                        label(f'{ms} ms', [x, y - .3, 0], 13))
        objects.add(label(f'{self.top:g} {unit}', [self.left - .55, self.point(0, self.top)[1], 0], 13),
                    label(f'−{self.top:g} {unit}', [self.left - .55, self.point(0, -self.top)[1], 0], 13))
        return objects

    def curve(self, times, values, color, width=2.5):
        stride = max(1, len(times)//600)
        shape = VMobject(stroke_color=color, stroke_width=width)
        return shape.set_points_as_corners([self.point(t, v)
                                            for t, v in zip(times[::stride], values[::stride])])


def ringdown(speaker, kick=0.1, duration=0.15, across=(OPEN, SHORT)):
    """The cone's place after a tap, once for each thing across the leads."""
    runs = {a: tap(speaker, a, kick, duration) for a in across}
    top = 1000*max(np.max(np.abs(r.place)) for r in runs.values())
    top = float(np.ceil(top*10)/10)                       # mm, rounded up to a tenth
    graph = Graph(duration, top)
    objects = VGroup(graph.axes('mm'),
                     label(f'The cone after a tap: Bl {bl(speaker):.2g} T·m, '
                           f'ringing {ring(speaker):.3g} rad/s on its spring',
                           [0, 3.55, 0], 20, INK))
    words = {OPEN: 'leads open', SHORT: 'leads shorted'}
    colors = ['#8f948c', INK, FORCE, COPPER]
    for row, (a, run) in enumerate(runs.items()):
        color = colors[row % len(colors)]
        name = words.get(a, f'{a:g} Ω across the leads')
        objects.add(graph.curve(run.time, 1000*run.place, color, 3 if row else 2.5),
                    label(name, [4.4, -2.9 - .36*row, 0], 17, color))
    return objects


def ringdown_still(speaker, pixels=1100, **choices):
    return snap(camera(pixels), ringdown(speaker, **choices))
