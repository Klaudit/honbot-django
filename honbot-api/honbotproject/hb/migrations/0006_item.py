# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hb', '0005_apicount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.PositiveSmallIntegerField(serialize=False, primary_key=True, db_index=True, unique=True)),
                ('name', models.TextField(null=True, default='')),
                ('cli_name', models.TextField(null=True, default='')),
                ('cost', models.PositiveIntegerField(default=0)),
                ('description', models.TextField(null=True, default='')),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
