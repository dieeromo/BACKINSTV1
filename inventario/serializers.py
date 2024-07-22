from rest_framework import serializers
from .models import TipoInventario,EstadoInventario,UbicacionInventario,InventarioIST


class tipoInventario_Serializer(serializers.ModelSerializer):
    value = serializers.CharField(source='id', read_only=True)
    label = serializers.CharField(source='tipo', read_only=True)
    class Meta:
        model = TipoInventario
        fields = "__all__"


class estadoInventario_Serializer(serializers.ModelSerializer):
    value = serializers.CharField(source='id', read_only=True)
    label = serializers.CharField(source='estado', read_only=True)
    class Meta:
        model = EstadoInventario
        fields = "__all__"



class ubicacionInventario_Serializer(serializers.ModelSerializer):
    value = serializers.CharField(source='id', read_only=True)
    label = serializers.CharField(source='ubicacion', read_only=True)
    class Meta:
        model = UbicacionInventario
        fields = "__all__"


class inventarioIST_Serializer(serializers.ModelSerializer):
    # tipo = serializers.CharField(source='tipo.tipo', read_only=True)
    # estado = serializers.CharField(source='estado.estado', read_only=True)
    ubicacion_name = serializers.CharField(source='ubicacion.ubicacion', read_only=True)
    asignado_name = serializers.CharField(source='asignado.get_full_name', read_only=True)
    digitador_name = serializers.CharField(source='digitador.get_full_name', read_only=True)
    estado_name = serializers.CharField(source='estado.estado', read_only=True)
    tipo_name = serializers.CharField(source='tipo.tipo', read_only=True)

    class Meta:
        model = InventarioIST
        fields = "__all__"


