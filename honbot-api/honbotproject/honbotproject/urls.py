from django.conf.urls import patterns, include, url
import hb.urls

urlpatterns = patterns(
    '',
    url('', include(hb.urls, namespace="honbot")),
    (r'^django-rq/', include('django_rq.urls'))
)
