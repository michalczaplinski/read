from django.conf.urls import patterns, url
from main import views
import allauth

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # url(r'^register/$', views.register, name='register'),
    url(r'^accounts/', include('allauth.urls')),

)
