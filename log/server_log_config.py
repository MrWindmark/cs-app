import logging
import os
from logging.handlers import TimedRotatingFileHandler


def create_logger():
    path = os.path.abspath(os.getcwd())
    path = os.path.join(path, 'logs', 'server.log')

    logging.basicConfig(
        filename=path,
        level=logging.DEBUG
    )

    log = logging.getLogger('app.server')
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler = TimedRotatingFileHandler(path, when='D', interval=1)
    handler.setFormatter(formatter)

    if log.hasHandlers():
        log.handlers.clear()
    log.addHandler(handler)
    return log


if __name__ == '__main__':
    create_logger()
