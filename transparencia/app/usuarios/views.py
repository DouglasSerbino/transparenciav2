from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model
from .forms import SignUpForm 
User = get_user_model()

# Create your views here.
def registro(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user =  authenticate(username=username, password=raw_password)
			login(request,user)
			return redirect('/')
	else:
		form = SignUpForm()
	return render(request,'Usuarios/registro.html',{'form':form})

def perfil(request):
	return render(request, 'Usuarios/perfil.html')