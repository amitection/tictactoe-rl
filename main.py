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
# limitations under the License.#

# TicTacToe code derived from https://inventwithpython.com


import common_utils
from player import Player
from game_env import GameBoard, is_winner, who_goes_first

logging = common_utils.setup_logging()
logger = logging.getLogger(__name__)


if __name__ == "__main__":

    debug = False

    # Reset the board
    game_board = GameBoard()
    roundNo = 1

    player1 = Player("Player 1")
    player2 = Player("Player 2")

    player1_letter, player2_letter = 'X', 'O'
    turn = who_goes_first(player1, player2)
    logger.info('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        letter = None

        if turn == player1.get_player_name():
            letter = player1_letter
            # Player 1 turn
            if debug:
                game_board.draw_board()
            move = player1.get_move(game_board, player2_letter)
            game_board.make_move(player1_letter, move)

        else:
            letter = player2_letter
            # Player 2 turn
            if debug:
                game_board.draw_board()
            move = player2.get_move(game_board, player2_letter)
            game_board.make_move(player2_letter, move)

        if is_winner(game_board.get_board(), letter):
            # Checking if game is over and some player has won
            game_board.draw_board()
            if letter == player1_letter:
                logger.info(player1.get_player_name() + ' has won the game!')
            else:
                logger.info(player2.get_player_name() + ' has won the game!')
            gameIsPlaying = False
        else:
            if game_board.is_board_full():
                roundNo += 1
                game_board = GameBoard(mesg="Starting round {}".format(roundNo))
                logger.info('The game is a tie!')
                break
            else:
                if turn == player1.get_player_name():
                    turn = player2.get_player_name()
                else:
                    turn = player1.get_player_name()



