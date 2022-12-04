from django.urls import path
from . import views

urlpatterns = [
    path('tambahkan-informasi-list-user', views.tambah_informasi_user, name="tambio"),
    path('biodata<int:id>/', views.update_bio, name="updatebio"),
    path('search_biodata', views.search_biodata, name="search_biodata"),

    
]