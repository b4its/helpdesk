# Generated by Django 3.2.12 on 2022-05-23 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('view_keluhan', '0002_auto_20220523_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file_upload',
            name='pembahasan',
            field=models.TextField(max_length=5000, null=True),
        ),
    ]