from django.template import Context, loader
from django.http import HttpResponse
from honbot.models import Matches, PlayerMatches


def main(request):
    m = list(PlayerMatches.objects.filter(mode="rnk", d).)
    t = loader.get_template('recent.html')
    c = Context({'matches': m})
    return HttpResponse(t.render(c))
