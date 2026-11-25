
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('daftar/', views.daftar, name='daftar'),
    path('logout/', views.logout_view, name='logout'),
    path('zikir/', views.zikir, name='zikir'),
    path('pengaturan/', views.settings, name='settings'),
    path('profil/', views.profil, name='profil'),
    path('explore/', views.explore, name='explore'),
    path('koleksi/', views.koleksi, name='koleksi'),
    path('suara-doa/', views.suara_doa, name='suara_doa'),
]
