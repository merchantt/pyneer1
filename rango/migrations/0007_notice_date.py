# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-14 16:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0006_notice'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='date',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
