# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-10 04:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guards', '0006_guard_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='guard',
            name='image',
            field=models.ImageField(default=b'/static/img/a1.jpg', upload_to=b'/static/img/images'),
        ),
    ]
