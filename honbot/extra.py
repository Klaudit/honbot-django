# This file is intended for extra pages like site stats and possibly an about page
from django.shortcuts import render_to_response
from .models import PlayerCount, MatchCount, APICount
from django_cron.models import CronJobLog
from django.views.decorators.cache import cache_page
from django.db.models import Avg


@cache_page(1000)
def stats(request):
    players = PlayerCount.objects.all().order_by('-date')[:20][::-1]
    matches = MatchCount.objects.all().order_by('-date')[:20][::-1]
    cronjobs = CronJobLog.objects.all().order_by('-start_time')[:20]
    api = APICount.objects.all().order_by('-date')[:20][::-1]
    apiavg = int(APICount.objects.all().aggregate(Avg('count'))['count__avg'])
    return render_to_response('sitestats.html', {'players':players, 'matches':matches, 'api':api, 'cronjobs': cronjobs, 'apiavg': apiavg})