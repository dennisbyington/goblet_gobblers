# ---------------------------------------------------------------------------
# Name of program: 

goblet_gobblers.py


# ---------------------------------------------------------------------------
# Description 

CLI implementation of the Goblet Gobblers board game 

  
# ---------------------------------------------------------------------------
# Game introduction:

Goblet Gobblers is a tic-tac-toe style board game where players can 'gobble' their opponents pieces.
Two players (X & O) begin with 6 pieces: 2 large, 2 medium, 2 small.

Players take turn placing pieces on the board. Players may choose a piece not in play or one on the board
already (although it is important to remember what has been 'gobbled' because uncovering an opposing player's
piece makes it active. Once piece is picked up it must be played. Larger pieces may nest on top of smaller
pieces only.  Play continues until someone wins.

Note: If moving a piece exposes a winning sequence for the opponent, and if the destination for the move
does not cover up one of the other pieces in the sequence, then the opponent wins—even if the move makes a
winning sequence for the moving player.

A pdf of the board games rules can be found in this directory: goblet_gobblers_rules.pdf

Additional rules can be found here: https://docs.racket-lang.org/games/gobblet.html


# ---------------------------------------------------------------------------
Data structures:

    - board: list of lists of strings.  Pieces are appended to list when played and popped from list when picked up.
                                      [-1] of each spot is the piece on 'top'

        board[1][-1] board[2][-1] board[3][-1]          'XXX' 'OOO' 'OO '
        board[4][-1] board[5][-1] board[6][-1]   <==>   'XX ' ' X ' 'XX '
        board[7][-1] board[8][-1] board[9][-1]          ' O ' 'OOO' ' X '


    - pieces: list of strings.  Represents the player's pieces.  Items 0-5 are X-pieces; 6-11 are O-pieces.
                              (the extra spaces for display formatting)

        ['XXX', 'XXX', 'XX ', 'XX ', ' X ', ' X ', 'OOO', 'OOO', 'OO ', 'OO ', ' O ', ' O ']
    

# ---------------------------------------------------------------------------
# Dependencies

- Python3 
- Imports: argparse, random


# ---------------------------------------------------------------------------
# Help
  
Help can be obtained by including the [-h] option to the program:

  ./goblet_gobblers.py -h


# ---------------------------------------------------------------------------
# Author

Dennis Byington
dennisbyington@mac.com


# ---------------------------------------------------------------------------
# Version History

0.1 - Initial release


# ---------------------------------------------------------------------------
# License

This software is licensed under the MIT License.  See license.txt for details.


# ---------------------------------------------------------------------------
# Acknowledgments

This is my sofware recreation of a board game that is produced by Blue Orange Games.  
Game created by Thierry Denoual.  Copyright 2002-2009 Blue Orange.  


