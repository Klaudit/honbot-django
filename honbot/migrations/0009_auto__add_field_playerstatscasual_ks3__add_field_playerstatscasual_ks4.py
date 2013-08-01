# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PlayerStatsCasual.ks3'
        db.add_column(u'honbot_playerstatscasual', 'ks3',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStatsCasual.ks4'
        db.add_column(u'honbot_playerstatscasual', 'ks4',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStatsCasual.ks5'
        db.add_column(u'honbot_playerstatscasual', 'ks5',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStatsCasual.ks6'
        db.add_column(u'honbot_playerstatscasual', 'ks6',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStatsCasual.ks7'
        db.add_column(u'honbot_playerstatscasual', 'ks7',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStatsCasual.ks8'
        db.add_column(u'honbot_playerstatscasual', 'ks8',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStatsCasual.ks9'
        db.add_column(u'honbot_playerstatscasual', 'ks9',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStatsCasual.ks10'
        db.add_column(u'honbot_playerstatscasual', 'ks10',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStatsCasual.ks15'
        db.add_column(u'honbot_playerstatscasual', 'ks15',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStatsCasual.bloodlust'
        db.add_column(u'honbot_playerstatscasual', 'bloodlust',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStatsCasual.doublekill'
        db.add_column(u'honbot_playerstatscasual', 'doublekill',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStatsCasual.triplekill'
        db.add_column(u'honbot_playerstatscasual', 'triplekill',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStatsCasual.quadkill'
        db.add_column(u'honbot_playerstatscasual', 'quadkill',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStatsCasual.annihilation'
        db.add_column(u'honbot_playerstatscasual', 'annihilation',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStatsCasual.smackdown'
        db.add_column(u'honbot_playerstatscasual', 'smackdown',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStatsCasual.humiliation'
        db.add_column(u'honbot_playerstatscasual', 'humiliation',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStatsCasual.nemesis'
        db.add_column(u'honbot_playerstatscasual', 'nemesis',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStatsCasual.retribution'
        db.add_column(u'honbot_playerstatscasual', 'retribution',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStatsCasual.level'
        db.add_column(u'honbot_playerstatscasual', 'level',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStatsCasual.level_exp'
        db.add_column(u'honbot_playerstatscasual', 'level_exp',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStatsCasual.min_exp'
        db.add_column(u'honbot_playerstatscasual', 'min_exp',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStatsCasual.max_exp'
        db.add_column(u'honbot_playerstatscasual', 'max_exp',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)


        # Changing field 'PlayerMatches.smackdown'
        db.alter_column(u'honbot_playermatches', 'smackdown', self.gf('django.db.models.fields.PositiveIntegerField')())
        # Adding field 'PlayerStats.ks3'
        db.add_column(u'honbot_playerstats', 'ks3',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStats.ks4'
        db.add_column(u'honbot_playerstats', 'ks4',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStats.ks5'
        db.add_column(u'honbot_playerstats', 'ks5',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStats.ks6'
        db.add_column(u'honbot_playerstats', 'ks6',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStats.ks7'
        db.add_column(u'honbot_playerstats', 'ks7',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStats.ks8'
        db.add_column(u'honbot_playerstats', 'ks8',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStats.ks9'
        db.add_column(u'honbot_playerstats', 'ks9',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStats.ks10'
        db.add_column(u'honbot_playerstats', 'ks10',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStats.ks15'
        db.add_column(u'honbot_playerstats', 'ks15',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStats.bloodlust'
        db.add_column(u'honbot_playerstats', 'bloodlust',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStats.doublekill'
        db.add_column(u'honbot_playerstats', 'doublekill',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStats.triplekill'
        db.add_column(u'honbot_playerstats', 'triplekill',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStats.quadkill'
        db.add_column(u'honbot_playerstats', 'quadkill',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStats.annihilation'
        db.add_column(u'honbot_playerstats', 'annihilation',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStats.smackdown'
        db.add_column(u'honbot_playerstats', 'smackdown',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStats.humiliation'
        db.add_column(u'honbot_playerstats', 'humiliation',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStats.nemesis'
        db.add_column(u'honbot_playerstats', 'nemesis',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStats.retribution'
        db.add_column(u'honbot_playerstats', 'retribution',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStats.level'
        db.add_column(u'honbot_playerstats', 'level',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStats.level_exp'
        db.add_column(u'honbot_playerstats', 'level_exp',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStats.min_exp'
        db.add_column(u'honbot_playerstats', 'min_exp',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStats.max_exp'
        db.add_column(u'honbot_playerstats', 'max_exp',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStatsPublic.ks3'
        db.add_column(u'honbot_playerstatspublic', 'ks3',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStatsPublic.ks4'
        db.add_column(u'honbot_playerstatspublic', 'ks4',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStatsPublic.ks5'
        db.add_column(u'honbot_playerstatspublic', 'ks5',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStatsPublic.ks6'
        db.add_column(u'honbot_playerstatspublic', 'ks6',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStatsPublic.ks7'
        db.add_column(u'honbot_playerstatspublic', 'ks7',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStatsPublic.ks8'
        db.add_column(u'honbot_playerstatspublic', 'ks8',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStatsPublic.ks9'
        db.add_column(u'honbot_playerstatspublic', 'ks9',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStatsPublic.ks10'
        db.add_column(u'honbot_playerstatspublic', 'ks10',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStatsPublic.ks15'
        db.add_column(u'honbot_playerstatspublic', 'ks15',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStatsPublic.bloodlust'
        db.add_column(u'honbot_playerstatspublic', 'bloodlust',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStatsPublic.doublekill'
        db.add_column(u'honbot_playerstatspublic', 'doublekill',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStatsPublic.triplekill'
        db.add_column(u'honbot_playerstatspublic', 'triplekill',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStatsPublic.quadkill'
        db.add_column(u'honbot_playerstatspublic', 'quadkill',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStatsPublic.annihilation'
        db.add_column(u'honbot_playerstatspublic', 'annihilation',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStatsPublic.smackdown'
        db.add_column(u'honbot_playerstatspublic', 'smackdown',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStatsPublic.humiliation'
        db.add_column(u'honbot_playerstatspublic', 'humiliation',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStatsPublic.nemesis'
        db.add_column(u'honbot_playerstatspublic', 'nemesis',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStatsPublic.retribution'
        db.add_column(u'honbot_playerstatspublic', 'retribution',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStatsPublic.level'
        db.add_column(u'honbot_playerstatspublic', 'level',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStatsPublic.level_exp'
        db.add_column(u'honbot_playerstatspublic', 'level_exp',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStatsPublic.min_exp'
        db.add_column(u'honbot_playerstatspublic', 'min_exp',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PlayerStatsPublic.max_exp'
        db.add_column(u'honbot_playerstatspublic', 'max_exp',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'PlayerStatsCasual.ks3'
        db.delete_column(u'honbot_playerstatscasual', 'ks3')

        # Deleting field 'PlayerStatsCasual.ks4'
        db.delete_column(u'honbot_playerstatscasual', 'ks4')

        # Deleting field 'PlayerStatsCasual.ks5'
        db.delete_column(u'honbot_playerstatscasual', 'ks5')

        # Deleting field 'PlayerStatsCasual.ks6'
        db.delete_column(u'honbot_playerstatscasual', 'ks6')

        # Deleting field 'PlayerStatsCasual.ks7'
        db.delete_column(u'honbot_playerstatscasual', 'ks7')

        # Deleting field 'PlayerStatsCasual.ks8'
        db.delete_column(u'honbot_playerstatscasual', 'ks8')

        # Deleting field 'PlayerStatsCasual.ks9'
        db.delete_column(u'honbot_playerstatscasual', 'ks9')

        # Deleting field 'PlayerStatsCasual.ks10'
        db.delete_column(u'honbot_playerstatscasual', 'ks10')

        # Deleting field 'PlayerStatsCasual.ks15'
        db.delete_column(u'honbot_playerstatscasual', 'ks15')

        # Deleting field 'PlayerStatsCasual.bloodlust'
        db.delete_column(u'honbot_playerstatscasual', 'bloodlust')

        # Deleting field 'PlayerStatsCasual.doublekill'
        db.delete_column(u'honbot_playerstatscasual', 'doublekill')

        # Deleting field 'PlayerStatsCasual.triplekill'
        db.delete_column(u'honbot_playerstatscasual', 'triplekill')

        # Deleting field 'PlayerStatsCasual.quadkill'
        db.delete_column(u'honbot_playerstatscasual', 'quadkill')

        # Deleting field 'PlayerStatsCasual.annihilation'
        db.delete_column(u'honbot_playerstatscasual', 'annihilation')

        # Deleting field 'PlayerStatsCasual.smackdown'
        db.delete_column(u'honbot_playerstatscasual', 'smackdown')

        # Deleting field 'PlayerStatsCasual.humiliation'
        db.delete_column(u'honbot_playerstatscasual', 'humiliation')

        # Deleting field 'PlayerStatsCasual.nemesis'
        db.delete_column(u'honbot_playerstatscasual', 'nemesis')

        # Deleting field 'PlayerStatsCasual.retribution'
        db.delete_column(u'honbot_playerstatscasual', 'retribution')

        # Deleting field 'PlayerStatsCasual.level'
        db.delete_column(u'honbot_playerstatscasual', 'level')

        # Deleting field 'PlayerStatsCasual.level_exp'
        db.delete_column(u'honbot_playerstatscasual', 'level_exp')

        # Deleting field 'PlayerStatsCasual.min_exp'
        db.delete_column(u'honbot_playerstatscasual', 'min_exp')

        # Deleting field 'PlayerStatsCasual.max_exp'
        db.delete_column(u'honbot_playerstatscasual', 'max_exp')


        # Changing field 'PlayerMatches.smackdown'
        db.alter_column(u'honbot_playermatches', 'smackdown', self.gf('django.db.models.fields.PositiveSmallIntegerField')())
        # Deleting field 'PlayerStats.ks3'
        db.delete_column(u'honbot_playerstats', 'ks3')

        # Deleting field 'PlayerStats.ks4'
        db.delete_column(u'honbot_playerstats', 'ks4')

        # Deleting field 'PlayerStats.ks5'
        db.delete_column(u'honbot_playerstats', 'ks5')

        # Deleting field 'PlayerStats.ks6'
        db.delete_column(u'honbot_playerstats', 'ks6')

        # Deleting field 'PlayerStats.ks7'
        db.delete_column(u'honbot_playerstats', 'ks7')

        # Deleting field 'PlayerStats.ks8'
        db.delete_column(u'honbot_playerstats', 'ks8')

        # Deleting field 'PlayerStats.ks9'
        db.delete_column(u'honbot_playerstats', 'ks9')

        # Deleting field 'PlayerStats.ks10'
        db.delete_column(u'honbot_playerstats', 'ks10')

        # Deleting field 'PlayerStats.ks15'
        db.delete_column(u'honbot_playerstats', 'ks15')

        # Deleting field 'PlayerStats.bloodlust'
        db.delete_column(u'honbot_playerstats', 'bloodlust')

        # Deleting field 'PlayerStats.doublekill'
        db.delete_column(u'honbot_playerstats', 'doublekill')

        # Deleting field 'PlayerStats.triplekill'
        db.delete_column(u'honbot_playerstats', 'triplekill')

        # Deleting field 'PlayerStats.quadkill'
        db.delete_column(u'honbot_playerstats', 'quadkill')

        # Deleting field 'PlayerStats.annihilation'
        db.delete_column(u'honbot_playerstats', 'annihilation')

        # Deleting field 'PlayerStats.smackdown'
        db.delete_column(u'honbot_playerstats', 'smackdown')

        # Deleting field 'PlayerStats.humiliation'
        db.delete_column(u'honbot_playerstats', 'humiliation')

        # Deleting field 'PlayerStats.nemesis'
        db.delete_column(u'honbot_playerstats', 'nemesis')

        # Deleting field 'PlayerStats.retribution'
        db.delete_column(u'honbot_playerstats', 'retribution')

        # Deleting field 'PlayerStats.level'
        db.delete_column(u'honbot_playerstats', 'level')

        # Deleting field 'PlayerStats.level_exp'
        db.delete_column(u'honbot_playerstats', 'level_exp')

        # Deleting field 'PlayerStats.min_exp'
        db.delete_column(u'honbot_playerstats', 'min_exp')

        # Deleting field 'PlayerStats.max_exp'
        db.delete_column(u'honbot_playerstats', 'max_exp')

        # Deleting field 'PlayerStatsPublic.ks3'
        db.delete_column(u'honbot_playerstatspublic', 'ks3')

        # Deleting field 'PlayerStatsPublic.ks4'
        db.delete_column(u'honbot_playerstatspublic', 'ks4')

        # Deleting field 'PlayerStatsPublic.ks5'
        db.delete_column(u'honbot_playerstatspublic', 'ks5')

        # Deleting field 'PlayerStatsPublic.ks6'
        db.delete_column(u'honbot_playerstatspublic', 'ks6')

        # Deleting field 'PlayerStatsPublic.ks7'
        db.delete_column(u'honbot_playerstatspublic', 'ks7')

        # Deleting field 'PlayerStatsPublic.ks8'
        db.delete_column(u'honbot_playerstatspublic', 'ks8')

        # Deleting field 'PlayerStatsPublic.ks9'
        db.delete_column(u'honbot_playerstatspublic', 'ks9')

        # Deleting field 'PlayerStatsPublic.ks10'
        db.delete_column(u'honbot_playerstatspublic', 'ks10')

        # Deleting field 'PlayerStatsPublic.ks15'
        db.delete_column(u'honbot_playerstatspublic', 'ks15')

        # Deleting field 'PlayerStatsPublic.bloodlust'
        db.delete_column(u'honbot_playerstatspublic', 'bloodlust')

        # Deleting field 'PlayerStatsPublic.doublekill'
        db.delete_column(u'honbot_playerstatspublic', 'doublekill')

        # Deleting field 'PlayerStatsPublic.triplekill'
        db.delete_column(u'honbot_playerstatspublic', 'triplekill')

        # Deleting field 'PlayerStatsPublic.quadkill'
        db.delete_column(u'honbot_playerstatspublic', 'quadkill')

        # Deleting field 'PlayerStatsPublic.annihilation'
        db.delete_column(u'honbot_playerstatspublic', 'annihilation')

        # Deleting field 'PlayerStatsPublic.smackdown'
        db.delete_column(u'honbot_playerstatspublic', 'smackdown')

        # Deleting field 'PlayerStatsPublic.humiliation'
        db.delete_column(u'honbot_playerstatspublic', 'humiliation')

        # Deleting field 'PlayerStatsPublic.nemesis'
        db.delete_column(u'honbot_playerstatspublic', 'nemesis')

        # Deleting field 'PlayerStatsPublic.retribution'
        db.delete_column(u'honbot_playerstatspublic', 'retribution')

        # Deleting field 'PlayerStatsPublic.level'
        db.delete_column(u'honbot_playerstatspublic', 'level')

        # Deleting field 'PlayerStatsPublic.level_exp'
        db.delete_column(u'honbot_playerstatspublic', 'level_exp')

        # Deleting field 'PlayerStatsPublic.min_exp'
        db.delete_column(u'honbot_playerstatspublic', 'min_exp')

        # Deleting field 'PlayerStatsPublic.max_exp'
        db.delete_column(u'honbot_playerstatspublic', 'max_exp')


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