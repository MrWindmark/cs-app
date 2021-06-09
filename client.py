from datetime import datetime
from socket import *
import json
import argparse


def start(_ip_address, _port):
    username = input('Enter your username: ')
    init_message = json.dumps(gen_presence_msg(username), indent=4, sort_keys=True, default=str)
    server_ans = send_to_server(msg=init_message, server_ip=_ip_address, port=int(_port))
    return server_ans.decode('utf-8')


def connection_check(_ip_address, _port):
    try:
        if len(_ip_address.split('.')) == 4:
            inet_aton(_ip_address)
        else:
            print('Incorrect IP. Check dots in IP-address and restart script')
            return False
    except error:
        print('Incorrect IP. Restart script with correct address parameter')
        return False

    if str(_port).isdigit():
        if int(_port) <= 0:
            print('Incorrect Port. Restart script with correct Port parameter')
            return False
    return True


def set_auth_msg(_username, _password):
    auth_msg = {
        "action": "authenticate",
        "time": datetime.now(),
        "user": {
            "account_name": "",
            "password": ""
        }
    }
    auth_msg["user"]["account_name"] = _username
    auth_msg["user"]["password"] = _password
    return auth_msg


def gen_presence_msg(_username):
    presence_msg = {
        "action": "presence",
        "time": datetime.now(),
        "type": "status",
        "user": {
            "account_name": "",
            "status": "on-line"
        }
    }
    presence_msg["user"]["account_name"] = _username
    return presence_msg


def get_logout_msg():
    return {"action": "quit"}


def send_to_server(msg, server_ip, port):
    s = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
    s.connect((server_ip, port))  # Соединиться с сервером
    s.send(msg.encode('utf-8'))
    data = s.recv(1000000)
    s.close()
    return data


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Ping script")

    parser.add_argument("-a", dest="ip", required=True)
    parser.add_argument("-p", dest="port", default=7777, type=int)

    args = parser.parse_args()
    print(args)

    if connection_check(args.ip, args.port):
        job_status = start(args.ip, args.port)
        print(job_status)
