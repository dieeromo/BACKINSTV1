from rest_framework import serializers
from .models import CategoriaObra, TipoObra, TipoMaterial, EstadoObra, Obras 


class categoriaObra_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaObra
        fields = "__all__"

class tipoObra_Serializer(serializers.ModelSerializer):
    class Meta:
        model = TipoObra
        fields = "__all__"

class tipoMaterial_Serializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMaterial
        fields = "__all__"

class estadoObra_Serializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoObra
        fields = "__all__"


class obras_Serializer(serializers.ModelSerializer):
    categoria = serializers.CharField(source='categoria.categoria', read_only=True)
    tipo_obra = serializers.CharField(source='tipo_obra.tipo', read_only=True)
    tipo_material = serializers.CharField(source='tipo_material.material', read_only=True)
    estado_obra = serializers.CharField(source='estado_obra.estado', read_only=True)

    digitador = serializers.CharField(source='digitador.get_full_name', read_only=True)
  
    class Meta:
        model = Obras
        fields = "__all__"


