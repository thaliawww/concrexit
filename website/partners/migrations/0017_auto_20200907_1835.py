# Generated by Django 3.1.1 on 2020-09-07 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0016_auto_20200125_1748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partnerevent',
            name='description_nl',
        ),
        migrations.RemoveField(
            model_name='partnerevent',
            name='location_nl',
        ),
        migrations.RemoveField(
            model_name='partnerevent',
            name='title_nl',
        ),
        migrations.RemoveField(
            model_name='vacancycategory',
            name='name_nl',
        ),
    ]
