import random


def random_player(game, state):
    """returns a random move from all available moves"""
    return random.choice(game.actions(state)) if game.actions(state) else None
