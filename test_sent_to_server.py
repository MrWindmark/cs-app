import json
from datetime import datetime

from client import start, send_to_server


# Run this test with -s param
def test_start_function():
    msg = {
        "response": 200,
        "alert": "Greetings!"
    }
    response = json.dumps(msg, indent=4, sort_keys=True, default=str)
    ip = '127.0.0.1'
    port = 7777

    assert start(ip, port) == response


def test_start_function_error():
    msg = {
        "response": 402,
        "error": "Something went wrong. Check password and username"
    }
    response = json.dumps(msg, indent=4, sort_keys=True, default=str)
    ip = '127.0.0.1'
    port = 7777

    assert start(ip, port) != response


def test_send_to_server_function():
    ip = '127.0.0.1'
    port = 7777
    msg = {
        "action": "presence",
        "time": datetime.now().strftime('%m/%d/%y %H:%M:%S'),
        "type": "status",
        "user": {
            "account_name": "user_name",
            "status": "on-line"
        }
    }
    msg = json.dumps(msg, indent=4, sort_keys=True, default=str)
    response_msg = {
        "response": 200,
        "alert": "Greetings!"
    }
    response_msg = json.dumps(response_msg,
                              indent=4,
                              sort_keys=True,
                              default=str).encode('UTF-8')

    assert send_to_server(msg, ip, port) == bytes(response_msg)

def test_send_to_server_function_bad_response():
    ip = '127.0.0.1'
    port = 7777
    msg = {
        "action": "presence",
        "time": datetime.now().strftime('%m/%d/%y %H:%M:%S'),
        "type": "status",
        "user": {
            "account_name": "user_name",
            "status": "on-line"
        }
    }
    msg = json.dumps(msg, indent=4, sort_keys=True, default=str)
    response_msg = {
        "response": 402,
        "error": "Something went wrong. Check password and username"
    }
    response_msg = json.dumps(response_msg,
                              indent=4,
                              sort_keys=True,
                              default=str).encode('UTF-8')

    assert send_to_server(msg, ip, port) != bytes(response_msg)