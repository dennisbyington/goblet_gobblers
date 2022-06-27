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
    play until someone wins.  Once piece is picked up it must be played

    NO TIES *************************
    If moving a piece exposes a winning sequence for the opponent, and if the destination for the move
    does not cover up one of the other pieces in the sequence, then the opponent wins—even if the move
    makes a winning sequence for the moving player.

    * add pdf of rules into the folder (with any additional rules explained in comments here

** notes to add **
    - describe all data structures here instead of in each docstring
    - pieces will be removed from the pieces lists and inserted onto the board
        - will never have to add pieces back to the list, they must remain on the board once placed
    - each board internal list represents a spot on the board (will push/pop pieces)


** check here for additional/clarified rules: https://docs.racket-lang.org/games/gobblet.html
------------------------------------------------------------------------------------------

current TODO: incorporate pickup piece & play piece

later:
    - check win (no ties - see here: https://docs.racket-lang.org/games/gobblet.html)
    - rando choose 1st player
    - incorporate all together
    - refactor, python-ize (look at tpp and online code for ideas) & smooth
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


def display_board(board, pieces):
    """Displays player's piece lists, piece names, and game board"""

    print('\033c', end="")  # clear terminal
    print(f'')
    print(f'                                     |         |         ')
    print(f'                               {board[1][-1]}   |   {board[2][-1]}   |   {board[3][-1]}   ')
    print(f'                                   1 |       2 |       3 ')
    print(f'                            -----------------------------')
    print(f'                                     |         |         ')
    print(f'                               {board[4][-1]}   |   {board[5][-1]}   |   {board[6][-1]}   ')
    print(f'                                   4 |       5 |       6 ')
    print(f'                            -----------------------------')
    print(f'                                     |         |         ')
    print(f'                               {board[7][-1]}   |   {board[8][-1]}   |   {board[9][-1]}   ')
    print(f'                                   7 |       8 |       9 ')
    print(f'')
    print(f'Player-X                                       Player-O')
    print(f'-------------------------------------          -------------------------------------')
    print(f'| {pieces[0]} | {pieces[1]} | {pieces[2]} | {pieces[3]} | {pieces[4]} | {pieces[5]} |  Pieces  '
          f'| {pieces[6]} | {pieces[7]} | {pieces[8]} | {pieces[9]} | {pieces[10]} | {pieces[11]} |')
    print(f'-------------------------------------          -------------------------------------')
    print(f'| 10  | 11  | 12  | 13  |  14 |  15 |          | 16  | 17  | 18  | 19  |  20 |  21 |')
    print(f'-------------------------------------          -------------------------------------')
    print(f'')


# --------------------------------------------------


# pick_piece (accepts: board, player?, player's piece list / returns: piece)
    # can select from own list or pieces on board (*need to figure out how to enumerate/label these)




    """
    Player-X pick your piece (X1, X2, etc):   
    Player-X pick your spot (1-9):
    """


# --------------------------------------------------


def pickup_piece_to_play(board, pieces, player):
    """Player picks up piece to play

    Prompts player for index of piece to play
    Validates piece to verify:
        - not empty spot
        - not opponent's piece
        - not picking up the smallest piece with no place to play it
    Removes piece from list/board

    Args:
        See top docstring

    Returns:
        piece_to_play <string>
            representation of piece that was selected.  Ex: 'XXX' 'OO ' ' X '
        piece_spot <int>
            index piece was picked up from
    """

    piece_to_play = ''

    while True:
        # get piece_spot & validate (is a num and valid location)
        piece_spot = input(f'Player-{player}, choose your piece: ')
        if not piece_spot.isnumeric():
            print(f'Error: invalid location')
            continue
        piece_spot = int(piece_spot)
        if piece_spot not in range(1, 22):
            print(f'Error: invalid location')
            continue

        # get piece_to_play from piece_spot
        if piece_spot < 10:  # piece on board
            piece_to_play = board[piece_spot][-1]
        else:  # piece in list
            piece_to_play = pieces[piece_spot - 10]

        # check not blank
        if piece_to_play == '   ':
            print('Error: there is not a piece in that spot')
            continue

        # check is correct player's piece (verify player name matches 1st or 2nd letter of piece_to_play)
        if piece_spot < 10:
            if piece_to_play[0] != player[0] and piece_to_play[1] != player[0]:
                print(f"Error: Can't pick opponents pieces")
                continue
        else:
            if piece_to_play[0] != player[0] and piece_to_play[1] != player[0]:
                print(f"Error: Can't pick opponents pieces")
                continue

        # check if smallest piece selected but no open spots on board:
        size_piece_to_play = piece_to_play.count('X') + piece_to_play.count('O')
        if (size_piece_to_play == 1) and ('   ' not in [board[i][-1] for i in range(0, 10)]):
            print(f"Error: Can't pick up that piece: no where to play it")
            continue

        # If here, have valid piece: remove if from board or list ('pickup')
        if piece_spot < 10:
            board[piece_spot].pop()
        else:
            pieces[piece_spot - 10] = '   '

        break  # have valid piece

    return piece_to_play, piece_spot  # 'pickup' piece


# --------------------------------------------------


def play_piece(board, pieces, piece_to_play, piece_spot):
    """Player piece on board

        Prompts player for index of spot to play on
        Validates spot to verify:
            - not same spot piece was picked up from
            - piece being played > piece being covered
        Places piece onto board

        Args:
            See top docstring

        Returns:
            None
        """

    while True:
        # pick spot_to_play & validate (is a num and valid location)
        spot_to_play = input(f'Player-X, choose spot to play "{piece_to_play}" on: ')
        if not spot_to_play.isnumeric():
            print(f'Error: invalid location')
            continue
        spot_to_play = int(spot_to_play)
        if spot_to_play not in range(1, 10):
            print(f'Error: invalid location')
            continue

        # get curr_on_spot from spot_to_play
        if spot_to_play < 10:  # piece on board
            curr_on_spot = board[spot_to_play][-1]
        else:  # piece in list
            curr_on_spot = pieces[spot_to_play - 10]

        # can't go back to same spot it came from
        if spot_to_play == piece_spot:
            print('Error: can not place into same spot')
            continue

        # can't play if size piece <= size curr piece in spot
        size_piece_to_play = piece_to_play.count('X') + piece_to_play.count('O')
        size_curr_in_spot = curr_on_spot.count('X') + curr_on_spot.count('O')
        if size_piece_to_play <= size_curr_in_spot:
            print(f'Error: Cannot nest onto a piece that is equal to or greater than in size')
            continue

        # pop into new location on board ('set down')
        board[spot_to_play].append(piece_to_play)

        break  # have valid spot


# --------------------------------------------------


# check_win (accepts: board, player / returns: win (bool), player (string representing player that won)
    # go through rows, columns, diagonals
        # if
    # check for wins
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
    pieces = ['XXX', 'XXX', 'XX ', 'XX ', ' X ', ' X ', 'OOO', 'OOO', 'OO ', 'OO ', ' O ', ' O ']  # extra spaces for display formatting
    board = ['buffer', ['   '], ['   '], ['   '],
                       ['   '], ['   '], ['   '],
                       ['   '], ['   '], ['   ']]  # extra list for index buffer

    # rando chose player for first turn
    player = 'X'  # remove later and use random choice
    display_board(board, pieces)

    while True:
        piece_to_play, piece_spot = pickup_piece_to_play(board, pieces, player)

        display_board(board, pieces)

        play_piece(board, pieces, piece_to_play, piece_spot)

        display_board(board, pieces)

        # check win/tie
        win = False  # fixme: build function for this
        if win:
            pass  # send message & break

        if player == 'X':
            player = 'O'
        else:
            player = 'X'


# --------------------------------------------------


if __name__ == '__main__':
    main()
