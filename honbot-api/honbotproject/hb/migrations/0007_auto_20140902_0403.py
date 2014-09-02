# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hb', '0006_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='item_id',
            new_name='id',
        ),
    ]
