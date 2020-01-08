from basics.player import Player, GameView
from basics.records import Color


NAME = "Maxer"


class Impl(Player):
    def play_first(self, view: GameView):
        return view.me_tiles[len(view.me_tiles) - 1]

    def play_second(self, view: GameView, other: Color):
        return view.me_tiles[len(view.me_tiles) - 1]

