# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2019-07-08 09:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0015_samplereads_write_her_files'),
    ]

    operations = [
        migrations.AddField(
            model_name='fullmsvmergedreads',
            name='_num_reads_F',
            field=models.PositiveIntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='fullmsvmergedreads',
            name='_num_reads_M',
            field=models.PositiveIntegerField(default=None, null=True),
        ),
    ]
