from django.db import models
from accounts.models import UserAccount
from criterios.models import ProcesoEvaluacion, Criterios
from sub_criterios.models import SubCriterios

# Create your models here.
class Indicadores(models.Model):
    criterio =  models.ForeignKey(Criterios, on_delete=models.CASCADE,)
    subCriterio =  models.ForeignKey(SubCriterios, on_delete=models.CASCADE,)
    numeracion = models.CharField(max_length=255)
    indicador = models.TextField()
    estadoVF = models.BooleanField(default = True)
    fecha_creacion = models.DateField()
    observacion = models.TextField(null=True, blank=True)
    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='digitadorIndicador')
    responsable = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='responsableIndicador')
    procesoEvaluacion=models.ForeignKey(ProcesoEvaluacion, on_delete=models.CASCADE)
    def __str__(self):
        return "{} - {} -- {}".format(self.numeracion,  self.indicador,self.estadoVF)
   

