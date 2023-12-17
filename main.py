#!/usr/bin/env python3

from args import *
from players import *
from goblet_gobblers import *


def main():
    """Starts goblet gobblers game based on command line arg inputs"""

    # get command line args
    args = get_args()

    # seed random module
    random.seed(args.r)

    # create game instance
    gg = GobletGobblers()

    # start game
    gg.play_game(args.X, args.O, verbose=args.v)


# ------------------------
if __name__ == '__main__':
    main()
