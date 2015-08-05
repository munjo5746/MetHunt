# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('UserAuthentication', '0006_auto_20150805_1759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='FirstName',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='LastName',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='Password',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='UserName',
        ),
        migrations.AddField(
            model_name='usermodel',
            name='User',
            field=models.OneToOneField(default=None, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='HuntCompleted',
            field=models.TextField(default=b'[]'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='HuntInProgress',
            field=models.TextField(default=b'[]'),
        ),
    ]
