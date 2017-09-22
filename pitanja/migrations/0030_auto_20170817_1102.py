# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-17 09:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pitanja', '0029_auto_20170817_1050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pitanje2_5',
            name='Namena',
        ),
        migrations.AddField(
            model_name='pitanje2_5',
            name='Namena',
            field=models.CharField(choices=[('Израда планова и карата', 'Израда планова и карата'), ('Пројектовање', 'Пројектовање'), ('Извештавање', 'Извештавање'), ('Управљање и планирање коришћења земљишта', 'Управљање и планирање коришћења земљишта'), ('Урбанизам и грађевински послови', 'Урбанизам и грађевински послови'), ('Праћење промена и просторне анализе', 'Праћење промена и просторне анализе'), ('Креирање и анализа ДМТ', 'Креирање и анализа ДМТ'), ('Геореференцирање и обрада растерских података', 'Геореференцирање и обрада растерских података'), ('Даљинска детекција', 'Даљинска детекција'), ('Обрада података добијених ласерским скенирањем', 'Обрада података добијених ласерским скенирањем'), ('Остало', 'Остало')], max_length=100, null=True),
        ),
    ]
