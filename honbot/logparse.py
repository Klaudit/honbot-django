# this file is replaceing magic.py
import re
from os import path, remove
from honbot.models import Chat, Builds, PlayerMatches
import requests
import codecs
from zipfile import ZipFile
from time import strftime, gmtime
import json

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
    log = honlog(match_id)
    log.setup()
    log.open_file()
    log.run()
    log.out()
    log.save()

class honlog:
    def __init__(self, match_id):
        self.match_id = match_id
        self.real_order, self.order_convert, self.teams = {}, {}, {}
        self.logfile = file
        self.date, self.time = '', ''
        self.names, self.psr, self.heroes, self.win, self.msg = [0]*10, [0]*10, [0]*10, [0]*10, []
        self.builds = [[] for i in range(10)]
    
    def run(self):
        for line in self.logfile:
            word = line.split()[0]
            try:
                methodToCall = getattr(self, word)
                methodToCall(line)
            except AttributeError:
                pass

    def setup(self):
        """
        This gets the proper order of players from the db
        creates self.real_order[player_id]=real_position
        """
        positions = PlayerMatches.objects.filter(match_id=self.match_id).order_by('position').values('position', 'player_id', 'hero', 'team', 'win')
        for p in positions:
            pid = str(p['player_id'])
            self.real_order[pid] = p['position']
            self.heroes[p['position']] = p['hero']
            self.teams[p['position']] = p['team']

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
        name = l[2].split(':')[1][1:-1] # get name
        name = name.split(']')[-1] # remove clan tag
        if psr != -1:
            position = int(l[1].split(':')[1])
            pid = str(l[-2].split(':')[1])
            self.names[self.real_order[pid]] = name
            self.psr[self.real_order[pid]] = psr
            self.order_convert[position] = self.real_order[pid]
        else:
            self.spectators[position] = name

    def save(self):
        c = Chat(match_id=self.match_id, json=json.dumps(self.msg))
        c.save()
        for index, build in enumerate(self.builds):
            if len(build) != 0 and self.heroes[index] != 0:
                difference = 25 - len(build)
                for d in range(difference):
                    build.append(0)
                b = Builds(match_id=self.match_id, json=json.dumps(build[:25-difference]), 
                           hero=self.heroes[index], nickname=self.names[index], 
                           mmr=self.psr[index], win=self.win[index], position=index,
                           lvl1=build[0], lvl2=build[1], lvl3=build[2], lvl4=build[3],
                           lvl5=build[4], lvl6=build[5], lvl7=build[6], lvl8=build[7],
                           lvl9=build[8], lvl10=build[9], lvl11=build[10], lvl12=build[11],
                           lvl13=build[12], lvl14=build[13], lvl15=build[14], lvl16=build[15],
                           lvl17=build[16], lvl18=build[17], lvl19=build[18], lvl20=build[19],
                           lvl21=build[20], lvl22=build[21], lvl23=build[22], lvl24=build[23], lvl25=build[24])
                b.save()

    def set_time(self, time):
        if int(time) < 3599999:
            time = strftime('%M:%S', gmtime(int(time) // 1000))
        else:
            time = strftime('%H:%M:%S', gmtime(int(time) // 1000))
        return time

    def ABILITY_UPGRADE(self, line):
        """
        ABILITY_UPGRADE time:0 x:1662 y:995 z:101 player:1 team:1 name:"Ability_Empath1" level:1 slot:0
        """
        l = line.split()
        ability = l[7].split('"')[1]
        if ability != 'Ability_AttributeBoost':
            ability = int(re.sub("\D", "", ability)[-1:])
        else:
            ability = 5
        self.builds[self.order_convert[int(l[5].split(':')[1])]].append(ability)

    def PLAYER_CHAT(self, line):
        """
        returns dict of chat line, two types of chat, one before start and after
        PLAYER_CHAT player:0 target:"team" msg:"hey team"
        PLAYER_CHAT time:55000 player:8 target:"team" msg:"in the game."
        """
        chat = {}
        chat['msg'] = ''
        l = line.split()
        if line[12] == 'p':
            chat['position'] = self.order_convert[int(l[1].split(':')[1])]
            chat['name'] = self.names[chat['position']]
            chat['target'] = l[2].split(':')[1][1:-1]
            chat['hero'] = self.heroes[chat['position']]
            chat['time'] = "Lobby"
            chat['msg'] = line.split('msg:')[1]
            if chat['target'] == 'all':
                chat['target'] = 3
            else:
                chat['target'] = self.teams[self.order_convert[int(l[1].split(':')[1])]]
        else:
            chat['position'] = self.order_convert[int(l[2].split(':')[1])]
            chat['time'] = self.set_time(l[1].split(':')[1])
            chat['name'] = self.names[chat['position']]
            chat['target'] = l[3].split(':')[1][1:-1]
            chat['msg'] = line.split('msg:')[1]
            chat['hero'] = self.heroes[chat['position']]
            if chat['target'] == 'all':
                chat['target'] = 3
            else:
                chat['target'] = self.teams[self.order_convert[int(l[2].split(':')[1])]]
        chat['msg'] = chat['msg'][1:-3]
        self.msg.append(chat)

    def out(self):
        print self.real_order
        print self.names
        print self.order_convert
        print self.builds