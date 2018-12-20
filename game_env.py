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

logging = common_utils.setup_logging()
logger = logging.getLogger(__name__)


class GameBoard:

    _board = None

    def __init__(self, mesg=None):
        if mesg is not None:
            logger.info("Resetting board. {}".format(mesg))
        else:
            logger.info("Initializing game board...")
        self._board = [' '] * 10

    def make_move(self, letter, move):
        self._board[move] = letter

    def get_board(self):
        return self._board

    def draw_board(self):
        # This function prints out the board that it was passed.

        # "board" is a list of 10 strings representing the board (ignore index 0)
        print('   |   |')
        print(' ' + self._board[7] + ' | ' + self._board[8] + ' | ' + self._board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self._board[4] + ' | ' + self._board[5] + ' | ' + self._board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self._board[1] + ' | ' + self._board[2] + ' | ' + self._board[3])
        print('   |   |')
        print(' \n\n')

    def is_board_full(self):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if is_space_free(self._board, i):
                return False
        return True


def is_winner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don't have to type as much.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal


def is_space_free(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '


# TODO: Use later when user interaction added
def input_player_letter():
    # Lets the player type which letter they want to be.
    # Returns a list with the player's letter as the first item, and the computer's letter as the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # the first element in the tuple is the player's letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def who_goes_first(player1, player2):
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return player1.get_player_name()
    else:
        return player2.get_player_name()


# TODO: Use later when user interaction added
def get_player_move(game_board):
    # Let the player type in his move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or \
            not is_space_free(game_board.get_board(), int(move)):
        print('What is your next move? (1-9)')
        move = input()

    return int(move)

