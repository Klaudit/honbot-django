import os.path
from os import remove
import time
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Context, loader
from PIL import Image
from random import randint
import advanced
import api_call
import banner
import match
import player
from error import error
import json


directory = str(os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'banners')) + '/'


def banner_view(request, name):
    path = directory + str(name) + ".png"
    # check file exists
    if os.path.isfile(path):
        # check file age
        now = time.time()
        fileCreation = os.path.getctime(path)
        day_ago = now - 60*60*24
        if fileCreation < day_ago:
            remove(path)
            return banner_view(request, name)
        else:
            # older than day remove
            response = HttpResponse(mimetype="image/png")
            img = Image.open(path)
            img.save(response, 'png')
            return response
    else:
        url = '/player_statistics/ranked/nickname/' + name
        data = api_call.get_json(url)
        if data is not None:
            statsdict = data
            s = player.player_math(statsdict, name, "rnk")
            now = time.time()
            response = HttpResponse(mimetype="image/png")
            img = banner.banner(s)
            img.save(response, 'png')
            img.save(directory + str(name) + ".png")
            return response
        else:
            response = HttpResponse()
            response.status_code = 404
            return response


def v404(request):
    return render_to_response('error.html')


def home(request):
    t = loader.get_template('home.html')
    random = randint(1, 74)
    c = Context({'random': random})
    return HttpResponse(t.render(c))


def match_view(request, match_id):
    stats = match.match(match_id)
    if stats is not None:
        t = loader.get_template('match.html')
        c = Context({'match_id': match_id, 'stats': stats})
        return HttpResponse(t.render(c))
    else:
        return error(request, "S2 Servers down or match id is incorrect. Try another match or try gently refreshing the page.")


def history(request, name):
    return HttpResponseRedirect("/player/" + name + "/")


def adv(request, match_id):
    data = advanced.main(match_id)
    if data is not None:
        t = loader.get_template('advanced.html')
        c = Context({'data': data, 'match_id': match_id})
        return HttpResponse(t.render(c))
    else:
        return error(request, "S2 Servers down or match id is incorrect. Try another match or try gently refreshing the page.")


def players(request, name):
    """
    controls the player show
    """
    mode = request.get_full_path().split('/')[1]
    if mode == "c":
        url = '/player_statistics/casual/nickname/' + name
        mode = "cs"
    elif mode == "p":
        url = '/player_statistics/public/nickname/' + name
        mode = "acc"
    else:
        url = '/player_statistics/ranked/nickname/' + name
        mode = "rnk"
    data = api_call.get_json(url)
    if data is not None:
        statsdict = data
        s = player.player_math(statsdict, name, mode)
        ### deliver to view ###
        t = loader.get_template('player.html')
        c = Context({'stats': s, 'mode': mode})
        return HttpResponse(t.render(c))
    else:
        return error(request, "S2 Servers down or name is incorrect. Try another name or try gently refreshing the page.")
