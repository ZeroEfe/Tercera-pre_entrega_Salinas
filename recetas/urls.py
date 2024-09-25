from django.urls import path

from recetas import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('chefs', views.chef, name='Chefs'),
    path('recetas', views.receta, name='Recetas'),
    path('ingredientes', views.ingredientes, name='Ingredientes'),
    path('crearchef', views.crear_chef, name='CreaChef'),
    path('creareceta', views.crea_receta, name='CreaReceta'),
    path('busquedareceta', views.buscarqueda_receta, name='BusquedaReceta'),
    path('buscarreceta', views.buscar_receta, name='BuscarReceta'),

]
