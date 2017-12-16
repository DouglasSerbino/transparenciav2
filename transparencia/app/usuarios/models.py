from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
	nivel = models.IntegerField(null=True)
	puntuacion = models.IntegerField(null=True)
	foto = models.ImageField(null=True, upload_to='fotos_perfil/')
