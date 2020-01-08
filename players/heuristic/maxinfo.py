from aitools.solve import possible_solves
from basics.player import Player, GameView
from basics.records import color, Color, Tile, TileN
from math import ceil
from typing import List, Optional, Tuple


NAME = "Max-Info"


class Impl(Player):
    def play_first(self, view: GameView):
        return self.play(view, None)

    def play_second(self, view: GameView, other: Color):
        return self.play(view, other)

    def play(self, view: GameView, other: Optional[Color]):
        worlds = list(possible_solves(list(view.moves)))
        tile_lists = make_tile_lists(worlds, other)
        tile_lists_weighted = [(calculate_weight(view.moves, w), tile_list) for w, tile_list in zip(worlds, tile_lists)]

        imperfection = {
            candidate:
                sum([weight * calculate_imperfection(tile_list, candidate) for weight, tile_list in tile_lists_weighted])
            for candidate in view.me_tiles
        }
        best_candidate = max(view.me_tiles, key=lambda t: (-imperfection[t], t))
        print(imperfection)
        return best_candidate


def calculate_weight(moves, world):
    return 1.0


def calculate_imperfection(tile_list, candidate):
    n_below = 0
    n_above = 0
    for i in tile_list:
        if i < candidate:
            n_below += 1
        elif i > candidate:
            n_above += 1
    return abs(n_above - n_below)


def make_tile_lists(worlds, other: Optional[Color]) -> List[Tuple[Tile]]:
    tile_lists = []
    if other is None:
        for world in worlds:
            tile_lists.append(tile_list(world))
    else:
        for world in worlds:
            tile_lists.append(tuple(p for p in tile_list(world) if color(p) == other))
    return tile_lists


def tile_list(pieces_used) -> Tuple[Tile]:
    all_others: List[Tile] = list(range(TileN))
    for i in pieces_used:
        all_others.remove(i)
    return tuple(all_others)
