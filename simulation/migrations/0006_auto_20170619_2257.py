# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-19 22:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simulation', '0005_auto_20170619_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarif',
            name='societe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='societe', to='simulation.Societe_Transfert'),
        ),
    ]
