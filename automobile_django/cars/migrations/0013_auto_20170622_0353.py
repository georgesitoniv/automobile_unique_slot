# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 03:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0012_auto_20170622_0349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='slot',
            name='slot_number',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
