from django.db.models import F

from .models import APICount
from datetime import date


def apicount():
    today = date.today().strftime("%Y-%m-%d")
    current_count = APICount.objects.filter(date=today)
    if current_count.exists():
        current_count.update(count=F('count') + 1)
    else:
        APICount(count=1).save()
