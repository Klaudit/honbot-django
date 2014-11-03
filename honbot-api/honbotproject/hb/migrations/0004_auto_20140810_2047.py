# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hb', '0003_auto_20140729_0548'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='playermatchacc',
            options={'ordering': ['-match_id']},
        ),
        migrations.AlterModelOptions(
            name='playermatchcs',
            options={'ordering': ['-match_id']},
        ),
        migrations.AlterModelOptions(
            name='playermatchrnk',
            options={'ordering': ['-match_id']},
        ),
        migrations.AddField(
            model_name='playermatchacc',
            name='date',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='playermatchcs',
            name='date',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='playermatchrnk',
            name='date',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
