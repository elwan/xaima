# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-19 22:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simulation', '0004_auto_20170619_1647'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarif',
            old_name='est_international',
            new_name='est_internationnal',
        ),
    ]