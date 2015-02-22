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
from remote_process_manager import RemoteProcessManager

parser = argparse.ArgumentParser()
parser.add_argument('command', type=str, choices=['start', 'stop', 'restart', 'status'])
args = parser.parse_args()

# init logger
logger = get_logger(os.path.join(root_dir, 'config', 'logger.json'), 'init')
logger.info("Absinthe server manager script")

# init config
try:
    config = Config(FileReader(), logger)
    config.load(os.path.join(root_dir, 'config', 'server.json'))
    logger.info('Config has been successfully loaded')
except Exception as e:
    logger.error('Exception occured during config parsing: ' + str(e))
    sys.exit(1)

# create manager
mgr = RemoteProcessManager(
    ['python', os.path.join(root_dir, 'server.py')],
    config.data['command_server']['port'].value,
    os.path.join(root_dir, 'absinthe_server.pid'),
    logger
)
command = getattr(mgr, args.command)

try:
    response = command()
    logger.info(response.message)
except Exception as e:
    raise

