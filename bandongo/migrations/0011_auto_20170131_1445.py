# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-31 14:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bandongo', '0010_auto_20170129_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='savelog',
            name='admin_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='admin', to='bandongo.Member'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='savelog',
            name='member_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person', to='bandongo.Member'),
        ),
    ]
