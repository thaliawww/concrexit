# Generated by Django 3.1.6 on 2021-02-17 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0044_event_tpay_allowed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='tpay_allowed',
            field=models.BooleanField(default=True, verbose_name='Allow Thalia Pay'),
        ),
    ]
