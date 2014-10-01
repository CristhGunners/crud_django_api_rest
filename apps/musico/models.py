from django.db import models

from apps.album import image

from django.contrib.sites.models import Site

# Create your models here.
ESTILOS = (
    ('blues', ('Blues')),
    ('jazz', ('Jazz')),
    ('rock', ('Rock')),
    ('clasica', ('Clasica')),
    ('tango', ('Tango')),
)

class Musico(models.Model):

	def img_path(self,filename):
		ruta = 'musicos/%s' % (str(filename))
		return ruta

	nombre = models.CharField(max_length=50)
	estilo = models.CharField(max_length=10, choices=ESTILOS)
	foto_perfil = models.ImageField(upload_to=img_path , null=True , blank=True)

	def __unicode__(self):
		return self.nombre

	def save(self, *args, **kwargs):
		super(Musico, self).save(*args, **kwargs)
		self.nombre = self.nombre.capitalize()
		if not self.id and not self.foto_perfil: return

		image.resize(image.THUMB, self.foto_perfil)
		image.resize(image.SINGLE, self.foto_perfil)
		image.resize(image.HOME, self.foto_perfil)

	# los diferentes imagenes para el sitio
	def get_home_image_url(self):
		return image.get_url_by(image.HOME, self.foto_perfil)

	def get_thumb_image_url(self):
		return image.get_url_by(image.THUMB, self.foto_perfil)

	def get_single_image_url(self):
		return image.get_url_by(image.SINGLE, self.foto_perfil)

	def full_path_picture(self):
		current_site = Site.objects.get_current()
		img_path = current_site.domain+str(image.get_url_by(image.THUMB, self.foto_perfil))
		return img_path