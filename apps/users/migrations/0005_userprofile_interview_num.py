# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-09 00:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20180102_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='Interview_Num',
            field=models.IntegerField(default=0, verbose_name='访问量'),
        ),
    ]