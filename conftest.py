import os
import json

from pytest import fixture
from playwright.sync_api import sync_playwright

from framework.base_page import BasePage


@fixture(autouse=True, scope='session')
def preconditions(request):
    environment = request.config.getoption('--environment')
    config_data = load_config(environment)
    print("create new user")
    #create_new_user(config_data['base_url'])
    yield config_data
    print("delete created user")

@fixture(scope='session')
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture(scope='session')
def get_browser(get_playwright, request):
    browser = request.config.getoption('--browser')
    headless = request.config.getini('headless')
    if not browser:
        browser = 'chromium'
    if headless == 'True':
        headless = True
    else:
        headless = False
    if 'chromium' in browser:
        browser_instance = get_playwright.chromium.launch(headless=headless)
    elif 'firefox' in browser:
        browser_instance = get_playwright.firefox.launch(headless=headless)
    elif 'webkit' in browser:
        browser_instance = get_playwright.webkit.launch(headless=headless)
    else:
        assert False, 'unsupported browser type'
    yield browser_instance
    browser_instance.close()


@fixture(scope='class')
def initial_page(preconditions, get_browser):
    app = BasePage(new_context=True, browser=get_browser, base_url=preconditions['base_url'])
    app.goto('/')
    yield app
    app.close()


def pytest_addoption(parser):
    parser.addoption('--environment', action='store', default='stage.json',
                     help='Path to the target environment config file')
    parser.addini('headless', help='Whether to execute browser in headless mode', default='False')


def load_config(file):
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
    with open(config_file) as config_data:
        return json.loads(config_data.read())
