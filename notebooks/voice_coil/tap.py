"""Tap the cone and watch it ring down. Claude.

Each small step: the spring, the losses, and the circuit's drag push on the
cone; the push changes its speed; the speed changes its place.
"""

from typing import NamedTuple
import numpy as np

from speaker import bl, drag


class Ringdown(NamedTuple):
    time: np.ndarray       # s
    place: np.ndarray      # m, out from rest
    speed: np.ndarray      # m/s
    current: np.ndarray    # A, around the coil and whatever's across the leads


def tap(speaker, across, kick=0.1, duration=0.15, steps=15000):
    """The cone after a tap leaves it moving out at `kick` m/s."""
    step = duration / steps
    slowing = speaker.friction + drag(speaker, across)
    place, speed = 0.0, kick
    places, speeds = [], []
    for _ in range(steps):
        places.append(place)
        speeds.append(speed)
        push = -speaker.stiffness*place - slowing*speed
        speed += push / speaker.mass * step
        place += speed * step
    speeds = np.array(speeds)
    current = -bl(speaker) * speeds / (speaker.resistance + across)   # its push opposes the motion
    return Ringdown(np.arange(steps)*step, np.array(places), speeds, current)
