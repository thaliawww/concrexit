# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 17:33
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailinglists', '0006_auto_20170226_1822'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='listalias',
            options={'verbose_name': 'List alias', 'verbose_name_plural': 'List aliasses'},
        ),
        migrations.AlterModelOptions(
            name='verbatimaddress',
            options={'verbose_name': 'Verbatim address', 'verbose_name_plural': 'Verbatim addresses'},
        ),
        migrations.AlterField(
            model_name='listalias',
            name='alias',
            field=models.CharField(help_text='Enter an alternative name for the list.', max_length=100, validators=[django.core.validators.RegexValidator(message='Enter a simpler name', regex='^[a-zA-Z0-9]+$')], verbose_name='Alternative name'),
        ),
        migrations.AlterField(
            model_name='mailinglist',
            name='archived',
            field=models.BooleanField(default=True, help_text='Indicate whether an archive should be kept.', verbose_name='Archived'),
        ),
        migrations.AlterField(
            model_name='mailinglist',
            name='committees',
            field=models.ManyToManyField(blank=True, help_text='Select entire committees to include in the list.', to='activemembers.Committee', verbose_name='Committees'),
        ),
        migrations.AlterField(
            model_name='mailinglist',
            name='members',
            field=models.ManyToManyField(blank=True, help_text='Select individual members to include in the list.', to='members.Member', verbose_name='Members'),
        ),
        migrations.AlterField(
            model_name='mailinglist',
            name='moderated',
            field=models.BooleanField(default=False, help_text='Indicate whether emails to the list require approval.', verbose_name='Moderated'),
        ),
        migrations.AlterField(
            model_name='mailinglist',
            name='name',
            field=models.CharField(help_text='Enter the name for the list (i.e. name@thalia.nu).', max_length=100, validators=[django.core.validators.RegexValidator(message='Enter a simpler name', regex='^[a-zA-Z0-9]+$')], verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='mailinglist',
            name='prefix',
            field=models.CharField(help_text='Enter a prefix that should be prefixed to subjects of all emails sent via this mailinglist.', max_length=200, verbose_name='Prefix'),
        ),
        migrations.AlterField(
            model_name='verbatimaddress',
            name='address',
            field=models.EmailField(help_text='Enter an explicit email address to include in the list.', max_length=254, verbose_name='Email address'),
        ),
    ]
