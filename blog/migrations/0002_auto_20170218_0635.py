# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 06:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='body',
            new_name='content',
        ),
    ]