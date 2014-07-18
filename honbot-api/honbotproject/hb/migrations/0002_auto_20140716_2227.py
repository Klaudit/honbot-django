# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playerhistory',
            name='history_updated',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
