from basics.records import *


def possible_solves(game: List[Move]):
    return _possible_solves(game, [])


def _possible_plays(move: Move):
    # NOTE:
    # There's tricky ways to compute this,
    # but I won't do any of them
    if move.result == Result.TIE:
        if color(move.me) == move.they: yield move.me

    elif move.result == Result.ME:
        # his tile is lower than mine
        for i in range(0, move.me, 1):
            if color(i) == move.they: yield i

    elif move.result == Result.THEY:
        # his tile is higher than mine
        for i in range(move.me + 1, TileN, 1):
            if color(i) == move.they: yield i


def _possible_solves(game: List[Move], they_spent: List[Tile]):
    if len(game) == 0:
        # note: there's no actual need to do this clone, as long as we do everything we need with it
        # before the next iteration
        yield tuple(they_spent)
        return

    head = game[0]
    tail = game[1:]

    for they_possible in _possible_plays(head):
        if they_possible in they_spent: continue

        they_spent.append(they_possible)
        for solve in _possible_solves(tail, they_spent):
            yield solve
        they_spent.pop()

