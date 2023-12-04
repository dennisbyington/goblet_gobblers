#!/usr/bin/env python3

import random
import copy
from args import *
from players import *
from goblet_gobblers import *


# todo : implement state-based goblet gobblers (check notes in goblet_gobblers.py)

def main():
    """Main function

    Initializes game variables and enters a forever loop where the game logic is located.  Stays here until
    a winner is found.

    pseudocode:
    -----------
    - Initialize game variables
    - Randomly choose first player
    - Game logic:
        - Player chooses piece
        - Player chooses spot to play on
        - Board is checked for a win
            - If no winner, play continues with next player
    """

    # new code (state based)
    # ------------------------------------
    args = get_args()               # get args
    random.seed(0)                  # seed random module

    gg = GobletGobblers()                               # create game instance
    gg.play_game(args.X, args.O, verbose=args.verbose)  # start game


    # # old code (non state based)
    # # ------------------------------------
    # # initial game variables
    # pieces = ['XXX', 'XXX', 'XX ', 'XX ', ' X ', ' X ',  # extra spaces for display formatting
    #           'OOO', 'OOO', 'OO ', 'OO ', ' O ', ' O ']
    # board = ['buffer', ['   '], ['   '], ['   '],
    #                    ['   '], ['   '], ['   '],
    #                    ['   '], ['   '], ['   ']]  # extra list for index buffer
    # player = random.choice('XO')  # rando chose player for first turn
    #
    # display_board(board, pieces)
    #
    # while True:
    #     piece_to_play, piece_spot = pickup_piece_to_play(board, pieces, player)
    #
    #     display_board(board, pieces)
    #
    #     play_piece(board, pieces, piece_to_play, piece_spot)
    #
    #     display_board(board, pieces)
    #
    #     # check win/tie
    #     win, winner = check_win(board, player)
    #     if win:
    #         print(f'Player-{winner} is the winner!')  # send message & break
    #         break
    #     else:  # change players and goto next turn
    #         if player == 'X':
    #             player = 'O'
    #         else:
    #             player = 'X'


# ------------------------
if __name__ == '__main__':
    main()
