"""A loudspeaker's motor: a coil of wire in a magnet's gap. Claude.

Bl is the field in the gap times the length of wire sitting in it.
Read one way it's push per amp; read the other, voltage per speed.
Both are the flux the wire captures per meter it moves.
"""

from dataclasses import dataclass
import numpy as np

TURN = 2*np.pi        # all the way round, in radians
OPEN = np.inf         # nothing across the leads: no current can flow
SHORT = 0.0           # leads twisted together, or a good amplifier


@dataclass(frozen=True)
class Speaker:
    field: float = 1.0           # T, in the gap, pointing out from the axis
    radius: float = 0.02         # m, the coil's
    turns: int = 64
    resistance: float = 6.0      # Ω, the coil's own wire
    mass: float = 0.020          # kg, cone and coil and the air they carry
    stiffness: float = 1250.0    # N/m, the suspension's spring
    friction: float = 1.0        # N per m/s, the suspension's own losses


def wire(speaker):
    """Wire in the gap, m: every winding is a turn at the coil's radius."""
    return speaker.turns * TURN * speaker.radius


def bl(speaker):
    """Field across wire: T·m, which is N/A, V·s/m, and Wb/m."""
    return speaker.field * wire(speaker)


def force(speaker, current):
    """The push on the coil, N, along the axis: Bl of the current."""
    return bl(speaker) * current


def voltage(speaker, speed):
    """The voltage the moving coil sets up, V: Bl of the speed."""
    return bl(speaker) * speed


def flux_captured(speaker, distance):
    """Wb: the wire sweeps a band, wire long and distance wide, through the field."""
    return speaker.field * wire(speaker) * distance


def drag(speaker, across):
    """N per m/s, from the circuit, with `across` ohms on the leads.

    The cone's speed captures a voltage, the voltage drives a current around
    the coil and whatever's across it, and the current's Bl pushes back:
    Bl acts twice, with a conductance between."""
    return bl(speaker)**2 / (speaker.resistance + across)


def ring(speaker):
    """rad/s: how fast the cone on its spring would swing with nothing slowing it."""
    return np.sqrt(speaker.stiffness / speaker.mass)


def q_mechanical(speaker):
    """Strokes of ringing for the suspension's losses to take the swing's energy down by e."""
    return ring(speaker) * speaker.mass / speaker.friction


def q_electrical(speaker):
    """The same, for the drag through shorted leads: the spec sheet's Qes."""
    return ring(speaker) * speaker.mass / drag(speaker, SHORT)
