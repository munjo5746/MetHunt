# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hunt', '0002_hunt_testattrip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hunt',
            name='TestAttrip',
        ),
    ]
