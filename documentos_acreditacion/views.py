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

from django.contrib.auth.decorators import login_required


@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def registroDocumentosAcreditacion(request,id_evidencia, id_responsable):
    data = request.data
    evidencia = Evidencias.objects.get(id=id_evidencia)
    criterio = Criterios.objects.get(id=evidencia.criterio.id)
    subcriterio = SubCriterios.objects.get(id=evidencia.subCriterio.id)
    indicador = Indicadores.objects.get(id=evidencia.indicador.id)
    proceso = ProcesoEvaluacion.objects.get(id= evidencia.procesoEvaluacion.id)
    if data['carrera'] :
        carrera = Coor_Carrera.objects.get(id=data['carrera'])       
    else:
        carrera = Coor_Carrera.objects.get(nombre='NA')
        

    if data['coor_institucionales'] :
        coor_ist = Coor_Institucionales.objects.get(id=data['coor_institucionales'])
    else:
        coor_ist = Coor_Institucionales.objects.get(nombre='NA')

    if data['otras_comisiones'] :
        print("******** SI SELEC")
        otras = Otras_Comisiones.objects.get(id=data['otras_comisiones'])
    else:
        print("******** NO SELEC")
        otras = Otras_Comisiones.objects.get(nombre='NA')
        
   
    

    fecha_actual = datetime.now().date()
    responsable = UserAccount.objects.get(id=id_responsable)
    digitador = UserAccount.objects.get(id=data['digitador'])
   
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
            #digitador = responsable,
            digitador = digitador,
            responsable = responsable,
            procesoEvaluacion = proceso,
            iniciadoVF = False,
            cumpleVF = False,
            fecha_limite= data['fecha_limite'],
    
            coor_carrera = carrera,
            coor_institucionales = coor_ist,
            otras_comisiones = otras,
            archivo = request.FILES.get('archivo')
        )

        serializer = documentos_acreditacion_Serializer(documento, many=False)

        return Response(serializer.data)
    except:
        message = {'detalle': 'algo esta mal en el registro del cliente'}

        return Response(message, status=status.HTTP_400_BAD_REQUEST)

#FILTRO POR EVIDENCIA
@api_view(['GET'])
@login_required()
def listDocumentosAcreditacionFilter(request,id):
    docs_acred = Documentos_acreditacion.objects.filter(evidencia=id).order_by('id') 
    serializer = documentos_acreditacion_Serializer(docs_acred, many=True)
    #print(serializer.data)
    return Response(serializer.data)


#FILTRO POR DOCENTE
@api_view(['GET'])
@login_required()
def listDocumentosAcreditacionFilterDocente(request,id):
    print(id)
    docs_acred = Documentos_acreditacion.objects.filter(responsable=id).order_by('id') 
    serializer = documentos_acreditacion_Serializer(docs_acred, many=True)
    print(serializer.data)
    return Response(serializer.data)








@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def uploadArchivoDocumento(request):
    print('petionnnn')
    print(request)
    data = request.data
    archivo_id = data['id']
    print('iddddddß')
    print(archivo_id)
    try:
        arc = Documentos_acreditacion.objects.get(id=archivo_id)
    except Documentos_acreditacion.DoesNotExist:
        return Response({'error':'El documento no existe'})
    
    try:
        arc.archivo = request.FILES.get('archivo')
        arc.save()
        return Response('pdf subido')
    except:
        return Response('falla al subir el pdf')


#DEVUELVE TODOS LOS DOCUMENTOS

@api_view(['GET'])
def listDocumentosAcreditacionAll(request):

    docs_acred = Documentos_acreditacion.objects.filter().order_by('criterio','subCriterio','indicador') 
    #docs_acred = Documentos_acreditacion.objects.filter()
    serializer = documentos_acreditacion_Serializer(docs_acred, many=True)
   #print(serializer.data)

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteEntradaDocumento(request):
    data = request.data 
    try: 
        documento = Documentos_acreditacion.objects.get(id=data['id'])
        documento.delete()
        return Response ({'mensaje':'El documento  se elimino'})
    except Documentos_acreditacion.DoesNotExist:
        return Response({'error':'El documento no existe'})
    except Exception as e:
        return Response ({'error':str(e)}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
def putNombreDocumento(request):
    data = request.data 
    try: 
        documento =Documentos_acreditacion.objects.get(id=data['id'])

    except Documentos_acreditacion.DoesNotExist:
        return Response({'error': 'El Documento no existe.'}, status=status.HTTP_404_NOT_FOUND)
 
    try:
        Documentos_acreditacion.objects.filter(id=data['id']).update(
            documento = data['documento'],
        )
        return Response(status=status.HTTP_200_OK)
    except:
        message = {'faaalla'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def deleteArchivoAcreditacion(request):
        data = request.data
        try:
            # Obtén el documento por su ID
            documento = Documentos_acreditacion.objects.get(id=data['id'])
        except Documentos_acreditacion.DoesNotExist:
            return Response({"message": "Documento no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        # Elimina el archivo del sistema de archivos
        documento.archivo.delete()
        # Elimina la entrada de la base de datos
        #documento.delete()
        return Response({"message": "Documento eliminado exitosamente"})
