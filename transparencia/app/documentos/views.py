from .models import Archivo
from .forms import ArchivoForm

from django.shortcuts import render
from django.db.models import F
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def cargarArchivos(request):
	documento = Archivo.objects.all()
	if request.method == 'POST':
		form = ArchivoForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return render(request, "Administracion/Documentos/archivos.html", {'form':form, 'documento':documento})
	else:
		form = ArchivoForm()
	return render(request,'Administracion/Documentos/archivos.html', {'form':form, 'documento':documento})

def puntuarArchivos(request):
	if request.method == 'POST':
		if request.POST.get('likes'):
			like = Archivo.objects.filter(id = request.POST.get('likes')).update(like=F('like')+1)
			archivo = Archivo.objects.filter(id = request.POST.get('likes'))
			response = serializers.serialize("json",archivo)
			return HttpResponse(response, content_type='application/json')
		else:
			nolike = Archivo.objects.filter(id = request.POST.get('nolike')).update(dislike=F('dislike')+1)
			archivo = Archivo.objects.filter(id = request.POST.get('nolike'))
			response = serializers.serialize("json",archivo)
			return HttpResponse(response, content_type='application/json')
	
	pass