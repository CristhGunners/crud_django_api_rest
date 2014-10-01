from rest_framework import serializers
from .models import Album

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
	path_foto_album = serializers.Field(source='full_path_img')

	class Meta:
		model = Album
		fields = ('url','musico','titulo','year','path_foto_album',)