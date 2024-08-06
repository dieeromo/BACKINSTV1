from django.db import models

from accounts.models import UserAccount
from general.models import DependenciasInstitucionales
from django.core.exceptions import ValidationError

def validate_pdf_size(value):
    if value.size > 5 * 1024 * 1024:
        raise ValidationError('El tamaño del archivo PDF no debe ser superior a 5 megabytes.')



class ModeloEvaluacion(models.Model):
    nombre = models.CharField(max_length=255)
    activo = models.BooleanField(default = True)
    def __str__(self):
        return "{} ".format(self.nombre)
    
class CriterioEvaluacion(models.Model):
    modeloEvaluacion = models.ForeignKey(ModeloEvaluacion, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    numeral = models.CharField(max_length=20)
    def __str__(self):
        return "{} {} ".format(self.numeral,self.nombre)
    
class SubCriterioEvaluacion(models.Model):
    criterioEvaluacion = models.ForeignKey(CriterioEvaluacion, on_delete=models.CASCADE)
    nombre = models.TextField()
    numeral = models.CharField(max_length=20)
    def __str__(self):
        return "{} {}".format(self.numeral, self.nombre)
    
class TipoIndicador(models.Model):
    nombre = models.CharField(max_length=255)
    def __str__(self):
        return "{}".format(self.nombre)
    
class IndicadorEvaluacion(models.Model):
    subCriterioEvaluacion = models.ForeignKey(SubCriterioEvaluacion, on_delete=models.CASCADE)
    nombre = models.TextField()
    numeral = models.CharField(max_length=20)
    calificacion1 = models.IntegerField(null=True, blank= True)
    tipoIndicador = models.ForeignKey(TipoIndicador, on_delete=models.CASCADE, null=True, blank=True)
    responsable = models.ForeignKey(UserAccount, on_delete=models.CASCADE, null=True, blank=True)
    coresponsable1 = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='coresponsableIndicador1', null=True, blank=True)
    coresponsable2 = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='coresponsableIndicador2', null=True, blank=True)
    coresponsable3 = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='coresponsableIndicador3', null=True, blank=True)
    coresponsable4 = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='coresponsableIndicador4', null=True, blank=True)
    coresponsable5 = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='coresponsableIndicador5', null=True, blank=True)
    def __str__(self):
        return "{} {} ".format(self.numeral, self.nombre)
    
class EvidenciaEvaluacion(models.Model):
    indicadorEvaluacion = models.ForeignKey(IndicadorEvaluacion, on_delete=models.CASCADE, related_name='evidencias')
    nombre = models.TextField()
    numeral = models.CharField(max_length=20)
    calificacion1 = models.IntegerField(null=True, blank= True)
    def __str__(self):
        return "{} ".format(self.nombre)
    
    
class PeriodoAcademico(models.Model):
    nombre = models.TextField()
    def __str__(self):
        return "{} ".format(self.nombre)
    
    
class DocumentoEvaluacion(models.Model):
    evidenciaEvaluacion = models.ForeignKey(EvidenciaEvaluacion, on_delete=models.CASCADE, related_name='documentos')
    nombre = models.TextField()
    numeral = models.IntegerField()
    periodoAcademico = models.ForeignKey(PeriodoAcademico, on_delete=models.CASCADE, null=True, blank=True)
    
    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='digitadorDocEvaluacion')
    responsable = models.ForeignKey(UserAccount, on_delete=models.CASCADE, null=True, blank=True,  related_name='responsableDocEvaluacion')
    
    calificacion1 = models.IntegerField(null=True, blank= True)
    
   
    revisado = models.BooleanField(default = False)
    edicion = models.BooleanField(default = True)
    
    
    
    archivo = models.FileField(upload_to='evaluacionCaces/', validators=[validate_pdf_size], null=True, blank=True)
    link = models.TextField(null=True, blank=True)
    
    estado = models.IntegerField(choices=[(1, 'Por revisar'), (2, 'Aprobado'),(3, 'Corregir') ], default=0)
    observacion = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return "{} ".format(self.nombre)
    
    def save(self, *args, **kwargs):
        if not self.archivo and not self.link:
            self.estado = 0
        super(DocumentoEvaluacion, self).save(*args, **kwargs)
    
    

