#!/usr/bin/env python

import os
import sys
import argparse

root_dir = os.path.dirname(__file__)

from tools.utils import extend_path

extend_path(root_dir, ['modules', 'tools'])

from logger import get_logger
from config import Config
from utils import FileReader
from absinthe_client import AbsintheClient

# init logger
logger = get_logger(os.path.join(root_dir, 'config', 'logger.json'), 'client')
logger.info('Absinthe client start')

# init config
try:
    config = Config(FileReader(), logger)
    config.load(os.path.join(root_dir, 'config', 'client.json'))
    logger.info('Config has been successfully loaded')
except Exception as e:
    logger.error('Exception occured during config parsing: ' + str(e))
    sys.exit(1)

client = AbsintheClient(config, logger)

# blocks console
client.start()

logger.info('Absinthe client stop')
