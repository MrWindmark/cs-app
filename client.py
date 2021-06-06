from datetime import datetime
from sys import argv
from socket import *
import json

auth_msg = {
    "action": "authenticate",
    "time": datetime.now(),
    "user": {
        "account_name": "",
        "password": ""
    }
}

presence_msg = {
    "action": "presence",
    "time": datetime.now(),
    "type": "status",
    "user": {
        "account_name": "",
        "status": "on-line"
    }
}

logout_msg = {
    "action": "quit"
}


def start():
    username = input('Enter your username: ')
    init_message = json.dumps(gen_presence_msg(username), indent=4, sort_keys=True, default=str)
    server_ans = send_to_server(msg=init_message, server_ip=__addrss, port=int(__port))
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

    if _port.isdigit():
        if int(_port) <= 0:
            print('Incorrect Port. Restart script with correct Port parameter')
            return False
    return True


def gen_presence_msg(_username):
    presence_msg["user"]["account_name"] = _username
    return presence_msg


def send_to_server(msg, server_ip, port):
    s = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
    s.connect((server_ip, port))  # Соединиться с сервером
    s.send(msg.encode('utf-8'))
    data = s.recv(1000000)
    s.close()
    return data


if len(argv) > 2:
    _, __addrss, __port = argv
    print(__addrss, __port)
elif len(argv) > 1:
    _, __addrss = argv
    __port = '7777'
    print(__addrss, __port)
else:
    raise ValueError('No IP and Port parameters. Restart script with correct parameters')

if __name__ == '__main__':
    if connection_check(__addrss, __port):
        job_status = start()
        print(job_status)
