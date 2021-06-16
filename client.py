from datetime import datetime
from socket import *
import json
import argparse
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
    init_message = json.dumps(gen_presence_msg(username), indent=4, sort_keys=True, default=str)
    server_ans = send_to_server(msg=init_message, server_ip=_ip_address, port=int(_port))
    return server_ans.decode('utf-8')


@log
def send_to_server(msg: str, server_ip: str, port: int):
    s = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
    s.connect((server_ip, port))  # Соединиться с сервером
    s.send(msg.encode('utf-8'))
    data = s.recv(1000000)
    # my_log.debug(data)
    s.close()
    return data


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Ping script")

    parser.add_argument("-a", dest="ip", required=True)
    parser.add_argument("-p", dest="port", default=7777, type=int)

    args = parser.parse_args()
    # my_log.debug(args)

    if connection_check(args.ip, args.port):
        job_status = start(args.ip, args.port)
        # my_log.info(job_status)
