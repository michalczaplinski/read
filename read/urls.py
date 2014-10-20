from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
import allauth
from main import views


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('main.urls', namespace='main')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', views.custom_login),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
     {'next_page': '/'}),
    url(r'^accounts/', include('allauth.urls'))
)
