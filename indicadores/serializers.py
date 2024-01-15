from rest_framework import serializers
from .models import Indicadores


class indicadores_Serializer(serializers.ModelSerializer):
    criterio = serializers.CharField(source='criterio.criterio', read_only=True)
    subCriterio = serializers.CharField(source='subCriterio.subCriterio', read_only=True)
    digitador = serializers.CharField(source='digitador.first_name', read_only=True)
    responsable = serializers.CharField(source='responsable.first_name', read_only=True)
    
    class Meta:
        model = Indicadores
        fields = "__all__"

