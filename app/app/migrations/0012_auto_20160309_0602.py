# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-09 06:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20160309_0556'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='descriptions',
            managers=[
                ('_default_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 9, 6, 2, 56, 648383)),
        ),
    ]
