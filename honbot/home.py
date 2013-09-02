from django.shortcuts import render_to_response
from django.http import HttpResponse
import api_call
from random import randint
from honbot.models import Matches, PlayerCount, PlayerStats
import datetime
from django.views.decorators.cache import cache_page
from django.template import Context, Template


@cache_page(60 * 5)
def server_status(request):
    json = api_call.pure('/items/id/10')
    test = """{"cli_name":"Item_CrushingClaws","attributes":{"icon":"Item_CrushingClaws.jpg","cost":"150","isPassive":false,"recipeCost":"150","usedIn":["Item_Strength5","Item_BloodChalice"],"strings":{"description_simple":"^9773 Strength^*","effect_header":"Status Effect(s)","search_terms":"crushingclaws,gauntletsofogrestrength,gauntlets,ogre,3s,3str,3strength,cc,strength,str,crushing,claws","shop_categories":"Filter_Strength","shop_flavor":"Crushing Claws are filled with clockwork gears, sprockets, and springs that give a boost of strength to whomever wears them.  Despite their role in numerous practical jokes gone awry, these gauntlets remain in widespread use in the ranks."},"name":"Crushing Claws"}}"""
    try:
        if json.text == test:
            return HttpResponse('<li><span class="text-success">Working</span></li>')
        else:
            return HttpResponse('<span class="text-danger">Down: Honbot will have trouble working</span>')
    except:
        return HttpResponse('<span class="text-danger">Down: Honbot will have trouble working</span>')

@cache_page(60)
def match_count(request):
    """
    Returns the current number of matches stored in the database
    """
    matches = Matches.objects.count()
    t = Template('{% load humanize %}Matches: {{ matches|intcomma }}')
    c = Context({'matches': matches})
    return HttpResponse(t.render(c))

@cache_page(60)
def player_count(request):
    """
    Returns the current number of players in the database
    """
    today = datetime.date.today().strftime("%Y-%m-%d")
    current_count = PlayerCount.objects.filter(date=today)
    if current_count.exists():
        count = current_count[0].count
    else:
        count = PlayerStats.objects.count()
        PlayerCount(count=count).save()
    t = Template('{% load humanize %}Players: {{ count|intcomma }}')
    c = Context({'count': count})
    return HttpResponse(t.render(c))


def home(request):
    """
    Makes a random background choice and ships that shit
    """
    random = randint(1, 74)
    return render_to_response('home.html', {'random': random})
