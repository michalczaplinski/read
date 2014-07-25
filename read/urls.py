from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^main/', include('main.urls', namespace='main')),
    url(r'^admin/', include(admin.site.urls)),

)


    # url(r'^accounts/', include('registration.backends.simple.urls')),

# Examples:
# url(r'^$', 'read.views.home', name='home'),
#
