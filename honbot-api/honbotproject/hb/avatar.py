from django.conf import settings
from django.utils.timezone import now
from bs4 import BeautifulSoup
from urllib.request import build_opener


def avatar(p):
    opener = build_opener()
    curl = settings.PHP
    opener.addheaders.append(('Cookie', curl))
    f = opener.open("http://forums.heroesofnewerth.com/member.php?" + str(p.player_id))
    soup = BeautifulSoup(f.read())
    try:
        img = soup.find("img", {"alt": "Account Icon"})['src']
    except:
        img = "images/default_avatar.png"
    if "account_icons" in img and "forums.heroesofnewerth.com" not in img:
        img = 'http://forums.heroesofnewerth.com/' + img
    if img and img != "http://forums.heroesofnewerth.com/" and img != "http://forums.heroesofnewerth.com//ui/fe2/store/icons/community.tga" and img != 'images/account_icons/default.png':
        pass
    else:
        img = "images/default_avatar.png"
    p.avatar = img
    p.avatar_updated = now()
    p.save(update_fields=['img', 'avatar_updated'])
