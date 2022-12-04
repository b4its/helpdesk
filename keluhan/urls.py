from django.urls import path
from . import views

urlpatterns = [
	path('keluhan', views.keluhan_teknisi, name="problem"),
  path('keluhanmu', views.keluhan_pengguna, name="keluhanmu"),
  path('search_teknisi', views.search_teknisi, name="search_teknisi"),
  path('tambahkan-keluhan', views.tambahkan_keluhan, name="tambahkan-problem"),
  path('keluhan/<int:id>', views.update_keluhan, name="update-keluhan"),
    
]