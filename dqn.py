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

import random
import copy
import pandas as pd
from nn import NNModel

class DQNAgent:

    def __init__(self):
        self.learning_freq = 10
        self.learning_starts = 1000
        self.target_update_freq = 50
        self.num_updates = 0
        self.num_calls = 0
        self.discount = 0.99

        # initialize the Q networks
        self.q_network = NNModel(learning_rate=0.001, no_inputs=9)
        self.target_q_network = NNModel(learning_rate=0.001, no_inputs=9)

    def get_action(self, state, legal_actions):
        """
        Compute the action to take in the current state.
        Epsilon decides whether to exploit the current policy or choice a new action randomly.
        A small value for epsilon indicates lesser exploration.
        :param state: state vector
        :param legal_actions: Set of physically valid moves in the current state.
                              A number representing the location of empty cells (1 - 9)
        :return: appropriate action to take in the current state.
                 Number in the range (1-9) representing the location where move can
                 be made
        """

        if self.__flip_coin(self.epsilon):
            print("Randomizing action...")
            action = random.choice(legal_actions)
        else:
            print("Selecting the best action based on policy...")
            action = self.__get_policy(state, legal_actions)

        return action

    def update_policy(self, state, action, reward):
        """
        Update the DRL learning with (S,A,R) tuple
        :param state:
        :param action:
        :param reward:
        :return:
        """
        pass

    def __get_policy(self, state, actions):
        return self.__compute_action_from_qValues(state, actions)

    def __compute_action_from_qValues(self, state, actions):
        """
        Compute the q_value for each action and return the max Q-value as the value of that state
        Expects a legal set of actions
        :param state:
        :return:
        """

        # No actions available
        if len(actions) == 0:
            return 0.0

        # Populating a new list of (action, value) pair from list of q_values
        action_value_pair = []
        for action in actions:
            action_value_pair.append((action, self.__get_qValue(state, action)))

        # Returning the action with maximum q_value
        return max(action_value_pair, key=lambda x: x[1])[0]

    def __get_qValue(self, state, action):
        """
        Compute Q-value from the NN
        :return:
        """
        input_vector = self.__update_state_with_action(state, action)
        q_value = self.q_network.predict(input_vector)

        return q_value

    def __update_state_with_action(self, state, action):
        """
        Game specific implementation. Simply update the board
        with the chosen move.
        :param state: board vector
        :param action: move chosen
        :return: DataFrame object representation of the input vector
        """
        input_vector = copy.deepcopy(state)
        input_vector[action] = 'S'
        input_vector = pd.DataFrame(input_vector)

        return input_vector

    def __flip_coin(p):
        r = random.random()
        return r < p