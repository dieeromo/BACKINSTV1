from rest_framework import serializers
from .models import SubCriterios


class subcriterios_Serializer(serializers.ModelSerializer):
    criterio = serializers.CharField(source='criterio.criterio', read_only=True)
    digitador = serializers.CharField(source='digitador.first_name', read_only=True)
    responsable = serializers.CharField(source='responsable.first_name', read_only=True)
    class Meta:
        model = SubCriterios
        fields = "__all__"

