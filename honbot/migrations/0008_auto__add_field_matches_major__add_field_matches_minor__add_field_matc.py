# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Matches.major'
        db.add_column(u'honbot_matches', 'major',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Matches.minor'
        db.add_column(u'honbot_matches', 'minor',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Matches.revision'
        db.add_column(u'honbot_matches', 'revision',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Matches.build'
        db.add_column(u'honbot_matches', 'build',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Matches.major'
        db.delete_column(u'honbot_matches', 'major')

        # Deleting field 'Matches.minor'
        db.delete_column(u'honbot_matches', 'minor')

        # Deleting field 'Matches.revision'
        db.delete_column(u'honbot_matches', 'revision')

        # Deleting field 'Matches.build'
        db.delete_column(u'honbot_matches', 'build')


    models = {
        u'honbot.matches': {
            'Meta': {'object_name': 'Matches'},
            '_map': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'build': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'major': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'match_id': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'minor': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'mode': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'realtime': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'replay_url': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '120'}),
            'revision': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['honbot']