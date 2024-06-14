
from rest_framework import serializers
from .models import ModalidadCarrera, Carreras_instituto, TipoAsignatura
from .models import Asignaturas_carreras, Semestre, Paralelo_Asignatura, Curso


class modalidadCarrera_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ModalidadCarrera
        fields = "__all__"


class carrerasInstituto_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Carreras_instituto
        fields = "__all__"

class tipoAsignatura_Serializer(serializers.ModelSerializer):
    class Meta:
        model = TipoAsignatura
        fields = "__all__"

class asignaturaCarreras_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Asignaturas_carreras
        fields = "__all__"

class semestre_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Semestre
        fields = "__all__"

class paraleloAsignatura_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Paralelo_Asignatura
        fields = "__all__"


class curso_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = "__all__"
