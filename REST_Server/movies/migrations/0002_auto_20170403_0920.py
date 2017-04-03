# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 09:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='person',
            name='last_name',
            field=models.CharField(default=True, max_length=64),
            preserve_default=False,
        ),
    ]
