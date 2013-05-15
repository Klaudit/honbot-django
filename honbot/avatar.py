from bs4 import BeautifulSoup
import urllib2
from django.http import HttpResponse

def avatar(request, number):
    opener = urllib2.build_opener()
    opener.addheaders.append(('Cookie', 'PHPSESSID=akibgsb94scim4hljas5q8i2h5; hf_userid=3837990; hf_password=703ef0c57f959dc7dcb8b27dddc82f15; hf_sessionhash=8929e6187eb86aec8a19018de6e47b3f'))
    f = opener.open("http://forums.heroesofnewerth.com/member.php?" + str(number))
    soup = BeautifulSoup(f.read())
    img = soup.find("img", {"alt": "Account Icon"})
    if img:
        return HttpResponse(str(img))
    else:
        return HttpResponse('<img src="/static/img/default_avatar.png">')

