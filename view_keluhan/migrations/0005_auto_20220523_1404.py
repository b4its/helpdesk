# Generated by Django 3.2.8 on 2022-05-23 06:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('view_keluhan', '0004_file_upload_judul'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file_upload',
            name='judul',
        ),
        migrations.AddField(
            model_name='file_upload',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='file_uploud', to=settings.AUTH_USER_MODEL),
        ),
    ]