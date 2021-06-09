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


def server_start():
    parser = argparse.ArgumentParser(description="Ping script")

    parser.add_argument("-a", dest="ip", required=True)
    parser.add_argument("-p", dest="port", default=7777, type=int)

    args = parser.parse_args()
    print(args)

    server = socket(AF_INET, SOCK_STREAM)
    server.bind((args.ip, args.port))
    server.listen(5)

    while True:
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
