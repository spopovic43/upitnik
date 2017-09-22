# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-08 13:09
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pitanja', '0053_auto_20170908_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pitanje3_2',
            name='Koordinatni_Sistem',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Гаус-Кригер', 'Гаус-Кригер'), ('ETRS89/UTM', 'ETRS89/UTM'), ('Географски координатни систем', 'Географски координатни систем'), ('Подаци нису просторно одређени', 'Подаци нису просторно одређени - геореференцирани'), ('Остало', 'Остало')], max_length=1000),
        ),
        migrations.AlterField(
            model_name='pitanje3_2',
            name='Nacin_Distribucije',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Поштом', 'Поштом'), ('Преко имејла', 'Преко имејла'), ('Директно преузимање ', 'Директно преузимање (дигитални медиј, папир)'), ('Преузимање преко интернета', 'Преузимање преко интернета (download: HTTP и FTP )'), ('Web сервиси', 'Web сервиси'), ('Остало', 'Остало')], max_length=1000),
        ),
    ]