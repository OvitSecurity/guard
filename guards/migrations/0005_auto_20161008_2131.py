# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-08 21:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guards', '0004_remove_guard_employement'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guard',
            old_name='licence_issue_date',
            new_name='license_issue_date',
        ),
        migrations.AddField(
            model_name='guard',
            name='motherslastname',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='guard',
            name='marital',
            field=models.CharField(choices=[(b'm', b'Married'), (b'd', b'Divorced'), (b'u', b'Unmarried')], default=b'u', max_length=1),
        ),
    ]