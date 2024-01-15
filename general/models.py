from django.db import models
from accounts.models import UserAccount


# Create your models here.
class Coor_Carrera(models.Model):

    siglas = models.CharField(max_length=255)
    nombre = models.TextField()
    estadoVF = models.BooleanField(default = True)
    fecha_creacion = models.DateField()
    observacion = models.TextField(null=True, blank=True)
    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    #def __str__(self):
    #    return "{} ".format(self.nombre)
   

class Coor_Institucionales(models.Model):
    siglas = models.CharField(max_length=255)
    nombre = models.TextField()
    estadoVF = models.BooleanField(default = True)
    fecha_creacion = models.DateField()
    observacion = models.TextField(null=True, blank=True)
    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    #def __str__(self):
    #    return "{} ".format(self.nombre)
   

class Otras_Comisiones(models.Model):
    siglas = models.CharField(max_length=255)
    nombre = models.TextField()
    estadoVF = models.BooleanField(default = True)
    fecha_creacion = models.DateField()
    observacion = models.TextField(null=True, blank=True)
    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    #def __str__(self):
    #    return "{} ".format(self.nombre)
   

