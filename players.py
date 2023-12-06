"""Games or Adversarial Search (Chapter 5)"""
# todo : add source credits in comments here & readme


import random
from searches import minmax_decision, alpha_beta_search, alpha_beta_cutoff_search



def random_player(game, state):
    """Returns a random move from all available moves"""
    return random.choice(game.actions(state)) if game.actions(state) else None


def human_player(game, state, verbose=False):
    """Prompts human player for move inputs - checks for valid move"""

    game.display(state)
    if verbose:
        print(f'utility: {state.utility}')
        print(f'to_move: {state.to_move}')

    while True:

        # chose piece
        piece = input(f"Player-{state.to_move}, choose your piece: ")

        # todo? : display board with piece picked-up

        # get spot to play on
        spot = input(f"Player-{state.to_move}, chose spot to play on: ")

        move = (int(piece), int(spot))

        # if valid, return move
        if move in game.actions(state):
            return move
        # if not valid, get new move
        else:
            print("\n** Invalid Move ** Try Again ** \n")
            continue


# note: for reference (REMOVE LATER)
def minmax_player(game, state):
    return minmax_decision(state, game)


# note: for reference (REMOVE LATER)
def alpha_beta_player(game, state):
    return alpha_beta_search(state, game)


def alpha_beta_cutoff_player(game, state):
    return alpha_beta_cutoff_search(state, game)
