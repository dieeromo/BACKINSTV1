from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from .models import Documentos_acreditacion
from .serializers import documentos_acreditacion_Serializer

from evidencias.models import Evidencias
from indicadores.models import Indicadores
from sub_criterios.models import SubCriterios
from criterios.models import Criterios, ProcesoEvaluacion
from general.models import Coor_Carrera, Coor_Institucionales, Otras_Comisiones
from accounts.models import UserAccount


@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def registroDocumentosAcreditacion(request,id_evidencia, id_responsable):
    print(id_evidencia)
    evidencia = Evidencias.objects.get(id=id_evidencia)
    criterio = Criterios.objects.get(id=evidencia.criterio.id)
    subcriterio = SubCriterios.objects.get(id=evidencia.subCriterio.id)
    indicador = Indicadores.objects.get(id=evidencia.indicador.id)
    proceso = ProcesoEvaluacion.objects.get(id= evidencia.procesoEvaluacion.id)

    carrera = Coor_Carrera.objects.get(id=1)
    coor_ist = Coor_Institucionales.objects.get(id=1)
    otras = Otras_Comisiones.objects.get(id=1)

    fecha_actual = datetime.now().date()
    responsable = UserAccount.objects.get(id=id_responsable)
    data = request.data
    try:
        documento = Documentos_acreditacion.objects.create(
            criterio = criterio,
            subCriterio = subcriterio,
            indicador = indicador,
            evidencia = evidencia,
            numeracion = data['numeracion'],
            documento = data['documento'],

            estadoVF = True,
            fecha_creacion = fecha_actual,
            observacion = data['observacion'],
            digitador = responsable,
            responsable = responsable,
            procesoEvaluacion = proceso,
            iniciadoVF = False,
            cumpleVF = False,
            fecha_limite= data['fecha_limite'],

            #coor_carrera = ,
            coor_institucionales = coor_ist,
            otras_comisiones = otras,
            archivo = request.FILES.get('archivo')



        )

        serializer = documentos_acreditacion_Serializer(documento, many=False)

        return Response(serializer.data)
    except:
        message = {'detalle': 'algo esta mal en el registro del cliente'}

        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def listDocumentosAcreditacionFilter(request,id):

    docs_acred = Documentos_acreditacion.objects.filter(evidencia=id).order_by('id') 
    serializer = documentos_acreditacion_Serializer(docs_acred, many=True)

    return Response(serializer.data)







@api_view(['PUT'])
#@permission_classes([IsAuthenticated])
def uploadArchivoDocumento(request):
    data = request.data
    archivo_id = data['id']
    arc = Documentos_acreditacion.objects.get(id=archivo_id)
    arc.archivo = request.FILES.get('archivo')
    arc.save()

    return Response('pdf subido')




@api_view(['GET'])
def listDocumentosAcreditacionAll(request):

    docs_acred = Documentos_acreditacion.objects.filter().order_by('criterio','subCriterio','indicador') 
    serializer = documentos_acreditacion_Serializer(docs_acred, many=True)

    return Response(serializer.data)