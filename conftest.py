import os
import json

from pytest import fixture
from playwright.sync_api import sync_playwright

from framework.base_page import BasePage
from utils.api_utils import create_new_email


@fixture(autouse=True, scope='session')
def read_config(request):
    environment = request.config.getoption('--environment')
    config_data = load_config(environment)
    yield config_data

@fixture(scope='session')
def generate_email():
    print("create new email")
    email = create_new_email()
    yield email
    print("delete created email")

'''@fixture(scope='session')
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture(scope='session')
def get_browser(get_playwright, request):
    browser = request.config.getoption('--browser')
    headed = request.config.getoption('--headed')
    if not browser:
        browser = 'chromium'
    if 'chromium' in browser:
        browser_instance = get_playwright.chromium.launch(headless=not headed)
    elif 'firefox' in browser:
        browser_instance = get_playwright.firefox.launch(headless=not headed)
    elif 'webkit' in browser:
        browser_instance = get_playwright.webkit.launch(headless=not headed)
    else:
        assert False, 'unsupported browser type'
    yield browser_instance
    browser_instance.close()
'''

@fixture(scope='class')
def initial_page(read_config, browser):
    base = BasePage(new_context=True, browser=browser, base_url=read_config['base_url'])
    base.goto('/')
    yield base
    base.close()


def pytest_addoption(parser):
    parser.addoption('--environment', action='store', default='stage.json',
                     help='Path to the target environment config file')


def load_config(file):
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
    with open(config_file) as config_data:
        return json.loads(config_data.read())
