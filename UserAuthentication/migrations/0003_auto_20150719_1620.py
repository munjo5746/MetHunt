# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserAuthentication', '0002_usermodel_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='UserName',
            field=models.CharField(default=b'', unique=True, max_length=50),
        ),
    ]
