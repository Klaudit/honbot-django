from django.core.management.base import BaseCommand
from honbot.api_call import get_json
from honbot.models import Items
from json import dumps


class Command(BaseCommand):
    help = 'This will get item data'

    def handle(self, *args, **options):
        items, bulk = [], []
        for itemid in range(0, 160):
            if itemid is not 73:
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
            item['attributes']['strings'].setdefault('effect_header', None)
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
                description_simple=item['attributes']['strings']['description_simple'],
                effect_header=item['attributes']['strings']['effect_header'],
                search_terms=item['attributes']['strings']['search_terms'],
                shop_categories=item['attributes']['strings']['shop_categories'],
                shop_flavor=item['attributes']['strings']['shop_flavor']
            ))
        Items.objects.all().delete()
        Items.objects.bulk_create(bulk)
        self.stdout.write("success")
