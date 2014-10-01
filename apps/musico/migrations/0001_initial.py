# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Musico'
        db.create_table(u'musico_musico', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('estilo', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('foto', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'musico', ['Musico'])


    def backwards(self, orm):
        # Deleting model 'Musico'
        db.delete_table(u'musico_musico')


    models = {
        u'musico.musico': {
            'Meta': {'object_name': 'Musico'},
            'estilo': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['musico']