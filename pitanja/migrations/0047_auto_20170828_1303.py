# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-28 11:03
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pitanja', '0046_auto_20170825_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saradnjaizmedjusubjekata',
            name='Ko_su_korisnici_vasih_proizvoda',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Сопствене потребе', 'Сопствене потребе'), ('Органи државне управе', 'Органи државне управе'), ('Органи територијалне аутономије', 'Органи територијалне аутономије'), ('Органи локалне самоуправе', 'Органи локалне самоуправе'), ('Јавне агенције', 'Јавне агенције'), ('Јавна предузећа', 'Јавна предузећа'), ('Научно-образовне установе', 'Научно-образовне установе'), ('Пројектантскo-урбанистичке организације', 'Пројектантскo-урбанистичке организације'), ('Приватне организације', 'Приватне организације'), ('Европске и друге међународне институције', 'Европске и друге међународне институције'), ('Грађани', 'Грађани'), ('Друго', 'Друго')], max_length=200),
        ),
        migrations.AlterField(
            model_name='saradnjaizmedjusubjekata',
            name='Kojem_modelu_finansiranja_NGIPA_treba_teziti',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Покривање трошкова производње из буџета', 'Покривање трошкова производње из буџета за кључне геоподатке, уз размену без накнаде између субјеката НИГП-а'), ('Накнада за коришћење геоподатака према договореним условима', 'Накнада за коришћење геоподатака према договореним условима'), ('Тржишни услови', 'Тржишни услови'), ('Друго', 'Друго')], max_length=200),
        ),
        migrations.AlterField(
            model_name='saradnjaizmedjusubjekata',
            name='Model_odredjivanja_cene',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Покривање трошкова производње', 'Покривање трошкова производње'), ('Тржишна цена', 'Тржишна цена'), ('Друго', 'Друго')], max_length=200),
        ),
        migrations.AlterField(
            model_name='saradnjaizmedjusubjekata',
            name='Na_koji_nacin_obezbedjujete_podatke_za_svoje_potrebe',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Сопствена производња података', 'Сопствена производња података'), ('Набавка кроз пројекте', 'Набавка кроз пројекте'), ('Преузимањем од других државних органа без накнаде', 'Преузимањем од других државних органа без накнаде'), ('Куповина', 'Куповина'), ('Друго', 'Друго')], max_length=200),
        ),
        migrations.AlterField(
            model_name='saradnjaizmedjusubjekata',
            name='Na_koji_nacin_saradjujete_sa_drugim_organizacijama_pri_razmeni',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('По захтеву', 'По захтеву'), ('На основу уговора/споразума', 'На основу уговора/споразума'), ('На основу закона', 'На основу закона'), ('Друго', 'Друго')], max_length=200),
        ),
        migrations.AlterField(
            model_name='saradnjaizmedjusubjekata',
            name='Problemi_prilikom_nabavke_geopodataka',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Непостојање геоподатака у дигиталној форми ', 'Непостојање геоподатака у дигиталној форми '), ('Слабо доступне информације о надлежној организацији за одређене геоподатке', 'Слабо доступне информације о надлежној организацији за одређене геоподатке'), ('Стари/неажурни подаци', 'Стари/неажурни подаци'), ('Некомплетни подаци', 'Некомплетни подаци (просторни обухват и атрибути)'), ('Неодговарајући квалитет података', 'Неодговарајући квалитет података'), ('Високе цене', 'Високе цене'), ('Некомпатибилни формати података', 'Некомпатибилни формати података'), ('Сложене и нејасне процедуре', 'Сложене и нејасне процедуре'), ('Кашњење у испоруци', 'Кашњење у испоруци'), ('Неодговарајућа корисничка подршка', 'Неодговарајућа корисничка подршка'), ('Ограничена права приступа ', 'Ограничена права приступа '), ('Друго', 'Друго')], max_length=200),
        ),
    ]
