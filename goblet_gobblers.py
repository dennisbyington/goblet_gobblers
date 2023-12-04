"""CLI implementation of the Goblet Gobblers board game
Based on the
"""

from collections import namedtuple
from players import random_player

# todo : current : implement state-based code
"""                    
    Step 5 ->   Remove old code 
                Clean up aima code
                Update comments & notes (also indicate that I am in the middle of a refactor and why I am refactoring)
                    -> Moving to state based code to implement a learning algo?
                Update readme to markdown
                Push 
"""
""" 
todo : next : trying to get minmax / a-b / mcst to work 

Issue: Minmax & A-B recurses too deep (exceeds system limits) -> I think this is due to the depth of gg search tree
        
        TODO --> do math on how big gg minmax tree is (just curious)

        TODO NEXT : Option A) Implement heuristic to allow for a-b pruning to cut off at a specified recursion depth (page 173 in aima)
                    Option B) Use MCST - if possible for deterministic games (tried this but was getting errors)
                    Option C) Use a neural net (possibly play against itself to learn?)    
"""
"""
todo : misc/later 

    - play_game_dict() --> implemented   

    - Change to this format for bank later?   [('X', 3), ('X', 3), ('X', 2), ('X', 2), ('X', 1), ('X', 1),
                                             ('O', 3), ('O', 3), ('O', 2), ('O', 2), ('O', 1), ('O', 1)]

    - Change to this format for board later?  [None] * 9                                      
"""


GobletGobblersGameState = namedtuple('GameState', 'to_move, utility, board, bank')


class GobletGobblers:
    """State based implementation of the Goblet Gobblers board game - full description in readme"""

    def __init__(self, h=3, v=3, k=3):
        self.h = h  # height of board
        self.v = v  # width of board
        self.k = k  # k in a row for win
        board = ['buffer', ['   '], ['   '], ['   '],  # extra list for index buffer
                 ['   '], ['   '], ['   '],
                 ['   '], ['   '], ['   ']]
        bank = ['XXX', 'XXX', 'XX ', 'XX ', ' X ', ' X ',  # extra spaces for display formatting
                'OOO', 'OOO', 'OO ', 'OO ', ' O ', ' O ']
        self.initial = GobletGobblersGameState(to_move='X',  # player name to move next
                                               utility=0,  # value to initial player 'X'; 1 for win, -1 for loss, 0 else
                                               board=board,  # empty board
                                               bank=bank)  # initial bank

    def actions(self, state):
        """Return a list of the allowable moves at this point;  moves: [(from_spot, to_spot)]"""

        moves = []

        # get moves from board to board -------------------------------
        for current_spot_index, current_spot in enumerate(state.board):  # loop through board
            curr_piece_to_play = current_spot[-1]
            if current_spot_index == 0 or curr_piece_to_play[
                1] != state.to_move:  # if buffer element, or if top piece not current player's piece, continue
                continue
            size_piece_to_play = curr_piece_to_play.count('X') + curr_piece_to_play.count('O')  # get size of top piece on spot
            # -- can move to any spot on board that has piece smaller than this (except current spot) --
            for to_spot_index, to_spot in enumerate(state.board):  # loop through board
                if to_spot_index == 0 or to_spot_index == current_spot_index:  # if buffer element, or if to_spot is current_spot, continue
                    continue
                piece_on_to_spot = to_spot[-1]  # get piece on top of spot
                size_to_spot = piece_on_to_spot.count('X') + piece_on_to_spot.count('O')  # get size of piece on to_spot
                if size_piece_to_play > size_to_spot:  # if spot able to play on (current piece size > spot piece size)
                    moves.append((current_spot_index, to_spot_index))  # save move (+10 to adjust for display indexing)

        # get moves from bank to board --------------------------------
        for bank_index, piece in enumerate(state.bank):  # loop through bank
            if piece[1] != state.to_move:  # if not current player's piece, continue
                continue
            size_piece_to_play = piece.count('X') + piece.count('O')  # get size of piece
            # -- can move to any spot on board that has a piece smaller than this one --
            for spot_index, spot in enumerate(state.board):  # for all spots on board
                if spot_index == 0:  # skip board buffer spot
                    continue
                curr_on_spot = spot[-1]  # get current piece on top of spot
                size_curr_in_spot = curr_on_spot.count('X') + curr_on_spot.count('O')  # get size of piece on spot
                if size_piece_to_play > size_curr_in_spot:  # if spot able to play on (current piece size > spot piece size)
                    moves.append((bank_index + 10, spot_index))  # save move (+10 to adjust for display indexing)

        return moves

    def result(self, state, move):
        """Return the state that results from making a move from a state."""

        # check valid move & return if not (illegal move has no effect)
        if move not in self.actions(state):
            return state

        # get local variables
        from_spot = move[0]
        to_spot = move[1]
        board = state.board.copy()
        bank = state.bank.copy()

        # set piece_to_play & remove it from board or bank (pickup)
        if from_spot < 10:  # piece on board
            piece_to_play = board[from_spot][-1]
            board[from_spot].pop()
        else:  # piece in bank
            piece_to_play = bank[from_spot - 10]
            bank[from_spot - 10] = '   '

        # pop into new location on board (set down)
        board[to_spot].append(piece_to_play)

        # get next to_move
        to_move = 'X' if state.to_move == 'O' else 'O'

        # get utility (1 if 'X' wins with this move; -1 if 'O' wins; 0 else)
        utility = self.compute_utility(board, state.to_move)

        # build new state
        new_state = GobletGobblersGameState(to_move=to_move,  # player name to move next
                                            utility=utility,  # current board utility
                                            board=board,  # updated board
                                            bank=bank)  # updated bank

        return new_state

    def utility(self, state, player):
        """Return the value to *this* player (could be X or O); 1 for win, -1 for loss, 0 otherwise.

                Given a terminal game state and a player, this method returns the utility for that player in the given terminal game state.
                While implementing this method assume that the game state is a terminal game state.
                The logic in this module is such that this method will be called only on terminal game states."""
        return state.utility if player == 'X' else -state.utility

    def terminal_test(self, state):
        """Return True if this is a final state for the game - A state is terminal if it is won or there are no empty squares."""
        return state.utility != 0

    def to_move(self, state):
        """Return the player whose move it is in this state (who is to play next)
        This information is typically stored in the game state, so all this method does is extract this information and return it."""
        return state.to_move

    def display(self, state):
        """Print or otherwise display the state"""

        # print('\033c', end="")  # clear terminal
        print(f"\n------------------------------------------------------------------------------------")
        print(f'')
        print(f'                                     |         |         ')
        print(f'                               {state.board[1][-1]}   |   {state.board[2][-1]}   |   {state.board[3][-1]}   ')
        print(f'                                   1 |       2 |       3 ')
        print(f'                            -----------------------------')
        print(f'                                     |         |         ')
        print(f'                               {state.board[4][-1]}   |   {state.board[5][-1]}   |   {state.board[6][-1]}   ')
        print(f'                                   4 |       5 |       6 ')
        print(f'                            -----------------------------')
        print(f'                                     |         |         ')
        print(f'                               {state.board[7][-1]}   |   {state.board[8][-1]}   |   {state.board[9][-1]}   ')
        print(f'                                   7 |       8 |       9 ')
        print(f'')
        print(f'Player-X                                       Player-O')
        print(f'-------------------------------------          -------------------------------------')
        print(f'| {state.bank[0]} | {state.bank[1]} | {state.bank[2]} | {state.bank[3]} | {state.bank[4]} | {state.bank[5]} |          '
              f'| {state.bank[6]} | {state.bank[7]} | {state.bank[8]} | {state.bank[9]} | {state.bank[10]} | {state.bank[11]} |')
        print(f'-------------------------------------   Bank   -------------------------------------')
        print(f'| 10  | 11  | 12  | 13  |  14 |  15 |          | 16  | 17  | 18  | 19  |  20 |  21 |')
        print(f'-------------------------------------          -------------------------------------')
        print(f'')

    def compute_utility(self, board, player):
        """If 'X' wins with this move, return 1; if 'O' wins return -1; else return 0.
            args: board (after move), player (who made that move)

        Cycles through each possible winning sequence of the board (rows, columns, diagonals).  If winning
        sequence is found, that player is appended to the winners list.  Winner is determined using the rules
        set in the top docstring.

        Possible outcomes:
            - No winning sequences: play continues
            - One winning sequence: that player wins
            - Two winning sequences
                - Same player x2: that player wins
                - 2 different players: The opposing player has won (see top docstring for rules)
        """

        winners = []

        # check each sequence for winner and append to list if found
        for a, b, c in ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)):
            if (board[a][-1].count('X') > 0) and (board[b][-1].count('X') > 0) and (board[c][-1].count('X') > 0):
                winners.append('X')
            if (board[a][-1].count('O') > 0) and (board[b][-1].count('O') > 0) and (board[c][-1].count('O') > 0):
                winners.append('O')

        # check number of winning sequences found & assign utility
        if len(winners) == 0:  # no winners, return 0
            return 0
        elif len(winners) == 1:  # 1 winner, if X return 1, else (O) return -1
            return 1 if winners[0] == 'X' else -1
        else:  # 2 winning sequences
            if winners[0] == winners[1]:  # if both the same player: if X return 1, else (O) return -1
                return 1 if winners[0] == 'X' else -1
            else:  # if different players, the opposing player has won
                return -1 if player == 'X' else 1

    def play_game(self, *players, verbose=False):
        """Play an n-person, move-alternating game (only used for non-human players)
           Returns utility for initial player
           verbose controls various mid-game & final state display options"""

        state = self.initial                            # get initial state of the game
        while True:                                     # forever loop
            for player in players:                          # for each player in game

                move = player(self, state)                  # get move to make

                if verbose and player == random_player:
                    # if random & verbose, print mid-game state info
                    self.print_verbose(state, 'random_mid_game', move)

                state = self.result(state, move)                # get result of this move

                if self.terminal_test(state):                   # if result is a terminal state
                    self.display(state)                                     # display state
                    if verbose:
                        self.print_verbose(state, 'final_state')
                    return self.utility(state, self.to_move(self.initial))  # return utility(state, initial player) --> 1 if x won, -1 if o won, 0 if tie

    def play_game_dict(self, players_and_strategies: dict, verbose=False):
        # note : (this is from jupyter notebook) : players_and_strategies => {player_name: strategy_function}
        # todo : implement later
        """Play an n-person, move-alternating game."""
        state = self.initial  # get initial state of the game
        while not self.terminal_test(state):  # while not in a terminal state
            player = state.to_move  # get player to move
            move = players_and_strategies[player](self, state)  # get move to make
            state = self.result(state, move)  # get result of this move
            if verbose:
                print(f'Player: {player}, Move: {move}')
                print(state)
        self.display(state)
        return state  # if here, have terminal state; return it

    def print_verbose(self, state, tag, move=None):
        """prints various mid-game & final state information"""

        if tag == 'random_mid_game':
            self.display(state)
            print(f'utility: {state.utility}')
            print(f'to_move: {state.to_move}')
            print(f"move: {move}")
        if tag == 'final_state':
            print(f"final state")
            print(f"-----------")
            print(f'utility: {state.utility}')
            print(f'to_move: {state.to_move}')
            print(f"------------------------------------------------------------------------------------\n")


def test_compute_utility():
    """Test GobletGobblers.compute_utility() function.  See check_win() docstring for full functionality

        ** Tested on 26NOV - PASS ** """

    gg = GobletGobblers()

    assert gg.new_compute_utility([['buffer'], ['   '], ['   '], ['   '],  # blank board: no win
                                   ['   '], ['   '], ['   '],
                                   ['   '], ['   '], ['   ']], 'X') == 0

    assert gg.new_compute_utility([['buffer'], [' X '], ['XX '], ['OOO'],  # random board: no win
                                   [' O '], ['OO '], [' X '],
                                   ['XX '], ['XXX'], ['OOO']], 'X') == 0

    assert gg.new_compute_utility([['buffer'], [' X '], ['XX '], ['XXX'],  # current player -> row #1 winner
                                   [' O '], ['OO '], [' X '],
                                   ['XX '], ['XXX'], ['OOO']], 'X') == 1

    assert gg.new_compute_utility([['buffer'], [' O '], ['XX '], [' O '],  # current player -> row #3 winner
                                   ['OO '], ['OO '], [' X '],
                                   ['XX '], ['XXX'], [' X ']], 'X') == 1

    assert gg.new_compute_utility([['buffer'], [' X '], ['XX '], ['OOO'],  # opposing player -> row #2 winner
                                   [' O '], ['OO '], [' O '],
                                   ['XX '], ['OO '], ['XXX']], 'X') == -1

    assert gg.new_compute_utility([['buffer'], [' X '], ['XX '], ['XXX'],  # current player -> col #1 winner
                                   [' X '], ['OO '], [' O '],
                                   ['XX '], ['XXX'], ['OOO']], 'X') == 1

    assert gg.new_compute_utility([['buffer'], [' O '], ['XX '], ['XXX'],  # current player -> col #3 winner
                                   [' O '], ['OO '], [' X '],
                                   ['XX '], ['OO '], ['XXX']], 'X') == 1

    assert gg.new_compute_utility([['buffer'], [' X '], ['OOO'], ['OOO'],  # opposing player -> col #2 winner
                                   [' O '], ['OO '], [' X '],
                                   ['XX '], ['OO '], ['XXX']], 'X') == -1

    assert gg.new_compute_utility([['buffer'], [' X '], ['OOO'], ['OOO'],  # current player -> diag #1 winner
                                   [' O '], ['XX '], [' X '],
                                   ['XX '], ['OO '], ['XXX']], 'X') == 1

    assert gg.new_compute_utility([['buffer'], [' O '], ['OOO'], ['XXX'],  # current player -> diag #2 winner
                                   [' O '], ['XX '], ['OO '],
                                   ['XX '], ['OO '], ['XXX']], 'X') == 1

    assert gg.new_compute_utility([['buffer'], [' X '], ['XX '], ['XXX'],  # 2 wins: current player -> row #1 & #3 winner
                                   [' O '], ['OO '], [' X '],
                                   ['XX '], ['XX '], ['XXX']], 'X') == 1

    assert gg.new_compute_utility([['buffer'], [' X '], ['XX '], ['OOO'],  # 2 wins: current player -> col #1 & #2 winner
                                   [' X '], ['XX '], [' X '],
                                   ['XX '], ['XX '], ['OOO']], 'X') == 1

    assert gg.new_compute_utility([['buffer'], [' X '], ['OO '], ['XXX'],  # 2 wins: current player -> diag #1 & #2 winner
                                   [' O '], ['XX '], [' O '],
                                   ['XX '], ['OOO'], ['XXX']], 'X') == 1

    assert gg.new_compute_utility([['buffer'], [' X '], ['OO '], ['XXX'],  # 2 col wins: opposing player is winner
                                   [' X '], ['OO '], [' O '],
                                   ['XX '], ['OO '], ['XXX']], 'X') == -1

    assert gg.new_compute_utility([['buffer'], [' X '], ['XX '], ['XXX'],  # 2 row wins: opposing player is winner
                                   [' O '], ['OO '], [' O '],
                                   ['XX '], ['OO '], ['XXX']], 'X') == -1
