# Generated by Django 3.2.8 on 2022-05-20 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keluhan', '0007_problem_teknisi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='judul',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='problem',
            name='pembahasan',
            field=models.TextField(max_length=5000),
        ),
    ]
