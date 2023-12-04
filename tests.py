from goblet_gobblers import *


def test_compute_utility():
    """Test GobletGobblers.compute_utility() function"""

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
