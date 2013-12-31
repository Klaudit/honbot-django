from __future__ import print_function

from datetime import date
from django.conf import settings
from django.db.models import F
from .models import APICount
from requests import get, exceptions
from time import sleep


baseurl = 'http://api.heroesofnewerth.com'
token = '/?token=%s' % settings.TOKEN


def get_json(endpoint):
    apicount()
    url = ''.join([baseurl, endpoint, token])
    raw = ''
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


def pure(endpoint):
    apicount()
    url = ''.join([baseurl, endpoint, token])
    raw = ''
    print(url)
    while True:
        count = 0
        try:
            raw = get(url, timeout=0.5)
        except exceptions.Timeout:
            count += 1
        if raw.status_code == 429 and count < 2:
            count += 1
            sleep(0.2)
        elif raw.status_code == 200:
            break
        else:
            return None
    return raw


def apicount():
    today = date.today().strftime("%Y-%m-%d")
    current_count = APICount.objects.filter(date=today)
    if current_count.exists():
        current_count.update(count=F('count') + 1)
    else:
        APICount(count=1).save()
