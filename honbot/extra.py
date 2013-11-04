# This file is intended for extra pages like site stats and possibly an about page
from django.shortcuts import render_to_response
from honbot.models import PlayerMatchCount, PlayerCount, MatchCount, APICount
from django_cron.models import CronJobLog
from django.views.decorators.cache import cache_page


def stats(request):
    players = PlayerCount.objects.all().order_by('-date')[:10][::-1]
    matches = MatchCount.objects.all().order_by('-date')[:10][::-1]
    playermatches = PlayerMatchCount.objects.all().order_by('-date')[:10][::-1]
    cronjobs = CronJobLog.objects.all().reverse()[:20]
    api = APICount.objects.all()
    return render_to_response('sitestats.html', {'players':players, 'matches':matches, 'playermatches':playermatches, 'api':api, 'cronjobs': cronjobs})