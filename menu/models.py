from django.db import models
from django.contrib.auth.models import User
# Create your models here.
status = (
	(1,'Admin'),
	(2,'Guest'),
)

class List_User(models.Model):
    nama = models.CharField(max_length=100)
    no_hp = models.CharField(max_length=70)
    status = models.IntegerField(choices = status , blank = True , null = True)
