# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 23:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traffic_api', '0005_auto_20170314_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intersectiondata',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
