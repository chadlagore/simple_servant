# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-30 01:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traffic_api', '0006_auto_20170314_2325'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalData',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField()),
                ('hour', models.IntegerField()),
                ('cars', models.IntegerField()),
            ],
        ),
    ]