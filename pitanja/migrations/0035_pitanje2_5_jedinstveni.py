# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-21 08:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pitanja', '0034_remove_pitanje2_5_jedinstveni'),
    ]

    operations = [
        migrations.AddField(
            model_name='pitanje2_5',
            name='Jedinstveni',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]