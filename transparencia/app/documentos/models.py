from django.db import models

from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.
class Archivo(models.Model):
	nombre_archivo = models.CharField(max_length=255)
	descripcion = models.CharField(max_length=500)
	like = models.IntegerField(null=True,default='0')
	dislike = models.IntegerField(null=True,default='0')
	archivo = models.FileField(upload_to='Documentos/')

	class Meta:
		verbose_name='Documento'
		verbose_name_plural='Documentos'

	def __str__(self):
		return self.nombre_archivo

@receiver(post_delete, sender=Archivo)
def documento(sender, instance, **kwargs):
	instance.documento.delete(False)