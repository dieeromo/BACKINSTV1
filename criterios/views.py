from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required

from .models import Criterios, ProcesoEvaluacion
from .serializers import criterios_Serializer, procesosEvaluacion_Serializer

from accounts.models import UserAccount


@api_view(['GET'])
#@permission_classes([IsAuthenticated])
@login_required()
def listCriterios(request):
    criterios = Criterios.objects.filter().order_by('id') 
    serializer = criterios_Serializer(criterios, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@login_required()
def postCriterio(request):
    dig = UserAccount.objects.get(id=2)
    proce = ProcesoEvaluacion.objects.get(id=1)
    data = request.data
    try:
        nuevo_criterio = Criterios.objects.create(
            numeracion = '0001',
            criterio = data['criterio'],
            estadoVF = False,
            fecha_creacion = data['fecha_creacion'],
            observacion = 'observacion',
            digitador = dig,
            responsable = dig,
            procesoEvaluacion = proce,
        )
        serializer = criterios_Serializer(nuevo_criterio, many=False)
        return Response(serializer.data)
    except:
        message = {'faaala'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def putCriterio(request):
    data = request.data 
    try: 
        criterio = Criterios.objects.get(id=data['id'])

    except Criterios.DoesNotExist:
        return Response({'error': 'El criterio no existe.'}, status=status.HTTP_404_NOT_FOUND)

    try:
        Criterios.objects.filter(id=data['id']).update(
            criterio = data['criterio'],
            fecha_creacion = data['fecha_creacion']
        )
        #criterio_actualizado = Criterios.objects.get(id=data['id'])
        return Response(status=status.HTTP_200_OK)
    except:
        message = {'faaala'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteCriterio(request):
    data = request.data 
    try: 
        criterio = Criterios.objects.get(id=data['id'])
        criterio.delete()
        return Response ({'mensaje':'El Criterio se elimino'})
    except Criterios.DoesNotExist:
        return Response({'error':'EL criterio no existe'})
    except Exception as e:
        return Response ({'error':str(e)}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def listProcesosEvaluacion(request):
    procesos = ProcesoEvaluacion.objects.filter().order_by('-id') 
    serializer = procesosEvaluacion_Serializer(procesos, many=True)
    return Response(serializer.data)