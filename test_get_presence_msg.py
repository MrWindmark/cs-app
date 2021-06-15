from client import gen_presence_msg
from datetime import datetime


def test_set_auth_msg():
    username = 'user_name'
    assert gen_presence_msg(username) == {
        "action": "presence",
        "time": datetime.now().strftime('%m/%d/%y %H:%M:%S'),
        "type": "status",
        "user": {
            "account_name": "user_name",
            "status": "on-line"
        }
    }


def test_set_auth_msg_wrong_date():
    username = 'user_name'
    password = 'ThisIsNotPassW0rd'
    assert gen_presence_msg(username) != {
        "action": "presence",
        "time": datetime.now().strftime('%m/%d/%y %H:%M'),
        "type": "status",
        "user": {
            "account_name": "user_name",
            "status": "on-line"
        }
    }


def test_set_auth_msg_incorrect_data():
    username = 'user_name'
    password = 'ThisIsNotPassW0rd'
    assert gen_presence_msg(username) != {
        "action": "presence",
        "time": datetime.now().strftime('%m/%d/%y %H:%M'),
        "type": "status",
        "user": {
            "account_name": "User_Name",
            "status": "on-line"
        }
    }
