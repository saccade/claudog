"""The square and the coil, checked. Claude."""

from dataclasses import replace

import numpy as np
from numpy.testing import assert_allclose

from square import Square, Machine, far_sweep, pace, matched, current, torques, powers, roles
from coil import Coil, capture, torque_by_levers, torque_by_capture, peak_capture

S = Square()


def test_the_belt_runs_at_one_pace():
    assert_allclose(pace(S), 3)
    assert_allclose(far_sweep(S) * S.far, pace(S))
    assert_allclose(far_sweep(S), 100)


def test_matched_levers_idle():
    idle = replace(S, two=Machine(matched(S)))
    assert_allclose(matched(S), .6)
    assert_allclose(current(idle), 0)
    assert_allclose(powers(idle), 0, atol=1e-12)


def test_a_hair_off():
    assert_allclose(current(S), 5)
    p = powers(S)
    assert_allclose([p.tractor, p.belt, p.made, p.used, p.heat], [25, 325, 325, 300, 25])


def test_the_tractor_pays_only_for_the_heat():
    for catch in (.5, .58, .62, .7):
        for sweep in (30, 60, 90):
            p = powers(replace(S, sweep=sweep, two=Machine(catch)))
            assert_allclose(p.tractor, p.heat, atol=1e-9)
            assert p.heat >= 0


def test_each_shaft_holds_steady():
    t = torques(S)
    assert_allclose(t.tractor + t.one + t.belt_near, 0, atol=1e-12)
    assert_allclose(t.two + t.belt_far, 0, atol=1e-12)


def test_power_flows_back_the_other_way_below_the_match():
    low = replace(S, two=Machine(.55))
    assert current(low) < 0
    assert roles(low) == ('machine 1 overhauled (generator)', 'machine 2 powering (motor)')
    assert powers(low).belt < 0


def test_the_lever_way_and_the_capture_way_agree():
    coil = Coil()
    for turn in np.linspace(0, 7, 41):
        assert_allclose(torque_by_levers(coil, turn, 2), torque_by_capture(coil, turn, 2), atol=1e-8)


def test_the_along_part_pushes_but_never_turns():
    upright = Coil(across=0)
    for turn in np.linspace(0, 7, 13):
        assert_allclose(torque_by_levers(upright, turn, 2), 0, atol=1e-12)
        assert_allclose(capture(upright, turn), 0, atol=1e-9)


def test_the_coil_at_a_3_4_5_lean_is_the_matched_machine():
    coil = Coil()
    assert_allclose(peak_capture(coil), matched(S))
    assert_allclose(max(abs(capture(coil, t)) for t in np.linspace(0, 7, 701)), .6, rtol=1e-4)
