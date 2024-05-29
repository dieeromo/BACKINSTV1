from django.db import models

from accounts.models import UserAccount
from general.models import DependenciasInstitucionales
from django.core.exceptions import ValidationError

def validate_pdf_size(value):
    if value.size > 5 * 1024 * 1024:
        raise ValidationError('El tamaño del archivo PDF no debe ser superior a 5 megabytes.')




class Pedi_version(models.Model):
    nombre = models.CharField(max_length=255)
    activo = models.BooleanField(default = True)
    fecha_aprobacion = models.DateField()
    fecha_finalizacion = models.DateField()
    fecha_actualizacion = models.DateField(null = True, blank=True)
    observacion = models.CharField(max_length=255, null=True, blank=True)
    archivo = models.FileField(upload_to='pedi/', validators=[validate_pdf_size], null=True, blank=True)
    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    def __str__(self):
        return "{} ".format(self.nombre)

    
class PoaDocumentos(models.Model):
    pedi = models.ForeignKey(Pedi_version, on_delete=models.CASCADE)
    anio = models.IntegerField()
    descripcion = models.TextField()
    archivo = models.FileField(upload_to='poa/documentos', validators=[validate_pdf_size], null=True, blank=True)
    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    


class Objetivo_estrategico(models.Model):
    nombre = models.TextField()
    sigla = models.CharField(max_length=50)
    activo = models.BooleanField(default = True)
    pedi = models.ForeignKey(Pedi_version, on_delete=models.CASCADE)
    observacion = models.TextField( null=True, blank=True)
    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    def __str__(self):
        return "{} ".format(self.nombre)



class Objetivo_especifico(models.Model):
    nombre = models.TextField()
    activo = models.BooleanField(default = True)
    objetivo_estrategico = models.ForeignKey(Objetivo_estrategico, on_delete=models.CASCADE)
    observacion = models.TextField( null=True, blank=True)
    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    def __str__(self):
        return "{} ".format(self.nombre)



class Meta_objetivo(models.Model):
    nombre = models.TextField()
    activo = models.BooleanField(default = True)
    objetivo_especifico = models.ForeignKey(Objetivo_especifico, on_delete=models.CASCADE)
    observacion = models.TextField( null=True, blank=True)
    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    def __str__(self):
        return "{} ".format(self.nombre)


class Actividad_meta(models.Model):
    nombre = models.TextField()
    activo = models.BooleanField(default = True)
    meta_objetivo = models.ForeignKey(Meta_objetivo, on_delete=models.CASCADE)
    observacion = models.TextField( null=True, blank=True)
    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    def __str__(self):
        return "{} ".format(self.nombre)



class Medio_verificacion(models.Model):
    nombre = models.TextField()
    activo = models.BooleanField(default = True)
    actividad_meta = models.ForeignKey(Actividad_meta, on_delete=models.CASCADE)
    observacion = models.TextField( null=True, blank=True)
    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    def __str__(self):
        return "{} ".format(self.nombre)


class IndicadorMedioVerificacion_Pedi(models.Model):
    nombre = models.TextField()
    total = models.IntegerField()
    anio1 = models.IntegerField()
    anio2 = models.IntegerField()
    anio3 = models.IntegerField()
    anio4 = models.IntegerField()
    anio5 = models.IntegerField()
    medio_verificacion = models.ForeignKey(Medio_verificacion, on_delete=models.CASCADE)
    entidadResponsable = models.ForeignKey(DependenciasInstitucionales, on_delete=models.CASCADE)
    activo = models.BooleanField(default = True)
    cumple = models.BooleanField(default = True)
    observacion = models.TextField( null=True, blank=True)
    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    numeroPoa = models.IntegerField(default= 1)
    def __str__(self):
        return "{} ".format(self.nombre)


class Poa(models.Model):
    indicadorPedi = models.ForeignKey(IndicadorMedioVerificacion_Pedi, on_delete=models.CASCADE)
    anio = models.IntegerField()
    totalAnio = models.IntegerField()
    pro1 = models.IntegerField()
    pro2 = models.IntegerField()
    pro3 = models.IntegerField()
    pro4 = models.IntegerField()
    pro5 = models.IntegerField()
    pro6 = models.IntegerField()
    pro7 = models.IntegerField()
    pro8 = models.IntegerField()
    pro9 = models.IntegerField()
    pro10 = models.IntegerField()
    pro11 = models.IntegerField()
    pro12 = models.IntegerField()

    eje1 = models.IntegerField(null=True, blank=True)
    eje2 = models.IntegerField(null=True, blank=True)
    eje3 = models.IntegerField(null=True, blank=True)
    eje4 = models.IntegerField(null=True, blank=True)
    eje5 = models.IntegerField(null=True, blank=True)
    eje6 = models.IntegerField(null=True, blank=True)
    eje7 = models.IntegerField(null=True, blank=True)
    eje8 = models.IntegerField(null=True, blank=True)
    eje9 = models.IntegerField(null=True, blank=True)
    eje10 = models.IntegerField(null=True, blank=True)
    eje11 = models.IntegerField(null=True, blank=True)
    eje12 = models.IntegerField(null=True, blank=True)

    activo = models.BooleanField(default = True)
    observacion = models.TextField( null=True, blank=True)
    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    NumeroSeguimiento = models.IntegerField(default= 1)


class JustificacionPoa(models.Model):
    poa = models.ForeignKey(Poa, on_delete=models.CASCADE)
    mes = models.IntegerField()
    justificacion = models.TextField()
    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='poa/justificaciones', validators=[validate_pdf_size], null=True, blank=True)


class VerificacionPoa(models.Model):
    poa = models.ForeignKey(Poa, on_delete=models.CASCADE)
    mes = models.IntegerField()
    descripcion = models.TextField()
    archivo = models.FileField(upload_to='poa/verificaciones', validators=[validate_pdf_size], null=True, blank=True)
    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    cumple = models.BooleanField(default = True)


