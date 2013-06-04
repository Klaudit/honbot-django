# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Matches'
        db.create_table(u'honbot_matches', (
            ('match_id', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True, primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'honbot', ['Matches'])


    def backwards(self, orm):
        # Deleting model 'Matches'
        db.delete_table(u'honbot_matches')


    models = {
        u'honbot.matches': {
            'Meta': {'object_name': 'Matches'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'match_id': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['honbot']