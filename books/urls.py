from django.conf.urls import *
from django.contrib import admin

urlpatterns = patterns('books.views',
                       url(r'^search-form/$', 'search_form'),
                       url(r'^search/$', 'search'),
                       url(r'^contact/$', 'contact'),
                       url(r'^maps/$', 'google_maps'),
                       url(r'^admin/', include(admin.site.urls))
                       )
