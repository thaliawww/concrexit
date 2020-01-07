# Generated by Django 2.2.6 on 2019-11-20 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0009_auto_20191120_1906'),
        ('events', '0038_auto_20191024_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='slide',
            field=models.ForeignKey(blank=True, help_text="Change the header-image on the event's info-page to onespecific to this event.", null=True, on_delete=django.db.models.deletion.SET_NULL, to='announcements.Slide', verbose_name='slide'),
        ),
    ]