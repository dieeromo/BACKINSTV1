from django.db import models
from accounts.models import UserAccount
from criterios.models import ProcesoEvaluacion, Criterios
from sub_criterios.models import SubCriterios
from indicadores.models import Indicadores

# Create your models here.
class Evidencias(models.Model):
    criterio =  models.ForeignKey(Criterios, on_delete=models.CASCADE,)
    subCriterio =  models.ForeignKey(SubCriterios, on_delete=models.CASCADE,)
    indicador =  models.ForeignKey(Indicadores, on_delete=models.CASCADE,)
    numeracion = models.CharField(max_length=255)
    evidencia = models.TextField()
    estadoVF = models.BooleanField(default = True)
    fecha_creacion = models.DateField()
    observacion = models.TextField(null=True, blank=True)
    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='digitadorEvidencia')
    responsable = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='responsableEvidencia')
    procesoEvaluacion=models.ForeignKey(ProcesoEvaluacion, on_delete=models.CASCADE)

    cumpleVF = models.BooleanField(default = False)
    fecha_limite = models.DateField(blank= True, null =True)

    def __str__(self):
        return "{} - {} -- {}".format(self.numeracion,  self.evidencia,self.estadoVF)
   

