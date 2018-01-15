# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-06 17:04
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_post_resolved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='reply',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='question',
            field=tinymce.models.HTMLField(),
        ),
    ]