# Generated by Django 4.0.4 on 2022-04-26 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0009_cour_title_projet_title_quizz_correction_quizz_title_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Quizz',
            new_name='homework',
        ),
    ]