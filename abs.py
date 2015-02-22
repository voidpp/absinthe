#!/usr/bin/env python

import os
import sys
import argparse
import pyjsonrpc

# realpath resolves symlinks
root_dir = os.path.dirname(os.path.realpath(__file__))

from tools.utils import extend_path

extend_path(root_dir, ['modules', 'tools'])

from config import Config
from utils import FileReader, SimpleResponse

try:
    config = Config(FileReader(), None)
    config.load(os.path.join(root_dir, 'config', 'server.json'))
except Exception as e:
    print "Cannot load config: " % e
    sys.exit(1)

config_raw = config.raw()

parser = argparse.ArgumentParser()
parser.add_argument('file', type = argparse.FileType('r')) #, nargs='+'
parser.add_argument('-p', '--path_base', type = str, choices = config_raw['paths'].keys(), default = config_raw['default-path'])
parser.add_argument('-v', '--verbose', action = 'store_true')
args = parser.parse_args()

client = pyjsonrpc.HttpClient(url = "http://%(host)s:%(port)d/jsonrpc" % config_raw['command_server'])

try:
    response = client.open_file(args.path_base, os.path.abspath(args.file.name))
    resp = SimpleResponse(**response)
    if resp.code != True or args.verbose:
        for msg in resp.message:
            print msg
except Exception as e:
    print e
