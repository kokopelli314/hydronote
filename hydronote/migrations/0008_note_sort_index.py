# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-27 01:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hydronote', '0007_note_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='sort_index',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
