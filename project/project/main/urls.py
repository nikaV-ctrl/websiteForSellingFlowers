from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('plants', views.plants, name='plants'),
    path('forPlants', views.forPlants, name='forPlants'),
    path('oceanTheme', views.oceanTheme, name='oceanTheme'),
    path('help', views.help, name='help'),
]