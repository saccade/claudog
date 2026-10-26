"""The square's power flows, and one coil worked out two ways, drawn with one Manim camera. Claude.

still() calls return a PIL image, so a notebook cell shows it directly.
"""

import numpy as np
from manim import (Camera, VGroup, VMobject, RoundedRectangle, Arrow, DashedLine, Line, Dot, Text)

from square import far_sweep, current, powers, roles
from coil import linkage, torque_by_levers, torque_by_capture

PAPER = '#f8f7f2'
INK = '#2b2b2b'
TEXT = '#626860'
STEEL = '#bec2bb'
SHAFT = '#2f7f86'
WIRE = '#9a6241'
HEAT = '#a85147'
LEVER = '#3d5a99'

TURN = 2*np.pi


def label(words, point, size=18, color=TEXT):
    return Text(words, font_size=size, color=color).move_to(point)


def camera(pixels=1100):
    return Camera(pixel_width=pixels, pixel_height=round(pixels*9/16),
                  frame_width=14.2, frame_height=14.2*9/16, background_color=PAPER)


def snap(cam, objects):
    cam.reset()
    cam.capture_mobjects([objects])
    return cam.get_image().copy()


def box(center, title, role, detail):
    return VGroup(RoundedRectangle(width=3.0, height=1.35, corner_radius=.15, color=INK,
                                   stroke_width=2, fill_color=PAPER, fill_opacity=1).move_to(center),
                  label(title, center + np.array([0, .32, 0]), 19, INK),
                  label(role, center + np.array([0, -.02, 0]), 15),
                  label(detail, center + np.array([0, -.34, 0]), 14))


def flow(start, end, power, biggest, color, words, shift):
    """An arrow along an edge, as wide as the power it carries, pointing the way it goes."""
    if abs(power) < 1e-9:
        return Line(start, end, color=STEEL, stroke_width=2)
    tail, tip = (start, end) if power > 0 else (end, start)
    width = 2 + 12*abs(power)/biggest
    return VGroup(Arrow(tail, tip, color=color, buff=0, stroke_width=width,
                        max_tip_length_to_length_ratio=.12, max_stroke_width_to_length_ratio=20),
                  label(words, (start + end)/2 + shift, 17, color))


def square_picture(square):
    one, belt, two, pto = (np.array([-4.3, 1.9, 0]), np.array([4.3, 1.9, 0]),
                           np.array([4.3, -1.9, 0]), np.array([-4.3, -1.9, 0]))
    p = powers(square)
    biggest = max(abs(v) for v in p) or 1
    role_one, role_two = (r.split(' ', 2)[2] for r in roles(square))
    drop = np.array([0, .82, 0])
    side = np.array([1.62, 0, 0])
    i = current(square)
    return VGroup(
        flow(pto + drop, one - drop, p.tractor, biggest, SHAFT, f'{p.tractor:.3g} pow', np.array([-.85, 0, 0])),
        flow(one + side, belt - side, p.belt, biggest, SHAFT, f'{abs(p.belt):.3g} pow', np.array([0, .45, 0])),
        flow(belt - drop, two + drop, p.belt, biggest, SHAFT, f'{abs(p.belt):.3g} pow', np.array([.85, 0, 0])),
        flow(two - side + np.array([0, .45, 0]), one + side - np.array([0, .45, 0]), p.made, biggest, WIRE,
             f'{max(abs(p.made), abs(p.used)):.3g} pow out, {min(abs(p.made), abs(p.used)):.3g} in',
             np.array([1.2, .55, 0])),
        label(f'{p.heat:.3g} pow to heat in the windings' if p.heat > 1e-9 else '',
              np.array([-.9, -.75, 0]), 16, HEAT),
        DashedLine(pto + side, two - side, color=STEEL, stroke_width=2),
        label('the frame: takes the reaction torques, carries no power', np.array([0, -3.0, 0]), 15),
        box(one, 'machine 1', role_one, f'{square.one.capture:g} catch · sweeping at {square.sweep:g}'),
        box(belt, 'belt and wheels', f'{square.near*100:g} cm to {square.far*100:g} cm',
            f'belt at {square.sweep*square.near:.3g} cat'),
        box(two, 'machine 2', role_two, f'{square.two.capture:.3g} catch · sweeping at {far_sweep(square):.3g}'),
        box(pto, 'tractor PTO', 'direct drive', f'sweeping at {square.sweep:g}'),
        label(f'{abs(i):.3g} A around the wires' if abs(i) > 1e-9 else 'the captures match the belt: the loop idles',
              np.array([0, 3.35, 0]), 18, WIRE))


def square_still(square, pixels=1100):
    return snap(camera(pixels), square_picture(square))


class Graph:
    """A turn across, a value up the side."""
    left, right = -5.4, 6.0

    def __init__(self, middle, height, top):
        self.middle, self.height, self.top = middle, height, top

    def point(self, turn, value):
        return np.array([self.left + (self.right - self.left)*turn/TURN,
                         self.middle + self.height*value/self.top, 0])

    def axes(self, unit):
        objects = VGroup(Line(self.point(0, 0), self.point(TURN, 0), color=STEEL, stroke_width=1.2),
                         Line(self.point(0, -self.top), self.point(0, self.top), color=STEEL, stroke_width=1.2),
                         label(f'{self.top:g} {unit}', self.point(0, self.top) + np.array([-.7, 0, 0]), 13),
                         label(f'−{self.top:g}', self.point(0, -self.top) + np.array([-.55, 0, 0]), 13))
        for quarter, words in ((1, '¼ turn'), (2, '½'), (3, '¾'), (4, '1 turn')):
            x = self.point(quarter*TURN/4, 0)
            objects.add(Line(x + np.array([0, -.06, 0]), x + np.array([0, .06, 0]), color=STEEL),
                        label(words, x + np.array([0, -.28, 0]), 13))
        return objects

    def curve(self, turns, values, color):
        return VMobject(stroke_color=color, stroke_width=3).set_points_as_corners(
            [self.point(t, v) for t, v in zip(turns, values)])


def coil_picture(coil, current=2.0):
    """The linkage around a turn, and the torque from it, with the lever way's answers as dots."""
    turns = np.linspace(0, TURN, 241)
    top = Graph(1.75, 1.15, round(max(abs(linkage(coil, t)) for t in turns), 2))
    torque_top = round(max(abs(torque_by_capture(coil, t, current)) for t in turns), 2)
    bottom = Graph(-1.65, 1.15, torque_top)
    dots = VGroup(*(Dot(bottom.point(t, torque_by_levers(coil, t, current)), radius=.06, color=LEVER)
                    for t in np.linspace(0, TURN, 25)))
    return VGroup(top.axes('Wb'), top.curve(turns, [linkage(coil, t) for t in turns], WIRE),
                  label('flux the coil links', top.point(TURN/2, 0) + np.array([0, 1.35, 0]), 16, WIRE),
                  bottom.axes('crank'),
                  bottom.curve(turns, [torque_by_capture(coil, t, current) for t in turns], SHAFT),
                  dots,
                  label(f'torque at {current:g} A: the capture way (line), the lever way (dots)',
                        bottom.point(TURN/2, 0) + np.array([0, -1.6, 0]), 16, INK))


def coil_still(coil, current=2.0, pixels=1100):
    return snap(camera(pixels), coil_picture(coil, current))
