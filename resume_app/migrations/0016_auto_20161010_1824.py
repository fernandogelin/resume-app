# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-10 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0015_auto_20161010_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='degree',
            field=models.CharField(choices=[('High School 1', 'High School 2'), ('AS', 'Associate'), ('BS', 'BS'), ('BA', 'BA'), ('MS', 'MS'), ('PHD', 'PHD')], default='HS', max_length=30),
        ),
    ]
