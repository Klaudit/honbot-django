# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hb', '0002_auto_20140716_2227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playeravatar',
            name='player_ptr',
        ),
        migrations.DeleteModel(
            name='PlayerAvatar',
        ),
        migrations.AddField(
            model_name='player',
            name='avatar',
            field=models.URLField(default='', max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='avatar_updated',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
