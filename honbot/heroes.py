from django.shortcuts import render_to_response
from django.views.decorators.cache import cache_page
from honbot.models import Heroes, HeroUse