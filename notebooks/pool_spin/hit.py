"""Two pool balls meet, seen from above. Claude.

→ is A's travel, ↑ on the page is the shot's left, and ↺ (widdershins on the
table) points up out of it. Everything happens in the instant of the hit: the
balls don't move, and the cloth's push is only their weight, too small to count.

Along the line of centers the balls push; across it their faces skid, and
friction is the only way spin can pass. Changes in travel are in cat: the push
on a ball, per lump, over the instant.
"""

from dataclasses import dataclass
from typing import NamedTuple
import numpy as np

FORWARD, LEFT, UP = np.eye(3)


@dataclass(frozen=True)
class Ball:
    radius: float = 0.03       # m
    mass: float = 1/6          # lump; a pool ball is about 170 g
    share: float = 2/5         # a solid ball's inertia: this share of its mass at the rim


@dataclass(frozen=True)
class Shot:
    speed: float = 3.0         # cat, A's travel
    sweep: float = 200.0       # strokes a second, A's sidespin; ↺ counts up
    fullness: float = 1.0      # 1 is full on, 0 is a miss; thinner cuts B to the right
    friction: float = 1/25     # between the faces, as a share of the push
    bounce: float = 1.0        # share of the closing speed the balls part with


class Motion(NamedTuple):
    travel: np.ndarray         # cat
    sweep: np.ndarray          # strokes a second, along UP


def coming(shot):
    return Motion(shot.speed*FORWARD, shot.sweep*UP)


def still():
    return Motion(0*FORWARD, 0*UP)


def line_of_centers(shot):
    """From A's center to B's at the hit. A thinner hit leans it toward A's right."""
    lean = np.arcsin(1 - shot.fullness)
    return np.cos(lean)*FORWARD - np.sin(lean)*LEFT


def face(ball, motion, lever):
    """How a point on the ball's surface moves: its travel, plus the sweep's pace at the lever."""
    return motion.travel + np.cross(motion.sweep, lever)


def turn(ball, lever, change):
    """The change in sweep when a change in travel lands at the lever."""
    return np.cross(lever, change) / (ball.share * ball.radius**2)


def across(arrow, line):
    """The part of the arrow at right angles to the line."""
    return arrow - (arrow @ line)*line


def hit(ball, shot):
    """A comes in; B sits still. Returns how each leaves."""
    a, b = coming(shot), still()
    line = line_of_centers(shot)
    lever = ball.radius*line                          # from A's center to the contact; B's is the opposite
    push = (1 + shot.bounce)/2 * (a.travel @ line)    # cat, along the line
    skid = across(face(ball, a, lever) - face(ball, b, -lever), line)
    closes = 2*(1 + 1/ball.share)                     # each cat of grip closes the skid this much: 7
    grip = min(shot.friction*push, np.linalg.norm(skid)/closes)
    drag = grip * skid/np.linalg.norm(skid) if grip else 0*FORWARD   # on B, along A's face; A gets the opposite
    a_after = Motion(a.travel - push*line - drag, a.sweep + turn(ball, lever, -drag))
    b_after = Motion(b.travel + push*line + drag, b.sweep + turn(ball, -lever, drag))
    return a_after, b_after


def punch(ball, motion):
    return ball.mass * (motion.travel @ motion.travel)/2


def hook(ball, motion):
    return ball.share * ball.mass * ball.radius**2 * (motion.sweep @ motion.sweep)/2


def energy(ball, motion):
    return punch(ball, motion) + hook(ball, motion)


def heat(ball, shot):
    """Thump lost in the instant: the skid's friction, and any bounce short of full."""
    a_after, b_after = hit(ball, shot)
    return energy(ball, coming(shot)) - energy(ball, a_after) - energy(ball, b_after)
