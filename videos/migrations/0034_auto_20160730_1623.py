# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-30 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0033_scene_framerate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='scenes',
            field=models.ManyToManyField(null=True, related_name='folders_in_tree', to='videos.Scene'),
        ),
    ]
