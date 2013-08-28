from os import path, remove
from honbot.models import Matches, Chat, PlayerMatches
import requests
from zipfile import ZipFile

directory = str(path.join(path.abspath(path.dirname(path.dirname(__file__))), 'match')) + '/'


def download(match_id, url):
    url = url[:-9] + 'zip'
    # download file
    r = requests.get(url)
    if r.status_code == 404:
        return False
    # write zip file to directory
    with open(directory + str(match_id) +".zip", "wb") as filesave:
        filesave.write(r.content)
    # unzip
    z = ZipFile(directory + str(match_id) + '.zip')
    z.extract(z.namelist()[0], directory)
    z.close()
    # delete zip
    remove(directory + str(match_id) + '.zip')
    return True

def parse(match_id):
    pass