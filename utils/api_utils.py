import requests
import re

def create_new_email(url):
    response = requests.post(url, params={})
    return response.text


def delete_user(url):
    requests.delete(url)