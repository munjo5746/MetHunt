# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hunt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hunt',
            name='TestAttrip',
            field=models.CharField(default='default', max_length=50),
            preserve_default=False,
        ),
    ]
