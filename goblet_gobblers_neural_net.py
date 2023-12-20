import copy
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np


class GobletGobblersNet(nn.Module):
    """ NN Architecture
        - Input Layer: 49 neurons: Size of gg state vector encoding
        - Hidden Layers: 2 layers with around 64 & 128 neurons each
        - Activation Function: ReLU for hidden layers
        - Output Layer: 180 neurons (number of possible moves) & softmax activation to choose best move
        - Loss Function: Negative Log-Likelihood Loss
        - Optimizer: Adam """

    def __init__(self):
        super(GobletGobblersNet, self).__init__()
        # Define the layers
        self.layer1 = nn.Linear(49, 128)  # First hidden layer
        self.layer2 = nn.Linear(128, 64)  # Second hidden layer
        self.layer3 = nn.Linear(64, 180)  # Output layer

    def forward(self, x):
        # Forward pass through the network
        x = F.relu(self.layer1(x))            # Activation function after first layer
        x = F.relu(self.layer2(x))            # Activation function after second layer
        x = F.log_softmax(self.layer3(x), dim=1)  # Softmax activation function for the output layer
        return x

    def get_nn_move(self, game, state):
        """returns move from nn - used for nn_player in players.py"""
        # note: need to test

        # Encode state into vector
        game_state_vector = self.encode_gg_state_to_vector(state)

        # Convert the game state vector to a PyTorch tensor
        state_tensor = torch.FloatTensor([game_state_vector])  # Add an extra dimension for batch

        # Forward pass through the model
        with torch.no_grad():  # Ensure gradients are not computed
            self.eval()  # Set the model to evaluation mode
            output_probabilities = self(state_tensor)

        # mask illegal moves
        np_probs = copy.deepcopy(output_probabilities.numpy())
        for index, move in enumerate(all_possible_moves):
            if move not in game.actions(state):
                np_probs[0][index] = -np.inf

        # Interpret the output to decide the move - choose the move with the highest probability
        chosen_move_index = np_probs.argmax().item()

        # Convert this index back to a move in the game
        chosen_move = all_possible_moves[chosen_move_index]

        return chosen_move

    def encode_gg_state_to_vector(self, state_to_encode):
        """Encodes state into a vector (for use as input into a neural net)

            vector = [board, bank, to move]

        1) Board encoding:
            Each spot will be represented by a vector of length 4 (3 possible pieces + empty spot)
            Encoding sequence is spots (top left - bottom right) and pieces (top piece - bottom (empty) piece)
            Each piece is encoded according to the table below

            Ex final vector:

                [3      5       0       0       6       2       4       0       6       0       0       0  ... 0]
                 ^                              ^                               ^
                 spot 1                         spot 2                          spot 3
                 1t     1m      1b      1e      2t      2m      2b      2e      3t      3m      3b      3e ... 9e
                 (t = top, m = middle, b = bottom, e = empty)

            Conversion table:
                                piece       num     (#x, #o)
            -----------------------------------------------
            Empty Spot          '   '       0       (0, 0)
            Small Piece (X)     ' X '       1       (1, 0)
            Medium Piece (X)    'XX '       2       (2, 0)
            Large Piece (X)     'XXX'       3       (3, 0)
            Small Piece (O)     ' O '       4       (0, 1)
            Medium Piece (O)    'OO '       5       (0, 2)
            Large Piece (O)     'OOO'       6       (0, 3)


        2) Bank Encoding
            The availability of each piece in the bank is also encoded using the same method


        3) Current Player Encoding
        The current player (to move) will be encoded in a similar manner

            state.to_move == 'X': 0
            state.to_move == 'O': 1

        The complete encoded vector for a game state consists of: [board, bank, to_move]

             board                                    bank                   to move
            [3, 5, 0, 0, 6, 2, 4, 0, 6, 0, 0, 0, ..., 3, 0, 2, 0, 1, 1, ..., 0]
        """

        piece_conversions = {(0, 0): 0,  # (x-count, o-count)
                             (1, 0): 1,
                             (2, 0): 2,
                             (3, 0): 3,
                             (0, 1): 4,
                             (0, 2): 5,
                             (0, 3): 6}

        encoded_vector = []

        state = copy.deepcopy(state_to_encode)

        # loop through board spots
        for spot in state.board:
            # skip buffer spot
            if spot == 'buffer':
                continue
            # if spot < length 4: pad with empty pieces
            while len(spot) < 4:
                spot.insert(0, '   ')
            # reverse to get list in order (left-right == top-bottom)
            spot.reverse()
            # get piece conversion and append to vector
            for piece in spot:
                encoded_vector.append(piece_conversions[(piece.count('X'), piece.count('O'))])
        # loop through bank pieces
        for piece in state.bank:
            # get piece conversion and append to vector
            encoded_vector.append(piece_conversions[(piece.count('X'), piece.count('O'))])

        # append player conversion to vector
        encoded_vector.append(0) if state.to_move == 'X' else encoded_vector.append(1)

        return encoded_vector

    def train_nn(self, game, num_games=1000):
        """use reinforcement learning to train model"""

        # Define Loss function (Negative Log-Likelihood Loss)
        criterion = nn.NLLLoss()

        # Define Optimizer (Adam).  Adjust learning rate as needed
        optimizer = torch.optim.Adam(self.parameters(), lr=0.001)

        # check initial weights
        weight_check_pre = copy.deepcopy(self.state_dict()['layer1.weight'][0])
        print(weight_check_pre)

        # play games & train on results
        for game_index in range(num_games):

            print(f"playing game {game_index}")

            game_state = game.initial  # # Initialize the game / Reset the game environment to a new state
            game_over = False
            move_history = []  # To keep track of the moves and states

            # get next move & apply it
            while not game_over:

                # Convert the current game state to a vector
                game_state_vector = self.encode_gg_state_to_vector(game_state)

                # Get the move from the model
                self.eval()  # Set the model to evaluation mode
                with torch.no_grad():
                    state_tensor = torch.FloatTensor([game_state_vector])  # Add an extra dimension for batch
                    output_probabilities = self(state_tensor)

                    # mask illegal moves
                    np_probs = copy.deepcopy(output_probabilities.numpy())
                    for index, move in enumerate(all_possible_moves):
                        if move not in game.actions(game_state):
                            np_probs[0][index] = -np.inf

                    # Interpret the output to decide the move - choose the move with the highest probability
                    # chosen_move_index = output_probabilities.argmax().item()
                    chosen_move_index = np_probs.argmax().item()

                    # Convert this index back to a move in the game
                    chosen_move = all_possible_moves[chosen_move_index]

                # Play the move and get the resultant (next) state
                next_state = game.result(game_state, chosen_move)

                # Save the current state, chosen move, and resulting utility for later training
                move_history.append((game_state_vector, chosen_move_index, next_state.utility))

                # Update the current state
                game_state = next_state

                # check for game over
                if game_state.utility != 0:
                    # print("game over")
                    game_over = True

            # train model on results
            self.train()  # Set the model to training mode
            for state_vector, chosen_move, reward in move_history:
                # Prepare the data for training
                state_tensor = torch.FloatTensor([state_vector])
                move_tensor = torch.tensor([chosen_move], dtype=torch.long)

                # Forward pass
                optimizer.zero_grad()
                predictions = self(state_tensor)

                # Calculate loss based on the reward and model's predictions
                loss = criterion(predictions, move_tensor)

                # Backward pass and optimize
                loss.backward()
                optimizer.step()

        # check post training
        weight_check_post = copy.deepcopy(self.state_dict()['layer1.weight'][0])
        print(weight_check_post)

        return self



all_possible_moves = [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9),
                      (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9),
                      (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9),
                      (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9),
                      (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (5, 7), (5, 8), (5, 9),
                      (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 7), (6, 8), (6, 9),
                      (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 8), (7, 9),
                      (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 9),
                      (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8),
                      (10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9),
                      (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9),
                      (12, 1), (12, 2), (12, 3), (12, 4), (12, 5), (12, 6), (12, 7), (12, 8), (12, 9),
                      (13, 1), (13, 2), (13, 3), (13, 4), (13, 5), (13, 6), (13, 7), (13, 8), (13, 9),
                      (14, 1), (14, 2), (14, 3), (14, 4), (14, 5), (14, 6), (14, 7), (14, 8), (14, 9),
                      (15, 1), (15, 2), (15, 3), (15, 4), (15, 5), (15, 6), (15, 7), (15, 8), (15, 9),
                      (16, 1), (16, 2), (16, 3), (16, 4), (16, 5), (16, 6), (16, 7), (16, 8), (16, 9),
                      (17, 1), (17, 2), (17, 3), (17, 4), (17, 5), (17, 6), (17, 7), (17, 8), (17, 9),
                      (18, 1), (18, 2), (18, 3), (18, 4), (18, 5), (18, 6), (18, 7), (18, 8), (18, 9),
                      (19, 1), (19, 2), (19, 3), (19, 4), (19, 5), (19, 6), (19, 7), (19, 8), (19, 9),
                      (20, 1), (20, 2), (20, 3), (20, 4), (20, 5), (20, 6), (20, 7), (20, 8), (20, 9),
                      (21, 1), (21, 2), (21, 3), (21, 4), (21, 5), (21, 6), (21, 7), (21, 8), (21, 9)]
