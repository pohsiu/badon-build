# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-23 21:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandongo', '0008_auto_20170123_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='expire',
            field=models.BooleanField(default=False),
        ),
    ]
