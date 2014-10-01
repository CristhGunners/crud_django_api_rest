from django.conf.urls import patterns, include, url
from django.conf import settings

from .views import *

urlpatterns = patterns('',
    url(r'^musicos/$',  Musico_Todos.as_view() , name='musicos'),
    url(r'^nuevo/$',  Musico_Nuevo.as_view() , name='musico_nuevo'),
    url(r'^(?P<pk>\d+)/$',  Musico_Detalle.as_view() , name='musico_detalle'),
    url(r'^editar/(?P<pk>\d+)/$', Musico_Modificar.as_view(), name='musico_modificar'),
  	url(r'^eliminar/(?P<pk>\d+)/$', Musico_Eliminar.as_view(), name='musico_eliminar'),


)