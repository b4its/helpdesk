# Generated by Django 3.2.12 on 2022-05-17 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_alter_management_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='management',
            name='status',
            field=models.IntegerField(blank=True, choices=[(1, 'Admin'), (2, 'Guest')], null=True),
        ),
    ]
