# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-11 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0019_auto_20161011_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='skills',
            name='category',
            field=models.CharField(blank=True, choices=[('programing language', 'programing language'), ('software', 'software'), ('web framework', 'web framework'), ('', '')], max_length=50, null=True),
        ),
    ]