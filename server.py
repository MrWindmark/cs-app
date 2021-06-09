import argparse
import json
from socket import *

system_msg = [
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


def server_start(testing=False) -> None:
    try:
        parser = argparse.ArgumentParser(description="Chat server")

        parser.add_argument("-a", dest="ip", default='127.0.0.1', type=str)
        parser.add_argument("-p", dest="port", default=7777, type=int)

        args = parser.parse_args()
        print(args)
    except Exception as e:
        print(e)

    server = socket(AF_INET, SOCK_STREAM)
    server.bind((args.ip, args.port))
    server.listen(5)

    while True:
        if testing:
            return
        client, addr = server.accept()
        data = client.recv(1000000)
        tmp = data.decode('utf-8')
        print(tmp)
        system_msg[0]['alert'] = 'Greetings!'
        ans_msg = json.dumps(system_msg[0], indent=4, sort_keys=True, default=str)
        client.send(ans_msg.encode('utf-8'))
        client.close()


if __name__ == '__main__':
    server_start()
