# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hunt', '0003_remove_hunt_testattrip'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='HintCrop',
            field=models.CharField(default='default', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='ItemImage',
            field=models.CharField(default='default', max_length=200),
            preserve_default=False,
        ),
    ]
