# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-30 03:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20181130_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='vip_id',
            field=models.IntegerField(default=1),
        ),
    ]