# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Matches'
        db.create_table(u'honbot_matches', (
            ('match_id', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True, primary_key=True, db_index=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('replay_url', self.gf('django.db.models.fields.URLField')(default='', max_length=120)),
            ('realtime', self.gf('django.db.models.fields.CharField')(default='', max_length=10)),
            ('mode', self.gf('django.db.models.fields.CharField')(default='', max_length=10)),
            ('map_used', self.gf('django.db.models.fields.CharField')(default='', max_length=30)),
            ('major', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('minor', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('revision', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('build', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('added', self.gf('django.db.models.fields.DateTimeField')(default=0, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'honbot', ['Matches'])

        # Adding model 'PlayerMatches'
        db.create_table(u'honbot_playermatches', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('player_id', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, db_index=True)),
            ('match', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['honbot.Matches'])),
            ('deaths', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('win', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('apm', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('cs', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('buybacks', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('bloodlust', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('razed', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('triplekill', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('doublekill', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('quadkill', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('annihilation', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('smackdown', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('gold_spent', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('exp_denied', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('bgold', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('secsdead', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('gpm', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('bdmg', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('herodmg', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('xpm', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('kdr', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('mmr_change', self.gf('django.db.models.fields.FloatField')(default=0)),
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
            ('items', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('mode', self.gf('django.db.models.fields.CharField')(default='', max_length=10)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(db_index=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'honbot', ['PlayerMatches'])

        # Adding model 'PlayerIcon'
        db.create_table(u'honbot_playericon', (
            ('player_id', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True, primary_key=True)),
            ('avatar', self.gf('django.db.models.fields.URLField')(default='', max_length=300)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(default=0, auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'honbot', ['PlayerIcon'])

        # Adding model 'PlayerHistory'
        db.create_table(u'honbot_playerhistory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('player_id', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('history', self.gf('django.db.models.fields.TextField')(default='')),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(default=0, auto_now=True, blank=True)),
            ('mode', self.gf('django.db.models.fields.CharField')(default='', max_length=10)),
        ))
        db.send_create_signal(u'honbot', ['PlayerHistory'])

        # Adding model 'PlayerStats'
        db.create_table(u'honbot_playerstats', (
            ('player_id', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True, primary_key=True, db_index=True)),
            ('nickname', self.gf('django.db.models.fields.CharField')(default='', max_length=30)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(default=0, auto_now=True, blank=True)),
            ('cccalls', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('deaths', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('cc', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('TSR', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('kdr', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('adenies', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('aconsumables', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('kills', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('winpercent', self.gf('django.db.models.fields.CharField')(default='', max_length=4)),
            ('kadr', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('akills', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('kicked', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('razed', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
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
            ('aassists', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('ks3', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('ks4', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('ks5', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('ks6', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('ks7', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('ks8', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('ks9', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('ks10', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('ks15', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('bloodlust', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('doublekill', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('triplekill', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('quadkill', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('annihilation', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('smackdown', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('humiliation', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('nemesis', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('retribution', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('level_exp', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('min_exp', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('max_exp', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal(u'honbot', ['PlayerStats'])

        # Adding model 'PlayerStatsCasual'
        db.create_table(u'honbot_playerstatscasual', (
            ('player_id', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True, primary_key=True)),
            ('nickname', self.gf('django.db.models.fields.CharField')(default='', max_length=30)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(default=0, auto_now=True, blank=True)),
            ('cccalls', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('deaths', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('cc', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('TSR', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('kdr', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('adenies', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('aconsumables', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('razed', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
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
            ('aassists', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('ks3', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('ks4', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('ks5', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('ks6', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('ks7', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('ks8', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('ks9', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('ks10', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('ks15', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('bloodlust', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('doublekill', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('triplekill', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('quadkill', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('annihilation', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('smackdown', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('humiliation', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('nemesis', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('retribution', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('level_exp', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('min_exp', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('max_exp', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal(u'honbot', ['PlayerStatsCasual'])

        # Adding model 'PlayerStatsPublic'
        db.create_table(u'honbot_playerstatspublic', (
            ('player_id', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True, primary_key=True)),
            ('nickname', self.gf('django.db.models.fields.CharField')(default='', max_length=30)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(default=0, auto_now=True, blank=True)),
            ('cccalls', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('deaths', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('cc', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('TSR', self.gf('django.db.models.fields.FloatField')(default=0, null=True)),
            ('razed', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
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
            ('aassists', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('ks3', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('ks4', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('ks5', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('ks6', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('ks7', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('ks8', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('ks9', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('ks10', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('ks15', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('bloodlust', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('doublekill', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('triplekill', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('quadkill', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('annihilation', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('smackdown', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('humiliation', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('nemesis', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('retribution', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('level_exp', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('min_exp', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('max_exp', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal(u'honbot', ['PlayerStatsPublic'])

        # Adding model 'PlayerHeroStats'
        db.create_table(u'honbot_playerherostats', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nickname', self.gf('django.db.models.fields.CharField')(default='', max_length=30)),
            ('data', self.gf('django.db.models.fields.TextField')(default='')),
            ('hero_id', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(default=0, auto_now=True, blank=True)),
            ('mode', self.gf('django.db.models.fields.CharField')(default='rnk', max_length=10)),
        ))
        db.send_create_signal(u'honbot', ['PlayerHeroStats'])

        # Adding model 'Chat'
        db.create_table(u'honbot_chat', (
            ('match_id', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True, primary_key=True, db_index=True)),
            ('json', self.gf('django.db.models.fields.TextField')(default='')),
        ))
        db.send_create_signal(u'honbot', ['Chat'])

        # Adding model 'Builds'
        db.create_table(u'honbot_builds', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('match_id', self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True)),
            ('hero', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0, db_index=True)),
            ('json', self.gf('django.db.models.fields.TextField')(default='')),
            ('nickname', self.gf('django.db.models.fields.CharField')(default='', max_length=30)),
            ('position', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('win', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('mmr', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('lvl1', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('lvl2', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('lvl3', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('lvl4', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('lvl5', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('lvl6', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('lvl7', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('lvl8', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('lvl9', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('lvl10', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('lvl11', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('lvl12', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('lvl13', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('lvl14', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('lvl15', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('lvl16', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('lvl17', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('lvl18', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('lvl19', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('lvl20', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('lvl21', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('lvl22', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('lvl23', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('lvl24', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('lvl25', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
        ))
        db.send_create_signal(u'honbot', ['Builds'])

        # Adding model 'PlayerCount'
        db.create_table(u'honbot_playercount', (
            ('date', self.gf('django.db.models.fields.DateField')(auto_now=True, unique=True, primary_key=True, db_index=True)),
            ('count', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal(u'honbot', ['PlayerCount'])

        # Adding model 'MatchCount'
        db.create_table(u'honbot_matchcount', (
            ('date', self.gf('django.db.models.fields.DateField')(auto_now=True, unique=True, primary_key=True, db_index=True)),
            ('count', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal(u'honbot', ['MatchCount'])

        # Adding model 'PlayerMatchCount'
        db.create_table(u'honbot_playermatchcount', (
            ('date', self.gf('django.db.models.fields.DateField')(auto_now=True, unique=True, primary_key=True, db_index=True)),
            ('count', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal(u'honbot', ['PlayerMatchCount'])

        # Adding model 'APICount'
        db.create_table(u'honbot_apicount', (
            ('date', self.gf('django.db.models.fields.DateField')(auto_now=True, unique=True, primary_key=True, db_index=True)),
            ('count', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal(u'honbot', ['APICount'])


    def backwards(self, orm):
        # Deleting model 'Matches'
        db.delete_table(u'honbot_matches')

        # Deleting model 'PlayerMatches'
        db.delete_table(u'honbot_playermatches')

        # Deleting model 'PlayerIcon'
        db.delete_table(u'honbot_playericon')

        # Deleting model 'PlayerHistory'
        db.delete_table(u'honbot_playerhistory')

        # Deleting model 'PlayerStats'
        db.delete_table(u'honbot_playerstats')

        # Deleting model 'PlayerStatsCasual'
        db.delete_table(u'honbot_playerstatscasual')

        # Deleting model 'PlayerStatsPublic'
        db.delete_table(u'honbot_playerstatspublic')

        # Deleting model 'PlayerHeroStats'
        db.delete_table(u'honbot_playerherostats')

        # Deleting model 'Chat'
        db.delete_table(u'honbot_chat')

        # Deleting model 'Builds'
        db.delete_table(u'honbot_builds')

        # Deleting model 'PlayerCount'
        db.delete_table(u'honbot_playercount')

        # Deleting model 'MatchCount'
        db.delete_table(u'honbot_matchcount')

        # Deleting model 'PlayerMatchCount'
        db.delete_table(u'honbot_playermatchcount')

        # Deleting model 'APICount'
        db.delete_table(u'honbot_apicount')


    models = {
        u'honbot.apicount': {
            'Meta': {'object_name': 'APICount'},
            'count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'unique': 'True', 'primary_key': 'True', 'db_index': 'True'})
        },
        u'honbot.builds': {
            'Meta': {'object_name': 'Builds'},
            'hero': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'json': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lvl1': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl10': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl11': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl12': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl13': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl14': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl15': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl16': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl17': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl18': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl19': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl2': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl20': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl21': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl22': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl23': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl24': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl25': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl3': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl4': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl5': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl6': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl7': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl8': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lvl9': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'match_id': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'db_index': 'True'}),
            'mmr': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'nickname': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'win': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'honbot.chat': {
            'Meta': {'object_name': 'Chat'},
            'json': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'match_id': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'primary_key': 'True', 'db_index': 'True'})
        },
        u'honbot.matchcount': {
            'Meta': {'object_name': 'MatchCount'},
            'count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'unique': 'True', 'primary_key': 'True', 'db_index': 'True'})
        },
        u'honbot.matches': {
            'Meta': {'ordering': "['-match_id']", 'object_name': 'Matches'},
            'added': ('django.db.models.fields.DateTimeField', [], {'default': '0', 'auto_now_add': 'True', 'blank': 'True'}),
            'build': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'major': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'map_used': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'match_id': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'primary_key': 'True', 'db_index': 'True'}),
            'minor': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'mode': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'realtime': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'replay_url': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '120'}),
            'revision': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        u'honbot.playercount': {
            'Meta': {'object_name': 'PlayerCount'},
            'count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'unique': 'True', 'primary_key': 'True', 'db_index': 'True'})
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
        u'honbot.playermatchcount': {
            'Meta': {'object_name': 'PlayerMatchCount'},
            'count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'unique': 'True', 'primary_key': 'True', 'db_index': 'True'})
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
            'player_id': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'primary_key': 'True', 'db_index': 'True'}),
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