from django.conf.urls import patterns, url, include
from main import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^bookmarks/$', views.bookmark_list, name='bookmarks'),
    url(r'^bookmarks/delete/(?P<id>\d+)/$', views.delete_bookmark, name='delete'),
    url(r'^bookmarks/add/$', views.add_bookmark, name='add')
)
