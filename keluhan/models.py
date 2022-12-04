from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
status = (
	(1,'Diajukan'),
	(2,'Diproses'),
    (3,'Selesai'),
)

judul = (
	(1,'Permasalahan website'),
	(2,'Permasalahan database'),
    (3,'Permasalahan lainnya'),
)

class List_keluhan(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE,related_name='problem' , blank = True , null = True )
    judul = models.IntegerField(choices = judul)
    pembahasan = models.CharField(max_length=5000)
    teknisi = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='teknisi', blank=True, null=True)
    status = models.IntegerField(choices = status ,default=1)
    date_posted = models.DateTimeField(default=timezone.now)
    