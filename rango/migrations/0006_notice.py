# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-14 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_auto_20161113_1629'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True)),
                ('num', models.IntegerField(default=0)),
                ('unread', models.BooleanField(default=True)),
            ],
        ),
    ]