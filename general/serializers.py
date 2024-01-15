from rest_framework import serializers
from .models import Coor_Carrera,Coor_Institucionales,Otras_Comisiones


class Coor_Carrera_Serializer(serializers.ModelSerializer):
    digitador = serializers.CharField(source='digitador.first_name', read_only=True)
    class Meta:
        model = Coor_Carrera
        fields = "__all__"

class Coor_Institucionales_Serializer(serializers.ModelSerializer):
    #digitador = serializers.CharField(source='digitador.first_name', read_only=True)
    class Meta:
        model = Coor_Institucionales
        fields = "__all__"

class Otras_comisiones_Serializer(serializers.ModelSerializer):
    digitador = serializers.CharField(source='digitador.first_name', read_only=True)
    class Meta:
        model = Otras_Comisiones
        fields = "__all__"

