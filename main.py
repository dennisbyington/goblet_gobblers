#!/usr/bin/env python3

from args import *
from players import *
from goblet_gobblers import *


def main():
    """Starts goblet gobblers game based on command line arg inputs"""

    # get command line args
    args = get_args()

    # seed random module
    random.seed(0)

    # create game instance
    gg = GobletGobblers()

    # start game
    # gg.play_game(args.X, args.O, verbose=args.verbose)



    # test state (testing heuristic) (remove later) -----------------------
    # board data struct (extra list in zero-index for index buffer)
    board = ['buffer', ['   '], ['   '], ['   '],
                       ['   '], ['   '], ['   '],
                       ['   '], ['   '], ['   ']]

    # bank data struct (extra spaces for display formatting)
    bank = ['XXX', 'XXX', 'XX ', 'XX ', ' X ', ' X ',
            'OOO', 'OOO', 'OO ', 'OO ', ' O ', ' O ']

    # create initial game state
    test_state = GobletGobblersGameState(to_move='X',
                                         utility=0,
                                         board=board,
                                         bank=bank)

    gg.initial = test_state
    gg.heuristic(gg.initial, gg.initial.to_move)    # note: may need to change who "player" is here (?should this be not state.to_move?)

    # --------------------------------------------------------------------


# ------------------------
if __name__ == '__main__':
    main()
