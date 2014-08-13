from django.conf.urls import patterns, url, include
from main import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'bookmarks/$', views.bookmark_list, name='bookmarks'),

)
