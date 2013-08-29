from os import path, remove
from honbot.models import Matches, Chat, PlayerMatches
import requests
import codecs
from zipfile import ZipFile

directory = str(path.join(path.abspath(path.dirname(path.dirname(__file__))), 'match')) + '/'


def download(match_id, url):
    return True #remove this dev only
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
    log = honlog(match_id)
    log.get_order()
    log.open_file()
    log.run()
    log.out()

class honlog:
    def __init__(self, match_id):
        self.match_id = match_id
        self.real_order, self.order_covert = {}, {}
        self.logfile = file
        self.date, self.time = '', ''
        self.names, self.psr = [0]*10, [0]*10,
    
    def run(self):
        for line in self.logfile:
            word = line.split()[0]
            try:
                methodToCall = getattr(self, word)
                methodToCall(line)
            except AttributeError:
                pass

    def get_order(self):
        """
        This gets the proper order of players from the db
        creates self.real_order[player_id]=real_position
        """
        positions = PlayerMatches.objects.filter(match_id=self.match_id).order_by('position').values('position', 'player_id')
        for p in positions:
            self.real_order[str(p['player_id'])]=p['position']

    def open_file(self):
        self.logfile = codecs.open(directory + 'm' + self.match_id + '.log', encoding='utf-16-le', mode='rb').readlines()
        self.INFO_DATE(self.logfile.pop(0))

    def INFO_DATE(self, line):
        """
        [\ufeffINFO_DATE', u'date:"2013/30/03"', u'time:"17:14:52"]
        has a fucking byte order mark http://en.wikipedia.org/wiki/Byte_order_mark
        """
        d = line.split()
        self.date = d[1].split(':')[1][1:-1]
        self.time = d[2].split('"')[1]

    def PLAYER_CONNECT(self, line):
        """
        PLAYER_CONNECT player:0 name:"NAMENAMENAME" id:3252583 psr:1522.0000
        spectators too
        PLAYER_CONNECT time:1617600 player:13 name:"[bMcE]Smexystyle`" id:7399320 psr:-1.0000
        """
        l = line.split()
        psr = int(float(l[-1].split(':')[1]))
        if psr != -1:
            name = l[2].split(':')[1][1:-1] # get name
            name = name.split(']')[-1] # remove clan tag
            position = int(l[1].split(':')[1])
            pid = str(l[-2].split(':')[1])
            self.names[self.real_order[pid]] = name
            self.psr[self.real_order[pid]] = psr
            self.order_convert[position] = self.real_order[pid]
        else:
            name = l[3].split(':')[1][1:-1]
            for letter in name:
                if letter == '[':
                    name = name.split(']')[1]
                else:
                    break
            self.spectators[position] = name

    def out(self):
        print self.real_order
        print self.names
        print self.order_convert