# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-11 05:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pitanja', '0054_auto_20170908_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='pitanje3_2',
            name='Koordinatni_Sistem_ostalo',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Координатни систем остало'),
        ),
        migrations.AddField(
            model_name='saradnjaizmedjusubjekata',
            name='Na_koji_nacin_obezbedjujete_podatke_za_svoje_potrebe_drugo',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='На који начин обезбеђујете податке за своје потребе друго'),
        ),
    ]
