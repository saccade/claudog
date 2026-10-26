"""A power square: a tractor, two machines, and a belt. Claude.

Seen from the shafts' ends, every shaft turns forward around. Machine 1 sits on
the tractor's PTO shaft. A belt carries that shaft's turning across to machine 2,
5 to 3, so machine 2 sweeps faster. Machine 2's wires run back across the square
to machine 1. The fourth side is the frame: it takes the reaction torques, and
since it never turns, no power runs through it.

Every machine is read the same way: its capture of the sweep is the voltage it
sets up, and its capture of the current is the torque on its shaft.
"""

from dataclasses import dataclass, field
from typing import NamedTuple


@dataclass(frozen=True)
class Machine:
    capture: float             # catch: Wb per stroke
    resistance: float = 0.5    # Ω, its winding


@dataclass(frozen=True)
class Square:
    sweep: float = 60.0        # strokes a second: the PTO, and machine 1's shaft
    near: float = 0.05         # m, the belt wheel on machine 1's shaft
    far: float = 0.03          # m, the belt wheel on machine 2's
    one: Machine = field(default_factory=lambda: Machine(1.0))
    two: Machine = field(default_factory=lambda: Machine(0.65))


def far_sweep(square):
    """The belt runs at one pace, so the smaller wheel sweeps faster."""
    return square.sweep * square.near / square.far


def pace(square):
    """The belt's speed, cat."""
    return square.sweep * square.near


def matched(square):
    """The capture machine 2 needs to set up the same voltage as machine 1: the belt's lever, inverted."""
    return square.one.capture * square.far / square.near


def current(square):
    """A, around the wires: out of machine 2 and into machine 1 when it comes out positive."""
    push = square.two.capture * far_sweep(square) - square.one.capture * square.sweep
    return push / (square.one.resistance + square.two.resistance)


class Torques(NamedTuple):
    tractor: float             # crank, on machine 1's shaft
    one: float                 # machine 1's capture of the current, on its own shaft
    two: float                 # machine 2's, on its own shaft (a drag when it comes out negative)
    belt_near: float           # the belt on machine 1's shaft
    belt_far: float            # the belt on machine 2's shaft
    tension: float             # push: tight side less slack side


def torques(square):
    """Steady running: each shaft's torques add to nothing. Forward around counts up."""
    i = current(square)
    one, two = square.one.capture * i, -square.two.capture * i
    belt_far = -two                                   # the belt holds machine 2's shaft steady
    tension = belt_far / square.far
    belt_near = -tension * square.near
    return Torques(-one - belt_near, one, two, belt_near, belt_far, tension)


class Powers(NamedTuple):
    tractor: float             # pow into machine 1's shaft from the PTO
    belt: float                # carried by the belt, from machine 1's shaft to machine 2's
    made: float                # electrical, out of machine 2's winding into the wires
    used: float                # electrical, into machine 1, turned back into shaft power
    heat: float                # in the two windings


def powers(square):
    i, t = current(square), torques(square)
    return Powers(tractor=t.tractor * square.sweep,
                  belt=t.tension * pace(square),
                  made=square.two.capture * far_sweep(square) * i,
                  used=square.one.capture * square.sweep * i,
                  heat=i**2 * (square.one.resistance + square.two.resistance))


def roles(square):
    """Which machine is powering and which is overhauled."""
    if current(square) > 0:
        return 'machine 1 powering (motor)', 'machine 2 overhauled (generator)'
    if current(square) < 0:
        return 'machine 1 overhauled (generator)', 'machine 2 powering (motor)'
    return 'machine 1 idling', 'machine 2 idling'
