# Description

Python implementation of the Goblet Gobblers board game

Goblet Gobblers is a tic-tac-toe style board game where players can 'gobble' their opponents pieces.
Two players (X & O) begin with 6 pieces: 2 large, 2 medium, 2 small.

Players take turns placing pieces on the board. Players may choose a piece not in play or one on the board
already - although it is important to remember what has been 'gobbled' because uncovering an opposing player's
piece makes it active.  Once a piece is picked up it must be played - and it may not be placed back in the spot
from which it was picked up.  Larger pieces may nest on top of smaller pieces only.  Play continues until someone wins.

Note: If moving a piece exposes a winning sequence for the opponent, and if the destination for the move
does not cover up one of the other pieces in the sequence, then the opponent wins - even if the move makes a
winning sequence for the moving player.

A pdf of the board games rules can be found in goblet_gobblers_rules.pdf

Additional rules can be found here: https://docs.racket-lang.org/games/gobblet.html

# Usage

Default play is 2 random players.  

X always goes first.

You may choose to make X or O a human player or a min-max (alpha-beta with heuristic) player.  

The final state is always shown and final state utility is always returned (int).

Human players are shown the game state before each move.  You may add verbose flag to display state information at each move and also show board during random player moves.


    usage: main.py [-h] [-X str] [-O str] [-v]

    options:
      -h, --help     show this help message and exit
      -X str         Player type for X: "random, ""human", or "alpha-beta" (default: random)
      -O str         Player type for X: "random, ""human", or "alpha-beta" (default: random)
      -v, --verbose  Print verbose game information (default: False)



# Data structures

    board: list of lists of strings.  Pieces are appended to list when played and popped from list when picked up.
                                      [-1] of each spot is the piece on 'top'

        board[1][-1] board[2][-1] board[3][-1]          'XXX' 'OOO' 'OO '
        board[4][-1] board[5][-1] board[6][-1]   <==>   'XX ' ' X ' 'XX '
        board[7][-1] board[8][-1] board[9][-1]          ' O ' 'OOO' ' X '


    pieces: list of strings.  Represents the player's pieces.  Items 0-5 are X-pieces; 6-11 are O-pieces.
                              (the extra spaces for display formatting)

        ['XXX', 'XXX', 'XX ', 'XX ', ' X ', ' X ', 'OOO', 'OOO', 'OO ', 'OO ', ' O ', ' O ']


# Dependencies

- Python3
- Imports: argparse, collections, copy, numpy, random


# Help

Help can be obtained by including the [-h] option to the program:

  ./goblet_gobblers.py -h


# Author

Dennis Byington
dennisbyington@mac.com


# Version history & release notes

- 0.3 - Min-max alpha beta (with heuristic) 
    - Incorporated Min-Max Alpha-Beta (with heuristic) search (search parameters not optimized yet)
    - Based on Alpha-Beta-Cutoff search from the textbook "Artificial Intelligence: A Modern Approach"
- 0.2 - State based
    - Refactored to state based implementation in preparation for ML learning algo
    - Based on Game base class from the textbook "Artificial Intelligence: A Modern Approach"
- 0.1 - Initial release


# Bugs

No known bugs.  However, I am seeking inputs and constructive criticism on areas I can improve.


# Future features

- Tune Min-Max alpha-beta heuristic parameters
- Train a neural net to play the game


# License

This software is licensed under the MIT License.  See LICENSE.txt for details.


# Acknowledgments

This is my software recreation of a board game that is produced by Blue Orange Games.
Game created by Thierry Denoual.  Copyright 2002-2009 Blue Orange.

Starter code for players, searches, & base class for GobletGobblers based on the textbook 
Artificial Intelligence: A Modern Approach (http://aima.cs.berkeley.edu/) (https://github.com/aimacode/aima-python/blob/master/README.md)
