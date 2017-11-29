# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 12:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0018_create_proxy_member'),
        ('events', '0020_4_user_foreign_keys'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='member',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='members.Member'),
        ),
    ]