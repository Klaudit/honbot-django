# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hb', '0003_auto_20140716_2232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playerhistory',
            name='player_ptr',
        ),
        migrations.DeleteModel(
            name='PlayerHistory',
        ),
        migrations.AddField(
            model_name='player',
            name='acc_history',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='cs_history',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='history_updated',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='rnk_history',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
    ]
