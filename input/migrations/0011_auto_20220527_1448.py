# Generated by Django 3.2.8 on 2022-05-27 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input', '0010_alter_biodata_no_hp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='biodata',
            name='no_hp',
        ),
        migrations.AddField(
            model_name='biodata',
            name='email',
            field=models.EmailField(blank=True, max_length=13, null=True),
        ),
    ]
