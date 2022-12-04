from django.urls import path

from . import views


urlpatterns = [
    
    path('menambahkan_gambar', views.index, name="tambah_gambar"),
    path('menampilkan_gambar', views.show_file, name="tampilan_gambar"),
    path('update_informasi_keluhan/<int:id>', views.update_informasi_keluhan, name="update_informasi_keluhan"),
    path('search', views.search, name="search"),

]