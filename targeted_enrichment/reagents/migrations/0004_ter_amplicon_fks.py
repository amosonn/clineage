# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-20 17:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('amplicons', '0001_initial'),
        ('reagents', '0003_om6padlockter'),
    ]

    operations = [
        migrations.AddField(
            model_name='pcr1primerpairter',
            name='amplicon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='amplicons.PlainTargetedAmplicon'),
        ),
        migrations.AddField(
            model_name='pcr1primerpairterdeprecated',
            name='amplicon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='amplicons.PlainTargetedAmplicon'),
        ),
        migrations.AddField(
            model_name='targetednotailprimerpairter',
            name='amplicon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='amplicons.PlainTargetedAmplicon'),
        ),
        migrations.AddField(
            model_name='pcr1withcompanytagprimerpairter',
            name='amplicon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='amplicons.TargetedAmpliconWithCompanyTag'),
        ),
        migrations.AddField(
            model_name='om6padlockterbase',
            name='amplicon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='amplicons.UMITargetedAmplicon'),
        ),
    ]
