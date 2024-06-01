from django.db import models

from accounts.models import UserAccount
from general.models import DependenciasInstitucionales
from django.core.exceptions import ValidationError

def validate_pdf_size(value):
    if value.size > 5 * 1024 * 1024:
        raise ValidationError('El tamaño del archivo PDF no debe ser superior a 5 megabytes.')





    

class ModalidadCarrera(models.Model):
    nombre = models.CharField(max_length=255)
    activo = models.BooleanField(default = True)
    observacion = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return "{} ".format(self.nombre)
    
class Carreras_instituto(models.Model):
    nombre = models.CharField(max_length=255)
    sigla = models.CharField(max_length=255)
    fecha_aprobacion = models.DateField()
    modalidad = models.ForeignKey(ModalidadCarrera, on_delete=models.CASCADE)
    archivo_malla = models.FileField(upload_to='pea/carrera/malla', validators=[validate_pdf_size], null=True, blank=True)
    archivo_microcurriculo = models.FileField(upload_to='pea/carrera/microcurriculo', validators=[validate_pdf_size], null=True, blank=True)
    dependencia_responsable = models.ForeignKey(DependenciasInstitucionales, on_delete=models.CASCADE)
    activo = models.BooleanField(default = True)
    observacion = models.CharField(max_length=255, null=True, blank=True)
    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    def __str__(self):
        return "{} ".format(self.nombre)
    

class TipoAsignatura(models.Model):
    nombre = models.CharField(max_length=255)
    observacion = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return "{} ".format(self.nombre)
    

class Asignaturas_carreras(models.Model):
    nombre = models.CharField(max_length=255)
    codigo = models.CharField(max_length=255)
    nivel = models.CharField(max_length=255)
    tipoAsignatura = models.ForeignKey(TipoAsignatura, on_delete=models.CASCADE)
    horasContactoDocente = models.IntegerField()
    horasPracticoExperimental = models.IntegerField()
    horasAprendizajeAutonomo = models.IntegerField()
    horasOtras = models.IntegerField(null=True, blank=True)

    carrera = models.ForeignKey(Carreras_instituto, on_delete=models.CASCADE)

    observacion = models.CharField(max_length=255, null=True, blank=True)
    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    def __str__(self):
        return "{} ".format(self.nombre)
    
    


class Semestre(models.Model):
    nombre = models.CharField(max_length=255)
    activo = models.BooleanField(default = True)
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField()
    observacion = models.CharField(max_length=255, null=True, blank=True)
    archivo_agenda = models.FileField(upload_to='semestres/', validators=[validate_pdf_size], null=True, blank=True)
    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    def __str__(self):
        return "{} ".format(self.nombre)
    
class Paralelo_Asignatura(models.Model):
    nombre = models.CharField(max_length=255)
    def __str__(self):
        return "{} ".format(self.nombre)
    

class Curso(models.Model):
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignaturas_carreras, on_delete=models.CASCADE)
    paralelo = models.ForeignKey(Paralelo_Asignatura, on_delete=models.CASCADE)
    docente = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    archivo_horario = models.FileField(upload_to='pea/curso/horario', validators=[validate_pdf_size], null=True, blank=True)
    archivo_pea = models.FileField(upload_to='pea/curso/pea', validators=[validate_pdf_size], null=True, blank=True)
    observacion = models.CharField(max_length=255, null=True, blank=True)
    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE)




