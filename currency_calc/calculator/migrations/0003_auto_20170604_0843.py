# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-04 08:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0002_auto_20170604_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='bgn_to_currency',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='currency',
            name='currency_name',
            field=models.TextField(max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='currency',
            name='currency_sign',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='currency',
            name='currency_to_bgn',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
