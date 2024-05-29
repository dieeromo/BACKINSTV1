from django.db import models
from accounts.models import UserAccount

from django.core.exceptions import ValidationError

def validate_pdf_size(value):
    if value.size > 5 * 1024 * 1024:
        raise ValidationError('El tamaño del archivo PDF no debe ser superior a 5 megabytes.')


# Create your models here.
class Coor_Carrera(models.Model):

    siglas = models.CharField(max_length=255)
    nombre = models.TextField()
    estadoVF = models.BooleanField(default = True)
    fecha_creacion = models.DateField()
    observacion = models.TextField(null=True, blank=True)
    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    def __str__(self):
        return "{} ".format(self.nombre)
   

class Coor_Institucionales(models.Model):
    siglas = models.CharField(max_length=255)
    nombre = models.TextField()
    estadoVF = models.BooleanField(default = True)
    fecha_creacion = models.DateField()
    observacion = models.TextField(null=True, blank=True)
    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    def __str__(self):
        return "{} ".format(self.nombre)
   

class Otras_Comisiones(models.Model):
    siglas = models.CharField(max_length=255)
    nombre = models.TextField()
    estadoVF = models.BooleanField(default = True)
    fecha_creacion = models.DateField()
    observacion = models.TextField(null=True, blank=True)
    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    def __str__(self):
        return "{} ".format(self.nombre)
   



class BolsaEmpleo(models.Model):
    institutcion = models.TextField()
    descripcion = models.TextField()
    fecha_limite = models.DateField(null=True, blank=True)
    url = models.CharField(max_length=500, null=True, blank=True)
    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    estadoVF = models.BooleanField(default = True)
    telefono = models.CharField(max_length=120,null=True, blank = True)
    email = models.CharField(max_length=120,null=True, blank = True)

##DEPENDENCIAS
class TipoDependencia(models.Model):
    nombre = models.TextField()
    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    activo = models.BooleanField(default = True)
    observacion = models.TextField(null=True, blank=True)
    def __str__(self):
        return "{} ** {}".format(self.nombre, self.activo)


class DependenciasInstitucionales(models.Model):
    nombre = models.TextField()
    siglas = models.CharField(max_length=50)
    tipo = models.ForeignKey(TipoDependencia, on_delete=models.CASCADE)
    activo = models.BooleanField(default = True)
    representante = models.ForeignKey(UserAccount, on_delete=models.CASCADE,related_name='representante')
    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='digitador')
    def __str__(self):
        return "{} * {} * {}".format(self.nombre, self.siglas,self.representante )

class OcurrenciaDependencias(models.Model):
    nombre = models.TextField()
    activo = models.BooleanField(default = True)
    def __str__(self):
        return "{} ** {}".format(self.nombre, self.activo)
    
class HistorialDependencias(models.Model):
     ocurrencia = models.ForeignKey(OcurrenciaDependencias, on_delete=models.CASCADE)
     descripcion = models.TextField()
     fecha = models.DateField()
     digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
     archivo = models.FileField(upload_to='dependencias/pdfs/', validators=[validate_pdf_size], null=True, blank=True)
     fecha = models.DateField(auto_now_add=True)
     edicion = models.BooleanField(default = True)
     def __str__(self):
        return "{} ** {}".format(self.ocurrencia, self.fecha)
     
     
    




