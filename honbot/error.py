from django.template import Context, loader
from django.http import HttpResponse


def error(request, msg):
    t = loader.get_template('error.html')
    c = Context({'msg': msg})
    return HttpResponse(t.render(c))
