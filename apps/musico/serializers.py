from rest_framework import serializers
from .models import Musico

class MusicoSerializer(serializers.HyperlinkedModelSerializer):
	path_foto_perfil = serializers.Field(source='full_path_picture')

	class Meta:
		model = Musico
		fields = ('url','nombre','estilo','path_foto_perfil',)
