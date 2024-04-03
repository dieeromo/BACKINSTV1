from rest_framework import serializers
from .models import Documentos_acreditacion
#from accounts.serializers import UserCreateSerializer


class documentos_acreditacion_Serializer(serializers.ModelSerializer):
    digitador = serializers.CharField(source='digitador.first_name', read_only=True)
    digitador_id = serializers.CharField(source='digitador.id', read_only=True)
    responsable = serializers.CharField(source='responsable.get_full_name', read_only=True)
    responsable_id = serializers.CharField(source='responsable.id', read_only=True)
    evidencia_id = serializers.CharField(source='evidencia.id', read_only=True)
    indicador_id = serializers.CharField(source='indicador.id', read_only=True)
    # este es un comentario de prueba
    #responsablef = serializers.CharField(source='responsable.last_name', read_only=True)
    
    criterio = serializers.CharField(source='criterio.criterio', read_only=True)
    subCriterio = serializers.CharField(source='subCriterio.subCriterio', read_only=True)
    indicador = serializers.CharField(source='indicador.indicador', read_only=True)
    indicador_key = serializers.CharField(source='indicador.numeracion', read_only=True)
    evidencia = serializers.CharField(source='evidencia.evidencia', read_only=True)
    evidencia_key = serializers.CharField(source='evidencia.numeracion', read_only=True)
    coor_carrera = serializers.CharField(source='coor_carrera.nombre', read_only=True)
    coor_institucionales = serializers.CharField(source='coor_institucionales.nombre', read_only=True)
    otras_comisiones = serializers.CharField(source='otras_comisiones.nombre', read_only=True)
    class Meta:
        model = Documentos_acreditacion
        fields = "__all__"
