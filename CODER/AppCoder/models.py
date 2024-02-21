from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    camada = models.IntegerField()

    def __str__(self):
        return self.nombre+" "+ str(self.camada)

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.nombre+" "+ self.apellido

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

    def __str__(self):
        return "NOMBRE: "+self.nombre+" "+"APELLIDO: "+ self.apellido+" "+"PROFESION: "+ self.profesion


class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()

def __str__(self):
        return self.nombre+" "+ str(self.fechaDeEntrega)


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)