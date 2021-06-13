import logging
import os


def create_logger():
    path = os.path.abspath(os.getcwd())
    path = os.path.join(path, 'logs', 'client.log')

    logging.basicConfig(
        filename=path,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.DEBUG
    )

    return logging.getLogger('app.client')


if __name__ == "__main__":
    create_logger()
