from rest_framework import serializers
from .models import Coor_Carrera,Coor_Institucionales,Otras_Comisiones
from .models import BolsaEmpleo


class Coor_Carrera_Serializer(serializers.ModelSerializer):
    digitador = serializers.CharField(source='digitador.first_name', read_only=True)
    value = serializers.CharField(source='id', read_only=True)
    label = serializers.CharField(source='nombre', read_only=True)
    class Meta:
        model = Coor_Carrera
        fields = "__all__"

class Coor_Institucionales_Serializer(serializers.ModelSerializer):
    #digitador = serializers.CharField(source='digitador.first_name', read_only=True)
    value = serializers.CharField(source='id', read_only=True)
    label = serializers.CharField(source='nombre', read_only=True)
    class Meta:
        model = Coor_Institucionales
        fields = "__all__"

class Otras_comisiones_Serializer(serializers.ModelSerializer):
    digitador = serializers.CharField(source='digitador.first_name', read_only=True)
    value = serializers.CharField(source='id', read_only=True)
    label = serializers.CharField(source='nombre', read_only=True)
    class Meta:
        model = Otras_Comisiones
        fields = "__all__"


class Bolsa_empleo_Serializer(serializers.ModelSerializer):
    digitador_name = serializers.CharField(source='digitador.first_name', read_only=True)
    class Meta:
        model = BolsaEmpleo
        fields = "__all__"
