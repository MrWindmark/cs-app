import argparse
import json
import select
from socket import *
from log.server_log_config import create_logger

__system_msg = [
    {
        "response": 200,
        "alert": "Необязательное сообщение/уведомление"
    },
    {
        "response": 402,
        "error": "Something went wrong. Check password and username"
    },
    {
        "response": 409,
        "error": "Someone is already connected with this username"
    },
]


def create_socket(ip: str, port: int):
    """
    This function create active socket for common network communication with clients
    :param ip: server IP which would get connects
    :param port: port number for connections
    :return server: Ready for work server socket
    """
    server = socket(AF_INET, SOCK_STREAM)
    server.bind((ip, port))
    server.settimeout(5)
    server.listen(5)
    return server


def server_start(testing=False) -> None:
    my_log = create_logger()

    try:
        parser = argparse.ArgumentParser(description="Chat server")

        parser.add_argument("-a", dest="ip", default='127.0.0.1', type=str)
        parser.add_argument("-p", dest="port", default=7777, type=int)

        args = parser.parse_args()
        my_log.debug('On start parsed args: %s', args)
    except Exception as e:
        my_log.error(e)

    clients = []
    messages = []
    server = create_socket(args.ip, args.port)

    while True:
        if testing:
            print("Test is on and all good")
            return
        try:
            client, addr = server.accept()
        except OSError as e:
            pass
        else:
            print("Получен запрос на соединение с %s" % str(addr))
            clients.append(client)
        finally:
            try:
                reads, send, excepts = select.select(clients, clients, [], 0)
            except Exception as er:
                # Some client disconnect. Ignore that
                pass
            finally:
                for connected_client in reads:
                    data = ''
                    try:
                        connected_client.settimeout(1)
                        data = connected_client.recv(1024)
                    except Exception as e:
                        pass
                    finally:
                        if data:
                            my_log.debug(f'We receive {data} with type {type(data)} and len {len(data)}')
                            message = json.loads(data)

                            if message["action"] == "presence":
                                __system_msg[0]['alert'] = 'You are in list'
                                ans_msg = json.dumps(__system_msg[0], indent=4, sort_keys=True, default=str)
                                try:
                                    connected_client.send(ans_msg.encode('utf-8'))
                                except Exception as e:
                                    clients.remove(connected_client)
                            elif message["action"] == "message":
                                messages.append(message)

                for connected_client in send:
                    for item in messages:
                        try:
                            my_log.debug(f'We send {item} with type {type(item)} and len {len(item)}')
                            ans_msg = json.dumps(item, indent=4, sort_keys=True, default=str)
                            connected_client.send(ans_msg.encode('utf-8'))
                        except Exception as e:
                            pass
                messages.clear()


if __name__ == '__main__':
    server_start()
