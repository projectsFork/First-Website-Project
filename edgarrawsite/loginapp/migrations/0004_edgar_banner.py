# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-07 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0003_auto_20161207_0433'),
    ]

    operations = [
        migrations.AddField(
            model_name='edgar',
            name='banner',
            field=models.CharField(default='', max_length=50),
        ),
    ]
