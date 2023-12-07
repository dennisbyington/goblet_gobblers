from collections import namedtuple
from players import random_player


# game state
GobletGobblersGameState = namedtuple('GameState', 'to_move, utility, board, bank')


class GobletGobblers:
    """State based implementation of the Goblet Gobblers board game - full game description in readme"""

    def __init__(self):
        """Default constructor"""

        # board data struct (extra list in zero-index for index buffer)
        board = ['buffer', ['   '], ['   '], ['   '],
                 ['   '], ['   '], ['   '],
                 ['   '], ['   '], ['   ']]

        # bank data struct (extra spaces for display formatting)
        bank = ['XXX', 'XXX', 'XX ', 'XX ', ' X ', ' X ',
                'OOO', 'OOO', 'OO ', 'OO ', ' O ', ' O ']

        # create initial game state
        self.initial = GobletGobblersGameState(to_move='X',
                                               utility=0,
                                               board=board,
                                               bank=bank)

    def actions(self, state):
        """Return a list of the allowable moves at this point;  moves: [(from_spot, to_spot)]"""

        moves = []

        # ----- get moves from board to board -----
        # loop through board
        for current_spot_index, current_spot in enumerate(state.board):

            # get piece on "top" of this spot
            curr_piece_to_play = current_spot[-1]

            # if buffer element, or if top piece not current player's piece, continue
            if current_spot_index == 0 or curr_piece_to_play[1] != state.to_move:
                continue

            # get size of top piece on spot
            size_piece_to_play = curr_piece_to_play.count('X') + curr_piece_to_play.count('O')

            # -- can move to any spot on board that has piece smaller than this (except current spot) --
            # loop through board
            for to_spot_index, to_spot in enumerate(state.board):

                # if buffer element, or if to_spot is current_spot, continue
                if to_spot_index == 0 or to_spot_index == current_spot_index:
                    continue

                # get piece on top of spot
                piece_on_to_spot = to_spot[-1]

                # get size of piece on to_spot
                size_to_spot = piece_on_to_spot.count('X') + piece_on_to_spot.count('O')

                # if spot able to play on (current piece size > spot piece size) save move
                if size_piece_to_play > size_to_spot:
                    moves.append((current_spot_index, to_spot_index))

        # ----- get moves from bank to board -----
        # loop through bank
        for bank_index, piece in enumerate(state.bank):

            # if not current player's piece, continue
            if piece[1] != state.to_move:
                continue

            # get size of piece
            size_piece_to_play = piece.count('X') + piece.count('O')

            # -- can move to any spot on board that has a piece smaller than this one --
            # loop through board
            for spot_index, spot in enumerate(state.board):

                # skip board buffer spot
                if spot_index == 0:
                    continue

                # get current piece on top of spot
                curr_on_spot = spot[-1]

                # get size of piece on spot
                size_curr_in_spot = curr_on_spot.count('X') + curr_on_spot.count('O')

                # if spot able to play on (current piece size > spot piece size) save move (+10 to adjust for display indexing)
                if size_piece_to_play > size_curr_in_spot:
                    moves.append((bank_index + 10, spot_index))

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

        # set piece_to_play & remove it from board or bank (aka: pickup)
        # piece on board
        if from_spot < 10:
            piece_to_play = board[from_spot][-1]
            board[from_spot].pop()
        # piece in bank
        else:
            piece_to_play = bank[from_spot - 10]
            bank[from_spot - 10] = '   '

        # pop into new location on board (aka: set down)
        board[to_spot].append(piece_to_play)

        # get next to_move
        to_move = 'X' if state.to_move == 'O' else 'O'

        # get utility
        utility = self.compute_utility(board, state.to_move)

        # build new state
        new_state = GobletGobblersGameState(to_move=to_move,
                                            utility=utility,
                                            board=board,
                                            bank=bank)

        return new_state

    def min_max_value(self, state, player):
        """Return the min-max value to *this* player (could be X or O); 1 for win, -1 for loss, 0 otherwise"""
        return state.utility if player == 'X' else -state.utility

    def terminal_test(self, state):
        """Return True if this is a terminal state"""
        return state.utility != 0

    def to_move(self, state):
        """Return the player who is to play next in this state"""
        return state.to_move

    def display(self, state):
        """display the state (board & bank only)"""
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

        # ----- check number of winning sequences found & assign utility -----
        # no winners, return 0
        if len(winners) == 0:
            return 0
        # 1 winner, if X return 1, else return -1
        elif len(winners) == 1:
            return 1 if winners[0] == 'X' else -1
        # 2 winning sequences
        else:
            # if both the same player: if X return 1, else return -1
            if winners[0] == winners[1]:
                return 1 if winners[0] == 'X' else -1
            # if different players, the opposing player has won
            else:
                return -1 if player == 'X' else 1

    def play_game(self, *players, verbose=False):
        """Play an n-person, move-alternating game.  Returns final state utility"""

        # get initial state of the game
        state = self.initial

        while True:
            # for each player in game
            for player in players:

                # get move to make
                move = player(self, state)

                if verbose and player == random_player:
                    self.print_verbose(state, 'random_mid_game', move)

                # get result of this move
                state = self.result(state, move)

                # if result is a terminal state display state & return utility
                if self.terminal_test(state):
                    self.display(state)
                    if verbose:
                        self.print_verbose(state, 'final_state')
                    return state.utility

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

    def heuristic(self, state, player):
        """
        state: game state we need a heuristic for
        player: player that made move that got us into "state"
                we want the heuristic for player (this is not state.to_move because "state" is after player has made their move)

        High positive values indicate favorable positions for "player", while low or negative values indicate unfavorable positions

        calculate normally: + if player has good positions
                            - if player has bad positions
                            return as is (do not negate or modify)

        Overall heuristic concept:
            1) Board Control and Piece Hierarchy
                - Assign values to each (top) piece based on size (Larger pieces have higher values)
                    - Add points for our piece on top, subtract for opponent's piece on top
                    - Extra points if we have gobbled an opponent's smaller piece

            2) Piece Mobility
                - Player pieces with more moves available get a higher score (more moves available = higher score)
                - Opponent pieces with more moves available get a lower score (more moves available = lower score)

            3) Threats and Opportunities
                - Add significant points for moves that lead to a win
                - Subtract significant points for moves that lead to a loss

        Need to experiment with points:
            piece size points:                      2x size  (maybe could use --> 1:1   2:3   3:5)
            points for covering opponent's piece:   2
            points available for each move:         +1 for player, -1 for opponent
            moves leading to win:                   100
            moves leading to loss:                 -100
        """

        def player_on_top(spot, player):
            return 2 * spot[-1].count(player)

        def opponent_on_top(spot, opponent):
            return -2 * spot[-1].count(opponent)

        def covering_opponents_piece(spot, player, opponent):
            # 1 piece or less on spot
            if len(spot) < 2:
                return 0
            # player on top, opponent below
            elif spot[-1].count(player) > 0 and spot[-2].count(opponent) > 0:
                return 2
            # all others
            else:
                return 0


        score = 0

        # Board Control and Piece Hierarchy -----
        for spot in state.board:
            # add points if we have top piece (points = 2 * piece size)
            score += player_on_top(spot, player)
            # additional points for covering opponent's piece (2 points)
            score += covering_opponents_piece(spot, player, state.to_move)
            # # subtract points if opponent has top piece (points = -2 * piece size)
            score += opponent_on_top(spot, state.to_move)
        print(f"board control: : {score}")


        # Piece Mobility -----
        # add points for each move player has available
        score += len(self.actions(GobletGobblersGameState(player, 0, state.board, state.bank)))  # using temp state because current state has opponent as to_move, so game.actions returns moves for opponent
        print(f"player available move: {len(self.actions(GobletGobblersGameState(player, 0, state.board, state.bank)))}")
        # subtract points for each move opponent has available
        score -= len(self.actions(state))
        print(f"opponent available move: -{len(self.actions(state))}")


        # # Threats and Opportunities -----
        # wins score large positive, losses score large negative
        score += 100 * self.min_max_value(state, player)     # min_max_value = 1 if player has won; -1 if opponent has won
        print(f"min_max_val: {100 * self.min_max_value(state, player)}")


        print(f"final score: {score}")


        return score
