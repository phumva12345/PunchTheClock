# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-29 13:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0025_remove_attendance_attendance_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='attendance_pic',
            field=models.ImageField(blank=True, null=True, upload_to='attendance_pics'),
        ),
    ]