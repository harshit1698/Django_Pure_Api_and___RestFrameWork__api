# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-05-23 15:15
from __future__ import unicode_literals

from django.db import migrations, models
import rest.models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ap',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=rest.models.upload_img),
        ),
    ]
