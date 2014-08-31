# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hb', '0004_auto_20140810_2047'),
    ]

    operations = [
        migrations.CreateModel(
            name='APICount',
            fields=[
                ('date', models.DateField(primary_key=True, unique=True, db_index=True, serialize=False, auto_now=True)),
                ('count', models.PositiveIntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
