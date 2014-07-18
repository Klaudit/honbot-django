from django.conf import settings
from requests import get, exceptions
from time import sleep


baseurl = 'http://api.heroesofnewerth.com'
token = '/?token=%s' % settings.TOKEN
debug = settings.DEBUG


def get_json(endpoint):
    url = ''.join([baseurl, endpoint, token])
    raw = ''
    if debug:
        print(url)
    while True:
        count = 0
        try:
            raw = get(url, timeout=0.8)
        except exceptions.Timeout:
            count += 1
            try:
                raw = get(url, timeout=2)
            except exceptions.Timeout:
                return None
        if raw.status_code == 429 and count < 5:
            count += 1
            sleep(0.2)
        elif raw.status_code == 200:
            break
        else:
            return None
    return raw.json()

