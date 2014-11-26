from __future__ import print_function
from config import token, q
from stats import count_increment

from flask import current_app
from requests import get, exceptions
from time import sleep


baseurl = 'http://api.heroesofnewerth.com'


def get_json(endpoint):
    url = ''.join([baseurl, endpoint, token])
    count = 0
    q.enqueue(count_increment, 'api')
    if current_app.debug:
        print(url)
    while True:
        try:
            raw = get(url)
        except exceptions.Timeout:
            count += 1
        if raw.status_code == 429 and count < 10:
            count += 1
            sleep(0.4)
        elif raw.status_code == 200:
            return raw.json()
        else:
            return None
