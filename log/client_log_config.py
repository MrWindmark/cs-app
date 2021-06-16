import inspect
import logging
import os
from functools import wraps


def create_logger():
    path = os.path.abspath(os.getcwd())
    path = os.path.join(path, 'logs', 'client.log')

    logging.basicConfig(
        filename=path,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.DEBUG
    )

    return logging.getLogger('app.client')


def debug_logger(func):
    log = create_logger()

    @wraps(func)
    def call_func(*args, **kwargs):
        log.debug(f'Function "{func.__name__}()" called with: {args}, {kwargs} - from "{inspect.stack()[1][3]}"')
        temp = func(*args, **kwargs)
        log.debug(f'Function {func.__name__} return: {temp}')
        return temp
    return call_func


if __name__ == "__main__":
    create_logger()
