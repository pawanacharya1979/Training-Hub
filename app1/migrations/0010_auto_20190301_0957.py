# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-01 09:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_assignment_assignment1'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='Totalassignmentscompleted',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assignment',
            name='Totalassignmentspending',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
