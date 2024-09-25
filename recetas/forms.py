from django import forms
from .models import *

class Creachef(forms.Form):

    nombre=forms.CharField()
    apellido=forms.CharField()
    especialidad=forms.CharField()

class CreaReceta(forms.Form):

    titulo = forms.CharField()
    descripcion = forms.CharField()
    chef = forms.ModelChoiceField(queryset=Chef.objects.all())

class CreaIngrediente(forms.Form):

    nombre=forms.CharField()
    cantidad=forms.CharField()
