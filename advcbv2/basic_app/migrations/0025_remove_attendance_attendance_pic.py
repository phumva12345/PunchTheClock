# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-29 13:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0024_auto_20170529_2033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='attendance_pic',
        ),
    ]
