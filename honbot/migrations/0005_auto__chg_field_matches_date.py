# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Matches.date'
        db.alter_column(u'honbot_matches', 'date', self.gf('django.db.models.fields.DateTimeField')())

    def backwards(self, orm):

        # Changing field 'Matches.date'
        db.alter_column(u'honbot_matches', 'date', self.gf('django.db.models.fields.DateField')())

    models = {
        u'honbot.matches': {
            'Meta': {'object_name': 'Matches'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'match_id': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['honbot']