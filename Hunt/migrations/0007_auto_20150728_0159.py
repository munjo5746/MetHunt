# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hunt', '0006_auto_20150724_0155'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=0, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='QuestionId',
            field=models.CharField(default=b'No Item ID', unique=True, max_length=50),
        ),
    ]
