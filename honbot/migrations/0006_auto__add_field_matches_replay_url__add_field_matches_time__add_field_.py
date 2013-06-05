# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Matches.replay_url'
        db.add_column(u'honbot_matches', 'replay_url',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=120),
                      keep_default=False)

        # Adding field 'Matches.time'
        db.add_column(u'honbot_matches', 'time',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=10),
                      keep_default=False)

        # Adding field 'Matches.mode'
        db.add_column(u'honbot_matches', 'mode',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=10),
                      keep_default=False)

        # Adding field 'Matches._map'
        db.add_column(u'honbot_matches', '_map',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=10),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Matches.replay_url'
        db.delete_column(u'honbot_matches', 'replay_url')

        # Deleting field 'Matches.time'
        db.delete_column(u'honbot_matches', 'time')

        # Deleting field 'Matches.mode'
        db.delete_column(u'honbot_matches', 'mode')

        # Deleting field 'Matches._map'
        db.delete_column(u'honbot_matches', '_map')


    models = {
        u'honbot.matches': {
            'Meta': {'object_name': 'Matches'},
            '_map': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'match_id': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'mode': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'replay_url': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '120'}),
            'time': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'})
        }
    }

    complete_apps = ['honbot']