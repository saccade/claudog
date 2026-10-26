"""One coil in a leaning field, worked out two ways. Claude.

The axle points out of the page, the way forward around points. The field leans
on the axle: its across part lies along the page's →, its along part along the
axle. The coil's face turns with the shaft.

The lever way: find the push on each of the coil's four sides, find each side's
lever from the axle at this point in the turn, cross them, keep the part along
the axle, and add. The capture way: follow the flux the coil links as it turns;
its slope per stroke is the capture, and the capture of the current is the torque.
"""

from dataclasses import dataclass
import numpy as np

ACROSS, SIDE, AXLE = np.eye(3)      # →, ↑, and out of the page


@dataclass(frozen=True)
class Coil:
    turns: int = 100
    width: float = 0.1              # m, across the axle
    length: float = 0.1             # m, along it
    field: float = 1.0              # T
    across: float = 3/5             # the field's lean: its across share (a 3-4-5)


def field(coil):
    return coil.field * (coil.across*ACROSS + np.sqrt(1 - coil.across**2)*AXLE)


def face(turn):
    """The way the coil's face points, `turn` strokes past facing →."""
    return np.cos(turn)*ACROSS + np.sin(turn)*SIDE


def linkage(coil, turn):
    """Wb: the turns times the area times the field through the face."""
    return coil.turns * coil.width * coil.length * (field(coil) @ face(turn))


def capture(coil, turn, step=1e-5):
    """catch: the linkage gained per stroke of turning, from the slope."""
    return (linkage(coil, turn + step) - linkage(coil, turn - step)) / (2*step)


def sides(coil, turn):
    """The four sides as (middle, run), the current running forward around the face."""
    out = np.cross(AXLE, face(turn))                  # across the coil, in its plane
    half_w, half_l = coil.width/2 * out, coil.length/2 * AXLE
    return [(-half_l, coil.width*out), (half_w, coil.length*AXLE),
            (half_l, -coil.width*out), (-half_w, -coil.length*AXLE)]


def torque_by_levers(coil, turn, current):
    """crank about the axle: each side's lever crossed with its push, along the axle, added."""
    total = 0.0
    for lever, run in sides(coil, turn):
        push = coil.turns * current * np.cross(run, field(coil))
        total += np.cross(lever, push) @ AXLE
    return total


def torque_by_capture(coil, turn, current):
    """crank about the axle: the capture of the current."""
    return capture(coil, turn) * current


def peak_capture(coil):
    """What a machine of many such coils, commutated, keeps: only the field's across part ever counts."""
    return coil.turns * coil.width * coil.length * coil.field * coil.across
