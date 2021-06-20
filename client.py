from datetime import datetime
from socket import *
import json
import argparse
from time import sleep

from log.client_log_config import create_logger
from log.client_log_config import log

my_log = create_logger()


def set_auth_msg(_username: str, _password: str):
    auth_msg = {
        "action": "authenticate",
        "time": datetime.now().strftime('%m/%d/%y %H:%M:%S'),
        "user": {
            "account_name": "",
            "password": ""
        }
    }
    auth_msg["user"]["account_name"] = _username
    auth_msg["user"]["password"] = _password
    return auth_msg


@log
def gen_presence_msg(_username: str):
    presence_msg = {
        "action": "presence",
        "time": datetime.now().strftime('%m/%d/%y %H:%M:%S'),
        "type": "status",
        "user": {
            "account_name": _username,
            "status": "on-line"
        }
    }
    return presence_msg


@log
def gen_text_msg(_username: str, _message: str):
    presence_msg = {
        "action": "message",
        "time": datetime.now().strftime('%m/%d/%y %H:%M:%S'),
        "type": "status",
        "user": {
            "account_name": _username,
            "status": "on-line"
        },
        "message": _message
    }
    return presence_msg


@log
def get_logout_msg():
    return {"action": "quit"}


def connection_check(_ip_address: str, _port: int):
    try:
        if len(_ip_address.split('.')) == 4:
            inet_aton(_ip_address)
        else:
            my_log.error('Incorrect IP. Check dots in IP-address and restart script')
            return False
    except error:
        my_log.error('Incorrect IP. Restart script with correct address parameter')
        return False

    if str(_port).isdigit():
        if int(_port) <= 1023:
            my_log.error('Incorrect Port. Restart script with correct Port parameter')
            return False
    return True


@log
def start(_ip_address: str, _port: int):
    username = input('Enter your username: ')
    client_type = input('Enter "r" if you are reader or "w" if you are writer: ')
    if client_type == 'r' or client_type == 'R':
        read_from_server(username, _ip_address, _port)
    else:
        write_to_server(username, _ip_address, _port)


def read_from_server(username: str, server_ip: str, port: int):
    s = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
    s.connect((server_ip, port))  # Соединиться с сервером
    msg = gen_presence_msg(username)
    tmp = json.dumps(msg, indent=4, sort_keys=True, default=str)
    s.send(tmp.encode('UTF-8'))
    while True:
        try:
            print('In work')
            sleep(2)
            tm = s.recv(1000000)
            print("Получено: %s" % tm.decode('utf-8'))
        except Exception as e:
            pass


def write_to_server(username: str, server_ip: str, port: int):
    s = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
    s.connect((server_ip, port))  # Соединиться с сервером
    while True:
        message = input('Enter you message: ')
        if message == 'exit':
            break
        data = json.dumps(gen_text_msg(username, message), indent=4, sort_keys=True, default=str)
        s.send(data.encode('utf-8'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Ping script")

    parser.add_argument("-a", dest="ip", default='127.0.0.1', required=False)
    parser.add_argument("-p", dest="port", default=7777, type=int)

    args = parser.parse_args()
    # my_log.debug(args)

    if connection_check(args.ip, args.port):
        job_status = start(args.ip, args.port)
        # my_log.info(job_status)
