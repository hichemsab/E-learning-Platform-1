# Generated by Django 4.0.4 on 2022-05-22 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0017_alter_module_speciality_delete_homework'),
    ]

    operations = [
        migrations.CreateModel(
            name='homework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('quizz', models.FileField(upload_to='homework')),
                ('module', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.module')),
            ],
        ),
    ]