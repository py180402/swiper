# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-30 03:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vip', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vippermrelation',
            old_name='prem_id',
            new_name='perm_id',
        ),
    ]
