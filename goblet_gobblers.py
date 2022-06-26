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
    - describe all data structures here instead of in each docstring
    - pieces will be removed from the pieces lists and inserted onto the board
        - will never have to add pieces back to the list, they must remain on the board once placed
    - each board internal list represents a spot on the board (will push/pop pieces)
------------------------------------------------------------------------------------------

current TODO: display board

later:
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


def display_board(board, x_pieces, o_pieces):
    """Displays player's piece lists, piece names, and game board"""

    print(f'Player-X                                       Player-O')
    print(f'-------------------------------------          -------------------------------------')
    print(f'| {x_pieces[0]} | {x_pieces[1]} | {x_pieces[2]} | {x_pieces[3]} | {x_pieces[4]} | {x_pieces[5]} |  Pieces  '
          f'| {o_pieces[0]} | {o_pieces[1]} | {o_pieces[2]} | {o_pieces[3]} | {o_pieces[4]} | {o_pieces[5]} |')
    print(f'-------------------------------------          -------------------------------------')
    print(f'| X1  | X2  | X3  | X4  |  X5 |  X6 |  Names   | O1  | O2  | O3  | O4  |  O5 |  O6 |')
    print(f'-------------------------------------          -------------------------------------')
    print(f'                                     |         |         ')
    print(f'                               {board[0][0]}   |   {board[1][0]}   |   {board[2][0]}   ')
    print(f'                                   1 |       2 |       3 ')
    print(f'                            -----------------------------')
    print(f'                                     |         |         ')
    print(f'                               {board[3][0]}   |   {board[4][0]}   |   {board[5][0]}   ')
    print(f'                                   4 |       5 |       6 ')
    print(f'                            -----------------------------')
    print(f'                                     |         |         ')
    print(f'                               {board[6][0]}   |   {board[7][0]}   |   {board[8][0]}   ')
    print(f'                                   7 |       8 |       9 ')
    print(f'')


# --------------------------------------------------


# pick_piece (accepts: board, player?, player's piece list / returns: piece)
    # can select from own list or pieces on board (*need to figure out how to enumerate/label these)




    """
    Player-X pick your piece (X1, X2, etc):   
    Player-X pick your spot (1-9):
    """


# --------------------------------------------------


# pick_spot (accepts: board, piece / returns: updated board)
    # check valid move
        # Error: Cannot nest onto a piece that is equal or greater in size
    # move piece(s)
        # ensure piece has been replaced by '-' in list (for display board functionality)


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

    # init pieces, and board
    x_pieces = ['XXX', 'XXX', 'OO ', 'XX ', ' X ', ' X ']   # extra spaces for display formatting
    o_pieces = ['XXX', 'OOO', 'OO ', 'OO ', ' X ', ' O ']
    board = [['   '], ['   '], ['   '], ['   '], ['   '], ['   '], ['   '], ['   '], ['   ']]

    # rando chose player for first turn

    # while no winner/tie:
        # display board
    display_board(board, x_pieces, o_pieces)

        # pick piece to play

        # pick spot

        # check win/tie
            # if yes: break
            # if no:  continue


# --------------------------------------------------


if __name__ == '__main__':
    main()
