import os
import json
from utils.api_utils import create_new_user

from _pytest.fixtures import fixture

@fixture(autouse=True, scope="session")
def preconditions(request):
    environment = request.config.getoption('--environment')
    config_data = load_config(environment)
    print("create new user")
    create_new_user(config_data['base_url'])
    yield
    print("delete created user")


def pytest_addoption(parser):
    parser.addoption('--environment', action='store', default = 'stage.json',
                     help='Path to the target environment config file')


def load_config(file):
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
    with open(config_file) as config_data:
        return json.loads(config_data.read())
