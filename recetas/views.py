from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.forms import formset_factory
from .models import *
from .forms import *



# Create your views here.

def inicio(req):

    return render(req, "inicio.html", {})

def receta(req):

        return render(req, "receta.html", {})

def chef(req):

        return render(req, "chef.html", {})

def ingredientes(req):

        return render(req, "ingredientes.html", {})

# Crear Chef 

def crear_chef(req):

    if req.method == 'POST':

        creachef = Creachef(req.POST)

        if creachef.is_valid():

            data = creachef.cleaned_data

            nuevo_chef = Chef(
                nombre=data["nombre"], 
                apellido=data["apellido"], 
                especialidad=data["especialidad"]
            )
            nuevo_chef.save()

            return render(req, "inicio.html", {})
        else:

            return render(req, "crear_chef.html", {"creachef": creachef})
    else:

        creachef = Creachef()
        return render(req, "crear_chef.html", {"creachef": creachef})
    
# Crear Receta

Ingrediente_FormSet = formset_factory(CreaIngrediente, extra=1)

def crea_receta(req):

    if req.method == 'POST':

        creareceta = CreaReceta(req.POST)

        ingrediente_formset = Ingrediente_FormSet(req.POST)

        if creareceta.is_valid() and ingrediente_formset.is_valid():
            
            data = creareceta.cleaned_data

            nueva_receta = Receta(titulo=data["titulo"], descripcion=data["descripcion"], chef=data["chef"])

            nueva_receta.save()

            for form in ingrediente_formset:
               
                if form.cleaned_data.get('nombre') and form.cleaned_data.get('cantidad'):

                    nuevo_ingrediente = Ingrediente(
                         
                        nombre=form.cleaned_data['nombre'],

                        cantidad=form.cleaned_data['cantidad'],

                        receta=nueva_receta 

                    )

                    nuevo_ingrediente.save()

            return render(req, "inicio.html", {})
        
        else:

            return render(req, 'crea_receta.html', {'creareceta': creareceta, 'ingrediente_formset': ingrediente_formset})
    
    else:

        creareceta = CreaReceta()
        ingrediente_formset = Ingrediente_FormSet()
        return render(req, 'crea_receta.html', {'creareceta': creareceta, 'ingrediente_formset': ingrediente_formset})
    
# Busqueda de receta

    
def buscarqueda_receta(req):

    return render(req, 'busqueda_receta.html')


def buscar_receta(req):

    if 'titulo' in req.GET:

        nom_receta = req.GET["titulo"]
        
        recetas = Receta.objects.filter(
            titulo__icontains=nom_receta
        )

        Receta.objects.filter(
            descripcion__icontains=nom_receta
        )
        
        return render(req, "resultado_busqueda.html", {"recetas": recetas, "titulo_busqueda": nom_receta})
    
    return render(req, "resultado_busqueda.html", {"recetas": [], "titulo_busqueda": ""})










# def buscar_receta(req):
     
#      nom_receta = req.GET["titulo"]

#      receta = Receta.objects.filter(titulo_icontains=nom_receta)

#      return render(req, "resultado_busqueda.html", {"titulo": receta, "descripcion": nom_receta})