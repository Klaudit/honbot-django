# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Matches.time'
        db.delete_column(u'honbot_matches', 'time')

        # Adding field 'Matches.realtime'
        db.add_column(u'honbot_matches', 'realtime',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=10),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Matches.time'
        db.add_column(u'honbot_matches', 'time',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=10),
                      keep_default=False)

        # Deleting field 'Matches.realtime'
        db.delete_column(u'honbot_matches', 'realtime')


    models = {
        u'honbot.matches': {
            'Meta': {'object_name': 'Matches'},
            '_map': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'match_id': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'mode': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'realtime': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'replay_url': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '120'})
        }
    }

    complete_apps = ['honbot']