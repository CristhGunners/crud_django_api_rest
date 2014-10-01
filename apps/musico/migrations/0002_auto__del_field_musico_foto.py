# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Musico.foto'
        db.delete_column(u'musico_musico', 'foto')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Musico.foto'
        raise RuntimeError("Cannot reverse this migration. 'Musico.foto' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Musico.foto'
        db.add_column(u'musico_musico', 'foto',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100),
                      keep_default=False)


    models = {
        u'musico.musico': {
            'Meta': {'object_name': 'Musico'},
            'estilo': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['musico']