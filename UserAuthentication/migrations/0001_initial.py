# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Email', models.EmailField(unique=True, max_length=254)),
                ('FirstName', models.CharField(default=b'', max_length=50)),
                ('LastName', models.CharField(default=b'', max_length=50)),
                ('Password', models.CharField(default=b'', max_length=100)),
            ],
        ),
    ]
