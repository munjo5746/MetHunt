# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserAuthentication', '0005_auto_20150719_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='HuntCompleted',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='HuntInProgress',
            field=models.TextField(default=b''),
        ),
    ]
