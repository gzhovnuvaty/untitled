from polls import admin

__author__ = 'gzhovnuvaty'


from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', 'polls.views.hello'),
    url(r'^$', 'polls.views.home_page'),
    url(r'^time/$', 'polls.views.current_datetime'),
    url(r'^time/plus/(\d{1,2})/$', 'polls.views.hours_ahead')
]