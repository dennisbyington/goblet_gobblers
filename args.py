import argparse
import players


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(description='CLI implementation of the Goblet Gobblers board game',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-X',                         # flag (player x)
                        type=str,                     # type
                        choices=['random', 'human', 'alpha-beta'],  # choices
                        default='random',             # default
                        help='Player type for X: "human" or "random"',     # help description
                        metavar='str')                # help type

    parser.add_argument('-O',                         # flag (player o)
                        type=str,                     # type
                        choices=['random', 'human', 'alpha-beta'],  # choices
                        default='random',             # default
                        help='Player type for O: "human" or "random"',     # help description
                        metavar='str')                # help type

    parser.add_argument('-v', '--verbose',                      # flag (verbose)
                        action='store_true',                    # action (default = false)
                        help='Print verbose game information')  # help description

    args = parser.parse_args()

    if args.X == 'random':                  # convert string into player functions
        args.X = players.random_player
    if args.X == 'human':
        args.X = players.human_player
    if args.X == 'alpha-beta':
        args.X = players.alpha_beta_cutoff_player
    if args.O == 'random':
        args.O = players.random_player
    if args.O == 'human':
        args.O = players.human_player
    if args.O == 'alpha-beta':
        args.O = players.alpha_beta_cutoff_player

    return args
