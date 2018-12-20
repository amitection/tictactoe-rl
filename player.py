# Copyright 2018 Amit Prasad
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# TicTacToe code derived from https://inventwithpython.com


import common_utils
import random
import game_env

logging = common_utils.setup_logging()
logger = logging.getLogger(__name__)


class Player:

    def __init__(self, player_name=None, letter=None):
        if player_name is None:
            self.player_name = common_utils.get_random_name()
        else:
            self.player_name = player_name

        if letter is not None:
            self.letter = letter
        else:
            pass
            # TODO: Handle this

        if letter == 'X':
            self.enemy_letter = 'O'
        else:
            self.enemy_letter = 'X'

        logger.debug("Initializing player {} with letter {} ...".format(self.player_name, self.letter))


    def get_move(self, game_state):

        move = self.rule_based_algo(game_state)
        return move


    def __get_board_copy(self, board):
        # Make a duplicate of the board list and return it the duplicate.
        dup_board = []
        for i in board:
            dup_board.append(i)

        return dup_board

    def __make_mock_move(self, board, letter, move):
        board[move] = letter

    def __choose_random_move_from_list(self, board, moves_list):
        # Returns a valid move from the passed list on the passed board.
        # Returns None if there is no valid move.
        possible_moves = []
        for i in moves_list:
            if game_env.is_space_free(board, i):
                possible_moves.append(i)

        if len(possible_moves) != 0:
            return random.choice(possible_moves)
        else:
            return None

    def get_player_name(self):
        return self.player_name

    def rule_based_algo(self, game_state):
        """
        Simple rule based algorithm that returns the
        move after computing checking if we can win in
        the next move or else block the enemy's move if
        he has a chance to win.

        :param game_state:
        :return:
        """
        board = game_state.get_board()
        # determine where to move and return that move.

        # Here is our algorithm for our Tic Tac Toe AI:
        # First, check if we can win in the next move
        for i in range(1, 10):
            board_copy = self.__get_board_copy(board)
            if game_env.is_space_free(board_copy, i):
                self.__make_mock_move(board_copy, self.letter, i)
                if game_env.is_winner(board_copy, self.letter):
                    return i

        # Check if the player could win on his next move, and block them.
        for i in range(1, 10):
            board_copy = self.__get_board_copy(board)
            if game_env.is_space_free(board_copy, i):
                self.__make_mock_move(board_copy, self.enemy_letter, i)
                if game_env.is_winner(board_copy, self.enemy_letter):
                    return i

        # Try to take one of the corners, if they are free.
        move = self.__choose_random_move_from_list(board, [1, 3, 7, 9])
        if move is not None:
            return move

        # Try to take the center, if it is free.
        if game_env.is_space_free(board, 5):
            return 5

        # Move on one of the sides.
        return self.__choose_random_move_from_list(board, [2, 4, 6, 8])