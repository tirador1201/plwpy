import random
import string


def get_random_string(length):
    """
    choose from all lowercase letter
    :param length:
    :return:
    """
    result_str = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
    return result_str
