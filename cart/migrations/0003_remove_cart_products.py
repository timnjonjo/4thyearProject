# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-13 04:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cart_prices'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='products',
        ),
    ]
