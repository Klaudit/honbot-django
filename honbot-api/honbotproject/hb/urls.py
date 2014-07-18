from rest_framework.routers import SimpleRouter
from django.conf.urls import patterns, url
from .players import PlayerViewSet

router = SimpleRouter()
router.register(r'player', PlayerViewSet, base_name="Player")
urlpatterns = router.urls

urlpatterns += patterns('',
    url(r'^player_history/(?P<pid>[0-9]+)/(?P<page>[0-9])/(?P<mode>.*)/$', 'hb.history.player_history'),
)
