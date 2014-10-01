# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Musico.foto_perfil'
        db.add_column(u'musico_musico', 'foto_perfil',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Musico.foto_perfil'
        db.delete_column(u'musico_musico', 'foto_perfil')


    models = {
        u'musico.musico': {
            'Meta': {'object_name': 'Musico'},
            'estilo': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'foto_perfil': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['musico']