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

import os
import sys
import json
import logging.config
import random


def setup_logging(properties_file='logging-properties.json'):
    '''
    Loads the logger configuration from the
    logging-properties.json file and adds a prefix
    to the logger path based on the OS type.

    ===USAGE===
    logging = setup_logging()
    logger = logging.getLogger(__name__)

    :param properties_file:
    :return: instance of logging
    '''

    log_file_name = 'tictactoe.log'

    # Checking for OS Type
    if sys.platform.startswith('win'):
        log_file_prefix='c:/temp/tictactoe'
    else:
        log_file_prefix='/var/log/tictactoe/'

    if os.path.exists(properties_file):
        with open(properties_file, 'rt') as f:
            config_file_dump = json.load(f)
            config_file_dump['handlers']['log_file_handler']['filename'] = log_file_prefix + log_file_name
            logging.config.dictConfig(config_file_dump)

    else:
        logging.basicConfig(level=logging.INFO)

    return logging


def get_random_name():
    name = "player" + str(random.randint(1, 100));
    return name