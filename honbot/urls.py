# app specific urls
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import TemplateView


urlpatterns = patterns(
    '',
    url('^$', 'honbot.views.home'),
    url(r'^player/(?P<name>.*)/$', 'honbot.views.players'),  # ranked player stats
    url(r'^c/player/(?P<name>.*)/$', 'honbot.views.players'),  # casual player stats
    url(r'^p/player/(?P<name>.*)/$', 'honbot.views.players'),  # public player stats
    url(r'^history/(?P<name>.*)/$', 'honbot.views.history'),
    url(r'^banner/(?P<name>.*)/$', 'honbot.views.banner_view'),
    url(r'^match/(?P<match_id>\d+)/$', 'honbot.views.match_view'),
    url(r'^chat/(?P<match_id>\d+)/$', 'honbot.views.chat_view'),
    url(r'^advanced/(?P<match_id>\d+)/$', 'honbot.views.adv'),
    url(r'^avatar/(?P<number>\d+)/$', 'honbot.avatar.avatar'),
    url(r'^match_history/(?P<number>\d+)/$', 'honbot.match_history.ranked'),
    (r'^robots\.txt$', TemplateView.as_view(template_name="robots.txt")),
)
