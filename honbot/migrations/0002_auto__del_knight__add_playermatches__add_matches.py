# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Knight'
        db.delete_table(u'honbot_knight')

        # Adding model 'PlayerMatches'
        db.create_table(u'honbot_playermatches', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('player_id', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('match', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['honbot.Matches'])),
            ('deaths', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('win', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('apm', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('cs', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('account_id', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('smackdown', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('secsdead', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('gpm', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('bdmg', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('herodmg', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('xpm', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('xdr', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('goldlost2death', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('denies', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('hero', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('kills', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('consumables', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('assists', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('nickname', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('level', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('wards', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('team', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('position', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
        ))
        db.send_create_signal(u'honbot', ['PlayerMatches'])

        # Adding model 'Matches'
        db.create_table(u'honbot_matches', (
            ('match_id', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True, primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('replay_url', self.gf('django.db.models.fields.URLField')(default='', max_length=120)),
            ('realtime', self.gf('django.db.models.fields.CharField')(default='', max_length=10)),
            ('mode', self.gf('django.db.models.fields.CharField')(default='', max_length=10)),
            ('_map', self.gf('django.db.models.fields.CharField')(default='', max_length=10)),
            ('major', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('minor', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('revision', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('build', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
        ))
        db.send_create_signal(u'honbot', ['Matches'])


    def backwards(self, orm):
        # Adding model 'Knight'
        db.create_table(u'honbot_knight', (
            ('of_the_round_table', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('dances_whenever_able', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('shrubberies', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'honbot', ['Knight'])

        # Deleting model 'PlayerMatches'
        db.delete_table(u'honbot_playermatches')

        # Deleting model 'Matches'
        db.delete_table(u'honbot_matches')


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
        },
        u'honbot.playermatches': {
            'Meta': {'object_name': 'PlayerMatches'},
            'account_id': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'apm': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'assists': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'bdmg': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'consumables': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'cs': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'deaths': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'denies': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'goldlost2death': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'gpm': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'hero': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'herodmg': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kills': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'level': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['honbot.Matches']"}),
            'nickname': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'player_id': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'secsdead': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'smackdown': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'team': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'wards': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'win': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'xdr': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'xpm': ('django.db.models.fields.FloatField', [], {'default': '0'})
        }
    }

    complete_apps = ['honbot']