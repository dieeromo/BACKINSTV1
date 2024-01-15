
# Create your models here.
from django.db import models
from django.core.exceptions import ValidationError
from django.core.exceptions import ValidationError

def validate_pdf_size(value):
    if value.size > 5 * 1024 * 1024:
        raise ValidationError('El tamaño del archivo PDF no debe ser superior a 5 megabytes.')


class ArchivoPDF(models.Model):
    nombre = models.CharField(max_length=255)
    archivo = models.FileField(upload_to='pdfs/', validators=[validate_pdf_size])



