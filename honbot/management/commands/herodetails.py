from django.core.management.base import BaseCommand, CommandError
from honbot.api_call import get_json, pure
from honbot.models import Heroes, HeroData
from json import dumps, loads


class Command(BaseCommand):
    help = 'This will get hero data'

    def handle(self, *args, **options):
        heroes = Heroes.objects.all().values('hero_id')
        bulk = []
        for hero in heroes:
            if hero['hero_id'] is not 185:
                data = get_json('/heroes/id/' + str(hero['hero_id']))
            else:
                data = pure('/heroes/id/' + str(hero['hero_id']))
                data = loads(data.text.split('line 84')[1])
            HeroData(hero_id=data['hero_id'],
                disp_name=data['disp_name'],
                cli_name=data['cli_name'],
                category=data['attributes']['CATEGORY'],
                difficulty=data['attributes']['DIFFICULTY'],
                solorating=data['attributes']['SOLORATING'],
                junglerating=data['attributes']['JUNGLERATING'],
                carryrating=data['attributes']['CARRYRATING'],
                supportrating=data['attributes']['SUPPORTRATING'],
                initiatorrating=data['attributes']['INITIATORRATING'],
                gankerating=data['attributes']['GANKERRATING'],
                pusherrating=data['attributes']['PUSHERRATING'],
                rangedrating=data['attributes']['RANGEDRATING'],
                meleerating=data['attributes']['MELEERATING'],
                movespeed=data['attributes']['MOVESPEED'],
                turnrate=data['attributes']['TURNRATE'],
                maxhealth=data['attributes']['MAXHEALTH'],
                healthregen=data['attributes']['HEALTHREGEN'],
                manaregen=data['attributes']['MANAREGEN'],
                armor=data['attributes']['ARMOR'],
                magicarmor=data['attributes']['MAGICARMOR'],
                attackduration=data['attributes']['ATTACKDURATION'],
                attackactiontime=data['attributes']['ATTACKACTIONTIME'],
                attackcooldown=data['attributes']['ATTACKCOOLDOWN'],
                attackdamagemin=data['attributes']['ATTACKDAMAGEMIN'],
                attackdamagemax=data['attributes']['ATTACKDAMAGEMAX'],
                attacknumanims=data['attributes']['ATTACKNUMANIMS'],
                attackrange=data['attributes']['ATTACKRANGE'],
                attacktype=data['attributes']['ATTACKTYPE'],
                aggrorange=data['attributes']['AGGRORANGE'],
                sightrangeday=data['attributes']['SIGHTRANGEDAY'],
                sightrangenight=data['attributes']['SIGHTRANGENIGHT'],
                wanderrange=data['attributes']['WANDERRANGE'],
                primaryattribute=data['attributes']['PRIMARYATTRIBUTE'],
                strength=data['attributes']['STRENGTH'],
                strengthperlevel=data['attributes']['STRENGTHPERLEVEL'],
                agility=data['attributes']['AGILITY'],
                agilityperlevel=data['attributes']['AGILITYPERLEVEL'],
                intelligence=data['attributes']['INTELLIGENCE'],
                intelligenceperlevel=data['attributes']['INTELLIGENCEPERLEVEL'],
                calcattackspeed=data['attributes']['CALCATTACKSPEED'],
                attackspeedpersec=data['attributes']['ATTACKSPEEDPERSEC'],
                effectivearmor=data['attributes']['EFFECTIVEARMOR'],
                health=data['attributes']['HEALTH'],
                mana=data['attributes']['MANA'],
                ability1=dumps(data['abilities'].items()[0]),
                ability2=dumps(data['abilities'].items()[1]),
                ability3=dumps(data['abilities'].items()[2]),
                ability4=dumps(data['abilities'].items()[3]),
                ).save()
        self.stdout.write("success")
