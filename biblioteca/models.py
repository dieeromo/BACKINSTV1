from django.db import models

from accounts.models import UserAccount
from django.core.exceptions import ValidationError

def validate_pdf_size(value):
    if value.size > 5 * 1024 * 1024:
        raise ValidationError('El tamaño del archivo PDF no debe ser superior a 5 megabytes.')


# Area de conocimientoi
class CategoriaObra(models.Model): 
    categoria = models.CharField(max_length=255)

#libro, revista, tesis
class TipoObra(models.Model):
    tipo = models.CharField(max_length=255)

# fisico o digital
class TipoMaterial(models.Model):
    material = models.CharField(max_length=255)

# alquilado/biblioteca o repopritorio
class EstadoObra(models.Model):
    estado = models.CharField(max_length=255)

class Obras(models.Model):
    codigo = models.CharField(max_length=255)
    titulo = models.CharField(max_length=800)
    editorial = models.CharField(max_length=255)
    autor = models.CharField(max_length=800)
    anio_publicacion = models.IntegerField()
    tomo = models.IntegerField(null=True)
    ubicacion = models.CharField(max_length=600)  # donde esta alojado

    categoria = models.ForeignKey(CategoriaObra, on_delete=models.CASCADE)
    tipo_obra = models.ForeignKey(TipoObra, on_delete=models.CASCADE)
    tipo_material = models.ForeignKey(TipoMaterial, on_delete=models.CASCADE)

    estado_obra = models.ForeignKey(EstadoObra, on_delete=models.CASCADE)
    
    estado_activo = models.BooleanField(default=True)

    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    observacion = models.TextField(null=True, blank=True)

    archivo = models.FileField(upload_to='pdfs_biblioteca/', validators=[validate_pdf_size],null=True, blank=True)

    
class Autores(models.Model):
    nombres = models.CharField(max_length=255)
    estado = models.IntegerField(null=True, blank=True)
    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    observacion = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{} - {}".format(self.nombres,  self.estado)



class ObrasAutores(models.Model):
    autor_id = models.ForeignKey(Autores, on_delete=models.CASCADE)
    obra_id = models.ForeignKey(Obras, on_delete=models.CASCADE)
    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    observacion = models.TextField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True,)
   

    def __str__(self):
        return "{} - {}".format(self.autor_id,  self.obra_id)

