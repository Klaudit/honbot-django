# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hb', '0004_auto_20140718_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
