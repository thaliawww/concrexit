# Generated by Django 2.1.3 on 2018-11-30 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0034_registration_payment_obj'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='payment_str',
        ),
    ]
