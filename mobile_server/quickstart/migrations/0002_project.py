# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-12 06:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('summary', models.TextField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('users', models.ManyToManyField(to='quickstart.User')),
            ],
        ),
    ]