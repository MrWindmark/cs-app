import pytest


def pytest_addoption(parser):
    parser.addoption("-a", action="store")
    parser.addoption("-p", action="store")


@pytest.fixture(scope='session')
def name(request):
    name_value = request.config.option.name
    if name_value is None:
        pytest.skip()
    return name_value
