from rest_framework import serializers
from .models import CategoriaObra, TipoObra, TipoMaterial, EstadoObra, Obras
from .models import  Autores, ObrasAutores


class categoriaObra_Serializer(serializers.ModelSerializer):
    value = serializers.CharField(source='id', read_only=True)
    label = serializers.CharField(source='categoria', read_only=True)
    class Meta:
        model = CategoriaObra
        fields = "__all__"

class tipoObra_Serializer(serializers.ModelSerializer):
    value = serializers.CharField(source='id', read_only=True)
    label = serializers.CharField(source='tipo', read_only=True)
    class Meta:
        model = TipoObra
        fields = "__all__"

class tipoMaterial_Serializer(serializers.ModelSerializer):
    value = serializers.CharField(source='id', read_only=True)
    label = serializers.CharField(source='material', read_only=True)
    class Meta:
        model = TipoMaterial
        fields = "__all__"

class estadoObra_Serializer(serializers.ModelSerializer):
    value = serializers.CharField(source='id', read_only=True)
    label = serializers.CharField(source='estado', read_only=True)
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



class autores_Serializer(serializers.ModelSerializer):
    value = serializers.CharField(source='id', read_only=True)
    label = serializers.CharField(source='nombres', read_only=True)
    class Meta:
        model = Autores
        fields = "__all__"


class obrasAutores_Serializer(serializers.ModelSerializer):
    autor = serializers.CharField(source='autor_id.nombres', read_only=True)
    obra = serializers.CharField(source='obra_id.titulo', read_only=True)
    id_obra = serializers.CharField(source='obra_id.id', read_only=True)
    archivo = serializers.CharField(source='obra_id.archivo', read_only=True)
    anio_publicacion = serializers.CharField(source='obra_id.anio_publicacion', read_only=True)
    tipo_obra = serializers.CharField(source='obra_id.tipo_obra.tipo', read_only=True)
    tipo_material = serializers.CharField(source='obra_id.tipo_material.material', read_only=True)
    digitador_name = serializers.CharField(source='digitador.first_name', read_only=True)
   
  
    #digitador  = serializers.SerializerMethodField()


    class Meta:
        model = ObrasAutores
        fields = "__all__"


