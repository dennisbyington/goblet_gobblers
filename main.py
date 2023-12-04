#!/usr/bin/env python3

from args import *
from players import *
from goblet_gobblers import *


def main():
    """Starts goblet gobblers game based on command line arg inputs"""

    args = get_args()               # get args
    random.seed(0)                  # seed random module

    gg = GobletGobblers()                               # create game instance
    gg.play_game(args.X, args.O, verbose=args.verbose)  # start game


# ------------------------
if __name__ == '__main__':
    main()
