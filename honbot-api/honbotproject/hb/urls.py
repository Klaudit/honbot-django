from rest_framework.routers import SimpleRouter
from django.conf.urls import patterns, url
from .player import PlayerViewSet
from .item import ItemsViewSet

router = SimpleRouter()
router.register(r'player', PlayerViewSet, base_name="Player")
router.register(r'item', ItemsViewSet, base_name="Item")
urlpatterns = router.urls

urlpatterns += patterns('',
    url(r'^banner/(?P<name>.*)/$', 'hb.banner.banner_view'),
    url(r'^items/$', 'hb.item.items'),
    url(r'^match/(?P<mid>[0-9]+)/$', 'hb.match.match'),
    url(r'^player_history/(?P<pid>[0-9]+)/(?P<page>[0-9])/(?P<mode>.*)/$', 'hb.history.player_history')
)
