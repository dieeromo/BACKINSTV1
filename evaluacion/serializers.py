from rest_framework import serializers
from .models import CriterioEvaluacion, DocumentoEvaluacion, PeriodoAcademico

class criteriosEvaluacion_Serializer(serializers.ModelSerializer):
    #value = serializers.CharField(source='id', read_only=True)
    #label = serializers.CharField(source='nombre', read_only=True)
    class Meta:
        model = CriterioEvaluacion
        fields = "__all__"
        
        
class documentosEvaluacion_Serializer(serializers.ModelSerializer):
    #value = serializers.CharField(source='id', read_only=True)
    #label = serializers.CharField(source='nombre', read_only=True)
    class Meta:
        model = DocumentoEvaluacion
        fields = "__all__"
        
        
class periodoAcademico_Serializer(serializers.ModelSerializer):
    value = serializers.CharField(source='id', read_only=True)
    label = serializers.CharField(source='nombre', read_only=True)
    class Meta:
        model = PeriodoAcademico
        fields = "__all__"