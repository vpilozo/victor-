from django.db import models

# Create your models here.
class maquina(models.Model):
    Titulo = models.CharField(max_length=100)
    Contenido = models.TextField()
    Imagen = models.ImageField(upload_to="projects")

    def __str__(self):
        return self.Titulo

class persona(models.Model):
    Titulo = models.CharField(max_length=100)
    Contenido = models.TextField()
    Imagen = models.ImageField(upload_to="projects")

    def __str__(self):
        return self.Titulo
