from django.template import Context, loader
from django.http import HttpResponse
from error import error
import json


def build(request, match_id):
    return error(request, "Match is more than 28 days old or the replay is not available.")
