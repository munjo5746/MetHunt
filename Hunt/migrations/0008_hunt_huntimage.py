# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hunt', '0007_auto_20150728_0159'),
    ]

    operations = [
        migrations.AddField(
            model_name='hunt',
            name='HuntImage',
            field=models.CharField(default=b'No Image', max_length=100),
        ),
    ]
