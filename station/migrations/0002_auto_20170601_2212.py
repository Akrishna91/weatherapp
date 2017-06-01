# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('station', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reading',
            name='humidity',
            field=models.CharField(default='None', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reading',
            name='icon_url',
            field=models.URLField(default='None'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reading',
            name='observation_time',
            field=models.CharField(default='None', max_length=100),
            preserve_default=False,
        ),
    ]
