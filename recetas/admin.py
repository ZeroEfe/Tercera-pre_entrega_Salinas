from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Chef)
admin.site.register(Ingrediente)
admin.site.register(Receta)

