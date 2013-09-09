import requests
from time import sleep
from django.conf import settings
from honbot.models import APICount
from django.db.models import F
import datetime


def get_json(endpoint):
    """
     returns json data for requested digg endpoint
    """
    apicount()
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
    apicount()
    url = ''.join(['http://api.heroesofnewerth.com', endpoint, '/?token=%s' % settings.TOKEN])
    raw = ''
    print url
    while True:
        count = 0
        try:
            raw = requests.get(url, timeout=0.5)
        except requests.exceptions.Timeout:
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
    today = datetime.date.today().strftime("%Y-%m-%d")
    current_count = APICount.objects.filter(date=today)
    if current_count.exists():
        current_count.update(count=F('count') + 1)
    else:
        APICount(count=1).save()