# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-17 01:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='cover',
            field=models.URLField(default='', verbose_name='封面'),
        ),
    ]
