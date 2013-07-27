from bs4 import BeautifulSoup
import urllib2
from django.http import HttpResponse
from honbot.models import PlayerIcon
from datetime import datetime
from django.conf import settings


def avatar(request, number, width):
    p = PlayerIcon.objects.filter(player_id=number)
    if bool(p):
        tdelta = datetime.now() - datetime.strptime(str(p.values()[0]['updated']), "%Y-%m-%d %H:%M:%S")
        if tdelta.days < 14:
            return HttpResponse('<img style="width:' + width + 'px;" src="' + p.values()[0]['avatar'] + '">')
    opener = urllib2.build_opener()
    curl = settings.PHP
    opener.addheaders.append(('Cookie', curl))
    f = opener.open("http://forums.heroesofnewerth.com/member.php?" + str(number))
    soup = BeautifulSoup(f.read())
    img = soup.find("img", {"alt": "Account Icon"})['src']
    if img:
        PlayerIcon(player_id=number, avatar=str(img)).save()
        return HttpResponse('<img style="width:' + width + 'px;" src="' + img + '">')
    else:
        return HttpResponse('<img style="width:' + width + 'px;" src="/static/img/default_avatar.png">')
