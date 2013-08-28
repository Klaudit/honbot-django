# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Matches._map'
        db.delete_column(u'honbot_matches', '_map')

        # Adding field 'Matches.map_used'
        db.add_column(u'honbot_matches', 'map_used',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Matches._map'
        db.add_column(u'honbot_matches', '_map',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30),
                      keep_default=False)

        # Deleting field 'Matches.map_used'
        db.delete_column(u'honbot_matches', 'map_used')


    models = {
        u'honbot.chat': {
            'Meta': {'object_name': 'Chat'},
            'json': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'match_id': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'primary_key': 'True', 'db_index': 'True'})
        },
        u'honbot.matches': {
            'Meta': {'ordering': "['-match_id']", 'object_name': 'Matches'},
            'added': ('django.db.models.fields.DateTimeField', [], {'default': '0', 'auto_now_add': 'True', 'blank': 'True'}),
            'build': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'major': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'map_used': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'match_id': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'primary_key': 'True', 'db_index': 'True'}),
            'minor': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'mode': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'realtime': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'replay_url': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '120'}),
            'revision': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        u'honbot.playerherostats': {
            'Meta': {'object_name': 'PlayerHeroStats'},
            'data': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'hero_id': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mode': ('django.db.models.fields.CharField', [], {'default': "'rnk'", 'max_length': '10'}),
            'nickname': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'default': '0', 'auto_now': 'True', 'blank': 'True'})
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
            'annihilation': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'apm': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'assists': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'bdmg': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'bgold': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'bloodlust': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'buybacks': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'consumables': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'cs': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'deaths': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'denies': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'doublekill': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'exp_denied': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'gold_spent': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
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
            'mmr_change': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'mode': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'nickname': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '25'}),
            'player_id': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'quadkill': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'razed': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'secsdead': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'smackdown': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'team': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'triplekill': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
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
            'annihilation': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'assists': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'atime': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'awards': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'axpmin': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'bloodlust': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'cc': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'cccalls': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'deaths': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'doublekill': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'hours': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'humiliation': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'kadr': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'kdr': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'kicked': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'kills': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ks10': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'ks15': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'ks3': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ks4': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ks5': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ks6': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ks7': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ks8': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ks9': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'left': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'level_exp': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'losses': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'matches': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'max_exp': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'min_exp': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'mmr': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'nemesis': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'nickname': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'player_id': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'quadkill': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'razed': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'retribution': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'smackdown': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'triplekill': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
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
            'annihilation': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'assists': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'atime': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'awards': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'axpmin': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'bloodlust': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'cc': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'cccalls': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'deaths': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'doublekill': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'hours': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'humiliation': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'kadr': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'kdr': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'kicked': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'kills': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ks10': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'ks15': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'ks3': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ks4': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ks5': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ks6': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ks7': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ks8': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ks9': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'left': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'level_exp': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'losses': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'matches': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'max_exp': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'min_exp': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'mmr': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'nemesis': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'nickname': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'player_id': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'quadkill': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'razed': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'retribution': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'smackdown': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'triplekill': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
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
            'annihilation': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'assists': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'atime': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'awards': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'axpmin': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'bloodlust': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'cc': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'cccalls': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'deaths': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'doublekill': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'hours': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'humiliation': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'kadr': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'kdr': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'kicked': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'kills': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ks10': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'ks15': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'ks3': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ks4': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ks5': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ks6': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ks7': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ks8': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ks9': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'left': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'level_exp': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'losses': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'matches': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'max_exp': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'min_exp': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'mmr': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'nemesis': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'nickname': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'player_id': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'quadkill': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'razed': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'retribution': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'smackdown': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'triplekill': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'default': '0', 'auto_now': 'True', 'blank': 'True'}),
            'winpercent': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '4'}),
            'wins': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['honbot']