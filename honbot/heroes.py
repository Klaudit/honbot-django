from django.shortcuts import render_to_response
from django.views.decorators.cache import cache_page
from django.forms.models import model_to_dict
from honbot.models import Heroes, HeroUse
from datetime import date
import json


def main(request):
    heroes = Heroes.objects.all().values()
    today = date.today().strftime("%Y-%m-%d")
    use = list(HeroUse.objects.filter(date=today).order_by('hero_id').values())
    print use
    for index, hero in enumerate(heroes):
        hero['popularity'] = use[index]['popularity']
    return render_to_response('heroes.html', {'heroes': heroes})