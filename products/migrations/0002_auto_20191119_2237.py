# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-11-19 22:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='max_buy',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=5, null=True),
        ),
    ]