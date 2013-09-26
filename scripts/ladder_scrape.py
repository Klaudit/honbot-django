# This script scrapes all usernames from the heroes of newerth ladder and creates a CSV
import requests
import json

f = open('names.txt', 'w')
for page in xrange(1, 8180):
    print page
    url = "http://www.heroesofnewerth.com/ladder/view/ "+ str(page) + "?casual=false&jsonpls=1"
    try:
        raw = requests.get(url, timeout=12)
    except requests.exceptions.Timeout:
        pass
    content = raw.json()
    for player in content['rows']:
        name = player[2][6:-7]
        print name
        f.write(name + ', ')
