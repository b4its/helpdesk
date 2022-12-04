from django.contrib import admin
from .models import List_User


@admin.register(List_User)
class managementAdmin(admin.ModelAdmin):
 list_display = ('id','nama','no_hp','status')



