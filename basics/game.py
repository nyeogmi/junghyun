from basics.player import GameView, Player
from basics.records import *
from typing import List, Set


def play(p1_template, p2_template, loud: bool = False):
    p1: Player = p1_template.Impl(p1_template.NAME + " 1")
    p2: Player = p2_template.Impl(p2_template.NAME + " 2")

    moves: List[ImpartialMove] = []

    def disp(s):
        if loud: print(s)

    get_p1_view = lambda: _game_view([move.for_p1() for move in moves])
    get_p2_view = lambda: _game_view([move.for_p2() for move in moves])

    def trick(a: Player, b: Player, a_view: GameView, b_view: GameView):
        # == a's turn ==
        disp("{0} starts.".format(a.name))

        a_tile = a.play_first(a_view)
        assert a_tile in a_view.me_tiles
        disp("{0} picks: {1}".format(a.name, a_tile))

        # == b's turn ==
        disp("{0} responds.".format(b.name))

        b_tile = b.play_second(b_view, color(a_tile))
        assert b_tile in b_view.me_tiles
        disp("{0} picks: {1}".format(b.name, b_tile))

        return a_tile, b_tile

    p1_view = get_p1_view()
    p2_view = get_p2_view()

    disp("{0} vs {1}".format(p1.name, p2.name))
    while len(moves) < TileN:  # there are tiles left
        disp("")
        if len(moves) % 2 == 0:
            p1_tile, p2_tile = trick(p1, p2, p1_view, p2_view)
        else:
            p2_tile, p1_tile = trick(p2, p1, p2_view, p1_view)

        moves.append(ImpartialMove(p1_tile, p2_tile))
        p1_view = get_p1_view()
        p2_view = get_p2_view()
        disp("New scores: {0} ({1}); {2} ({3})".format(p1.name, p1_view.me_score, p2.name, p2_view.me_score))

        if abs(p1_view.me_score - p2_view.me_score) > TileN - len(moves):
            disp("Game no longer winnable.")
            break

    disp("")
    if p1_view.me_score > p2_view.me_score:
        return "p1"
    elif p2_view.me_score > p1_view.me_score:
        return "p2"
    else:
        return "tie"


def _game_view(partial_moves: List[Move]):
    me_tiles: Set[Tile] = set(range(TileN))
    they_tiles = set(range(TileN))

    me_score = 0
    they_score = 0

    for move in partial_moves:
        me_tiles.discard(move.me)
        they_tiles.discard(move.they)

        if move.result == Result.ME:
            me_score += 1
        elif move.result == Result.THEY:
            they_score += 1

    they_black = 0
    they_white = 0

    for tile in they_tiles:
        if color(tile) == Colors.BLACK:
            they_black += 1
        else:
            they_white += 1

    return GameView(
        moves=tuple(partial_moves),

        me_score=me_score,
        they_score=they_score,

        me_tiles=tuple(sorted(me_tiles)),
        they_black=they_black,
        they_white=they_white,
    )
