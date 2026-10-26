"""The hit, checked from several sides. Claude."""

from dataclasses import replace

import numpy as np
from numpy.testing import assert_allclose

from hit import (Ball, Shot, FORWARD, LEFT, UP, coming, still, hit, line_of_centers,
                 face, punch, hook, energy, heat)

BALL, SHOT = Ball(), Shot()


def test_the_full_hit():
    a, b = hit(BALL, SHOT)
    assert_allclose(b.travel, 3*FORWARD + .12*LEFT, atol=1e-12)
    assert_allclose(a.travel, -.12*LEFT, atol=1e-12)
    assert_allclose(b.sweep @ UP, -10)              # ↻: spin passes the other way around
    assert_allclose(a.sweep @ UP, 190)              # the spin stays home


def test_most_of_the_energy_starts_in_the_spin():
    a = coming(SHOT)
    assert_allclose(punch(BALL, a), .75)
    assert_allclose(hook(BALL, a), 1.2)


def test_motion_is_kept():
    a, b = hit(BALL, replace(SHOT, fullness=.7, bounce=.9))
    assert_allclose(a.travel + b.travel, coming(SHOT).travel, atol=1e-12)


def test_spin_about_a_fixed_point_is_kept():
    shot = replace(SHOT, fullness=.6, friction=.3)
    line = line_of_centers(shot)
    pa, pb = -BALL.radius*line, BALL.radius*line     # centers, with the contact at the origin
    k = BALL.share*BALL.radius**2

    def spin(p, m):
        return np.cross(p, m.travel) + k*m.sweep
    a, b = hit(BALL, shot)
    assert_allclose(spin(pa, coming(shot)) + spin(pb, still()), spin(pa, a) + spin(pb, b), atol=1e-12)


def test_heat_is_friction_over_the_average_skid():
    a, b = hit(BALL, SHOT)
    before, after = 6.0, 6 - 7*.12
    assert_allclose(heat(BALL, SHOT), BALL.mass * .12 * (before + after)/2)


def test_enough_grip_closes_the_skid():
    shot = replace(SHOT, friction=10)
    a, b = hit(BALL, shot)
    line = line_of_centers(shot)
    skid = face(BALL, a, BALL.radius*line) - face(BALL, b, -BALL.radius*line)
    assert_allclose(skid - (skid @ line)*line, 0*FORWARD, atol=1e-12)


def test_no_english_no_throw():
    a, b = hit(BALL, replace(SHOT, sweep=0))
    assert_allclose(b.travel, 3*FORWARD, atol=1e-12)
    assert_allclose(b.sweep, 0*UP, atol=1e-12)


def test_english_the_other_way_throws_the_other_way():
    _, right = hit(BALL, SHOT)
    _, left = hit(BALL, replace(SHOT, sweep=-200))
    assert right.travel @ LEFT > 0 > left.travel @ LEFT


def test_heat_is_never_negative():
    for fullness in (1, .8, .5, .3):
        for sweep in (-300, 0, 120, 300):
            assert heat(BALL, replace(SHOT, fullness=fullness, sweep=sweep, bounce=.93)) > -1e-12
