# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Album'
        db.create_table(u'album_album', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('musico', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['musico.Musico'])),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('year', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=4)),
            ('portada', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'album', ['Album'])

        # Adding model 'Cancion'
        db.create_table(u'album_cancion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['album.Album'])),
        ))
        db.send_create_signal(u'album', ['Cancion'])


    def backwards(self, orm):
        # Deleting model 'Album'
        db.delete_table(u'album_album')

        # Deleting model 'Cancion'
        db.delete_table(u'album_cancion')


    models = {
        u'album.album': {
            'Meta': {'object_name': 'Album'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'musico': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['musico.Musico']"}),
            'portada': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'year': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '4'})
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
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['album']