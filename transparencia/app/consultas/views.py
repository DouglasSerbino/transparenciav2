from django.shortcuts import render

from app.documentos.models import Archivo
# Create your views here.
def index(request):
	return render(request,'Principal/index.html',{})

def documentos(request):
	archivo = Archivo.objects.all()
	return render(request, 'Principal/documentos.html',{'archivo':archivo})