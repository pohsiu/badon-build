# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-07 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandongo', '0030_auto_20170207_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog',
            name='choosed',
            field=models.BooleanField(default=False),
        ),
    ]
