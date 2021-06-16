import logging
import os
from functools import wraps
from logging.handlers import TimedRotatingFileHandler


def create_logger():
    path = os.path.abspath(os.getcwd())
    path = os.path.join(path, 'logs', 'server.log')

    log = logging.getLogger('app.server')
    log.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler = TimedRotatingFileHandler(path, when='D', interval=1)
    handler.setFormatter(formatter)
    if log.hasHandlers():
        log.handlers.clear()
    log.addHandler(handler)
    return log


def server_logger(func):
    logger = create_logger()
    @wraps(func)
    def call_func(*args, **kwargs):
        logger.debug(f'')


if __name__ == '__main__':
    create_logger()
