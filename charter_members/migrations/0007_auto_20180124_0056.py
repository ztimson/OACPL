# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-24 05:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charter_members', '0006_auto_20180123_2302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='position',
            old_name='position_name',
            new_name='name',
        ),
    ]
