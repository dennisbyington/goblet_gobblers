import argparse
import players


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(description='CLI implementation of the Goblet Gobblers board game',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-X',  # flag (player x)
                        type=str,
                        choices=['random', 'human', 'alpha_beta', 'neural_net'],
                        default='random',
                        help='Player type for X: [random, human, alpha_beta, neural_net]',
                        metavar='str')  # help type

    parser.add_argument('-O',  # flag (player o)
                        type=str,
                        choices=['random', 'human', 'alpha_beta', 'neural_net'],
                        default='random',
                        help='Player type for O: [random, human, alpha_beta, neural_net]',
                        metavar='str')  # help type

    parser.add_argument('-r',  # flag (random seed)
                        type=int,
                        default=None,
                        help='Seed for random module',
                        metavar='int')  # help type

    parser.add_argument('-t',  # flag (train nn)
                        type=int,
                        default=None,
                        help='Train neural net [Number games] *will save updated model*',
                        metavar='+int')  # help type

    parser.add_argument('-v',  # flag (verbose)
                        action='store_true',  # action is to store a true value (default = false)
                        help='Print verbose game information')

    args = parser.parse_args()

    if args.X == 'random':                  # convert string into player functions
        args.X = players.random_player
    if args.X == 'human':
        args.X = players.human_player
    if args.X == 'alpha_beta':
        args.X = players.alpha_beta_cutoff_player
    if args.X == 'neural_net':
        args.X = players.neural_net_player
    if args.O == 'random':
        args.O = players.random_player
    if args.O == 'human':
        args.O = players.human_player
    if args.O == 'alpha_beta':
        args.O = players.alpha_beta_cutoff_player
    if args.O == 'neural_net':
        args.O = players.neural_net_player

    return args
