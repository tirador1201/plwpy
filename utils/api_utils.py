import requests


from utils.common_utils import get_random_string

API_URL = 'https://www.1secmail.com/api/v1/'
EMAIL_URL = 'https://www.1secmail.com/'
DOMAIN = '1secmail.net'

def create_new_email():
    email = f'{get_random_string(10)}'
    registration_link = f'{EMAIL_URL}?login=={email}&domain={DOMAIN}'
    requests.get(registration_link)
    return f'{email}@{DOMAIN}'

def retrieveCode():
    emails_link = f'{API_URL}?action=getMessages&login=qqnihefhiy&domain={DOMAIN}'
    response = requests.get(emails_link)
    print(response)
