from client import set_auth_msg
from datetime import datetime


def test_set_auth_msg():
    username = 'user_name'
    password = 'ThisIsNotPassW0rd'
    assert set_auth_msg(username, password) == {
        "action": "authenticate",
        "time": datetime.now().strftime('%m/%d/%y %H:%M:%S'),
        "user": {
            "account_name": "user_name",
            "password": "ThisIsNotPassW0rd"
        }
    }


def test_set_auth_msg_wrong_date():
    username = 'user_name'
    password = 'ThisIsNotPassW0rd'
    assert set_auth_msg(username, password) != {
        "action": "authenticate",
        "time": datetime.now().strftime('%m/%d/%y %H:%M'),
        "user": {
            "account_name": "user_name",
            "password": "ThisIsNotPassW0rd"
        }
    }


def test_set_auth_msg_incorrect_data():
    username = 'user_name'
    password = 'ThisIsNotPassW0rd'
    assert set_auth_msg(username, password) != {
        "action": "authenticate",
        "time": datetime.now().strftime('%m/%d/%y %H:%M'),
        "user": {
            "account_name": "User_name",
            "password": "thisisnotpassw0rd"
        }
    }
