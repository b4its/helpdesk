# Generated by Django 3.2.12 on 2022-04-28 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_management_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='management',
            name='status',
            field=models.IntegerField(blank=True, choices=[(1, 'Admin'), (2, 'Guest')], null=True),
        ),
    ]
