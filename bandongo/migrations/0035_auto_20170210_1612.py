# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-10 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandongo', '0034_auto_20170209_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='bag',
            field=models.IntegerField(choices=[('one', 1), ('two', 2), ('three', 3)]),
        ),
    ]
