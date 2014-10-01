from django.conf.urls import patterns, include, url
from django.conf import settings

from .views import *

urlpatterns = patterns('',
    url(r'^$',  Album_Todos.as_view() , name='album_todos'),
    url(r'^album/nuevo/$', Album_Nuevo.as_view(), name='album_nuevo'),
    url(r'^album/(?P<pk>\d+)/$', Album_Detalle.as_view(), name='album_detalle'),
    url(r'^album/editar/(?P<pk>\d+)/$', Album_Modificar.as_view(), name='album_modificar'),
  	url(r'^album/eliminar/(?P<pk>\d+)/$', Album_Eliminar.as_view(), name='album_eliminar'),
  	url(r'^album/filtro/(?P<estilo_id>[\w_-]+)/', Album_Estilo.as_view(), name='album_estilo'),
)