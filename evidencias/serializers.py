
from rest_framework import serializers
from .models import Evidencias


class evidencias_Serializer(serializers.ModelSerializer):
    digitador = serializers.CharField(source='digitador.first_name', read_only=True)
    responsable = serializers.CharField(source='responsable.first_name', read_only=True)
    criterio = serializers.CharField(source='criterio.criterio', read_only=True)
    subCriterio = serializers.CharField(source='subCriterio.subCriterio', read_only=True)
    indicador = serializers.CharField(source='indicador.indicador', read_only=True)
    class Meta:
        model = Evidencias
        fields = "__all__"

