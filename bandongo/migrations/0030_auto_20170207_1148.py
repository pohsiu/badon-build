# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-07 11:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bandongo', '0029_auto_20170207_1119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='savelog',
            old_name='commemt',
            new_name='comment',
        ),
    ]
