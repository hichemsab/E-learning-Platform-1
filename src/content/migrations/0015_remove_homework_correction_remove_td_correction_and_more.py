# Generated by Django 4.0.4 on 2022-04-30 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0014_remove_module_prof'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homework',
            name='correction',
        ),
        migrations.RemoveField(
            model_name='td',
            name='correction',
        ),
        migrations.RemoveField(
            model_name='tp',
            name='correction',
        ),
        migrations.CreateModel(
            name='correction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('correction', models.FileField(upload_to='')),
                ('module', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.module')),
            ],
        ),
    ]