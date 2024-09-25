from django.db import models

class Chef(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Receta(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    
class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.CharField(max_length=50)
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE, related_name='ingredientes')

    def __str__(self):
        return f"{self.cantidad} de {self.nombre}"