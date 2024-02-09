from rest_framework import serializers
from .models import TipoInventario,EstadoInventario,UbicacionInventario,InventarioIST


class tipoInventario_Serializer(serializers.ModelSerializer):
    class Meta:
        model = TipoInventario
        fields = "__all__"


class estadoInventario_Serializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoInventario
        fields = "__all__"



class ubicacionInventario_Serializer(serializers.ModelSerializer):
    class Meta:
        model = UbicacionInventario
        fields = "__all__"


class inventarioIST_Serializer(serializers.ModelSerializer):
    tipo = serializers.CharField(source='tipo.tipo', read_only=True)
    estado = serializers.CharField(source='estado.estado', read_only=True)
    ubicacion = serializers.CharField(source='ubicacion.ubicacion', read_only=True)
    asignado = serializers.CharField(source='asignado.get_full_name', read_only=True)

    class Meta:
        model = InventarioIST
        fields = "__all__"


