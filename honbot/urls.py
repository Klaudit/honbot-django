from django.conf.urls import patterns, url
from django.views.generic import TemplateView, RedirectView, ListView
from .player_browse import PlayerList
from .models import PlayerBrackets

urlpatterns = patterns(
    '',
    # Home Page
    url('^$', TemplateView.as_view(template_name="home.html")),
    # API's for Server stats
    url(r'^server_status/$', 'honbot.home.server_status'),
    url(r'^database_count/$', 'honbot.home.database_count'),
    # Player Browser
    url(r'^pdata/$', PlayerList.as_view()),
    url(r'^player/$', 'honbot.player_browse.browse'),
    # Player Distribution
    url(r'^distribution/$', 'honbot.player.distribution'),
    # Player
    url(r'^player/(?P<name>.*)/$', 'honbot.player.player_ranked'),
    url(r'^c/player/(?P<name>.*)/$', 'honbot.player.player_casual'),
    url(r'^p/player/(?P<name>.*)/$', 'honbot.player.player_public'),
    # player tooltip
    url(r'^ptip/(?P<account_id>[0-9]+)/$', 'honbot.player.tooltip_ranked'),
    url(r'^p/ptip/(?P<account_id>[0-9]+)/$', 'honbot.player.tooltip_public'),
    url(r'^c/ptip/(?P<account_id>[0-9]+)/$', 'honbot.player.tooltip_casual'),
    ## CHARTS (needs to be renamed)
    # Player Charts
    url(r'^chart/(?P<name>[^/]+)/$', 'honbot.chart.chart_default', {'limit': 50, 'mode': "rnk"}),
    url(r'^c/chart/(?P<name>[^/]+)/$', 'honbot.chart.chart_default', {'limit': 50, 'mode': "cs"}),
    url(r'^p/chart/(?P<name>[^/]+)/$', 'honbot.chart.chart_default', {'limit': 50, 'mode': "acc"}),
    # player charts with limits
    url(r'^chart/(?P<name>[^/]+)/(?P<limit>\d+)/$', 'honbot.chart.chart_default', {'mode': "rnk"}),
    url(r'^c/chart/(?P<name>[^/]+)/(?P<limit>\d+)/$', 'honbot.chart.chart_default', {'mode': "cs"}),
    url(r'^p/chart/(?P<name>[^/]+)/(?P<limit>\d+)/$', 'honbot.chart.chart_default', {'mode': "acc"}),
    # Player Avatar
    url(r'^avatar/(?P<number>[0-9]+)/(?P<width>[0-9]+)/$', 'honbot.avatar.avatar'),
    # Player History
    url(r'^player_history/(?P<account_id>[0-9]+)/(?P<page>[0-9])/$', 'honbot.player_history.history_ranked'),
    url(r'^c/player_history/(?P<account_id>[0-9]+)/(?P<page>[0-9])/$', 'honbot.player_history.history_casual'),
    url(r'^p/player_history/(?P<account_id>[0-9]+)/(?P<page>[0-9])/$', 'honbot.player_history.history_public'),
    # Player Banner
    url(r'^banner/(?P<name>.*)/$', 'honbot.banner.banner_view'),
    # Player Hero page
    url(r'^player_hero/(?P<name>.*)/$', 'honbot.player_hero.ranked_view'),
    url(r'^p/player_hero/(?P<name>.*)/$', 'honbot.player_hero.public_view'),
    url(r'^c/player_hero/(?P<name>.*)/$', 'honbot.player_hero.casual_view'),
    # Player hero data
    url(r'^player_hero_stats/(?P<name>.*)/(?P<hero>[0-9]+)/$', 'honbot.player_hero.ph_ranked'),
    url(r'^c/player_hero_stats/(?P<name>.*)/(?P<hero>[0-9]+)/$', 'honbot.player_hero.ph_casual'),
    url(r'^p/player_hero_stats/(?P<name>.*)/(?P<hero>[0-9]+)/$', 'honbot.player_hero.ph_public'),
    # Match View
    url(r'^match/(?P<match_id>[0-9]+)/$', 'honbot.match.match_view'),
    # Match Chat
    url(r'^chat/(?P<match_id>[0-9]+)/$', 'honbot.chat.chat_view'),
    # Recent Matches
    url(r'^match/$', 'honbot.match.recent'),
    # High scores
    url(r'^top/$', 'honbot.top.seven'),
    # Site stats
    url(r'^sitestats/$', 'honbot.extra.stats'),
    # Robots.txt
    (r'^robots\.txt$', TemplateView.as_view(template_name="robots.txt")),
    # heroes main page
    url(r'^hero/$', 'honbot.heroes.main'),
    url(r'^hero/(?P<name>.*)/$', 'honbot.heroes.hero'),
    # items pages
    url(r'^item/$', 'honbot.items.main'),
    url(r'^item/(?P<item_id>[0-9]+)/$', 'honbot.items.item'),
    (r'^brackets/$', ListView.as_view(model=PlayerBrackets, template_name='brackets.html')),
)
