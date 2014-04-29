# Things currently wrong:
# bad fallbacks
# repeating code for saving banner
# updaring the player is called poorly
# poorly written and huge ifs
# has to be updated and tested for all use cases
# banner creating code is okay
# must try to get a new one before removing old one and fucking oneself

from django.http import HttpResponseBadRequest, HttpResponse

from .models import PlayerStats
from player import update_player

from PIL import Image, ImageDraw, ImageFont

from time import time
from os import remove, path


directory = str(path.join(path.abspath(path.dirname(path.dirname(__file__))), 'banners')) + '/'
fonts = str(path.join(path.abspath(path.dirname(path.dirname(__file__))), 'fonts')) + '/'

# BANNER PROCESS
#  check if banner already exists
#  try to create new banner
#  check banner age and decide if too old
#  if banner is too old update stats and serve new
#  give up and deliver old banner


def banner_view(request, name):
    if '/' in name:
        name = name.split('/')[1]
    location = directory + str(name) + ".png"
    # check file exists
    exists = path.isfile(location)
    # if doesn't exist create new or 404
    if not exists:
        return new_banner(request, location, name, exists)
    # check file age
    now = time()
    fileCreation = path.getctime(location)
    # 86400 is one day in seconds
    day_ago = now - (86400)
    if fileCreation < day_ago:
        # try to make new banner
        return new_banner(request, location, name, exists)
    else:
        return serve_banner(request, Image.open(location))


def serve_banner(request, img):
    """
    serves banner correct http response
    """
    response = HttpResponse(mimetype="image/png")
    img.save(response, 'png')
    return response


def new_banner(request, location, name, exists):
    """
    create a new banner or serves old one depending on if the api is currently working
    sends 404 if there isn't an existing banner and api returned nothing
    doesn't get banner if player doesn't exist in database
    """
    p = PlayerStats.objects.filter(nickname=name).first()
    if p is None:
        return HttpResponseBadRequest()
    stats_updated = update_player(p.player_id, "rnk")
    if stats_updated:
        p = PlayerStats.objects.filter(nickname=name).first()
        if exists:
            remove(location)
        img = banner(p)
        img.save(directory + str(name) + ".png")
        return serve_banner(request, img)
    else:
        if exists:
            return serve_banner(request, location)
        else:
            return HttpResponseBadRequest()


def banner(data):
    name_font = ImageFont.truetype(fonts + "Prototype.ttf", 30)
    mmr_font = ImageFont.truetype(fonts + "Prototype.ttf", 18)
    honbot_font = ImageFont.truetype(fonts + "Prototype.ttf", 10)
    img = Image.new("RGBA", (400, 60), (25, 25, 25))
    draw = ImageDraw.Draw(img)
    draw.text((2, -2), data.nickname, (255, 255, 255), font=name_font)
    draw.text((335, 0), "honbot.com", (200, 200, 200), font=honbot_font)
    draw.text((1, 38), "MMR: " + str(data.mmr), (0, 128, 255), font=mmr_font)
    draw.text((98, 38), "|", (140, 140, 140), font=mmr_font)
    draw.text((110, 38), "TSR: " + str(data.TSR), (220, 220, 220), font=mmr_font)
    draw.text((185, 38), "|", (140, 140, 140), font=mmr_font)
    draw.text((194, 38), " W: " + str(data.wins), (0, 153, 0), font=mmr_font)
    next = 245 + (8 * len(str(data.wins)))
    draw.text((next, 38), "|", (140, 140, 140), font=mmr_font)
    next += 15
    draw.text((next, 38), "L: " + str(data.losses), (153, 0, 0), font=mmr_font)
    draw = ImageDraw.Draw(img)
    return img
