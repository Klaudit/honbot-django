from django.http import HttpResponse
from api_call import get_json
from datetime import datetime
from .models import PlayerStats
from os import remove, path
from PIL import Image, ImageDraw, ImageFont
from player import player_math, player_save
from time import time


directory = str(path.join(path.abspath(path.dirname(path.dirname(__file__))), 'banners')) + '/'
fonts = str(path.join(path.abspath(path.dirname(path.dirname(__file__))), 'fonts')) + '/'


def banner_view(request, name):
    if '/' in name:
        name = name.split('/')[1]
    location = directory + str(name) + ".png"
    # check file exists
    if path.isfile(location):
        # check file age
        now = time()
        fileCreation = path.getctime(location)
        day_ago = now - 60*60*24
        if fileCreation < day_ago:
            remove(location)
            return banner_view(request, name)
        else:
            # older than day remove
            response = HttpResponse(mimetype="image/png")
            img = Image.open(location)
            img.save(response, 'png')
            return response
    else:
        p = PlayerStats.objects.filter(nickname=name).first()
        url = '/player_statistics/ranked/nickname/' + name
        if p is not None:
            tdelta = datetime.now() - datetime.strptime(str(p.updated), "%Y-%m-%d %H:%M:%S")
            if tdelta.seconds + (tdelta.days * 86400) < 1000:
                response = HttpResponse(mimetype="image/png")
                img = banner(p)
                img.save(response, 'png')
                img.save(directory + str(name) + ".png")
                return response
        data = get_json(url)
        if data is not None:
            statsdict = data
            p = player_math(statsdict, "rnk")
            player_save(p, "rnk")
            response = HttpResponse(mimetype="image/png")
            img = banner(p)
            img.save(response, 'png')
            img.save(directory + str(name) + ".png")
            return response
        else:
            response = HttpResponse()
            response.status_code = 404
            return response


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
