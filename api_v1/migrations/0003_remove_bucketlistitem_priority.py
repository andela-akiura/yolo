# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-03 00:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_v1', '0002_bucketlistitem_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bucketlistitem',
            name='priority',
        ),
    ]
