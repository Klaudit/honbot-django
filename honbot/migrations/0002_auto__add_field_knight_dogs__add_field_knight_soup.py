# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Knight.dogs'
        db.add_column(u'honbot_knight', 'dogs',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Knight.soup'
        db.add_column(u'honbot_knight', 'soup',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Knight.dogs'
        db.delete_column(u'honbot_knight', 'dogs')

        # Deleting field 'Knight.soup'
        db.delete_column(u'honbot_knight', 'soup')


    models = {
        u'honbot.knight': {
            'Meta': {'object_name': 'Knight'},
            'dances_whenever_able': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dogs': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'of_the_round_table': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'shrubberies': ('django.db.models.fields.IntegerField', [], {}),
            'soup': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['honbot']