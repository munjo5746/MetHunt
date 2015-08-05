# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserAuthentication', '0007_auto_20150805_1823'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermodel',
            old_name='User',
            new_name='BelongTo',
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='HuntCompleted',
            field=models.TextField(default=b'[]', blank=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='HuntInProgress',
            field=models.TextField(default=b'[]', blank=True),
        ),
    ]
