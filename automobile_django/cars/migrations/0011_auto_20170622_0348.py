# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 03:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0010_auto_20170622_0340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='slot_number',
        ),
        migrations.AlterField(
            model_name='car',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
    ]
