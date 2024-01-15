from django.db import models
from accounts.models import UserAccount

class ProcesoEvaluacion(models.Model):
    proceso = models.TextField()
    comentario = models.TextField(null=True, blank=True)
    estadoVF = models.BooleanField(default = True)
    fecha_creacion = models.DateField()
    

class Criterios(models.Model):
    numeracion = models.CharField(max_length=255)
    criterio = models.TextField()
    estadoVF = models.BooleanField(default = True)
    fecha_creacion = models.DateField()
    observacion = models.TextField(null=True, blank=True)
    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='digitadorCriterio')
    responsable = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='responsableResponsable')
    procesoEvaluacion=models.ForeignKey(ProcesoEvaluacion, on_delete=models.CASCADE)
    def __str__(self):
        return "{} - {} -- {}".format(self.numeracion,  self.criterio,self.estadoVF)



# Create your models here.
