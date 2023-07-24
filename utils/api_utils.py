import requests


def create_new_user(url):
    response = requests.post(url, params={})
    return response.text


def delete_user(url):
    requests.delete(url)