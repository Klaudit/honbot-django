from django.conf import settings
from requests import get, exceptions
from time import sleep


baseurl = 'http://api.heroesofnewerth.com'
token = '/?token=%s' % settings.TOKEN
debug = settings.DEBUG


def get_json(endpoint):
    url = ''.join([baseurl, endpoint, token])
    count = 0
    while True:
        try:
            raw = get(url, timeout=5)
            if debug:
                print(raw.url)
                print(raw.status_code)
        except exceptions.Timeout:
            if debug:
                print('timeout')
            count += 1
        if raw.status_code == 429 and count < 10:
            count += 1
            sleep(0.5)
        elif raw.status_code == 200:
            return raw.json()
            break
        else:
            return None
