# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-01 18:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20180601_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='overview',
            field=models.CharField(default=django.utils.timezone.now, max_length=300),
            preserve_default=False,
        ),
    ]