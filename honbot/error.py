from django.shortcuts import render_to_response


def error(request, msg):
    return render_to_response('error.html', {'msg': msg})
