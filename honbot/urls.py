# app specific urls
from django.conf.urls import patterns, url
from django.views.generic import TemplateView


urlpatterns = patterns(
    '',
    url('^$', 'honbot.home.home'),
    url(r'^server_status/$', 'honbot.home.server_status'),
    url(r'^match_count/$', 'honbot.home.match_count'),
    url(r'^player_count/$', 'honbot.home.player_count'),
    url(r'^player/(?P<name>.*)/$', 'honbot.player.players'),  # ranked player stats
    url(r'^c/player/(?P<name>.*)/$', 'honbot.player.players'),  # casual player stats
    url(r'^p/player/(?P<name>.*)/$', 'honbot.player.players'),  # public player stats
    url(r'^banner/(?P<name>.*)/$', 'honbot.banner.banner_view'),
    url(r'^player_hero/(?P<name>.*)/$', 'honbot.player_hero.player_hero'),
    url(r'^player_hero_stats/(?P<name>.*)/(?P<hero>[0-9]+)/$', 'honbot.player_hero.player_hero_stats'),
    url(r'^match/(?P<match_id>[0-9]+)/$', 'honbot.views.match_view'),
    url(r'^builds/(?P<match_id>[0-9]+)/$', 'honbot.builds.build'),
    url(r'^chat/(?P<match_id>[0-9]+)/$', 'honbot.chat.chat'),
    url(r'^avatar/(?P<number>[0-9]+)/(?P<width>[0-9]+)/$', 'honbot.avatar.avatar'),
    url(r'^match_history/(?P<account_id>[0-9]+)/$', 'honbot.match_history.history'),
    url(r'^recent/$', 'honbot.recent.recent'),
    url(r'^top/$', 'honbot.top.seven'),
    (r'^robots\.txt$', TemplateView.as_view(template_name="robots.txt")),
)
