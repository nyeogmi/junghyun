from basics.player import Player, GameView
from basics.records import Color
import random


NAME = "Random"


class Impl(Player):
    def play_first(self, view: GameView):
        return random.choice(view.me_tiles)

    def play_second(self, view: GameView, other: Color):
        return random.choice(view.me_tiles)

