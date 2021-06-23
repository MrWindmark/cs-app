from client import get_logout_msg


def test_logout_message():
    assert get_logout_msg() == {"action": "quit"}