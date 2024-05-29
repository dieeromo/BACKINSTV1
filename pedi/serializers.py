from rest_framework import serializers
from .models import Pedi_version, Objetivo_estrategico, Objetivo_especifico, Meta_objetivo
from .models import Actividad_meta, Medio_verificacion, IndicadorMedioVerificacion_Pedi
from .models import Poa



class pediVersion_Serializer(serializers.ModelSerializer):
    value = serializers.CharField(source='id', read_only=True)
    label = serializers.CharField(source='nombre', read_only=True)
    class Meta:
        model = Pedi_version
        fields = "__all__"


class objeticoEstrategico_Serializer(serializers.ModelSerializer):
    pediNombre = serializers.CharField(source='pedi.nombre', read_only=True)
    value = serializers.CharField(source='id', read_only=True)
    label = serializers.CharField(source='nombre', read_only=True)
    class Meta:
        model = Objetivo_estrategico
        fields = "__all__"

class objeticoEspecifico_Serializer(serializers.ModelSerializer):
    value = serializers.CharField(source='id', read_only=True)
    label = serializers.CharField(source='nombre', read_only=True)
    class Meta:
        model = Objetivo_especifico
        fields = "__all__"


class metaObjeticoEspecifico_Serializer(serializers.ModelSerializer):
    #value = serializers.CharField(source='id', read_only=True)
    #label = serializers.CharField(source='nombre', read_only=True)
    class Meta:
        model = Meta_objetivo
        fields = "__all__"

class actividadMeta_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad_meta
        fields = "__all__"

class medio_verificacion_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Medio_verificacion
        fields = "__all__"

class indicador_medioPedi_Serializer(serializers.ModelSerializer):
    entidad = serializers.CharField(source='entidadResponsable.siglas', read_only=True)
    representante_id = serializers.CharField(source='entidadResponsable.representante.id', read_only=True)
    class Meta:
        model = IndicadorMedioVerificacion_Pedi
        fields = "__all__"

class poa_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Poa
        fields = "__all__"