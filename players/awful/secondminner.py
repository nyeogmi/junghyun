from basics.player import Player, GameView
from basics.records import Color


# counterplay to minner
NAME = "Second-Minner"


class Impl(Player):
    def play_first(self, view: GameView):
        return view.me_tiles[min(1, len(view.me_tiles))]

    def play_second(self, view: GameView, other: Color):
        return view.me_tiles[min(1, len(view.me_tiles))]

