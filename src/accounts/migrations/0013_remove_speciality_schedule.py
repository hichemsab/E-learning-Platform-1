# Generated by Django 4.0.4 on 2022-05-24 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_speciality_schedule_alter_speciality_speciality'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='speciality',
            name='schedule',
        ),
    ]
