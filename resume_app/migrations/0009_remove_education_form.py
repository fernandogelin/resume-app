# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-07 20:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0008_education_form'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='form',
        ),
    ]
