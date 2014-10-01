# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Album.year'
        db.alter_column(u'album_album', 'year', self.gf('django.db.models.fields.IntegerField')(max_length=4))

    def backwards(self, orm):

        # Changing field 'Album.year'
        db.alter_column(u'album_album', 'year', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=4))

    models = {
        u'album.album': {
            'Meta': {'object_name': 'Album'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'musico': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['musico.Musico']"}),
            'portada': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'year': ('django.db.models.fields.IntegerField', [], {'max_length': '4'})
        },
        u'album.cancion': {
            'Meta': {'object_name': 'Cancion'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['album.Album']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'musico.musico': {
            'Meta': {'object_name': 'Musico'},
            'estilo': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['album']