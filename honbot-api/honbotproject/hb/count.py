from django.db.models import F

from .models import APICount

from rest_framework.decorators import api_view, throttle_classes
from datetime import date


def apicount():
    today = date.today().strftime("%Y-%m-%d")
    current_count = APICount.objects.filter(date=today)
    if current_count.exists():
        current_count.update(count=F('count') + 1)
    else:
        APICount(count=1).save()


# @api_view(['GET'])
# @throttle_classes([])
# def getapicount(request, *pid):
#     players = Player.objects.filter(pk__in=list(pid))
#     serializer = PlayerSerializer(players, many=True)
#     return Response(serializer.data)