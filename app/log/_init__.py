import logging
import time
import os
import sys
import socket
import json
import traceback

from dynaconf import settings


INITIALIZED = False


class LogFormatter(logging.Formatter):
    def __init__(self, environment, application):
        self._env = environment
        self._application = application
        super().__init__()

    def format(self, record):
        data = {
            'timestamp': record.created,
            'short_message': str(record.msg),
            'host': socket.gethostname(),
            'level': record.levelno,
            'Severity': record.levelname,
            '_product': 'listings',
            '_application': self._application,
            '_environment': self._env,
            '_log_type': 'application'
        }

        if record.levelname == 'ERROR':
            lines = traceback.format_exception(record.exc_info[0],
                                               record.exc_info[1],
                                               record.exc_info[2])
            data['full_message'] = ''.join('' + line for line in lines)

        return json.dumps(data)


def init():
    # pylint: disable=global-statement
    global INITIALIZED

    if INITIALIZED:
        return
    else:
        INITIALIZED = True

    application = settings('application_name')
    env = os.getenv('ENV', 'DEV')
    default_log_level = logging.getLevelName(os.getenv('LOG_LEVEL', 'INFO'))

    log_format = '%(asctime)s - %(name)s - %(thread)d - %(levelname)s - %(message)s'
    formatter = logging.Formatter(log_format, datefmt='%Y-%m-%d %H:%M:%S')
    formatter.converter = time.gmtime
    logger = logging.getLogger()
    logger.setLevel(default_log_level)

    formatter = LogFormatter(env, application)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
