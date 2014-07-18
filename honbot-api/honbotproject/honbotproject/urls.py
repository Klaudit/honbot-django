from django.conf.urls import patterns, include, url
from django.contrib import admin
import hb.urls

urlpatterns = patterns('',
    url('', include(hb.urls, namespace="honbot")),
    (r'^django-rq/', include('django_rq.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
