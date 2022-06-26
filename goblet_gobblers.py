#!/usr/bin/env python3

"""
Dennis Byington
dennis.byington@mac.com
25 Jun 2022
CLI implementation of the Goblet Gobblers board game

------------------------------------------------------------------------------------------
general info:
-------------
game elements:
    board
    players (2)
    pieces (6 per player: 2 large, 2 medium, 2 small)

game play:
    players take turns placing pieces on the board
        may choose a piece not in play or one on the board already (need to remember what is nested)
    check for win after each turn (should not have a draw but may have a tie?)

rules:
    larger pieces may nest on top of smaller pieces only (must be >, not <=)
    if a piece is moved that is already on the board, what ever was below is now active
    play until someone wins

** notes to add **
    - pieces will be removed from the pieces lists and inserted onto the board
    - each board internal list represents a spot on the board (will push/pop pieces)
------------------------------------------------------------------------------------------

current TODO: init variables

later:
    - display board
    - pick piece
    - pick spot
    - check win/tie
    - rando choose 1st player
    - incorporate all together
    - refactor & smooth
"""


import argparse


# --------------------------------------------------


def get_args():
    """Get command-line arguments

    Parses and packages command line arguments into a argparse object based
    on the flags & options initialized within this function.

    In this instance, no options/flags are set except the default [-h] (help).

    Args:
        None

    Returns:
        parser.parse_args(): An argparse object with members that correlate to any
        options/flags that are initialized in this function
    """

    parser = argparse.ArgumentParser(description='CLI implementation of the Goblet Gobblers board game',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # parser.add_argument('positional',  # name
    #                     type=str,  # type
    #                     metavar='str',  # help type
    #                     help='A positional argument')  # help description
    #
    # parser.add_argument('-o', '--opt',  # flags (name)
    #                     type=str,  # type
    #                     choices=['choiceA', 'choiceB'],  # choices
    #                     default=None,  # default
    #                     help='An optional string argument',  # help description
    #                     metavar='str')  # help type
    #
    # parser.add_argument('-f', '--file',  # flags (name)
    #                     type=argparse.FileType('rt'),  # type
    #                     default=None,  # default
    #                     metavar='FILE',  # help name
    #                     help='A readable file')  # help title
    #
    # parser.add_argument('-b', '--bool',  # flags (name)
    #                     action='store_true',  # action (default = false)
    #                     help='A boolean flag')  # help description

    return parser.parse_args()


# --------------------------------------------------


class Piece:
    """Class to represent game pieces"""

    def __init__(self, player, size, name):
        self.player = player  # X or O
        self.size = size  # 1, 2, 3
        self.name = name  # X1, X2, O3, O4, etc

    def __gt__(self, other):
        return self.size > other.size


# --------------------------------------------------


# display_board (accepts: board / return: nothing)
    # print board and players piece lists (see details below)
"""
display board (*smooth this out)
--------------

Player-X                                       Player-O
-------------------------------------          -------------------------------------
| XXX | XXX | XX  | XX  |  X  |  X  |  Pieces  | OOO | OOO | OO  | OO  |  O  |  O  |
-------------------------------------          -------------------------------------
| X1  | X2  | X3  | X4  |  X5 |  X6 |  Names   | O1  | O2  | O3  | O4  |  O5 |  O6 |
-------------------------------------          -------------------------------------

                                     |         |
                               XX    |    X    |   OOO
                                   1 |       2 |       3
                            -----------------------------
                                     |         |
                                O    |   OO    |   OOO
                                   4 |       5 |       6
                            -----------------------------
                                     |         |
                                X    |   XX    |   XXX
                                   7 |       8 |       9


Player-X pick your piece (X1, X2, etc):
Player-X pick your spot (1-9):


after pieces have been used
---------------------------

Player-X                                       Player-O
-------------------------------------          -------------------------------------
|     | XXX |     | XX  |     |  X  |  Pieces  | OOO | OOO |     |     |  O  |  O  |
-------------------------------------          -------------------------------------
|     | X2  |     | X4  |     |  X6 |  Labels  | O1  | O2  |     |     |  O5 |  O6 |
-------------------------------------          -------------------------------------
"""


# --------------------------------------------------


# pick_piece (accepts: board, player?, player's piece list / returns: piece)
    # can select from own list or pieces on board (*need to figure out how to enumerate/label these)


# --------------------------------------------------


# pick_spot (accepts: board, piece / returns: updated board)
    # check valid move
    # move piece(s)


# --------------------------------------------------


# check_win_tie (accepts: board / returns: int (0 = no win/tie / 1 = win or tie)
    # go through rows, columns, diagonals
    # check for wins & ties
    # print message if so


# --------------------------------------------------


def main():
    """Short description

    Long description

    Args:
        Arg:
            descrption

    Returns:
        return:
            description
    """

    args = get_args()  # only used for -h flag

    # init pieces, lists of pieces, and board
    X1 = Piece('X', 3, 'X1')
    X2 = Piece('X', 3, 'X2')
    X3 = Piece('X', 2, 'X3')
    X4 = Piece('X', 2, 'X4')
    X5 = Piece('X', 1, 'X5')
    X6 = Piece('X', 1, 'X6')
    O1 = Piece('O', 3, 'O1')
    O2 = Piece('O', 3, 'O2')
    O3 = Piece('O', 2, 'O3')
    O4 = Piece('O', 2, 'O4')
    O5 = Piece('O', 1, 'O5')
    O6 = Piece('O', 1, 'O6')
    x_pieces = [X1, X2, X3, X4, X5, X6]
    o_pieces = [O1, O2, O3, O4, O5, O6]
    board = [[], [], [], [], [], [], [], [], []]

    # rando chose player for first turn

    # while no winner/tie:
        # display board

        # pick piece to play

        # pick spot

        # check win/tie
            # if yes: break
            # if no:  continue


# --------------------------------------------------


if __name__ == '__main__':
    main()
