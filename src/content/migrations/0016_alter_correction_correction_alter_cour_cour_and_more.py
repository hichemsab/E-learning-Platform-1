# Generated by Django 4.0.4 on 2022-05-06 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0015_remove_homework_correction_remove_td_correction_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='correction',
            name='correction',
            field=models.FileField(upload_to='correction'),
        ),
        migrations.AlterField(
            model_name='cour',
            name='cour',
            field=models.FileField(upload_to='Cour'),
        ),
        migrations.AlterField(
            model_name='homework',
            name='quizz',
            field=models.FileField(upload_to='homework'),
        ),
        migrations.AlterField(
            model_name='td',
            name='td',
            field=models.FileField(blank=True, null=True, upload_to='TD'),
        ),
        migrations.AlterField(
            model_name='tp',
            name='tp',
            field=models.FileField(upload_to='TP'),
        ),
    ]