# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Knight'
        db.delete_table(u'honbot_knight')


    def backwards(self, orm):
        # Adding model 'Knight'
        db.create_table(u'honbot_knight', (
            ('of_the_round_table', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('dances_whenever_able', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('soup', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('shrubberies', self.gf('django.db.models.fields.IntegerField')()),
            ('dogs', self.gf('django.db.models.fields.IntegerField')(default=0)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'honbot', ['Knight'])


    models = {
        
    }

    complete_apps = ['honbot']