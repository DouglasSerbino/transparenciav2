from django.urls import path
from app.usuarios import views

app_name = 'usuarios'
urlpatterns = [
	path('registro/', views.registro, name='registro' ),
	#path('perfil/', views.perfil, name='perfil'),
]
