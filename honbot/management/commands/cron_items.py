from django.core.management.base import BaseCommand
from honbot.api_call import get_json
from honbot.models import Items
from json import dumps


class Command(BaseCommand):
    help = 'This will get item data'

    def handle(self, *args, **options):
        items, bulk = [], []
        banned_items = [73, 66, 110, 122, 123, 131, 134]
        for itemid in range(0, 160):
            if itemid not in banned_items:
                temp_item = get_json('/items/id/' + str(itemid))
                if temp_item is not None:
                    items.append(temp_item)
                    items[-1]['item_id'] = itemid
        for item in items:
            item['attributes'].setdefault('usedIn', None)
            item['attributes']['strings'].setdefault('shop_flavor', None)
            item['attributes']['strings'].setdefault('shop_categories', None)
            item['attributes']['strings'].setdefault('search_terms', None)
            item['attributes']['strings'].setdefault('description_simple', None)
            item['attributes']['strings'].setdefault('description', None)
            item['attributes']['strings'].setdefault('effect_header', None)
            item['attributes']['strings'].setdefault('IMPACT_effect', None)
            try:
                item['attributes']['cost']=int(item['attributes']['cost'])
            except:
                item['attributes']['cost']=0
            try:
                item['attributes']['recipeCost']=int(item['attributes']['recipeCost'])
            except:
                item['attributes']['recipeCost']=0
            bulk.append(Items(
                item_id=item['item_id'],
                name=item['attributes']['name'],
                cli_name=item['cli_name'],
                icon=item['attributes']['icon'],
                cost=item['attributes']['cost'],
                ispassive=item['attributes']['isPassive'],
                recipecost=item['attributes']['recipeCost'],
                usedin=dumps(item['attributes']['usedIn']),
                description_simple=hon2html(item['attributes']['strings']['description_simple']),
                description=hon2html(item['attributes']['strings']['description']),
                impact_effect=item['attributes']['strings']['IMPACT_effect'],
                effect_header=item['attributes']['strings']['effect_header'],
                search_terms=item['attributes']['strings']['search_terms'],
                shop_categories=item['attributes']['strings']['shop_categories'],
                shop_flavor=hon2html(item['attributes']['strings']['shop_flavor'])
            ))
        Items.objects.all().delete()
        Items.objects.bulk_create(bulk)
        self.stdout.write("success")


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