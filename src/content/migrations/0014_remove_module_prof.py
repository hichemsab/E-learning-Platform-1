# Generated by Django 4.0.4 on 2022-04-27 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0013_module_prof'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='prof',
        ),
    ]