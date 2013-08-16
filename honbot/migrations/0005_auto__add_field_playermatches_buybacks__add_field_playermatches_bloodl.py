# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PlayerMatches.buybacks'
        db.add_column(u'honbot_playermatches', 'buybacks',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerMatches.bloodlust'
        db.add_column(u'honbot_playermatches', 'bloodlust',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerMatches.razed'
        db.add_column(u'honbot_playermatches', 'razed',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerMatches.triplekill'
        db.add_column(u'honbot_playermatches', 'triplekill',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerMatches.doublekill'
        db.add_column(u'honbot_playermatches', 'doublekill',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerMatches.quadkill'
        db.add_column(u'honbot_playermatches', 'quadkill',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerMatches.annihilation'
        db.add_column(u'honbot_playermatches', 'annihilation',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerMatches.gold_spent'
        db.add_column(u'honbot_playermatches', 'gold_spent',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerMatches.exp_denied'
        db.add_column(u'honbot_playermatches', 'exp_denied',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerMatches.bgold'
        db.add_column(u'honbot_playermatches', 'bgold',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerMatches.mmr_change'
        db.add_column(u'honbot_playermatches', 'mmr_change',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding index on 'PlayerMatches', fields ['player_id']
        db.create_index(u'honbot_playermatches', ['player_id'])


    def backwards(self, orm):
        # Removing index on 'PlayerMatches', fields ['player_id']
        db.delete_index(u'honbot_playermatches', ['player_id'])

        # Deleting field 'PlayerMatches.buybacks'
        db.delete_column(u'honbot_playermatches', 'buybacks')

        # Deleting field 'PlayerMatches.bloodlust'
        db.delete_column(u'honbot_playermatches', 'bloodlust')

        # Deleting field 'PlayerMatches.razed'
        db.delete_column(u'honbot_playermatches', 'razed')

        # Deleting field 'PlayerMatches.triplekill'
        db.delete_column(u'honbot_playermatches', 'triplekill')

        # Deleting field 'PlayerMatches.doublekill'
        db.delete_column(u'honbot_playermatches', 'doublekill')

        # Deleting field 'PlayerMatches.quadkill'
        db.delete_column(u'honbot_playermatches', 'quadkill')

        # Deleting field 'PlayerMatches.annihilation'
        db.delete_column(u'honbot_playermatches', 'annihilation')

        # Deleting field 'PlayerMatches.gold_spent'
        db.delete_column(u'honbot_playermatches', 'gold_spent')

        # Deleting field 'PlayerMatches.exp_denied'
        db.delete_column(u'honbot_playermatches', 'exp_denied')

        # Deleting field 'PlayerMatches.bgold'
        db.delete_column(u'honbot_playermatches', 'bgold')

        # Deleting field 'PlayerMatches.mmr_change'
        db.delete_column(u'honbot_playermatches', 'mmr_change')


    models = {
        u'honbot.matches': {
            'Meta': {'ordering': "['-match_id']", 'object_name': 'Matches'},
            '_map': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'added': ('django.db.models.fields.DateTimeField', [], {'default': '0', 'auto_now_add': 'True', 'blank': 'True'}),
            'build': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'major': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
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
            'smackdown': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
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