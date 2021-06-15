from server import server_start


def test_server_run():
    assert server_start(True) is None