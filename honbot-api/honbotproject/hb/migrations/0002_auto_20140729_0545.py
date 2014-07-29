# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playermatchacc',
            name='secs_dead',
            field=models.PositiveIntegerField(null=True, default=0),
        ),
        migrations.AlterField(
            model_name='playermatchcs',
            name='secs_dead',
            field=models.PositiveIntegerField(null=True, default=0),
        ),
        migrations.AlterField(
            model_name='playermatchrnk',
            name='secs_dead',
            field=models.PositiveIntegerField(null=True, default=0),
        ),
    ]
