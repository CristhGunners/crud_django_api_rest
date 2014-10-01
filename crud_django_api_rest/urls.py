from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

from rest_framework import routers
from apps.musico.views import MusicoViewSet
from apps.album.views import AlbumViewSet

router = routers.DefaultRouter()
router.register(r'musicos',MusicoViewSet)
router.register(r'albums',AlbumViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'crud_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^musico/', include('apps.musico.urls')),
    url(r'^', include('apps.album.urls')),
)

urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT,}),
)
