# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-27 15:53
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20171227_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='Content',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='', verbose_name='内容'),
        ),
    ]
