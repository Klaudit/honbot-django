from config import PHP
from app import db

from bs4 import BeautifulSoup
from urllib.request import build_opener
from flask.ext.rq import job

from datetime import datetime


@job
def avatar(p):
    opener = build_opener()
    opener.addheaders.append(('Cookie', PHP))
    f = opener.open("http://forums.heroesofnewerth.com/member.php?" + str(p))
    soup = BeautifulSoup(f.read())
    try:
        img = soup.find("img", {"alt": "Account Icon"})['src']
    except:
        img = "assets/images/default_avatar.png"
    if "account_icons" in img and "forums.heroesofnewerth.com" not in img:
        img = 'http://forums.heroesofnewerth.com/' + img
    if img and img != "http://forums.heroesofnewerth.com/" and img != "http://forums.heroesofnewerth.com//ui/fe2/store/icons/community.tga" and img != 'assets/images/account_icons/default.png':
        pass
    else:
        img = "images/default_avatar.png"
    p.avatar = img
    p.avatar_updated = datetime.utcnow()
    db.session.commit()
