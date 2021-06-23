import pytest


def pytest_addoption(parser):
    parser.addoption("-Adress", action="store", default="127.0.0.1", dest="ip")
    parser.addoption("-Port", action="store", default=7777, dest="port")


@pytest.fixture(scope='session')
def name(request):
    name_value = request.config.option.name
    if name_value is None:
        pytest.skip()
    return name_value
