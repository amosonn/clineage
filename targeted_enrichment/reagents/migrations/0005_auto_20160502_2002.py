# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-02 20:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reagents', '0004_auto_20160420_1723'),
        ('amplicons', '0002_create_ter_amplicons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pcr1primerpairter',
            name='amplicon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amplicons.PlainTargetedAmplicon'),
        ),
        migrations.AlterField(
            model_name='pcr1primerpairterdeprecated',
            name='amplicon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amplicons.PlainTargetedAmplicon'),
        ),
        migrations.AlterField(
            model_name='pcr1withcompanytagprimerpairter',
            name='amplicon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amplicons.TargetedAmpliconWithCompanyTag'),
        ),
        migrations.AlterField(
            model_name='shortpadlockfirstter',
            name='amplicon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amplicons.UMITargetedAmplicon'),
        ),
    ]
