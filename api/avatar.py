from bs4 import BeautifulSoup
from urllib.request import build_opener
from pytz import utc
from app import RDB_HOST, RDB_PORT, HB_DB
import rethinkdb as r

from app import PHP

from datetime import datetime


def avatar(p):
    opener = build_opener()
    opener.addheaders.append(('Cookie', PHP))
    f = opener.open("http://forums.heroesofnewerth.com/member.php?" + str(p))
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
    rconn = r.connect(host=RDB_HOST, port=RDB_PORT, db=HB_DB)
    r.table('players').get(p).update({'avatar': img, 'avatar_updated': datetime.now(utc)}).run(rconn)
    rconn.close()
