# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-06 18:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_subjects_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjects',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Year'),
        ),
    ]
