# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-08-25 02:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='total',
            new_name='subtotal',
        ),
    ]
