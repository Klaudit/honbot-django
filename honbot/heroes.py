from django.shortcuts import render_to_response
from django.views.decorators.cache import cache_page
from django.forms.models import model_to_dict
from honbot.models import Heroes, HeroUse, HeroData
from datetime import date
import json


def main(request):
    heroes = Heroes.objects.all().values()
    today = date.today().strftime("%Y-%m-%d")
    data = HeroData.objects.all().order_by('hero_id').values('cli_name')
    use = list(HeroUse.objects.filter(date=today).order_by('hero_id').values())
    for index, hero in enumerate(heroes):
        hero['popularity'] = use[index]['popularity']
        hero['cli_name'] = data[index]['cli_name']
    return render_to_response('heroes.html', {'heroes': heroes})


def hero(request, name):
	h = HeroData.objects.filter(cli_name=name).values()[0]
	use = HeroUse.objects.filter(hero_id=h['hero_id'])[:10]
	popularity = HeroUse.objects.filter(hero_id=h['hero_id'])[:1][0]
	return render_to_response('hero.html', {'hero': h, 'use': use, 'popularity': popularity})