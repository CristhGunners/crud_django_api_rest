from django.db import models
from django.core.urlresolvers import reverse

from apps.musico.models import Musico
from apps.album import image

from django.contrib.sites.models import Site

# Create your models here.
import datetime

YEAR_CHOICES = []
for r in range(1950, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))

class Album(models.Model):

	def img_path(self,filename):
		ruta = 'discos/%s' % (str(filename))
		return ruta

	musico = models.ForeignKey(Musico)
	titulo = models.CharField(max_length=50)
	year = models.IntegerField(max_length=4 , choices=YEAR_CHOICES)
	portada = models.ImageField(upload_to=img_path)

	def __unicode__(self):
		return "%s" % self.titulo

	def get_absolute_url(self):
		return reverse('album_detalle', kwargs={'pk': self.pk})

	def full_path_img(self):
		current_site = Site.objects.get_current()
		img_path = current_site.domain+str(image.get_url_by(image.THUMB, self.portada))
		return img_path

	class Meta:
		ordering = ["musico"]

	def save(self, *args, **kwargs):
		super(Album, self).save(*args, **kwargs)
		self.titulo = self.titulo.capitalize()
		if not self.id and not self.portada: return

		image.resize(image.THUMB, self.portada)
		image.resize(image.SINGLE, self.portada)
		image.resize(image.HOME, self.portada)

	# los diferentes imagenes para el sitio
	def get_home_image_url(self):
		return image.get_url_by(image.HOME, self.portada)

	def get_thumb_image_url(self):
		return image.get_url_by(image.THUMB, self.portada)

	def get_single_image_url(self):
		return image.get_url_by(image.SINGLE, self.portada)

class Cancion(models.Model):
	titulo = models.CharField(max_length=50)
	album = models.ForeignKey(Album)

	def __unicode__(self):
		return self.titulo
