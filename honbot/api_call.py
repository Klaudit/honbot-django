import requests
from time import sleep
from django.conf import settings


def get_json(endpoint):
    """
     returns json data for requested digg endpoint
    """
    url = ''.join(['http://api.heroesofnewerth.com', endpoint, '/?token=%s' % settings.TOKEN])
    raw = ''
    print url
    while True:
        count = 0
        try:
            raw = requests.get(url, timeout=0.8)
        except requests.exceptions.Timeout:
            count += 1
            try:
                raw = requests.get(url, timeout=2)
            except requests.exceptions.Timeout:
                return None
        if raw.status_code == 429 and count < 5:
            count += 1
            sleep(0.2)
        elif raw.status_code == 200:
            break
        else:
            return None
    return raw.json()


def pure(endpoint):
    """
    returns data for requested digg endpoint
    """
    url = ''.join(['http://api.heroesofnewerth.com', endpoint, '/?token=%s' % settings.TOKEN])
    raw = ''
    print url
    while True:
        count = 0
        try:
            raw = requests.get(url, timeout=0.8)
        except requests.exceptions.Timeout:
            count += 1
            try:
                raw = requests.get(url, timeout=2)
            except requests.exceptions.Timeout:
                return None
        if raw.status_code == 429 and count < 5:
            count += 1
            sleep(0.2)
        elif raw.status_code == 200:
            break
        else:
            return None
    return raw
