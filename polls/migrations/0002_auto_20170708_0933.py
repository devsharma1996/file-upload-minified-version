# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-08 04:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ekfile',
            name='path_of_file',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='ekfile',
            name='type_of_file',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]