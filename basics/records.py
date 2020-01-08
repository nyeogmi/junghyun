from enum import Enum
from typing import NamedTuple, List


Tile = int
Color = int
TileN = 9


class Colors(object):
    BLACK = 0
    WHITE = 1


class Result(Enum):
    ME = 0
    THEY = 1
    TIE = 2


class Move(NamedTuple):
    me: Tile
    they: Color
    result: Result


class ImpartialMove(NamedTuple):
    p1: Tile
    p2: Tile

    def for_p1(self):
        return Move(self.p1, color(self.p2), result(self.p1, self.p2))

    def for_p2(self):
        return Move(self.p2, color(self.p1), result(self.p2, self.p1))


def color(tile: Tile) -> Color:
    return tile % 2


def result(me: Tile, they: Tile) -> Result:
    return (
        Result.ME if me > they else
        Result.THEY if me < they else
        Result.TIE
    )