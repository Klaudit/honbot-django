from bs4 import BeautifulSoup
import requests
from json import dumps

url = 'https://www.heroesofnewerth.com/heroes/'
r = requests.get(url)

soup = BeautifulSoup(r.text)
heroes = []
for a in soup.find_all("div", attrs={"class": "filterObjectGrid"}):
    try:
        heroes.append(a.select("a")[0].get('href'))
    except:
        pass
counter = 0

result = []
for hero in heroes:
    url = 'https://www.heroesofnewerth.com' + hero
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    alts = int(soup.find("p", class_="subTitle fontM").text[-1])
    for x in xrange(alts):
        with open('src/assets/images/largehero/' + str(counter) + '.png', 'wb') as handle:
            url = 'https://www.heroesofnewerth.com/images/heroes/'
            if x == 0:
                url += str(hero.split('/')[-1].split("#")[0]) + "/store_hero.png"
            elif x == 1:
                url += str(hero.split('/')[-1].split("#")[0]) + "/store_alt.png"
            else:
                url += str(hero.split('/')[-1].split("#")[0]) + "/store_alt" + str(x) + ".png"
            print url
            result.append(url)
            # this would download the files
            # request = requests.get(url, stream=True)
            # if request.status_code == 200:
            #     for block in request.iter_content(1024):
            #         if not block:
            #             break
            #         handle.write(block)
            #     counter += 1
print dumps(result)
