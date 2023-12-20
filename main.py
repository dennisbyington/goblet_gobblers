#!/usr/bin/env python3

import copy
from args import *
from players import *
from goblet_gobblers import GobletGobblers
from goblet_gobblers_neural_net import *


def main():
    """Starts goblet gobblers game based on command line arg inputs"""

    # get command line args
    args = get_args()

    # seed random module
    random.seed(args.r)

    # create game instance
    gg = GobletGobblers()

    # create model instance, load & set to evaluation mode
    model = GobletGobblersNet()
    model.load_state_dict(torch.load('goblet_gobblers_model.pt'))

    if args.t:
        # train & save model
        model.train_nn(gg, num_games=args.t)
        torch.save(model.state_dict(), 'goblet_gobblers_model.pt')
    else:
        # set model to evaluation mode & start game
        model.eval()
        gg.play_game(args.X, args.O, verbose=args.v, model=model)


# ------------------------
if __name__ == '__main__':
    main()
