# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-07 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default='none'),
            preserve_default=False,
        ),
    ]
