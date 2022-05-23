# Generated by Django 4.0.4 on 2022-04-25 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='COUR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cour', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='PROJET',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projet', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Quizz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quizz', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='TD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('td', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='TP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tp', models.FileField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='modules',
            name='contenu',
        ),
        migrations.DeleteModel(
            name='Contenu',
        ),
    ]