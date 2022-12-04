from django.contrib import admin

from .models import FileUpload
# Register your models here.

@admin.register(FileUpload)
class file_uploudAdmin(admin.ModelAdmin):
 list_display = ('file_name','pembahasan','status')

