from django.contrib import admin
from django.urls import path
from app.consultas import views 

app_name = 'consultas'
urlpatterns = [
   path('', views.index, name='inicio'),
   path('documentos/', views.documentos, name='documentos'),
]
