from django.db import models
from accounts.models import UserAccount
from criterios.models import Criterios, ProcesoEvaluacion

class SubCriterios(models.Model):
    criterio =  models.ForeignKey(Criterios, on_delete=models.CASCADE,)
    numeracion = models.CharField(max_length=255)
    subCriterio = models.TextField()
    estadoVF = models.BooleanField(default = True)
    fecha_creacion = models.DateField()
    observacion = models.TextField(null=True, blank=True)
    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='digitadorSubcriterio')
    responsable = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='responsableSubcriterio')
    procesoEvaluacion=models.ForeignKey(ProcesoEvaluacion, on_delete=models.CASCADE)
    def __str__(self):
        return "{} - {} -- {}".format(self.numeracion,  self.subCriterio,self.estadoVF)

