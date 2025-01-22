from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import DependenciasInstitucionales, HistorialDependenciasInstitucionales

@receiver(post_save, sender=DependenciasInstitucionales)
def crear_historial_dependencias(sender, instance, created, **kwargs):
    """
    Crea una entrada en HistorialDependenciasInstitucionales cada vez que se
    crea o actualiza una entrada en DependenciasInstitucionales.
    """
    HistorialDependenciasInstitucionales.objects.create(
        dependencia=instance,
        nombre=instance.nombre,
        siglas=instance.siglas,
        tipo=instance.tipo,
        activo=instance.activo,
        representante=instance.representante,
        digitador=instance.digitador,
        fecha=instance.fecha
    )
