# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-23 11:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('interest', '0002_book_num_pages'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='author',
            managers=[
                ('people', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='sex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
            preserve_default=False,
        ),
    ]
