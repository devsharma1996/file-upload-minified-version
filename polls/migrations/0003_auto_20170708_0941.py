# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-08 04:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20170708_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ekfile',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]