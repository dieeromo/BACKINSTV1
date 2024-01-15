from rest_framework import serializers
from .models import Criterios, ProcesoEvaluacion


class criterios_Serializer(serializers.ModelSerializer):
    digitador = serializers.CharField(source='digitador.first_name', read_only=True)
    responsable = serializers.CharField(source='responsable.first_name', read_only=True)
    class Meta:
        model = Criterios
        fields = "__all__"



class procesosEvaluacion_Serializer(serializers.ModelSerializer):

    class Meta:
        model = ProcesoEvaluacion
        fields = "__all__"
