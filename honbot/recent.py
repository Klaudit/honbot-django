from django.template import Context, loader
from django.http import HttpResponse
from honbot.models import Matches, PlayerMatches


def recent(request):
    m = list(Matches.objects.all()[:5])
    print str(m[0])
    t = loader.get_template('recent.html')
    c = Context({'matches': m})
    return HttpResponse(t.render(c))
