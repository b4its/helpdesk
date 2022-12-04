from django.urls import path
from . import views

urlpatterns = [
	path('list-user', views.list_user, name='list_user'),
    path('help', views.help, name='help'),    
]