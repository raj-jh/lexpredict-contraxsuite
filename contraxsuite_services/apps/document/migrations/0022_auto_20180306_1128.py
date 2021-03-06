# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-06 11:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_projectupload'),
        ('document', '0021_auto_20180305_1947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='projects',
        ),
        migrations.AddField(
            model_name='document',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Project'),
        ),
        migrations.AddField(
            model_name='document',
            name='upload',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.ProjectUpload'),
        ),
        migrations.AddField(
            model_name='historicaldocument',
            name='project',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='project.Project'),
        ),
        migrations.AddField(
            model_name='historicaldocument',
            name='upload',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='project.ProjectUpload'),
        ),
    ]
