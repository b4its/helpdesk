from django.contrib import admin
from .models import Keluhan,Biodata
# Register your models here.
@admin.register(Biodata)
class biodataAdmin(admin.ModelAdmin):
 list_display = ('id','user','email','alamat')


