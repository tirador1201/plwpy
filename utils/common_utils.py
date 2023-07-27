import json
import os
import random
import string
from pathlib import Path

def get_project_root() -> Path:
    '''
    Get root of the project
    :return: root path
    '''
    return Path(__file__).parent.parent

def get_random_string(length):
    """
    choose from all lowercase letter
    :param length:
    :return:
    """
    result_str = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
    return result_str

def read_json(file):
    json_data = os.path.join(get_project_root(), file)
    with open(json_data) as data:
        return json.loads(data.read())