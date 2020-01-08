from basics.player import Player, GameView
from basics.records import Color


NAME = "Minner"


class Impl(Player):
    def play_first(self, view: GameView):
        return view.me_tiles[0]

    def play_second(self, view: GameView, other: Color):
        return view.me_tiles[0]

