from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView , ListView , DeleteView
from django.core.urlresolvers import reverse_lazy

from .models import Musico
from apps.album.models import Album

from .serializers import MusicoSerializer
from rest_framework import viewsets

class Musico_Todos(ListView):
    model = Musico
    template_name = 'musico/all_musico.html'
    context_object_name = "all_musico"

class Musico_Nuevo(CreateView):
    model = Musico
    template_name = 'musico/nuevo_musico.html'
    success_url = reverse_lazy('musicos')

class Musico_Detalle(DetailView):
    model = Musico
    template_name = 'musico/musico.html'
    context_object_name = "musico"

    def get_context_data(self, **kwargs):
        context = super(Musico_Detalle, self).get_context_data(**kwargs)
        musico = self.get_object()
        context['all_album'] = Album.objects.filter(musico=musico).order_by('titulo')
        return context

class Musico_Modificar(UpdateView):
    model = Musico
    success_url = reverse_lazy('musicos')
    template_name = 'musico/nuevo_musico.html'

class Musico_Eliminar(DeleteView):
    model = Musico
    success_url = reverse_lazy('musicos')
    template_name = 'musico/eliminar_musico.html'

class MusicoViewSet(viewsets.ModelViewSet):
    queryset = Musico.objects.all()
    serializer_class = MusicoSerializer