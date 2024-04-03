from django.db import models
from accounts.models import UserAccount
from general.models import Coor_Carrera,Coor_Institucionales,Otras_Comisiones
from criterios.models import ProcesoEvaluacion, Criterios
from sub_criterios.models import SubCriterios
from indicadores.models import Indicadores
from evidencias.models import Evidencias

from django.core.exceptions import ValidationError
from django.core.exceptions import ValidationError

def validate_pdf_size(value):
    if value.size > 5 * 1024 * 1024:
        raise ValidationError('El tamaño del archivo PDF no debe ser superior a 5 megabytes.')


class Documentos_acreditacion(models.Model):
    criterio =  models.ForeignKey(Criterios, on_delete=models.CASCADE,)
    subCriterio =  models.ForeignKey(SubCriterios, on_delete=models.CASCADE,)
    indicador =  models.ForeignKey(Indicadores, on_delete=models.CASCADE,)
    evidencia = models.ForeignKey(Evidencias, on_delete=models.CASCADE,)
    numeracion = models.CharField(max_length=255)
    documento = models.TextField()
    
    estadoVF = models.BooleanField(default = True)
    fecha_creacion = models.DateField()
    observacion = models.TextField(null=True, blank=True)
    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='digitadorDocumentos')
    responsable = models.ForeignKey(UserAccount, on_delete=models.CASCADE, null=True, blank=True,  related_name='responsableDocumentos')
    procesoEvaluacion=models.ForeignKey(ProcesoEvaluacion, on_delete=models.CASCADE)
    iniciadoVF = models.BooleanField(default = False)
    cumpleVF = models.BooleanField(default = False)
    fecha_limite = models.DateField(blank= True, null =True)

    coor_carrera =  models.ForeignKey(Coor_Carrera, on_delete=models.CASCADE,null=True, blank=True)
    coor_institucionales =  models.ForeignKey(Coor_Institucionales, on_delete=models.CASCADE,null=True, blank=True)
    otras_comisiones =  models.ForeignKey(Otras_Comisiones, on_delete=models.CASCADE,null=True, blank=True)

    archivo = models.FileField(upload_to='pdfs/', validators=[validate_pdf_size], null=True, blank=True)

    
    def __str__(self):
        return "{} @ {} @ {} @ {} ".format(self.id,self.indicador,self.evidencia,self.documento)
   