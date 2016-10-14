# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-13 12:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0023_auto_20161013_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='GPA',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='country',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='level',
            field=models.CharField(choices=[('Associate', 'Associate'), ('BS', 'BS'), ('BA', 'BA'), ('MS', 'MS'), ('PHD', 'PHD'), ('online', 'online'), ('specialization', 'specialization'), ('certificate', 'certificate')], default='HS', max_length=30),
        ),
        migrations.AlterField(
            model_name='education',
            name='state',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]