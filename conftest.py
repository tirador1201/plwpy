from pytest import fixture

from framework.base_page import BasePage
from utils.api_utils import create_new_email
from utils.common_utils import read_json


@fixture(autouse=True, scope='session')
def read_config(request):
    environment = request.config.getoption('--environment')
    config_data = read_json(environment)
    yield config_data

@fixture(scope='session')
def generate_magic_link():
    print("create new email")
    email = create_new_email()
    yield email

@fixture(scope='class')
def initial_page(read_config, browser):
    base = BasePage(new_context=True, browser=browser, base_url=read_config['base_url'])
    base.goto('/')
    yield base
    base.close()


def pytest_addoption(parser):
    parser.addoption('--environment', action='store', default='stage.json',
                     help='Path to the target environment config file')
