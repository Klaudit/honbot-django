from django.shortcuts import render_to_response
from .models import Items


def main(request):
    heroes = Heroes.objects.all().values()
    today = date.today().strftime("%Y-%m-%d")
    data = HeroData.objects.all().order_by('hero_id').values('cli_name')
    use = list(HeroUse.objects.filter(date=today).order_by('hero_id').values())
    for index, hero in enumerate(heroes):
        try:
            hero['popularity'] = use[index]['popularity']
        except:
            hero['popularity'] = 0
        hero['cli_name'] = data[index]['cli_name']
    return render_to_response('heroes.html', {'heroes': heroes})