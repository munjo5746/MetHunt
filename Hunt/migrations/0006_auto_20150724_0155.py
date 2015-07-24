# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hunt', '0005_auto_20150713_0137'),
    ]

    operations = [
        migrations.AddField(
            model_name='hunt',
            name='Category',
            field=models.CharField(default=b'No Category', max_length=100),
        ),
        migrations.AddField(
            model_name='hunt',
            name='Start',
            field=models.CharField(default=b'No Start Location', max_length=300),
        ),
        migrations.AddField(
            model_name='item',
            name='OrderNumber',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
    ]
