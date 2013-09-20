# app specific urls
from django.conf.urls import patterns, url
from django.views.generic import TemplateView


urlpatterns = patterns(
    '',
    url('^$', 'honbot.home.home'),
    url(r'^server_status/$', 'honbot.home.server_status'),
    url(r'^match_count/$', 'honbot.home.match_count'),
    url(r'^player_count/$', 'honbot.home.player_count'),
    url(r'^api_count/$', 'honbot.home.api_count'),
    url(r'^player_match_count/$', 'honbot.home.player_match_count'),
    url(r'^distribution/$', 'honbot.player.distribution'),  # global player page
    url(r'^player/(?P<name>.*)/$', 'honbot.player.player_ranked'),  # ranked player stats
    url(r'^c/player/(?P<name>.*)/$', 'honbot.player.player_casual'),  # casual player stats
    url(r'^p/player/(?P<name>.*)/$', 'honbot.player.player_public'),  # public player stats
    url(r'^banner/(?P<name>.*)/$', 'honbot.banner.banner_view'), # stats banner img
    url(r'^player_hero/(?P<name>.*)/$', 'honbot.player_hero.ranked_view'),
    url(r'^p/player_hero/(?P<name>.*)/$', 'honbot.player_hero.public_view'),
    url(r'^c/player_hero/(?P<name>.*)/$', 'honbot.player_hero.casual_view'),
    url(r'^player_hero_stats/(?P<name>.*)/(?P<hero>[0-9]+)/$', 'honbot.player_hero.ph_ranked'),
    url(r'^c/player_hero_stats/(?P<name>.*)/(?P<hero>[0-9]+)/$', 'honbot.player_hero.ph_casual'),
    url(r'^p/player_hero_stats/(?P<name>.*)/(?P<hero>[0-9]+)/$', 'honbot.player_hero.ph_public'),
    url(r'^match/(?P<match_id>[0-9]+)/$', 'honbot.match.match_view'),
    url(r'^builds/(?P<match_id>[0-9]+)/$', 'honbot.builds.build_view'),
    url(r'^chat/(?P<match_id>[0-9]+)/$', 'honbot.chat.chat_view'),
    url(r'^avatar/(?P<number>[0-9]+)/(?P<width>[0-9]+)/$', 'honbot.avatar.avatar'),
    url(r'^match_history/(?P<account_id>[0-9]+)/$', 'honbot.match_history.history'),
    url(r'^match/$', 'honbot.player.recent'),
    url(r'^chart/(?P<name>.*)/$', 'honbot.chart.ranked_view'),
    url(r'^p/chart/(?P<name>.*)/$', 'honbot.chart.public_view'),
    url(r'^c/chart/(?P<name>.*)/$', 'honbot.chart.casual_view'), 
    url(r'^top/$', 'honbot.top.seven'),
    url(r'^sitestats/$', 'honbot.extra.stats'),
    (r'^robots\.txt$', TemplateView.as_view(template_name="robots.txt")),
)
