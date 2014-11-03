from pytz import utc
from datetime import datetime


def div(x, y):
    try:
        return round(float(x) / float(y), 4)
    except ZeroDivisionError:
        return 0


def divmin(x, y):
    try:
        return round(float(x) / (float(y) / 60), 4)
    except ZeroDivisionError:
        return 0


def needs_update(previous_date, age_allowed):
    nowutc = datetime.now(utc)
    tdelta = nowutc - previous_date
    if (tdelta.seconds + (tdelta.days * 86400)) > age_allowed:
        return True
    return False
