from django.contrib import admin
from django.urls import path
from app.documentos import views 

app_name = 'archivos'
urlpatterns = [
   path('udocs/', views.cargarArchivos, name='cargardocs'),
]
