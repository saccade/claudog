"""Bl, checked from both sides. Claude."""

from dataclasses import replace

import numpy as np
import pytest
from numpy.testing import assert_allclose
from pint import UnitRegistry

from speaker import (Speaker, wire, bl, force, voltage, flux_captured, drag, ring,
                     q_electrical, q_mechanical, OPEN, SHORT, TURN)
from tap import tap

units = UnitRegistry()
S = Speaker()


def test_one_unit_four_names():
    for other in ('newton / ampere', 'volt * second / meter', 'weber / meter'):
        assert units.Quantity(1, 'tesla * meter').to(other).magnitude == pytest.approx(1)


def test_the_wire_is_its_windings_at_the_radius():
    assert_allclose(wire(S), 64 * TURN * .02)
    assert round(bl(S)) == 8


def test_added_weight_and_the_current_that_lifts_it_back():
    weight = .010 * 10                        # a 10 g washer, dog gravity
    current = weight / bl(S)
    assert round(1000*current) == 12          # about 12 mA
    assert_allclose(force(S, current), weight)


def test_the_voltage_is_the_rate_of_flux_captured():
    speed, moment = .1, 1e-3
    assert_allclose(flux_captured(S, speed*moment) / moment, voltage(S, speed))


@pytest.mark.parametrize('current, speed', [(.3, .1), (-.2, .05)])
def test_push_at_speed_is_voltage_of_current(current, speed):
    assert_allclose(force(S, current) * speed, voltage(S, speed) * current)


def test_open_leads_carry_nothing_and_add_no_drag():
    run = tap(S, OPEN)
    assert drag(S, OPEN) == 0
    assert not np.any(run.current)


def test_the_tap_energy_all_ends_as_heat():
    """Punch at the start = suspension losses + the coil's and the leads' heat."""
    across = 2.0
    run = tap(S, across, duration=.3, steps=60000)
    step = run.time[1]
    start = S.mass * .1**2 / 2
    burned = np.sum(S.friction * run.speed**2 + (S.resistance + across) * run.current**2) * step
    assert_allclose(burned, start, rtol=.01)


def test_shorted_leads_damp_the_ringing():
    open_, shorted = tap(S, OPEN), tap(S, SHORT)
    late = open_.time > .05
    assert np.max(np.abs(shorted.place[late])) < np.max(np.abs(open_.place[late])) / 50


def test_spec_sheet_qs():
    assert ring(S) == pytest.approx(250)
    assert q_mechanical(S) == pytest.approx(5)
    assert_allclose(q_electrical(S), ring(S) * S.mass * S.resistance / bl(S)**2)
    stronger = replace(S, field=2*S.field)
    assert_allclose(q_electrical(stronger), q_electrical(S) / 4)


def test_the_winch_from_its_cable():
    capture, drum = .5, .05                   # Wb/rad, m
    cable = capture / drum                     # Wb/m: the winch's Bl
    assert cable == pytest.approx(10)
    assert cable * 2 == pytest.approx(20)      # 2 A holds the 20 N weight
    assert cable * .8 == pytest.approx(8)      # 0.8 m/s sets up 8 V
