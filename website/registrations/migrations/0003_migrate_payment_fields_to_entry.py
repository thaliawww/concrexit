# Generated by Django 2.0.1 on 2018-02-03 13:27

from django.db import migrations


def forwards_func(apps, schema_editor):
    Payment = apps.get_model('registrations', 'payment')
    db_alias = schema_editor.connection.alias
    for payment in Payment.objects.using(db_alias).all():
        entry = payment.entry
        entry.payment = payment
        entry.membership = payment.membership
        entry.save()


def reverse_func(apps, schema_editor):
    Entry = apps.get_model('registrations', 'entry')
    db_alias = schema_editor.connection.alias
    for entry in Entry.objects.using(db_alias).all():
        payment = entry.payment
        payment.old_entry = entry
        payment.old_membership = entry.membership
        payment.save()


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0002_add_payment_fields_to_entry'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]