# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-29 16:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tpj', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='contribution',
            table='contribs',
        ),
        migrations.AlterModelTable(
            name='donor',
            table='contributors',
        ),
        migrations.AlterModelTable(
            name='filer',
            table='filers',
        ),
    ]
