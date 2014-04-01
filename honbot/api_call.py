from datetime import date
from django.conf import settings
from django.db.models import F
from .models import APICount
from requests import get, exceptions
from time import sleep
from thread import start_new_thread


baseurl = 'http://api.heroesofnewerth.com'
token = '/?token=%s' % settings.TOKEN
debug = settings.DEBUG


def get_json(endpoint):
    start_new_thread(apicount, ())
    url = ''.join([baseurl, endpoint, token])
    raw = ''
    if debug:
        print url
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


def pure(endpoint):
    start_new_thread(apicount, ())
    url = ''.join([baseurl, endpoint, token])
    raw = ''
    while True:
        count = 0
        try:
            raw = get(url, timeout=0.5)
            if raw.status_code == 429:
                count += 1
                sleep(0.2)
            elif raw.status_code == 200:
                break
        except exceptions.Timeout:
            count += 1
            sleep(0.2)
        if count > 2:
            return None
    return raw


def apicount():
    today = date.today().strftime("%Y-%m-%d")
    current_count = APICount.objects.filter(date=today)
    if current_count.exists():
        current_count.update(count=F('count') + 1)
    else:
        APICount(count=1).save()
