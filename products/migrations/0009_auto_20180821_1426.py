# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-08-21 06:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20180821_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank='true', unique=True),
        ),
    ]