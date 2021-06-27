from client import connection_check


def test_connection_check():
    ip = "127.0.0.7"
    port = 4000

    assert connection_check(ip, port) == True


def test_connection_check_port_error():
    ip = "127.0.0.7"
    port = 22

    assert connection_check(ip, port) == False


def test_connection_check_ip_error():
    ip = "127.0.0"
    port = 4000

    assert connection_check(ip, port) == False


def test_connection_check_data_error():
    ip = "127.0.0"
    port = 20

    assert connection_check(ip, port) == False
