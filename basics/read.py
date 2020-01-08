from basics.records import *
from typing import List


def read_game(s):
    # sample: "B<8 B<4 W<3"
    moves: List[Move] = []
    for line in s.split():
        assert len(line) == 3
        assert line[0] in "WB"
        assert line[1] in "><="
        assert line[2] in "012345678"
        moves.append(Move(
            Tile(line[2]),
            Color(line[0] == "W"),
            (
                Result.ME if line[1] == "<" else
                Result.THEY if line[1] == ">" else
                Result.TIE
            )
        ))
    return moves
