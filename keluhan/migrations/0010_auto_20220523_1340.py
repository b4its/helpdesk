# Generated by Django 3.2.8 on 2022-05-23 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('keluhan', '0009_rename_problem_list_keluhan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list_keluhan',
            name='foto1',
        ),
        migrations.RemoveField(
            model_name='list_keluhan',
            name='foto2',
        ),
    ]
