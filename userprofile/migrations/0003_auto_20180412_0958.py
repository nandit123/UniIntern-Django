# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-12 09:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_studentprojects'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StudentProjects',
            new_name='StudentProject',
        ),
    ]
