# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-12 08:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_remove_content_folder_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='folder_file',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='content',
            name='json_file',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='ekfile',
            name='file',
            field=models.FileField(upload_to=b''),
        ),
    ]
