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

    Board data structure:
    ---------------------
    board[1][-1] board[2][-1] board[3][-1]          'XXX' 'OOO' 'OO '
    board[4][-1] board[5][-1] board[6][-1]   <==>   'XX ' ' X ' 'XX '
    board[7][-1] board[8][-1] board[9][-1]          ' O ' 'OOO' ' X '

** check here for additional/clarified rules: https://docs.racket-lang.org/games/gobblet.html
------------------------------------------------------------------------------------------

current TODO: check win

later:
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


def check_win(board, player):
    """Checks the current board for winning sequences

    Cycles through each possible winning sequence of the board (rows, columns, diagonals).  If winning
    sequence is found, that player is appended to the winners list.  Winner is determined using the rules
    set in the top docstring.

    Possible outcomes:
        - No winning sequences: play continues
        - One winning sequence: that player wins
        - Two winning sequences
            - Same player x2: that player wins
            - 2 different players: The opposing player has won (see below)

                If moving a piece exposes a winning sequence for the opponent,
                and if the destination for the move does not cover up one of
                the other pieces in the sequence, then the opponent wins—even
                if the move makes a winning sequence for the moving player.

    Board data structure:
    ---------------------
    board[1][-1] board[2][-1] board[3][-1]          'XXX' 'OOO' 'OO '
    board[4][-1] board[5][-1] board[6][-1]   <==>   'XX ' ' X ' 'XX '
    board[7][-1] board[8][-1] board[9][-1]          ' O ' 'OOO' ' X '

    Args:
        board:
            current playing board
        player:
            current player

    Returns:
        win:
            bool that indicates if a winning sequence has been found
        winner
            string that represents the winner (or '' if no winner)
        """

    winner = ''
    win = False
    winners = []

    # check each sequence for winner and append to list if found
    for a, b, c in ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)):
        if (board[a][-1].count('X') > 0) and (board[b][-1].count('X') > 0) and (board[c][-1].count('X') > 0):
            winners.append('X')
        if (board[a][-1].count('O') > 0) and (board[b][-1].count('O') > 0) and (board[c][-1].count('O') > 0):
            winners.append('O')

    # check number of winning sequences found
    if len(winners) == 0:  # no winners, return default values
        return win, winner
    elif len(winners) == 1:  # 1 winner, return that player
        win = True
        winner = winners[0]
        return win, winner
    else:  # 2 winning sequences
        # if both the same player: return that player as winner
        if winners[0] == winners[1]:
            win = True
            winner = winners[0]  # get winner from winning_sequence
            return win, winner
        # if different players, the opposing player has won
        else:
            win = True
            # get opposing player
            if player == 'X':
                winner = 'O'
            else:
                winner = 'X'
            return win, winner


# --------------------------------------------------


def test_check_win():
    """Test check_win() function

    See check_win() docstring for full functionality
    """

    assert check_win([['buffer'], ['   '], ['   '], ['   '],    # blank board: no win
                                  ['   '], ['   '], ['   '],
                                  ['   '], ['   '], ['   ']], 'X') == (False, '')

    assert check_win([['buffer'], [' X '], ['XX '], ['OOO'],    # random board: no win
                                  [' O '], ['OO '], [' X '],
                                  ['XX '], ['XXX'], ['OOO']], 'X') == (False, '')

    assert check_win([['buffer'], [' X '], ['XX '], ['XXX'],    # current player -> row #1 winner
                                  [' O '], ['OO '], [' X '],
                                  ['XX '], ['XXX'], ['OOO']], 'X') == (True, 'X')

    assert check_win([['buffer'], [' O '], ['XX '], [' O '],    # current player -> row #3 winner
                                  ['OO '], ['OO '], [' X '],
                                  ['XX '], ['XXX'], [' X ']], 'X') == (True, 'X')

    assert check_win([['buffer'], [' X '], ['XX '], ['OOO'],    # opposing player -> row #2 winner
                                  [' O '], ['OO '], [' O '],
                                  ['XX '], ['OO '], ['XXX']], 'X') == (True, 'O')

    assert check_win([['buffer'], [' X '], ['XX '], ['XXX'],    # current player -> col #1 winner
                                  [' X '], ['OO '], [' O '],
                                  ['XX '], ['XXX'], ['OOO']], 'X') == (True, 'X')

    assert check_win([['buffer'], [' O '], ['XX '], ['XXX'],    # current player -> col #3 winner
                                  [' O '], ['OO '], [' X '],
                                  ['XX '], ['OO '], ['XXX']], 'X') == (True, 'X')

    assert check_win([['buffer'], [' X '], ['OOO'], ['OOO'],    # opposing player -> col #2 winner
                                  [' O '], ['OO '], [' X '],
                                  ['XX '], ['OO '], ['XXX']], 'X') == (True, 'O')

    assert check_win([['buffer'], [' X '], ['OOO'], ['OOO'],    # current player -> diag #1 winner
                                  [' O '], ['XX '], [' X '],
                                  ['XX '], ['OO '], ['XXX']], 'X') == (True, 'X')

    assert check_win([['buffer'], [' O '], ['OOO'], ['XXX'],    # current player -> diag #2 winner
                                  [' O '], ['XX '], ['OO '],
                                  ['XX '], ['OO '], ['XXX']], 'X') == (True, 'X')

    assert check_win([['buffer'], [' X '], ['XX '], ['XXX'],    # 2 wins: current player -> row #1 & #3 winner
                                  [' O '], ['OO '], [' X '],
                                  ['XX '], ['XX '], ['XXX']], 'X') == (True, 'X')

    assert check_win([['buffer'], [' X '], ['XX '], ['OOO'],    # 2 wins: current player -> col #1 & #2 winner
                                  [' X '], ['XX '], [' X '],
                                  ['XX '], ['XX '], ['OOO']], 'X') == (True, 'X')

    assert check_win([['buffer'], [' X '], ['OO '], ['XXX'],    # 2 wins: current player -> diag #1 & #2 winner
                                  [' O '], ['XX '], [' O '],
                                  ['XX '], ['OOO'], ['XXX']], 'X') == (True, 'X')

    assert check_win([['buffer'], [' X '], ['OO '], ['XXX'],    # 2 col wins: opposing player is winner
                                  [' X '], ['OO '], [' O '],
                                  ['XX '], ['OO '], ['XXX']], 'X') == (True, 'O')

    assert check_win([['buffer'], [' X '], ['XX '], ['XXX'],  # 2 row wins: opposing player is winner
                                  [' O '], ['OO '], [' O '],
                                  ['XX '], ['OO '], ['XXX']], 'X') == (True, 'O')


# --------------------------------------------------


def main():
    """Short description

    Long description

    Args:
        Arg:
            description

    Returns:
        return:
            description
    """

    args = get_args()  # only used for -h flag

    # init pieces, and board
    pieces = ['XXX', 'XXX', 'XX ', 'XX ', ' X ', ' X ',  # extra spaces for display formatting
              'OOO', 'OOO', 'OO ', 'OO ', ' O ', ' O ']
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
        win, winner = check_win(board, player)
        if win:
            print(f'Player-{winner} is the winner!')  # send message & break
            break
        else:  # change players and goto next turn
            if player == 'X':
                player = 'O'
            else:
                player = 'X'


# --------------------------------------------------


if __name__ == '__main__':
    main()
