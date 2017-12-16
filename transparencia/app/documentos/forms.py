from django import forms 
from .models import Archivo

class ArchivoForm(forms.ModelForm):
    class Meta:
    	model = Archivo
    	fields = ('nombre_archivo','descripcion','archivo')
    
    def __init__(self, *args, **kwargs):
    	super(ArchivoForm, self).__init__(*args, **kwargs)
    	self.fields['nombre_archivo'].widget.attrs.update({'class' : 'form-control'}),
    	self.fields['descripcion'].widget.attrs.update({'class' : 'form-control'}),
    	self.fields['archivo'].widget.attrs.update({'class' : 'dropify' })
    