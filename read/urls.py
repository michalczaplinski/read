from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import allauth

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('main.urls', namespace='main')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout',
     {'next_page': '/'}),
    url(r'^accounts/', include('allauth.urls')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()


    # url(r'^accounts/', include('registration.backends.simple.urls')),

# Examples:
# url(r'^$', 'read.views.home', name='home'),
#
