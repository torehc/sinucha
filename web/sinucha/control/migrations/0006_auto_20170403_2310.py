# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 22:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0005_auto_20170403_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 3, 23, 10, 42, 730268)),
        ),
        migrations.AlterField(
            model_name='sale_history',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 3, 23, 10, 42, 790733)),
        ),
        migrations.AlterField(
            model_name='shopping_history',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 3, 23, 10, 42, 767475)),
        ),
    ]