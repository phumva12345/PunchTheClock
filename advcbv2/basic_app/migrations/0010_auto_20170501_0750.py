# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 07:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0009_auto_20170424_1358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='name',
        ),
        migrations.AlterField(
            model_name='attendance',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
