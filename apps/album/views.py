from django.views.generic.base import TemplateView
from django.views.generic import CreateView, UpdateView, DetailView , ListView , DeleteView
from django.core.urlresolvers import reverse_lazy

from .models import Album
#from .forms import AlbumForm

from .serializers import AlbumSerializer
from rest_framework import viewsets

class Album_Todos(ListView):
	model = Album
	template_name = 'album/all_album.html'
	context_object_name = "all_album"

class Album_Detalle(DetailView):
    model = Album
    template_name = 'album/album.html'
    context_object_name = "album"

class Album_Nuevo(CreateView):
    model = Album
    success_url = reverse_lazy('album_todos')
    template_name = 'album/add_album.html'

class Album_Modificar(UpdateView):
    model = Album
    success_url = reverse_lazy('album_todos')
    template_name = 'album/add_album.html'

class Album_Eliminar(DeleteView):
    model = Album
    success_url = reverse_lazy('album_todos')
    template_name = 'album/eliminar_album.html'

class Album_Estilo(ListView):
    model = Album
    template_name = 'album/album_filtro.html'
    context_object_name = "all_album"

    def get_queryset(self):
        return Album.objects.filter(musico__estilo=self.kwargs['estilo_id']).order_by('musico__estilo')

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer