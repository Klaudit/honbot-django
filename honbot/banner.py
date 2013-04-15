from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import os.path

directory = str(os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'fonts')) + '/'


def banner():
    name_font = ImageFont.truetype(directory + "Prototype.ttf", 30)
    mmr_font = ImageFont.truetype(directory + "Prototype.ttf", 18)
    honbot_font = ImageFont.truetype(directory + "Prototype.ttf", 10)
    img = Image.new("RGBA", (400, 60), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.text((2, -2), "stridex", (255, 255, 255), font=name_font)
    draw.text((335, 0), "honbot.com", (200, 200, 200), font=honbot_font)
    draw.text((1, 38), "MMR: 1665", (0, 128, 255), font=mmr_font)
    draw.text((98, 38), "|", (140, 140, 140), font=mmr_font)
    draw.text((110, 38), "TSR: 6.7", (220, 220, 220), font=mmr_font)
    draw.text((185, 38), "|", (140, 140, 140), font=mmr_font)
    draw.text((194, 38), " W: 592", (0, 153, 0), font=mmr_font)
    draw.text((265, 38), "|", (140, 140, 140), font=mmr_font)
    draw.text((280, 38), "L: 567", (153, 0, 0), font=mmr_font)
    draw.text((340, 38), "|", (140, 140, 140), font=mmr_font)
    draw.text((355, 38), "51%", (140, 140, 140), font=mmr_font)
    draw = ImageDraw.Draw(img)
    #img.save("banner2.jpg")
    return img
