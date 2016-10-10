# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-05 14:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0003_education_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='degree',
            field=models.CharField(choices=[('hs', 'High School'), ('a', 'Associate'), ('bs', 'BS'), ('ba', 'BA'), ('ms', 'MS'), ('phd', 'PHD')], default='hs', max_length=30),
        ),
        migrations.AlterField(
            model_name='education',
            name='GPA',
            field=models.FloatField(blank=True),
        ),
    ]
