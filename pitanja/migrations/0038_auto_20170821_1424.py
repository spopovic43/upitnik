# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-21 12:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pitanja', '0037_auto_20170821_1154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='building',
            name='block',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='family',
        ),
        migrations.RemoveField(
            model_name='tenant',
            name='building',
        ),
        migrations.RemoveField(
            model_name='pitanje3_1',
            name='Jedinstveni',
        ),
        migrations.RemoveField(
            model_name='pitanje3_2',
            name='Jedinstveni',
        ),
        migrations.RemoveField(
            model_name='pitanje3_3',
            name='Jedinstveni',
        ),
        migrations.RemoveField(
            model_name='pitanje3_4',
            name='Jedinstveni',
        ),
        migrations.RemoveField(
            model_name='pitanje3_5',
            name='Jedinstveni',
        ),
        migrations.RemoveField(
            model_name='pitanje4_7',
            name='Jedinstveni',
        ),
        migrations.RemoveField(
            model_name='pitanje5_1',
            name='Jedinstveni',
        ),
        migrations.RemoveField(
            model_name='pitanje5_12',
            name='Jedinstveni',
        ),
        migrations.RemoveField(
            model_name='pitanje5_13',
            name='Jedinstveni',
        ),
        migrations.RemoveField(
            model_name='pitanje5_14',
            name='Jedinstveni',
        ),
        migrations.RemoveField(
            model_name='pitanje5_2',
            name='Jedinstveni',
        ),
        migrations.RemoveField(
            model_name='pitanje5_4',
            name='Jedinstveni',
        ),
        migrations.RemoveField(
            model_name='prostornipodaci',
            name='Jedinstveni',
        ),
        migrations.RemoveField(
            model_name='saradnjaizmedjusubjekata',
            name='Jedinstveni',
        ),
        migrations.RemoveField(
            model_name='standardizacijaotvorenihpodataka',
            name='Jedinstveni',
        ),
        migrations.DeleteModel(
            name='Block',
        ),
        migrations.DeleteModel(
            name='Building',
        ),
        migrations.DeleteModel(
            name='FamilyMember',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='Tenant',
        ),
    ]
