# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-07-05 14:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0047_auto_20180628_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentfielddetector',
            name='extraction_hint',
            field=models.CharField(blank=True, choices=[('TAKE_FIRST', 'TAKE_FIRST'), ('TAKE_SECOND', 'TAKE_SECOND'), ('TAKE_LAST', 'TAKE_LAST'), ('TAKE_MIN', 'TAKE_MIN'), ('TAKE_MAX', 'TAKE_MAX')], db_index=True, default='TAKE_FIRST', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='documentfieldvalue',
            name='extraction_hint',
            field=models.CharField(blank=True, choices=[('TAKE_FIRST', 'TAKE_FIRST'), ('TAKE_SECOND', 'TAKE_SECOND'), ('TAKE_LAST', 'TAKE_LAST'), ('TAKE_MIN', 'TAKE_MIN'), ('TAKE_MAX', 'TAKE_MAX')], db_index=True, default='TAKE_FIRST', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='historicaldocumentfieldvalue',
            name='extraction_hint',
            field=models.CharField(blank=True, choices=[('TAKE_FIRST', 'TAKE_FIRST'), ('TAKE_SECOND', 'TAKE_SECOND'), ('TAKE_LAST', 'TAKE_LAST'), ('TAKE_MIN', 'TAKE_MIN'), ('TAKE_MAX', 'TAKE_MAX')], db_index=True, default='TAKE_FIRST', max_length=30, null=True),
        ),
    ]