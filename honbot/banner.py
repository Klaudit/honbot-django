from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import os.path

directory = str(os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'fonts')) + '/'


def banner(data):
    name_font = ImageFont.truetype(directory + "Prototype.ttf", 30)
    mmr_font = ImageFont.truetype(directory + "Prototype.ttf", 18)
    honbot_font = ImageFont.truetype(directory + "Prototype.ttf", 10)
    img = Image.new("RGBA", (400, 60), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.text((2, -2), data['nickname'], (255, 255, 255), font=name_font)
    draw.text((335, 0), "honbot.com", (200, 200, 200), font=honbot_font)
    draw.text((1, 38), "MMR: " + str(data['mmr']), (0, 128, 255), font=mmr_font)
    draw.text((98, 38), "|", (140, 140, 140), font=mmr_font)
    draw.text((110, 38), "TSR: " + str(data['TSR']), (220, 220, 220), font=mmr_font)
    draw.text((185, 38), "|", (140, 140, 140), font=mmr_font)
    draw.text((194, 38), " W: " + str(data['wins']), (0, 153, 0), font=mmr_font)
    next = 245 + (8 * len(str(data['wins'])))
    draw.text((next, 38), "|", (140, 140, 140), font=mmr_font)
    next += 15
    draw.text((next, 38), "L: " + str(data['losses']), (153, 0, 0), font=mmr_font)
    draw = ImageDraw.Draw(img)
    return img
