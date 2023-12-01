import random


def random_player(game, state):
    """returns a random move from all available moves"""
    return random.choice(game.actions(state)) if game.actions(state) else None


def human_player(game, state):
    """prompts human player for move inputs - checks for valid move"""

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
