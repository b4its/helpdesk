# Generated by Django 3.2.8 on 2022-05-30 08:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('view_keluhan', '0012_remove_fileupload_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileupload',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fileuploud', to=settings.AUTH_USER_MODEL),
        ),
    ]
