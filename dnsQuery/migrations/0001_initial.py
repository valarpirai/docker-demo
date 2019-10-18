# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-03 05:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request', models.CharField(max_length=200)),
                ('response', models.CharField(max_length=200)),
                ('created', models.DateTimeField(verbose_name='created date')),
            ],
        ),
    ]