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
            ('smackdown', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('secsdead', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('gpm', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('bdmg', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('herodmg', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('xpm', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('kdr', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('goldlost2death', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('denies', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('hero', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('kills', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('consumables', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('assists', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('nickname', self.gf('django.db.models.fields.TextField')(default='', max_length=25)),
            ('level', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('wards', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('team', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('position', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
        ))
        db.send_create_signal(u'honbot', ['PlayerMatches'])

        # Adding model 'PlayerStats'
        db.create_table(u'honbot_playerstats', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(default='', max_length=30)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(default=0, auto_now=True, blank=True)),
            ('ccalls', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('deaths', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('cc', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('TSR', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('player_id', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('kdr', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('adenies', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('aconsumables', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('kills', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('winpercent', self.gf('django.db.models.fields.CharField')(default='', max_length=4)),
            ('kadr', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('akills', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('kicked', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('agoldmin', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('matches', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('mmr', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('hours', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('assists', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('awards', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('atime', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('aactionsmin', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('axpmin', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('adeaths', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('acs', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('wins', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('losses', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('left', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal(u'honbot', ['PlayerStats'])

        # Adding model 'PlayerIcon'
        db.create_table(u'honbot_playericon', (
            ('player_id', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True, primary_key=True)),
            ('avatar', self.gf('django.db.models.fields.URLField')(default='', max_length=120)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(default=0, auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'honbot', ['PlayerIcon'])

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
            ('added', self.gf('django.db.models.fields.DateTimeField')(default=0, auto_now_add=True, blank=True)),
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

        # Deleting model 'PlayerStats'
        db.delete_table(u'honbot_playerstats')

        # Deleting model 'PlayerIcon'
        db.delete_table(u'honbot_playericon')

        # Deleting model 'Matches'
        db.delete_table(u'honbot_matches')


    models = {
        u'honbot.matches': {
            'Meta': {'object_name': 'Matches'},
            '_map': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'added': ('django.db.models.fields.DateTimeField', [], {'default': '0', 'auto_now_add': 'True', 'blank': 'True'}),
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
        u'honbot.playericon': {
            'Meta': {'object_name': 'PlayerIcon'},
            'avatar': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '120'}),
            'player_id': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'default': '0', 'auto_now': 'True', 'blank': 'True'})
        },
        u'honbot.playermatches': {
            'Meta': {'object_name': 'PlayerMatches'},
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
            'herodmg': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kdr': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'kills': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'level': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['honbot.Matches']"}),
            'nickname': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '25'}),
            'player_id': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'secsdead': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'smackdown': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'team': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'wards': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'win': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'xpm': ('django.db.models.fields.FloatField', [], {'default': '0'})
        },
        u'honbot.playerstats': {
            'Meta': {'object_name': 'PlayerStats'},
            'TSR': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'aactionsmin': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'aconsumables': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'acs': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'adeaths': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'adenies': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'agoldmin': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'akills': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'assists': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'atime': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'awards': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'axpmin': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'cc': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ccalls': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'deaths': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'hours': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kadr': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'kdr': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'kicked': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'kills': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'left': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'losses': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'matches': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'mmr': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'player_id': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'default': '0', 'auto_now': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'winpercent': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '4'}),
            'wins': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['honbot']