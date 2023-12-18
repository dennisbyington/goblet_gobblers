from goblet_gobblers import *


def test_heuristic():
    """ Test GobletGobblers.heuristic(state, player) function

    state: game state we need a heuristic for

    player: player that made move that got us into "state"
                we want the heuristic for player (this is not state.to_move because "state" is after player has made their move)


    scenario    3   4   5   6   7   8
    ----------------------------------
    utility     0   0   1  -1   1  -1
    to move     X   O   O   X   X   O
    player      O   X   X   O   O   X
    """

    gg = GobletGobblers()


    """
    1: empty board / X to move / O is player
    board           empty
    bank            initial
    utility         0
    to move         X
    player          O
    
    board control
        + player pieces on top (2x size each) ...  +0 
        + covering opponent (2 each) ............  +0
        - opp pieces on top (-2x size each) .....  -0
        
    Mobility
        + player moves available (1 each) ....... +54      
        - opp moves available (-1 each) ......... -54
        
    Win/lose
        + player win (100) ....................... +0
        - player loss (-100) ..................... -0
        
    Total ........................................  0
    """
    test_state_01 = GobletGobblersGameState(to_move='X',
                                            utility=0,
                                            board=['buffer', ['   '], ['   '], ['   '],
                                                             ['   '], ['   '], ['   '],
                                                             ['   '], ['   '], ['   ']],
                                            bank=['XXX', 'XXX', 'XX ', 'XX ', ' X ', ' X ',
                                                  'OOO', 'OOO', 'OO ', 'OO ', ' O ', ' O '])

    test_01 = gg.heuristic(test_state_01, 'O')
    assert test_01 == 0  # PASS


    """
    2: empty board / O to move / X is player
    board           empty
    bank            initial
    utility         0
    to move         O
    player          X
    
    board control
        + player pieces on top (2x size each) ...  +0 
        + covering opponent (2 each) ............  +0
        - opp pieces on top (-2x size each) .....  -0
        
    Mobility
        + player moves available (1 each) ....... +54      
        - opp moves available (-1 each) ......... -54
        
    Win/lose
        + player win (100) ......................  +0
        - player loss (-100) ....................  -0
        
    Total ........................................  0
    """
    test_state_02 = GobletGobblersGameState(to_move='O',
                                            utility=0,
                                            board=['buffer', ['   '], ['   '], ['   '],
                                                             ['   '], ['   '], ['   '],
                                                             ['   '], ['   '], ['   ']],
                                            bank=['XXX', 'XXX', 'XX ', 'XX ', ' X ', ' X ',
                                                  'OOO', 'OOO', 'OO ', 'OO ', ' O ', ' O '])

    test_02 = gg.heuristic(test_state_02, 'X')
    assert test_02 == 0  # PASS


    """
    3: mid-game board & bank (same as test 04) / X to move / O is player
    
    ------------------------------------------------------------------------------------

                                         |         |         
                                   XXX   |   OOO   |   XXX   
                                       1 |       2 |       3 
                                -----------------------------
                                         |         |         
                                    O    |   OOO   |    X    
                                       4 |       5 |       6 
                                -----------------------------
                                         |         |         
                                         |   XX    |         
                                       7 |       8 |       9 
    
    Player-X                                       Player-O
    -------------------------------------          -------------------------------------
    |     |     |     |     |     |  X  |          |     |     |     | OO  |     |  O  |
    -------------------------------------   Bank   -------------------------------------
    | 10  | 11  | 12  | 13  |  14 |  15 |          | 16  | 17  | 18  | 19  |  20 |  21 |
    -------------------------------------          -------------------------------------    
     
     
    board           ['buffer', ['   ', 'XXX'],        ['   ', 'OOO'], ['   ', 'OO ', 'XXX'], 
                               ['   ', ' O '], ['   ', 'XX ', 'OOO'],               ['   '], 
                                      ['   '],        ['   ', 'XX '],               ['   ']]
    bank            ['   ', '   ', '   ', '   ', ' X ', ' X ', 
                     '   ', '   ', '   ', 'OO ', '   ', ' O '] 
    utility         0
    to move         X
    player          O
    
    board control
        + player pieces on top (2x size each) ... +14 
        + covering opponent (2 each) ............  +2
        - opp pieces on top (-2x size each) ..... -18
        
    Mobility
        + player moves available (1 each) ....... +18    
        - opp moves available (-1 each) ......... -18
        
    Win/lose
        + player win (100) ....................... +0
        - player loss (-100) ..................... -0
        
    Total ........................................ -2
    """
    test_state_03 = GobletGobblersGameState(to_move='X',
                                            utility=0,
                                            board=['buffer', ['   ', 'XXX'],        ['   ', 'OOO'], ['   ', 'OO ', 'XXX'],
                                                             ['   ', ' O '], ['   ', 'XX ', 'OOO'],               [' X '],
                                                                    ['   '],        ['   ', 'XX '],               ['   ']],
                                            bank=['   ', '   ', '   ', '   ', '   ', ' X ',
                                                  '   ', '   ', '   ', 'OO ', '   ', ' O '])

    test_03 = gg.heuristic(test_state_03, 'O')
    assert test_03 == -2  # PASS


    """
    4: mid-game board & bank (same as test 03) / O to move / X is player 
    
    ------------------------------------------------------------------------------------

                                         |         |         
                                   XXX   |   OOO   |   XXX   
                                       1 |       2 |       3 
                                -----------------------------
                                         |         |         
                                    O    |   OOO   |    X    
                                       4 |       5 |       6 
                                -----------------------------
                                         |         |         
                                         |   XX    |         
                                       7 |       8 |       9 
    
    Player-X                                       Player-O
    -------------------------------------          -------------------------------------
    |     |     |     |     |     |  X  |          |     |     |     | OO  |     |  O  |
    -------------------------------------   Bank   -------------------------------------
    | 10  | 11  | 12  | 13  |  14 |  15 |          | 16  | 17  | 18  | 19  |  20 |  21 |
    -------------------------------------          -------------------------------------    
    
    
    board           ['buffer', ['   ', 'XXX'],        ['   ', 'OOO'], ['   ', 'OO ', 'XXX'], 
                               ['   ', ' O '], ['   ', 'XX ', 'OOO'],               ['   '], 
                                      ['   '],        ['   ', 'XX '],               ['   ']]
    bank            ['   ', '   ', '   ', '   ', ' X ', ' X ', 
                     '   ', '   ', '   ', 'OO ', '   ', ' O '] 
    utility         0
    to move         O
    player          X

    board control
        + player pieces on top (2x size each) ... +18 
        + covering opponent (2 each) ............  +2
        - opp pieces on top (-2x size each) ..... -14
        
    Mobility
        + player moves available (1 each) ....... +18    
        - opp moves available (-1 each) ......... -18
        
    Win/lose
        + player win (100) ....................... +0
        - player loss (-100) ..................... -0
        
    Total ........................................  6
    """
    test_state_04 = GobletGobblersGameState(to_move='O',
                                            utility=0,
                                            board=['buffer', ['   ', 'XXX'],        ['   ', 'OOO'], ['   ', 'OO ', 'XXX'],
                                                             ['   ', ' O '], ['   ', 'XX ', 'OOO'],               [' X '],
                                                                    ['   '],        ['   ', 'XX '],               ['   ']],
                                            bank=['   ', '   ', '   ', '   ', '   ', ' X ',
                                                  '   ', '   ', '   ', 'OO ', '   ', ' O '])

    test_04 = gg.heuristic(test_state_04, 'X')
    assert test_04 == 6  # PASS


    """
    5: Final state (regular win) / X is winner / O to move / X is player
    
    ------------------------------------------------------------------------------------

                                         |         |         
                                         |         |   OOO   
                                       1 |       2 |       3 
                                -----------------------------
                                         |         |         
                                   OO    |   OOO   |         
                                       4 |       5 |       6 
                                -----------------------------
                                         |         |         
                                   XXX   |   XX    |   XXX   
                                       7 |       8 |       9 
    
    Player-X                                       Player-O
    -------------------------------------          -------------------------------------
    |     |     |     |     |  X  |  X  |          |     |     |     | OO  |     |  O  |
    -------------------------------------   Bank   -------------------------------------
    | 10  | 11  | 12  | 13  |  14 |  15 |          | 16  | 17  | 18  | 19  |  20 |  21 |
    -------------------------------------          -------------------------------------
    
    
    board           ['buffer',        ['   '],               ['   '],        ['   ', 'OOO'], 
                               ['   ', 'OO '], ['   ', 'XX ', 'OOO'],               ['   '], 
                               ['   ', 'XXX'],        ['   ', 'XX '], ['   ', ' O ', 'XXX']]
    bank            ['   ', '   ', '   ', '   ', ' X ', ' X ', 
                    '   ', '   ', '   ', 'OO ', '   ', ' O ']
    utility         1
    to move         O
    player          X
    
    board control
        + player pieces on top (2x size each) ... +16 
        + covering opponent (2 each) ............  +2
        - opp pieces on top (-2x size each) ..... -16
        
    Mobility
        + player moves available (1 each) ....... +19    
        - opp moves available (-1 each) ......... -19
        
    Win/lose
        + player win (100) ...................... +100
        - player loss (-100) ....................   -0
        
    Total ........................................ 102  
    """
    test_state_05 = GobletGobblersGameState(to_move='O',
                                            utility=1,
                                            board=['buffer',        ['   '],               ['   '],        ['   ', 'OOO'],
                                                             ['   ', 'OO '], ['   ', 'XX ', 'OOO'],               ['   '],
                                                             ['   ', 'XXX'],        ['   ', 'XX '], ['   ', ' O ', 'XXX']],
                                            bank=['   ', '   ', '   ', '   ', ' X ', ' X ',
                                                  '   ', '   ', '   ', 'OO ', '   ', ' O '])

    test_05 = gg.heuristic(test_state_05, 'X')
    assert test_05 == 102  # PASS


    """
    6: Final state (regular win) / O is winner / X to move / O is player
    
    ------------------------------------------------------------------------------------
                                         |         |         
                                   OOO   |   XXX   |         
                                       1 |       2 |       3 
                                -----------------------------
                                         |         |         
                                   OO    |   OOO   |         
                                       4 |       5 |       6 
                                -----------------------------
                                         |         |         
                                    O    |         |   XXX   
                                       7 |       8 |       9 
    
    Player-X                                       Player-O
    -------------------------------------          -------------------------------------
    |     |     |     |     |  X  |  X  |          |     |     |     |     |     |  O  |
    -------------------------------------   Bank   -------------------------------------
    | 10  | 11  | 12  | 13  |  14 |  15 |          | 16  | 17  | 18  | 19  |  20 |  21 |
    -------------------------------------          -------------------------------------
    
    
    board           ['buffer', ['   ', 'XX ', 'OOO'], ['   ', 'OO ', 'XXX'],        ['   '], 
                                      ['   ', 'OO '], ['   ', 'XX ', 'OOO'],        ['   '], 
                                      ['   ', ' O '],               ['   '], ['   ', 'XXX']]
    bank            ['   ', '   ', '   ', '   ', ' X ', ' X ', 
                     '   ', '   ', '   ', '   ', '   ', ' O ']    
    utility        -1
    to move         X
    player          O
    
    board control
        + player pieces on top (2x size each) ... +18 
        + covering opponent (2 each) ............  +4
        - opp pieces on top (-2x size each) ..... -12
        
    Mobility
        + player moves available (1 each) ....... +20    
        - opp moves available (-1 each) ......... -16
        
    Win/lose
        + player win (100) ....................... +100
        - player loss (-100) .....................   -0
        
    Total ........................................  114 
    """

    test_state_06 = GobletGobblersGameState(to_move='X',
                                            utility=-1,
                                            board=['buffer', ['   ', 'XX ', 'OOO'], ['   ', 'OO ', 'XXX'],        ['   '],
                                                                    ['   ', 'OO '], ['   ', 'XX ', 'OOO'],        ['   '],
                                                                    ['   ', ' O '],               ['   '], ['   ', 'XXX']],
                                            bank=['   ', '   ', '   ', '   ', ' X ', ' X ',
                                                  '   ', '   ', '   ', '   ', '   ', ' O '])

    test_06 = gg.heuristic(test_state_06, 'O')
    assert test_06 == 114  # PASS


    """
    7: Final state (irregular win) / X is winner / X to move / O is player
    
     ------------------------------------------------------------------------------------

                                         |         |         
                                   XXX   |         |   OOO   
                                       1 |       2 |       3 
                                -----------------------------
                                         |         |         
                                   XX    |   OOO   |   XXX   
                                       4 |       5 |       6 
                                -----------------------------
                                         |         |         
                                    X    |    O    |   XX    
                                       7 |       8 |       9 
    
    Player-X                                       Player-O
    -------------------------------------          -------------------------------------
    |     |     |     |     |  X  |     |          |     |     |     | OO  |     |  O  |
    -------------------------------------   Bank   -------------------------------------
    | 10  | 11  | 12  | 13  |  14 |  15 |          | 16  | 17  | 18  | 19  |  20 |  21 |
    -------------------------------------          -------------------------------------
    
    
    board:          ['buffer', ['   ', 'XXX'],        ['   '],        ['   ', 'OOO'], 
                               ['   ', 'XX '], ['   ', 'OOO'], ['   ', 'OO ', 'XXX'], 
                               ['   ', ' X '], ['   ', ' O '],        ['   ', 'XX ']]
    bank:           ['   ', '   ', '   ', '   ', ' X ', '   ', 
                     '   ', '   ', '   ', 'OO ', '   ', ' O ']  
    utility         1
    to move         X
    player          O
    
    board control
        + player pieces on top (2x size each) ...   +14 
        + covering opponent (2 each) ............    +0
        - opp pieces on top (-2x size each) .....   -22
        
    Mobility
        + player moves available (1 each) .......   +15    
        - opp moves available (-1 each) .........   -18
        
    Win/lose
        + player win (100) .......................   +0
        - player loss (-100) ..................... -100
        
    Total ........................................ -111  
    """
    test_state_07 = GobletGobblersGameState(to_move='X',
                                            utility=1,
                                            board=['buffer', ['   ', 'XXX'],        ['   '],        ['   ', 'OOO'],
                                                             ['   ', 'XX '], ['   ', 'OOO'], ['   ', 'OO ', 'XXX'],
                                                             ['   ', ' X '], ['   ', ' O '],        ['   ', 'XX ']],
                                            bank=['   ', '   ', '   ', '   ', ' X ', '   ',
                                                  '   ', '   ', '   ', 'OO ', '   ', ' O '])

    test_07 = gg.heuristic(test_state_07, 'O')
    assert test_07 == -111  # PASS


    """
    8: Final state (irregular win) / O is winner / O to move / X is player
    
    ------------------------------------------------------------------------------------

                                         |         |         
                                   OOO   |         |   XXX   
                                       1 |       2 |       3 
                                -----------------------------
                                         |         |         
                                   OO    |   XX    |   OO    
                                       4 |       5 |       6 
                                -----------------------------
                                         |         |         
                                   OOO   |   XXX   |   XX    
                                       7 |       8 |       9 
    
    Player-X                                       Player-O
    -------------------------------------          -------------------------------------
    |     |     |     |     |  X  |     |          |     |     |     |     |     |  O  |
    -------------------------------------   Bank   -------------------------------------
    | 10  | 11  | 12  | 13  |  14 |  15 |          | 16  | 17  | 18  | 19  |  20 |  21 |
    -------------------------------------          -------------------------------------
    
    
    board:          ['buffer', ['   ', ' X ', 'OOO'],               ['   '], ['   ', 'XXX'], 
                                      ['   ', 'OO '],        ['   ', 'XX '], ['   ', 'OO '], 
                                      ['   ', 'OOO'], ['   ', ' O ', 'XXX'], ['   ', 'XX ']]
    bank:           ['   ', '   ', '   ', '   ', ' X ', '   ', 
                     '   ', '   ', '   ', '   ', '   ', ' O ']
    utility        -1
    to move         O
    player          X

    board control
        + player pieces on top (2x size each) ...  +20 
        + covering opponent (2 each) ............   +2
        - opp pieces on top (-2x size each) .....  -20
        
    Mobility
        + player moves available (1 each) .......  +13    
        - opp moves available (-1 each) .........  -13
        
    Win/lose
        + player win (100) .......................   +0
        - player loss (-100) ..................... -100
        
    Total ........................................  -98 
    """
    test_state_08 = GobletGobblersGameState(to_move='O',
                                            utility=-1,
                                            board=['buffer', ['   ', ' X ', 'OOO'],               ['   '], ['   ', 'XXX'],
                                                                    ['   ', 'OO '],        ['   ', 'XX '], ['   ', 'OO '],
                                                                    ['   ', 'OOO'], ['   ', ' O ', 'XXX'], ['   ', 'XX ']],
                                            bank=['   ', '   ', '   ', '   ', ' X ', '   ',
                                                  '   ', '   ', '   ', '   ', '   ', ' O '])

    test_08 = gg.heuristic(test_state_08, 'X')
    assert test_08 == -98  # TBD


def test_compute_utility():
    """Test GobletGobblers.compute_utility() function"""

    gg = GobletGobblers()

    assert gg.compute_utility([['buffer'], ['   '], ['   '], ['   '],  # blank board: no win
                                               ['   '], ['   '], ['   '],
                                               ['   '], ['   '], ['   ']], 'X') == 0

    assert gg.compute_utility([['buffer'], [' X '], ['XX '], ['OOO'],  # random board: no win
                                               [' O '], ['OO '], [' X '],
                                               ['XX '], ['XXX'], ['OOO']], 'X') == 0

    assert gg.compute_utility([['buffer'], [' X '], ['XX '], ['XXX'],  # current player -> row #1 winner
                                               [' O '], ['OO '], [' X '],
                                               ['XX '], ['XXX'], ['OOO']], 'X') == 1

    assert gg.compute_utility([['buffer'], [' O '], ['XX '], [' O '],  # current player -> row #3 winner
                                               ['OO '], ['OO '], [' X '],
                                               ['XX '], ['XXX'], [' X ']], 'X') == 1

    assert gg.compute_utility([['buffer'], [' X '], ['XX '], ['OOO'],  # opposing player -> row #2 winner
                                               [' O '], ['OO '], [' O '],
                                               ['XX '], ['OO '], ['XXX']], 'X') == -1

    assert gg.compute_utility([['buffer'], [' X '], ['XX '], ['XXX'],  # current player -> col #1 winner
                                               [' X '], ['OO '], [' O '],
                                               ['XX '], ['XXX'], ['OOO']], 'X') == 1

    assert gg.compute_utility([['buffer'], [' O '], ['XX '], ['XXX'],  # current player -> col #3 winner
                                               [' O '], ['OO '], [' X '],
                                               ['XX '], ['OO '], ['XXX']], 'X') == 1

    assert gg.compute_utility([['buffer'], [' X '], ['OOO'], ['OOO'],  # opposing player -> col #2 winner
                                               [' O '], ['OO '], [' X '],
                                               ['XX '], ['OO '], ['XXX']], 'X') == -1

    assert gg.compute_utility([['buffer'], [' X '], ['OOO'], ['OOO'],  # current player -> diag #1 winner
                                               [' O '], ['XX '], [' X '],
                                               ['XX '], ['OO '], ['XXX']], 'X') == 1

    assert gg.compute_utility([['buffer'], [' O '], ['OOO'], ['XXX'],  # current player -> diag #2 winner
                                               [' O '], ['XX '], ['OO '],
                                               ['XX '], ['OO '], ['XXX']], 'X') == 1

    assert gg.compute_utility([['buffer'], [' X '], ['XX '], ['XXX'],  # 2 wins: current player -> row #1 & #3 winner
                                               [' O '], ['OO '], [' X '],
                                               ['XX '], ['XX '], ['XXX']], 'X') == 1

    assert gg.compute_utility([['buffer'], [' X '], ['XX '], ['OOO'],  # 2 wins: current player -> col #1 & #2 winner
                                               [' X '], ['XX '], [' X '],
                                               ['XX '], ['XX '], ['OOO']], 'X') == 1

    assert gg.compute_utility([['buffer'], [' X '], ['OO '], ['XXX'],  # 2 wins: current player -> diag #1 & #2 winner
                                               [' O '], ['XX '], [' O '],
                                               ['XX '], ['OOO'], ['XXX']], 'X') == 1

    assert gg.compute_utility([['buffer'], [' X '], ['OO '], ['XXX'],  # 2 col wins: opposing player is winner
                                               [' X '], ['OO '], [' O '],
                                               ['XX '], ['OO '], ['XXX']], 'X') == -1

    assert gg.compute_utility([['buffer'], [' X '], ['XX '], ['XXX'],  # 2 row wins: opposing player is winner
                                               [' O '], ['OO '], [' O '],
                                               ['XX '], ['OO '], ['XXX']], 'X') == -1


def test_vector_encoding():

    gg = GobletGobblers()

    # Test 1: Empty board, initial bank, X to move - PASS
    test_state_1 = GobletGobblersGameState(to_move='X',
                                           utility=0,
                                           board=['buffer', ['   '], ['   '], ['   '], ['   '], ['   '], ['   '], ['   '], ['   '], ['   ']],
                                           bank=['XXX', 'XXX', 'XX ', 'XX ', ' X ', ' X ', 'OOO', 'OOO', 'OO ', 'OO ', ' O ', ' O '])
    test_vector_1 = gg.vector_encoding(test_state_1)
    expected_vector_1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 2, 2, 1, 1, 6, 6, 5, 5, 4, 4, 0]
    assert test_vector_1 == expected_vector_1


    # Test 2: Board with a Single Piece, Partial Bank, X to Move - PASS
    test_state_2 = GobletGobblersGameState(to_move='X',
                                           utility=0,
                                           board=['buffer', ['   ', ' X '], ['   '], ['   '], ['   '], ['   '], ['   '], ['   '], ['   '], ['   ']],
                                           bank=['XXX', 'XXX', 'XX ', 'XX ', ' X ', '   ', 'OOO', 'OOO', 'OO ', 'OO ', ' O ', ' O '])

    expected_vector_2 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 2, 2, 1, 0, 6, 6, 5, 5, 4, 4, 0]
    test_vector_2 = gg.vector_encoding(test_state_2)
    assert test_vector_2 == expected_vector_2


    # Test 3: Mid-Game Complex Board, Partial Bank, O to Move - PASS
    test_state_3 = GobletGobblersGameState(to_move='O',
                                           utility=0,
                                           board=['buffer', ['   ', ' X ', 'OOO'], ['   '], ['   ', ' O '], ['   '], ['   ', ' X ', 'XX '], ['   ', 'XXX'], ['   ', ' OO'], ['   '], ['   ', 'XXX']],
                                           bank=['   ', '   ', '   ', 'XX ', '   ', '   ', 'OOO', '   ', 'OO ', '   ', ' O ', '   '])
    expected_vector_3 = [6, 1, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 3, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 2, 0, 0, 6, 0, 5, 0, 4, 0, 1]
    test_vector_3 = gg.vector_encoding(test_state_3)
    assert test_vector_3 == expected_vector_3


    # Test 4: Full Board, No Bank Pieces, X to Move - PASS
    test_state_4 = GobletGobblersGameState(to_move='X',
                                           utility=0,
                                           board=['buffer', ['   ', ' O ', 'XX '],        ['   ', 'OOO'], ['   ', ' XX', 'OOO'],
                                                            ['   ', ' X ', ' OO'],        ['   ', 'XXX'], ['   ', ' X ', ' OO'],
                                                                          ['   '], ['   ', ' O ', 'XXX'],               ['   ']],
                                           bank=['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
    expected_vector_4 = [2, 4, 0, 0, 6, 0, 0, 0, 6, 2, 0, 0, 5, 1, 0, 0, 3, 0, 0, 0, 5, 1, 0, 0, 0, 0, 0, 0, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    test_vector_4 = gg.vector_encoding(test_state_4)
    assert test_vector_4 == expected_vector_4



    # Test 5: Mid-game, O to Move - PASS
    test_state_5 = GobletGobblersGameState(to_move='O',
                                           utility=0,
                                           board=['buffer', ['   ', 'XX '],               ['   '], ['   ', ' XX', 'OOO'],
                                                            ['   ', ' X ', ' OO'], ['   ', 'XXX'],        ['   ', ' OO'],
                                                            ['   '],               ['   ', ' O '],              ['   ']],
                                           bank=['XXX', '   ', '   ', '   ', '   ', ' X ', 'OOO', '   ', '   ', '   ', '   ', ' O '])
    test_vector_5 = gg.vector_encoding(test_state_5)
    expected_vector_5 = [2, 0, 0, 0, 0, 0, 0, 0, 6, 2, 0, 0, 5, 1, 0, 0, 3, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 1, 6, 0, 0, 0, 0, 4, 1]
    assert test_vector_5 == expected_vector_5
