from requests import get, exceptions
from time import sleep

from os import environ


baseurl = 'http://api.heroesofnewerth.com'
token = '/?token=%s' % environ.get('API_TOKEN')


def get_json(endpoint):
    url = ''.join([baseurl, endpoint, token])
    count = 0
    while True:
        try:
            raw = get(url)
        except exceptions.Timeout:
            count += 1
        if raw.status_code == 429 and count < 10:
            count += 1
            sleep(0.5)
        elif raw.status_code == 200:
            return raw.json()
            break
        else:
            return None
