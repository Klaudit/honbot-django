from bs4 import BeautifulSoup
from urllib2 import build_opener
from django.http import HttpResponse
from .models import PlayerIcon
from datetime import datetime
from django.conf import settings


def avatar(request, number, width):
    p = PlayerIcon.objects.filter(player_id=number)
    if p.exists():
        tdelta = datetime.now() - datetime.strptime(str(p.values()[0]['updated']), "%Y-%m-%d %H:%M:%S")
        if tdelta.days < 25:
            return HttpResponse('<img style="width:' + str(width) + 'px;" src="' + p.values('avatar')[0]['avatar'] + '">')
    opener = build_opener()
    curl = settings.PHP
    opener.addheaders.append(('Cookie', curl))
    f = opener.open("http://forums.heroesofnewerth.com/member.php?" + str(number))
    soup = BeautifulSoup(f.read())
    try:
        img = soup.find("img", {"alt": "Account Icon"})['src']
    except:
        PlayerIcon(player_id=number, avatar="/static/img/default_avatar.png").save()
        return HttpResponse('<img style="width:' + str(width) + 'px;" src="/static/img/default_avatar.png">')
    if "account_icons" in img:
        img = 'http://forums.heroesofnewerth.com/' + img
    if img and img != "http://forums.heroesofnewerth.com/" and img != "http://forums.heroesofnewerth.com//ui/fe2/store/icons/community.tga" and img != 'images/account_icons/default.png':
        PlayerIcon(player_id=number, avatar=str(img)).save()
        return HttpResponse('<img style="width:' + str(width) + 'px;" src="' + img + '">')
    else:
        PlayerIcon(player_id=number, avatar="/static/img/default_avatar.png").save()
        return HttpResponse('<img style="width:' + str(width) + 'px;" src="/static/img/default_avatar.png">')
