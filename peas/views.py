
from rest_framework import serializers, routers, viewsets, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required


from .models import ModalidadCarrera, Carreras_instituto, TipoAsignatura
from .models import Asignaturas_carreras, Semestre, Paralelo_Asignatura, Curso

from .serializers import modalidadCarrera_Serializer, carrerasInstituto_Serializer
from .serializers import tipoAsignatura_Serializer, asignaturaCarreras_Serializer
from .serializers import semestre_Serializer, paraleloAsignatura_Serializer, curso_Serializer




class ModalidadCarrera_ViewSet(viewsets.ModelViewSet):
    queryset = ModalidadCarrera.objects.all().order_by('-id')
    serializer_class = modalidadCarrera_Serializer
router = routers.DefaultRouter()


class CarreraInstituto_ViewSet(viewsets.ModelViewSet):
    queryset = Carreras_instituto.objects.all().order_by('-id')
    serializer_class = carrerasInstituto_Serializer
router = routers.DefaultRouter()

class TipoAsignatura_ViewSet(viewsets.ModelViewSet):
    queryset = TipoAsignatura.objects.all().order_by('-id')
    serializer_class = tipoAsignatura_Serializer
router = routers.DefaultRouter()

class AsignaturasCarreras_ViewSet(viewsets.ModelViewSet):
    queryset = Asignaturas_carreras.objects.all().order_by('-id')
    serializer_class = asignaturaCarreras_Serializer
router = routers.DefaultRouter()


class Semestre_ViewSet(viewsets.ModelViewSet):
    queryset = Semestre.objects.all().order_by('-id')
    serializer_class = semestre_Serializer
router = routers.DefaultRouter()



class ParaleloAsignatura_ViewSet(viewsets.ModelViewSet):
    queryset = Paralelo_Asignatura.objects.all().order_by('-id')
    serializer_class = paraleloAsignatura_Serializer
router = routers.DefaultRouter()


class Curso_ViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all().order_by('-id')
    serializer_class = curso_Serializer
router = routers.DefaultRouter()


