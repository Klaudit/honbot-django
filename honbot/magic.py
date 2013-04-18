import re
from hero_id import hero


class Magic:
    def __init__(self, match_id):
        self.date = ''
        self.time = ''
        self.match_id = match_id
        self.server = ''
        self.version = ''
        self.map = ''
        self.mode = ''
        self.players = []
        self.spectators = []
        self.team = []
        self.id = []
        self.psr = []
        self.hero = [None] * 10
        self.items = [[] for i in range(10)]
        self.ability_upgrade = [[] for i in range(10)]
        self.apm = [[] for i in range(10)]
        self.add = [0] * 10
        self.chunk = 1
        self.hapm = []
        self.lapm = []
        self.pause = [0] * 10
        self.cc = [0] * 10
        self.remake = [0] * 10
        self.ability = [[0] * 5 for i in range(10)]

    def finish(self, names):
        """
        this will do my required math and sorting
        """
        #init
        print names
        self.hapm = [0] * len(self.apm[1])
        self.lapm = [0] * len(self.apm[1])
        myorder = []
        newplayers = [None] * 10
        newitems = [None] * 10
        newteam = [None] * 10
        newability_upgrade = [None] * 10
        newhero = [None] * 10
        newid = [None] * 10
        newapm = [None] * 10
        newpsr = [None] * 10
        newpause = [None] * 10
        newcc = [None] * 10
        newremake = [None] * 10
        newability = [[0] * 5 for i in range(10)]
        # compare names from api and get order
        for p in self.players:
            myorder.append(names.index(p))
        print myorder
        # copy into new order
        for i, order in enumerate(myorder):
            newplayers[order] = self.players[i]
            newitems[order] = self.items[i]
            newteam[order] = self.team[i]
            newhero[order] = self.hero[i]
            newid[order] = self.id[i]
            newability_upgrade[order] = self.ability_upgrade[i]
            newapm[order] = self.apm[i]
            newpsr[order] = self.psr[i]
            newpause[order] = self.pause[i]
            newcc[order] = self.cc[i]
            newremake[order] = self.remake[i]
            newability[order] = self.ability[i]
        self.players = newplayers
        self.items = newitems
        self.ability_upgrade = newability_upgrade
        self.team = newteam
        self.hero = newhero
        self.id = newid
        self.apm = newapm
        self.psr = newpsr
        self.pause = newpause
        self.cc = newcc
        self.remake = newremake
        self.ability = newability
        #get average apm
        for i, player in enumerate(self.apm):
            for d, chunk in enumerate(player):
                if i < 5:
                    self.lapm[d] += chunk
                else:
                    self.hapm[d] += chunk
        self.lapm = [x/5 for x in self.lapm]
        self.hapm = [x/5 for x in self.hapm]

    def INFO_DATE(self, line):
        """
        [u'\ufeffINFO_DATE', u'date:"2013/30/03"', u'time:"17:14:52"']
        """
        d = line.split()
        self.date = d[1].split(':')[1][1:-1]
        self.time = d[2].split('"')[1]

    def INFO_SERVER(self, line):
        """
        INFO_SERVER name:"USE 21"
        """
        self.server = line.split('"')[1]

    def INFO_GAME(self, line):
        """
        INFO_GAME name:"Heroes of Newerth" version:"3.0.6.0"
        """
        self.version = line.split('"')[-2]

    def INFO_MAP(self, line):
        """
        INFO_MAP name:"caldavar" version:"0.0.0"
        """
        self.map = line.split('"')[1]

    def INFO_SETTINGS(self, line):
        """
        INFO_SETTINGS mode:"Mode_Normal" options:"Option_None"
        """
        self.mode = line.split('"')[1]

    def PLAYER_CHAT(self, line):
        """
        returns dict of chat line, two types of chat, one before start and after
        works perfect now ladies
        """
        pass

    def PLAYER_CONNECT(self, line):
        """
        PLAYER_CONNECT player:0 name:"NAMENAMENAME" id:3252583 psr:1522.0000
        spectators too
        PLAYER_CONNECT time:1617600 player:13 name:"[bMcE]Smexystyle`" id:7399320 psr:-1.0000
        """
        l = line.split()
        psr = int(float(l[-1].split(':')[1]))
        if psr != -1 and len(self.players) != 10:
            name = l[2].split(':')[1][1:-1]
            for letter in name:
                if letter == '[':
                    name = name.split(']')[1]
                else:
                    break
            self.players.append(name)
            self.psr.append(psr)
            self.id.append(int(l[-2].split(':')[1]))
        else:
            name = l[3].split(':')[1][1:-1]
            for letter in name:
                if letter == '[':
                    name = name.split(']')[1]
                else:
                    break
            self.spectators.append(name)

    def PLAYER_TEAM_CHANGE(self, line):
        """
        PLAYER_TEAM_CHANGE player:0 team:1
        """
        self.team.append(int(line[-3]))

    def PLAYER_SELECT(self, line):
        """
        PLAYER_SELECT player:6 hero:"Hero_Krixi"
        """
        l = line.split()
        self.hero[int(l[1].split(':')[1])] = hero(l[2].split('"')[1])

    def PLAYER_SWAP(self, line):
        """
        PLAYER_SWAP player:6 oldhero:"Hero_FlintBeastwood" newhero:"Hero_WitchSlayer"
        PLAYER_SWAP player:1 oldhero:"Hero_WitchSlayer" newhero:"Hero_FlintBeastwood"
        """
        l = line.split()
        self.hero[int(l[1].split(':')[1])] = hero(l[3].split('"')[1])

    def PLAYER_RANDOM(self, line):
        """
        PLAYER_RANDOM player:5 hero:"Hero_Engineer"
        """
        l = line.split()
        self.hero[int(l[1].split(':')[1])] = hero(l[2].split('"')[1])

    def ITEM_PURCHASE(self, line):
        """
        ITEM_PURCHASE time:0 x:13740 y:13363 z:110 player:3 team:2 item:"Item_LoggersHatchet" cost:225
        """
        l = line.split()
        item = {}
        item['item'] = l[7].split('"')[1]
        item['price'] = int(l[8].split(':')[1])
        item['time'] = int(l[1].split(':')[1])
        if item['time'] == 0:
            self.items[int(l[5].split(':')[1])].append(item)

    def ITEM_SELL(self, line):
        """
        ITEM_SELL time:925200 x:11803 y:7957 z:128 player:8 team:2 item:"Item_MinorTotem" value:26
        """
        l = line.split()
        item = {}
        item['item'] = l[7].split('"')[1]
        item['price'] = int(l[8].split(':')[1])
        item['time'] = int(l[1].split(':')[1])
        player = int(l[5].split(':')[1])
        # check last three items if item has been returned
        try:
            if self.items[player][-1]['price'] == item['price']:
                self.items[player].pop()
            elif self.items[player][-2]['price'] == item['price']:
                self.items[player].pop(-2)
            elif self.items[player][-3]['price'] == item['price']:
                self.items[player].pop(-3)
            elif self.items[player][-4]['price'] == item['price']:
                self.items[player].pop(-4)
            elif self.items[player][-5]['price'] == item['price']:
                self.items[player].pop(-5)
            elif self.items[player][-6]['price'] == item['price']:
                self.items[player].pop(-6)
        except:
            pass

    def ITEM_ASSEMBLE(self, line):
        """
        ITEM_ASSEMBLE time:926200 x:15320 y:3993 z:128 player:1 team:1 item:"Item_EnhancedMarchers"
        """
        l = line.split()
        item = {}
        item['item'] = l[7].split('"')[1]
        item['price'] = 9999999
        item['time'] = int(l[1].split(':')[1])
        self.items[int(l[5].split(':')[1])].append(item)

    def ABILITY_UPGRADE(self, line):
        """
        ABILITY_UPGRADE time:0 x:1662 y:995 z:101 player:1 team:1 name:"Ability_Empath1" level:1 slot:0
        """
        l = line.split()
        a = {}
        a['time'] = int(l[1].split(':')[1])
        ability = l[7].split('"')[1]
        if ability != 'Ability_AttributeBoost':
            ability = int(re.sub("\D", "", ability)[-1:])
        else:
            ability = 5
        a['ability'] = ability
        self.ability_upgrade[int(l[5].split(':')[1])].append(a)

    def PLAYER_CALL_VOTE(self, line):
        """
        PLAYER_CALL_VOTE time:419500 player:6 type:pause
        """
        l = line.split()
        if len(l) > 3:
            player = int(l[2].split(':')[1])
            t = l[3].split(':')[1]
        else:
            player = int(l[1].split(':')[1])
            t = l[2].split(':')[1]
        if t == "pause":
            self.pause[player] += 1
        elif t == "remake":
            self.remake[player] += 1
        elif t == "concede":
            self.cc[player] += 1

    def PLAYER_ACTIONS(self, line):
        """
        PLAYER_ACTIONS player:6 count:16 period:20000 team:2
        PLAYER_ACTIONS time:10050 player:1 count:60 period:20000 team:2
        """
        l = line.split()
        if int(l[-1].split(':')[1]) == 0:
            return
        if self.chunk != 8:
            if len(l) == 5:  # length is 5 if before time 0
                self.add[int(l[1].split(':')[1])] += int(l[2].split(':')[1])
                if int(l[1].split(':')[1]) == 0:
                    self.chunk += 1
            else:
                self.add[int(l[2].split(':')[1])] += int(l[3].split(':')[1])
                if int(l[2].split(':')[1]) == 0:
                    self.chunk += 1
        else:
            if len(l) == 5:
                self.add[int(l[1].split(':')[1])] += int(l[2].split(':')[1])
                self.apm[int(l[1].split(':')[1])].append(self.add[int(l[1].split(':')[1])] / 3)
                self.add[int(l[1].split(':')[1])] = 0
                if int(l[1].split(':')[1]) == 0:
                    self.chunk = 0
            else:
                self.add[int(l[2].split(':')[1])] += int(l[3].split(':')[1])
                self.apm[int(l[2].split(':')[1])].append(self.add[int(l[2].split(':')[1])] / 3)
                self.add[int(l[2].split(':')[1])] = 0
                if int(l[2].split(':')[1]) == 0:
                    self.chunk = 0

    def ABILITY_ACTIVATE(self, line):
        """
        ABILITY_ACTIVATE time:2265050 x:9762 y:8540 z:0 player:1 team:1 name:"Ability_Devourer2" level:4 slot:1
        """
        l = line.split()
        player = int(l[5].split(':')[1])
        ability = l[7].split('"')[1]
        if ability != "Ability_Taunt":
            ability = int(re.sub("\D", "", ability)[-1:])
        else:
            ability = 5
        self.ability[player][ability-1] += 1
