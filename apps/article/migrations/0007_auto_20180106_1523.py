# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-06 15:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0006_auto_20171227_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='User',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='分类用户'),
        ),
        migrations.AddField(
            model_name='comment',
            name='Comment_User',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='评论用户'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='Comment_ComId',
            field=models.IntegerField(default=0, verbose_name='被评论用户'),
        ),
    ]
