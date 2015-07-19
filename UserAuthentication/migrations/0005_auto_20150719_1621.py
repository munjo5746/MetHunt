# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserAuthentication', '0004_auto_20150719_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='UserName',
            field=models.CharField(max_length=50),
        ),
    ]
