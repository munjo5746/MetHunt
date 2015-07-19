# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hunt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Title', models.CharField(max_length=100)),
                ('Items', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('QuestionId', models.CharField(max_length=50, unique=True, serialize=False, primary_key=True)),
                ('Category', models.CharField(max_length=50)),
                ('Clue', models.CharField(max_length=100)),
                ('Location', models.CharField(max_length=300)),
                ('Hint', models.CharField(max_length=200)),
                ('Fact', models.CharField(max_length=200)),
                ('BelongTo', models.ManyToManyField(to='Hunt.Hunt')),
            ],
        ),
    ]
