import os, sys

root_dir = os.path.dirname(__file__)
from tools.utils import extend_path
extend_path(root_dir, ['modules', 'tools'])

from logger import get_logger
from config import Config
from utils import FileReader

from absinthe_server import AbsintheServer

# init logger
logger = get_logger(os.path.join(root_dir, 'config', 'logger.json'), 'server')
logger.info("Welcome to the lofasz. (pid: %d)" % os.getpid())

# init config
try:
    config = Config(FileReader(), logger)
    config.load(os.path.join(root_dir, 'config', 'server.json'))
    logger.info('Config has been successfully loaded')
except Exception as e:
    logger.error('Exception occured during config parsing: ' + str(e))
    sys.exit(1)

server = AbsintheServer(config, logger)
server.start_command_server()
