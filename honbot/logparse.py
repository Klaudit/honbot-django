from codecs import open as op
from .models import Chat, PlayerMatches
from json import dumps
from os import path, remove
from re import sub
from requests import get
from time import strftime, gmtime
from zipfile import ZipFile

# Directory where match logs and zips will be saved, unzipped, and read from
directory = str(path.join(path.abspath(path.dirname(path.dirname(__file__))), 'match')) + '/'


# calls all appropriate functions in correct order
# creates the honlog class object
def parse(match_id, players):
    log = honlog(match_id, players)
    log.open_file()
    log.run()
    if log.save():
        return True
    else:
        return False
    log.delete()
    return True

# downloads match, returns false if unable to download
def download(match_id, url):
    if url is None:
        return False
    url = url[:-9] + 'zip'
    # download file
    print url
    r = get(url)
    if r.status_code == 404:
        return False
    # write zip file to directory
    with open(directory + str(match_id) + ".zip", "wb") as filesave:
        filesave.write(r.content)
    # unzip
    z = ZipFile(directory + str(match_id) + '.zip')
    z.extract(z.namelist()[0], directory)
    z.close()
    # delete zip
    remove(directory + str(match_id) + '.zip')
    return True

# the parsing class
class honlog:
    def __init__(self, match_id, players):
        self.match_id = match_id
        self.matchpos, self.playerinfo, self.posfind, self.spectators = {}, {}, {}, {}
        self.logfile = file
        self.date, self.time = '', ''
        self.msg = []
        for player in players:
            self.matchpos[str(player['player_id'])] = player['position']
            self.playerinfo[str(player['position'])] = player

    ## non parsing functions ##
    # loops over each line in log file
    def run(self):
        for line in self.logfile:
            word = line.split()[0]
            try:
                methodToCall = getattr(self, word)
                methodToCall(line)
            except AttributeError:
                pass

    # deletes logfile from self.match_id
    def delete(self):
        remove(directory + 'm' + str(self.match_id) + '.log')

    # opens self.match_id with correct encoding
    def open_file(self):
        self.logfile = op(directory + 'm' + self.match_id + '.log', encoding='utf-16-le', mode='rb').readlines()
        self.INFO_DATE(self.logfile.pop(0))

    # returns data from the player model copied earlier into an array
    # starts to get funky with spectators
    def getinfo(self, chat_pos, req):
        if str(chat_pos) in self.posfind:
            return self.playerinfo[str(self.posfind[str(chat_pos)])][req]
        else:
            if req is "position":
                return 9999
            elif req is "nickname":
                return self.spectators[str(chat_pos)]
            elif req is "hero":
                return 9999

    # converts time from some sort of milisecond into nice formatting
    # uses hours only if longer than an hour
    def set_time(self, time):
        if int(time) < 3599999:
            time = strftime('%M:%S', gmtime(int(time) // 1000))
        else:
            time = strftime('%H:%M:%S', gmtime(int(time) // 1000))
        return time

    # saves chat mesages to the model
    def save(self):
        if len(self.msg) > 0:
            Chat(match_id=self.match_id, json=dumps(self.msg)).save()
            return True
        else:
            return False

    ## parsing functions ##

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
        PLAYER_CONNECT player:10 name:"[ATMS]Gingersnapz" id:6022781 psr:-1.0000
        """
        l = line.split()
        pid = str(l[-2].split(':')[1])
        if self.matchpos.has_key(str(pid)):
            player = int(l[1].split(':')[1])
            self.posfind[str(player)] = self.matchpos[pid]
        else:
            if len(l) == 5:
                name = l[2].split(':')[1][1:-1]  # get name
                name = name.split(']')[-1]  # remove clan tag
                player = int(l[1].split(':')[1])
            else:
                name = l[3].split(':')[1][1:-1]  # get name
                name = name.split(']')[-1]  # remove clan tag
                player = int(l[2].split(':')[1])
            self.spectators[str(player)] = name

    def HERO_DEATH(self, line):
        """
        HERO_DEATH time:430300 x:2663 y:13571 z:128 player:7 team:1 attacker:"Hero_Legionnaire" owner:2
        [u'HERO_DEATH', u'time:3605100', u'x:8930', u'y:12665', u'z:128', u'player:7', u'team:1', u'attacker:"Hero_Ra"', u'owner:9']
        [u'HERO_DEATH', u'time:235200', u'x:5017', u'y:12836', u'z:128', u'player:9', u'team:2', u'attacker:"Neutral_WolfCommander"']
        """
        l = line.split()
        kill = {}
        kill['kill'] = True
        kill['time'] = self.set_time(l[1].split(':')[1])
        if "owner:" not in line:
            kill['killer'] = 42
            kill['herokiller'] = None
            kill['killername'] = "Neutrals"
        else:
            killerpos = int(sub("\D", "", l[-1]))
            kill['killer'] = self.getinfo(killerpos, 'position')
            kill['herokiller'] = self.getinfo(killerpos, 'hero')
            kill['killername'] = self.getinfo(killerpos, 'nickname')
        killedpos = int(sub("\D", "", l[5]))
        kill['killed'] = self.getinfo(killedpos, 'position')
        kill['herokilled'] = self.getinfo(killedpos, 'hero')
        kill['killedname'] = self.getinfo(killedpos, 'nickname')
        self.msg.append(kill)

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
            pos = l[1].split(':')[1]
            chat['position'] = self.getinfo(pos, 'position')
            chat['name'] = self.getinfo(pos, 'nickname')
            chat['target'] = l[2].split(':')[1][1:-1]
            chat['hero'] = self.getinfo(pos, 'hero')
            chat['time'] = "Lobby"
            chat['msg'] = line.split('msg:')[1]
            if chat['target'] == 'all':
                chat['target'] = 3
            else:
                chat['target'] = self.getinfo(pos, 'team')
        else:
            pos = l[2].split(':')[1]
            chat['position'] = self.getinfo(pos, 'position')
            chat['time'] = self.set_time(l[1].split(':')[1])
            chat['name'] = self.getinfo(pos, 'nickname')
            chat['target'] = l[3].split(':')[1][1:-1]
            chat['msg'] = line.split('msg:')[1]
            chat['hero'] = self.getinfo(pos, 'hero')
            if chat['target'] == 'all':
                chat['target'] = 3
            else:
                chat['target'] = self.getinfo(pos, 'team')
        chat['msg'] = chat['msg'][1:-3]
        self.msg.append(chat)