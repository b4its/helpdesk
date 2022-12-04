from distutils.command import upload
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Biodata(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, related_name= 'biodata' , blank = True , null = True)
    email = models.EmailField(max_length=200,null = True , blank = True)
    alamat = models.TextField(max_length=1000) 

class Keluhan(models.Model):
	user = models.ForeignKey(User, on_delete= models.CASCADE,related_name='keluhan' , blank = True , null = True )
	judul = models.CharField(max_length=70)
	pembahasan = models.TextField(max_length=5000)


    

