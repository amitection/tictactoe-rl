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

import tensorflow as tf

class NNModel:

    def __init__(self, learning_rate, no_inputs):

        # create feature columns
        feature_cols = []
        for i in range(no_inputs):
            feature_cols.append(tf.feature_column.categorical_column_with_vocabulary_list(
                str(i+1), vocabulary_list=['S', 'O', 'E']
            ))

        hidden_layer_units = [27, 27, 27]

        # instantiate estimator
        self.estimator = tf.estimator.DNNRegressor(feature_columns=feature_cols,
                                                   model_dir='train',
                                                   hidden_units=hidden_layer_units,
                                                   optimizer=lambda: tf.AdamOptimizer(
                                                        learning_rate=tf.exponential_decay(
                                                            learning_rate=0.1,
                                                            global_step=tf.get_global_step(),
                                                            decay_steps=10000,
                                                            decay_rate=0.96))
                                                   )

    def train(self, input):
        input_fn = tf.estimator.inputs.pandas_input_fn(x=input, shuffle=True)
        self.estimator.train(input_fn)
        return

    def predict(self, input):
        input_fn = tf.estimator.inputs.pandas_input_fn(x=input, shuffle=False)
        return self.estimator.predict(input_fn)

