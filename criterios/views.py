from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required

from .models import Criterios, ProcesoEvaluacion
from .serializers import criterios_Serializer, procesosEvaluacion_Serializer


@api_view(['GET'])
#@permission_classes([IsAuthenticated])
#@login_required()
def listCriterios(request):
    criterios = Criterios.objects.filter().order_by('id') 
    serializer = criterios_Serializer(criterios, many=True)
    return Response(serializer.data)

@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def listProcesosEvaluacion(request):
    procesos = ProcesoEvaluacion.objects.filter().order_by('-id') 
    serializer = procesosEvaluacion_Serializer(procesos, many=True)
    return Response(serializer.data)