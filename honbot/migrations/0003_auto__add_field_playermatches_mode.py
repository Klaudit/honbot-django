# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PlayerMatches.mode'
        db.add_column(u'honbot_playermatches', 'mode',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=10),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'PlayerMatches.mode'
        db.delete_column(u'honbot_playermatches', 'mode')


    models = {
        u'honbot.matches': {
            'Meta': {'ordering': "['-match_id']", 'object_name': 'Matches'},
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
        u'honbot.playerhistory': {
            'Meta': {'object_name': 'PlayerHistory'},
            'history': ('django.db.models.fields.TextField', [], {'default': "''"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mode': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'player_id': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'default': '0', 'auto_now': 'True', 'blank': 'True'})
        },
        u'honbot.playericon': {
            'Meta': {'object_name': 'PlayerIcon'},
            'avatar': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '300'}),
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
            'items': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'kdr': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'kills': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'level': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['honbot.Matches']"}),
            'mode': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'nickname': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '25'}),
            'player_id': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'secsdead': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
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
            'aassists': ('django.db.models.fields.FloatField', [], {'default': '0'}),
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
            'cccalls': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'deaths': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'hours': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'kadr': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'kdr': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'kicked': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'kills': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'left': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'losses': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'matches': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'mmr': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'nickname': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'player_id': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'default': '0', 'auto_now': 'True', 'blank': 'True'}),
            'winpercent': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '4'}),
            'wins': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'honbot.playerstatscasual': {
            'Meta': {'object_name': 'PlayerStatsCasual'},
            'TSR': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'aactionsmin': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'aassists': ('django.db.models.fields.FloatField', [], {'default': '0'}),
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
            'cccalls': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'deaths': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'hours': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'kadr': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'kdr': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'kicked': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'kills': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'left': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'losses': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'matches': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'mmr': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'nickname': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'player_id': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'default': '0', 'auto_now': 'True', 'blank': 'True'}),
            'winpercent': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '4'}),
            'wins': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'honbot.playerstatspublic': {
            'Meta': {'object_name': 'PlayerStatsPublic'},
            'TSR': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True'}),
            'aactionsmin': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'aassists': ('django.db.models.fields.FloatField', [], {'default': '0'}),
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
            'cccalls': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'deaths': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'hours': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'kadr': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'kdr': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'kicked': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'kills': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'left': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'losses': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'matches': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'mmr': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'nickname': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'player_id': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'default': '0', 'auto_now': 'True', 'blank': 'True'}),
            'winpercent': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '4'}),
            'wins': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['honbot']