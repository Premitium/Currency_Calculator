# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-03 16:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency_name', models.TextField(max_length=225)),
                ('currency_sign', models.CharField(max_length=3)),
                ('currency_to_bgn', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bgn_to_currency', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]