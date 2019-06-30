import logging
from json import dumps
from socket import gethostname
from time import time

from dynaconf import settings


logger = None


def create_logger():
    global logger

    if logger is not None:
        return logger

    logger = logging.getLogger(settings('application_name'))
    logger.setLevel(level=1)

    handler_stream = logging.StreamHandler()
    handler_stream.formatter = LogFormatter()
    logger.addHandler(handler_stream)
    logger.propagate = False

    return logger


class LogFormatter(logging.Formatter):
    def __init__(self):
        self._env = "DEV"
        self._host = gethostname()
        logging.Formatter.__init__(self)

    def format(self, record):
        log = {
            "timestamp": time(),
            "_application": settings('application_name'),
            "_environment": self._env,
            "host": self._host,
            "level": self.__get_log_level(record.levelno),
            "_log_type": "application",
            "short_message": record.msg,
        }

        for attr in vars(record):
            if attr[0] == "_":
                log[attr] = getattr(record, attr)

        return dumps(log)

    @staticmethod
    def __get_log_level(levelno):
        return {
            logging.INFO: 6,
            logging.DEBUG: 7,
            logging.ERROR: 3,
            logging.WARN: 4,
            logging.WARNING: 4,
            logging.CRITICAL: 2,
        }.get(levelno, 6)


if logger is None:
    create_logger()
