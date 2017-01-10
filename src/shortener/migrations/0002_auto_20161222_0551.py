# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-22 05:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QprttURLManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='qprtturl',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='qprtturl',
            name='shortcode',
            field=models.CharField(blank=True, max_length=4, unique=True),
        ),
    ]