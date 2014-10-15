from django.conf import settings
from PIL import Image,ImageOps
import os

# constantes
THUMB   = 'thumb'
SINGLE  = 'single'
HOME    = 'home'

# devolver la url a la imagen
def get_url_by(type, imagen):
	parts = str(imagen).rsplit('.', 1)
	return '%s%s-%s.%s' % (settings.MEDIA_URL, parts[0], type, parts[1])

# devolver el archivo a la imagen
def get_path_by(type, path):
	parts = path.rsplit('.', 1)
	return '%s-%s.%s' % (parts[0], type, parts[1])

def resize(type, imagen):
	path = os.path.join(settings.MEDIA_ROOT, str(imagen))
	# tomar el tamano del archivo de configuracion
	
	size = settings.IMG_SIZE_THUMB
	if type == SINGLE: size = settings.IMG_SIZE_SINGLE
	elif type == HOME: size = settings.IMG_SIZE_HOME
	
	try:
		image = Image.open(path)
		image = ImageOps.fit(image, size, Image.ANTIALIAS, centering=(0.5,0.5))
		image.save(get_path_by(type, path))
	except Exception as e:
		pass