"""The hit seen from above, drawn with one Manim camera. Claude.

still() calls return a PIL image, so a notebook cell shows it directly.
On the page, → is A's travel and ↑ is the shot's left.
"""

from fractions import Fraction

import numpy as np
from manim import (Camera, VGroup, Circle, Arc, Arrow, DashedLine, Rectangle, Text)

from hit import FORWARD, LEFT, UP, coming, still, hit, line_of_centers, across, punch, hook, heat

PAPER = '#f8f7f2'
INK = '#2b2b2b'
TEXT = '#626860'
CUE = '#ffffff'
ONE = '#e3b23c'          # the 1-ball's yellow
TRAVEL = '#2f7f86'
SPIN = '#3d5a99'
FORCE = '#a85147'
LINE = '#bec2bb'

SIZE = 1.0               # a ball's radius on the page
PER_CAT = .6             # page units of arrow per cat of travel


def label(words, point, size=18, color=TEXT):
    return Text(words, font_size=size, color=color).move_to(point)


def camera(pixels=1100):
    return Camera(pixel_width=pixels, pixel_height=round(pixels*9/16),
                  frame_width=14.2, frame_height=14.2*9/16, background_color=PAPER)


def snap(cam, objects):
    cam.reset()
    cam.capture_mobjects([objects])
    return cam.get_image().copy()


def page(arrow):
    """A table arrow on the page: forward is right, left is up."""
    return np.array([arrow @ FORWARD, arrow @ LEFT, 0])


def ball(center, color):
    return Circle(radius=SIZE, color=INK, stroke_width=2, fill_color=color,
                  fill_opacity=1).move_to(center)


def travel(center, motion, coming=False, tiny=.05):
    """The ball's travel as an arrow: leaving from its center, or coming in to its back.
    A short one is drawn ten times over."""
    length = np.linalg.norm(motion.travel)
    if length < tiny:
        return VGroup()
    grow = 10 if length < .5 else 1
    way = page(motion.travel)/length
    reach = PER_CAT*grow*length*way
    tail, tip = (center - SIZE*way - reach, center - SIZE*way) if coming else (center, center + reach)
    words = f'{length:.2g} cat' + (' (drawn ×10)' if grow > 1 else '')
    return VGroup(Arrow(tail, tip, color=TRAVEL, buff=0, stroke_width=5,
                        max_tip_length_to_length_ratio=.25 if grow > 1 or length > 1 else .4),
                  label(words, (tail + tip)/2 + np.array([0, .32, 0]) if coming
                        else tip + .6*way + np.array([0, -.3, 0]), 16, TRAVEL))


def spin(center, motion):
    """An arc around the ball, ↺ or ↻, with its sweep."""
    sweep = motion.sweep @ UP
    if abs(sweep) < .5:
        return VGroup()
    reach = (.5 + 1.1*min(abs(sweep)/200, 1)) * np.sign(sweep)
    arc = Arc(radius=SIZE + .22, start_angle=np.pi/2 - reach/2, angle=reach,
              color=SPIN, stroke_width=4).move_arc_center_to(center)
    arc.add_tip(tip_length=.22, tip_width=.22)
    mark = '↺' if sweep > 0 else '↻'
    return VGroup(arc, label(f'{mark} {abs(sweep):.3g}', center + np.array([0, SIZE + .6, 0]), 17, SPIN))


def pair(middle, shot, motions, words, coming=False):
    """Both balls touching at `middle`, A on the near side of the line of centers."""
    line = page(line_of_centers(shot))
    a_at, b_at = middle - SIZE*line, middle + SIZE*line
    a, b = motions
    return VGroup(DashedLine(a_at - 1.3*line, b_at + 3.2*line, color=LINE, stroke_width=1.5),
                  ball(a_at, CUE), ball(b_at, ONE),
                  label('A', a_at, 20, INK), label('B', b_at, 20, INK),
                  spin(a_at, a), spin(b_at, b), travel(a_at, a, coming), travel(b_at, b),
                  label(words, middle + np.array([0, -3.15, 0]), 20, INK))


def friction(middle, ball_, shot):
    """Where the faces skid: friction drags B's face along A's, and A's the other way."""
    line = line_of_centers(shot)
    drag = across(hit(ball_, shot)[1].travel, line)
    if np.linalg.norm(drag) < 1e-9:
        return VGroup()
    way, into_b = page(drag)/np.linalg.norm(drag), .16*page(line)
    on_b = Arrow(middle + into_b, middle + into_b + .9*way, color=FORCE, buff=0, stroke_width=4,
                 max_tip_length_to_length_ratio=.35)
    on_a = Arrow(middle - into_b, middle - into_b - .9*way, color=FORCE, buff=0, stroke_width=4,
                 max_tip_length_to_length_ratio=.35)
    return VGroup(on_b, on_a,
                  label('friction on B', middle + into_b + 1.2*way + 4*into_b, 15, FORCE),
                  label('on A', middle - into_b - 1.2*way - 3*into_b, 15, FORCE))


def table(ball_, shot):
    """At the hit, and just after."""
    before = np.array([-2.9, .25, 0])
    after = np.array([3.0, .25, 0])
    return VGroup(pair(before, shot, (coming(shot), still()), 'at the hit', coming=True),
                  friction(before, ball_, shot),
                  pair(after, shot, hit(ball_, shot), 'just after'))


def table_still(ball_, shot, pixels=1100):
    return snap(camera(pixels), table(ball_, shot))


def ledger(ball_, shot):
    """Where the thump goes: punch and hook before, then after, then heat."""
    a, b = hit(ball_, shot)
    rows = [('before', [('A punch', punch(ball_, coming(shot)), TRAVEL),
                        ('A hook', hook(ball_, coming(shot)), SPIN)]),
            ('after', [('A punch', punch(ball_, a), TRAVEL), ('A hook', hook(ball_, a), SPIN),
                       ('B punch', punch(ball_, b), TRAVEL), ('B hook', hook(ball_, b), SPIN),
                       ('heat', heat(ball_, shot), FORCE)])]
    total = sum(v for _, parts in rows[:1] for _, v, _ in parts)
    width = 9.8 / total
    objects = VGroup(label('Where the thump goes', [0, 2.9, 0], 22, INK))
    for row, (name, parts) in enumerate(rows):
        y = 1.2 - 2.2*row
        x = -5.0
        objects.add(label(name, [-6.1, y, 0], 18, INK))
        for words, value, color in parts:
            if value*width < .02:
                continue
            bar = Rectangle(width=value*width, height=.8, stroke_width=1, stroke_color=PAPER,
                            fill_color=color, fill_opacity=.85).move_to([x + value*width/2, y, 0])
            objects.add(bar)
            if value*width > .9:
                objects.add(label(f'{words} {value:.2g}', [x + value*width/2, y - .75, 0], 15, color))
            elif (words, value, color) == parts[-1]:
                objects.add(label(f'{words} {value:.2g}', [x + value*width + .75, y, 0], 15, color))
            x += value*width
    objects.add(label(f'thump, for balls of {Fraction(ball_.mass).limit_denominator(12)} lump', [0, -2.7, 0], 16))
    return objects


def ledger_still(ball_, shot, pixels=1100):
    return snap(camera(pixels), ledger(ball_, shot))
