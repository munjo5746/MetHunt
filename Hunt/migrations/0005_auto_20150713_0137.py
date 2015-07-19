# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hunt', '0004_auto_20150713_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hunt',
            name='Items',
            field=models.CharField(default=b'No Hunt Items', max_length=100),
        ),
        migrations.AlterField(
            model_name='hunt',
            name='Title',
            field=models.CharField(default=b'No Hunt Title', max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='Category',
            field=models.CharField(default=b'No Item Category', max_length=50),
        ),
        migrations.AlterField(
            model_name='item',
            name='Clue',
            field=models.CharField(default=b'No Item Clue', max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='Fact',
            field=models.CharField(default=b'No Item Fact', max_length=200),
        ),
        migrations.AlterField(
            model_name='item',
            name='Hint',
            field=models.CharField(default=b'No Item Hint', max_length=200),
        ),
        migrations.AlterField(
            model_name='item',
            name='HintCrop',
            field=models.CharField(default=b'No Item HintCrop', max_length=200),
        ),
        migrations.AlterField(
            model_name='item',
            name='ItemImage',
            field=models.CharField(default=b'No Item Image', max_length=200),
        ),
        migrations.AlterField(
            model_name='item',
            name='Location',
            field=models.CharField(default=b'No Item Location', max_length=300),
        ),
        migrations.AlterField(
            model_name='item',
            name='QuestionId',
            field=models.CharField(default=b'No Item ID', max_length=50, unique=True, serialize=False, primary_key=True),
        ),
    ]
