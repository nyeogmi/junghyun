from basics.records import Color, Move, Tile
from typing import NamedTuple, Tuple


class GameView(NamedTuple):
    moves: Tuple[Move]

    me_score: int
    they_score: int

    me_tiles: Tuple[Tile]
    they_black: int
    they_white: int


class Player(object):
    def __init__(self, name):
        self.name = name

    def play_first(self, view: GameView):
        raise NotImplementedError("play first")

    def play_second(self, view: GameView, color: Color):
        raise NotImplementedError("play second")
