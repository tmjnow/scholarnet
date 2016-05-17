# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-08 18:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20160308_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='descriptions',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Subjects'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 8, 18, 9, 14, 130872)),
        ),
    ]
