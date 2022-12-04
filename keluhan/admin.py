from django.contrib import admin
from .models import List_keluhan
from django.conf import settings
# Register your models here.
@admin.register(List_keluhan)
class list_keluhanAdmin(admin.ModelAdmin):
 list_display = ('user','judul','teknisi','status')
