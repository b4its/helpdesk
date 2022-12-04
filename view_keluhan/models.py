from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
status = (
	(1,'Diajukan'),
	(2,'Diproses'),
    (3,'Selesai'),
)


class FileUpload(models.Model):
    ids = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=255)
    pembahasan = models.TextField(max_length=5000,null=True)
    my_file = models.FileField(upload_to='keluhan/sebelum',blank=True,null=True)
    my_file2 = models.FileField(upload_to='keluhan/sesudah',blank=True,null=True)
    status = models.IntegerField(choices = status ,default=1)
    date_posted = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return self.file_name
    
