from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,'Principal/index.html',{})

def documentos(request):
	return render(request, 'Principal/documentos.html',{})