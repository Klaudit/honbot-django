from __future__ import print_function

from api import get_json

from flask.ext.script import Command

import json


class heroes(Command):
    def run(self):
        allheroes = get_json('/heroes/all')
        if allheroes is None:
            raise "WHY IS NO HEROES?!"
        for hero in allheroes:
            del allheroes[hero]['description']
            del allheroes[hero]['hero_id']
        f = open('heroes.json','w')
        print(json.dumps(allheroes), file=f)


def isDigit(c):
    return c in ['0','1','2','3','4','5','6','7','8','9']


def hon2html(msg):
    if msg is not None:
        hon_colors = ["00","1C","38","54","70","8C","A8","C4","E0","FF"]
        msg = msg.replace('\\n','<br>')
        parts = msg.split('^')
        base = '<span>'
        #msg = '<span style="color: white;">' + parts[0]
        msg = base + parts[0]
        for part in parts[1:]:
            if len(part) < 1:
                msg += '^'
            elif part[0] == 'w' or part[0] == 'W':
                msg += '</span><span style="color: white;">' + part[1:]
            elif part[0] == 'r' or part[0] == 'R':
                msg += '</span><span style="color: #FF4C4C;">' + part[1:]
            elif part[0] == 'y' or part[0] == 'Y':
                msg += '</span><span style="color: #FFFF19;">' + part[1:]
            elif part[0] == 'g' or part[0] == 'G':
                msg += '</span><span style="color: #008000;">' + part[1:]
            elif part[0] == 'k' or part[0] == 'K':
                msg += '</span><span style="color: #000000;">' + part[1:]
            elif part[0] == 'c' or part[0] == 'C':
                msg += '</span><span style="color: #00FFFF;">' + part[1:]
            elif part[0] == 'b' or part[0] == 'B':
                msg += '</span><span style="color: #4C4CFF;">' + part[1:]
            elif part[0] == 't' or part[0] == 'T':
                msg += '</span><span style="color: teal;">' + part[1:]
            elif part[0] == 'o' or part[0] == 'O':
                msg += '</span><span style="color: orange;">' + part[1:]
            elif part[0] == 'm' or part[0] == 'M':
                msg += '</span><span style="color: #FF00FF;">' + part[1:]
            elif len(part) >= 3 and isDigit(part[0]) and isDigit(part[1]) and isDigit(part[2]):
                msg += '</span><span style="color: #%s%s%s;">' % (hon_colors[int(part[0])],hon_colors[int(part[1])],hon_colors[int(part[2])]) + part[3:]
            elif part[0] == '*':
                msg += '</span>' + base + part[1:]
            elif part[0] in [';',':']:
                msg += part[1:]
            else:
                msg += part
        return msg + '</span>'
    return ''
