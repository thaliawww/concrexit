# Generated by Django 2.2.6 on 2019-11-29 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0010_payment_registration'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pizzaevent',
            options={'ordering': ('-start',)},
        ),
    ]