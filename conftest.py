from pytest import fixture

from framework.base_page import BasePage
from pages.home_page import HomePage
from utils.api_utils import create_new_email
from utils.common_utils import read_json


@fixture(autouse=True, scope='session')
def read_config(request):
    '''
    Reads config from the cli
    :param request: cli request
    :return: data from json file
    '''
    environment = request.config.getoption('--environment')
    config_data = read_json(environment)
    yield config_data


@fixture(scope='session')
def generate_magic_link(page, read_config):
    '''
    Necessary to generate magic link for logging to the system
    :return:
    '''
    print("create new email")
    url_for_magic_link = read_config['url_for_magic_link']
    page_instance = page
    response = page_instance.request.post(url_for_magic_link)
    magic_link = response.json().magic_link
    yield magic_link


@fixture()
def initial_page(read_config, browser):
    '''
    Launches browser and return the base page instance
    :param read_config: data from config file
    :param browser: plw fixture for launching browser
    :return: base page instance
    '''
    base = BasePage(browser=browser, base_url=read_config['base_url'])
    base.goto('/')
    yield base
    base.close()


@fixture()
def home_page(initial_page, generate_magic_link):
    '''
    Launches browser and return the homepage instance: when user has already logged in
    :param read_config: data from config file
    :param browser: plw fixture for launching browser
    :return: homepage instance
    '''
    # get magic link from the API
    link = generate_magic_link
    initial_page.goto(link, False)
    home = HomePage(initial_page)
    yield home


@fixture()
def page(browser):
    '''
    Return random page which can be used for API requests and validation based on the url
    :param browser:
    :return:
    '''
    context = browser.new_context(base_url="")
    page = context.new_page()
    yield page
    page.close()
    context.close()


def pytest_addoption(parser):
    '''
    Adds param to the cli
    :param parser:
    :return:
    '''
    parser.addoption('--environment', action='store', default='stage.json',
                     help='Path to the target environment config file')
