from .models import Archivo
from .forms import ArchivoForm

from django.shortcuts import render

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