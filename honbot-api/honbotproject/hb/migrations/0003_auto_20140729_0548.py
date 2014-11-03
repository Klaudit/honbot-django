# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hb', '0002_auto_20140729_0545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playermatchacc',
            name='clan_id',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='playermatchcs',
            name='clan_id',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='playermatchrnk',
            name='clan_id',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]
