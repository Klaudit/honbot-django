from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context, Template
from django.views.decorators.cache import cache_page
from .models import Matches, PlayerCount, PlayerStats, MatchCount, PlayerMatches, APICount
from api_call import pure
from datetime import date
from random import randint
from json import dumps


@cache_page(60 * 10)
def server_status(request):
    json = pure('/items/id/10')
    test = """{"cli_name":"Item_CrushingClaws","attributes":{"icon":"Item_CrushingClaws.jpg","cost":"150","isPassive":false,"recipeCost":"150","usedIn":["Item_Strength5","Item_BloodChalice"],"strings":{"description_simple":"^9773 Strength^*","effect_header":"Status Effect(s)","search_terms":"crushingclaws,gauntletsofogrestrength,gauntlets,ogre,3s,3str,3strength,cc,strength,str,crushing,claws","shop_categories":"Filter_Strength","shop_flavor":"Crushing Claws are filled with clockwork gears, sprockets, and springs that give a boost of strength to whomever wears them.  Despite their role in numerous practical jokes gone awry, these gauntlets remain in widespread use in the ranks."},"name":"Crushing Claws"}}"""
    try:
        if json.text == test:
            return HttpResponse('<span class="text-success">Working</span>')
        else:
            return HttpResponse('<span class="text-danger">Down, Honbot will have trouble working</span>')
    except:
        return HttpResponse('<span class="text-danger">Down, Honbot will have trouble working</span>')


def new_count(countobj, dataobj):
    count = dataobj.objects.count()
    countobj(count=count).save()
    return count


def current_count(countobj, dataobj, today):
    current_count = countobj.objects.filter(date=today)
    if current_count.exists():
        return current_count[0].count
    else:
        return new_count(countobj, dataobj)


@cache_page(60)
def database_count(request):
    today = date.today().strftime("%Y-%m-%d")
    counts = {}
    counts['matches'] = current_count(MatchCount, Matches, today)
    counts['players'] = current_count(PlayerCount, PlayerStats, today)
    try:
        counts['apicount'] = APICount.objects.filter(date=today)[0].count
    except:
        APICount(count=1).save()
        counts['api'] = 1
    return HttpResponse(dumps(counts), content_type="application/json")