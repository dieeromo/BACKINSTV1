
from rest_framework.views import APIView
from rest_framework import serializers, routers, viewsets, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required

from .models import  Pedi_version, Objetivo_estrategico,Objetivo_especifico, Meta_objetivo
from .models import Actividad_meta,Medio_verificacion,IndicadorMedioVerificacion_Pedi
from .models import Poa

from .serializers import  pediVersion_Serializer, objeticoEstrategico_Serializer, objeticoEspecifico_Serializer
from .serializers import  metaObjeticoEspecifico_Serializer
from .serializers import actividadMeta_Serializer, medio_verificacion_Serializer, indicador_medioPedi_Serializer
from .serializers import poa_Serializer
from accounts.models import UserAccount


class PediData(APIView):
    def get(self, request):
        data = []
        pedis = Pedi_version.objects.all()
        for pedi in pedis:
            oestrategicos = Objetivo_estrategico.objects.filter(pedi=pedi)
            for oestrategico in oestrategicos:
                oespecificos = Objetivo_especifico.objects.filter(objetivo_estrategico=oestrategico)
                for oespecifico in oespecificos:
                    metas = Meta_objetivo.objects.filter(objetivo_especifico=oespecifico)
                    for meta in metas:
                        actividades = Actividad_meta.objects.filter(meta_objetivo=meta)
                        for actividad in actividades:
                            medios_verificacio = Medio_verificacion.objects.filter(actividad_meta=actividad)
                            for medio in medios_verificacio:
                                indicadores_medios = IndicadorMedioVerificacion_Pedi.objects.filter(medio_verificacion = medio)
                                for indicador in indicadores_medios:
                                    data.append({
                                        'pedi': pedi.nombre,
                                        'oestrategico': oestrategico.nombre,
                                        'oestrategico_sigla':oestrategico.sigla,
                                        'oespecifico': oespecifico.nombre,
                                        'meta': meta.nombre,
                                        'actividad': actividad.nombre,
                                        'medio':medio.nombre,
                                        'indicadorPedi': indicador.nombre,
                                        'totalPedi': indicador.total,
                                        'anio1':indicador.anio1,
                                        'anio2':indicador.anio2,
                                        'anio3':indicador.anio3,
                                        'anio4':indicador.anio4,
                                        'anio5':indicador.anio5,
                                        'responsable':indicador.entidadResponsable.nombre,
                                        'responsable_sigla':indicador.entidadResponsable.siglas,
                                    })
        return Response(data)

class PoaData(APIView):
    def get(self, request):
        entidadResponsableSigla = request.GET.get('entidadSigla', None)
        anio = request.GET.get('anio', None)
        data = []
        pedis = Pedi_version.objects.all()
        for pedi in pedis:
            oestrategicos = Objetivo_estrategico.objects.filter(pedi=pedi)
            for oestrategico in oestrategicos:
                oespecificos = Objetivo_especifico.objects.filter(objetivo_estrategico=oestrategico)
                for oespecifico in oespecificos:
                    metas = Meta_objetivo.objects.filter(objetivo_especifico=oespecifico)
                    for meta in metas:
                        actividades = Actividad_meta.objects.filter(meta_objetivo=meta)
                        for actividad in actividades:
                            medios_verificacio = Medio_verificacion.objects.filter(actividad_meta=actividad)
                            for medio in medios_verificacio:
                                indicadores_medios = IndicadorMedioVerificacion_Pedi.objects.filter(medio_verificacion = medio, entidadResponsable__siglas__icontains = entidadResponsableSigla )
                                for indicador in indicadores_medios:
                                        data.append({
                                            'pedi': pedi.nombre,
                                            'oestrategico': oestrategico.nombre,
                                            'oestrategico_sigla':oestrategico.sigla,
                                            'oespecifico': oespecifico.nombre,
                                            'meta': meta.nombre,
                                            'actividad': actividad.nombre,
                                            'medio':medio.nombre,
                                            'indicadorPedi': indicador.nombre,
                                            'indicadorID':indicador.id,
                                            'totalPedi': indicador.total,
                                            'anio1':indicador.anio1,
                                            'anio2':indicador.anio2,
                                            'anio3':indicador.anio3,
                                            'anio4':indicador.anio4,
                                            'anio5':indicador.anio5,
                                            'medio_verificacion_id':medio.id,
                                            'activo_indicador': indicador.activo,
                                            'cumple_indicador':indicador.cumple,
                                            'observacion_indicador':indicador.observacion,
                                            'digitador':indicador.digitador.id,
                                            
                                 

                                            'responsable':indicador.entidadResponsable.nombre,
                                            'responsable_id':indicador.entidadResponsable.id,
                                            'responsable_sigla':indicador.entidadResponsable.siglas,
                                            'coordinador_entidad':indicador.entidadResponsable.representante.id,
                                            'numeroPoa':indicador.numeroPoa,
                                        })
                                        
        
                                     
        for datos in data:
            poaData = Poa.objects.filter(indicadorPedi = datos['indicadorID'], anio=2024)
            for p in poaData:
                datos['idPoa'] = p.id
                datos['anioPoa'] = p.anio
                datos['totalAnio'] = p.totalAnio
                datos['pro1'] = p.pro1
                datos['pro2'] = p.pro2
                datos['pro3'] = p.pro3
                datos['pro4'] = p.pro4
                datos['pro5'] = p.pro5
                datos['pro6'] = p.pro6
                datos['pro7'] = p.pro7
                datos['pro8'] = p.pro8
                datos['pro9'] = p.pro9
                datos['pro10'] = p.pro10
                datos['pro11'] = p.pro11
                datos['pro12'] = p.pro12
                datos['NumeroSeguimiento'] = p.NumeroSeguimiento
                
                datos['totalAnioEje'] = p.totalAnioEje
                datos['eje1'] = p.eje1
                datos['eje2'] = p.eje2
                datos['eje3'] = p.eje3
                datos['eje4'] = p.eje4
                datos['eje5'] = p.eje5
                datos['eje6'] = p.eje6
                datos['eje7'] = p.eje7
                datos['eje8'] = p.eje8
                datos['eje9'] = p.eje9
                datos['eje10'] = p.eje10
                datos['eje11'] = p.eje11
                datos['eje12'] = p.eje12
                

        return Response(data)


class PediVersion_ViewSet(viewsets.ModelViewSet):
    queryset = Pedi_version.objects.all().order_by('-id')
    serializer_class = pediVersion_Serializer
router = routers.DefaultRouter()



class ObjetivoEstrategico_ViewSet(viewsets.ModelViewSet):
    queryset = Objetivo_estrategico.objects.all().order_by('-id')
    serializer_class = objeticoEstrategico_Serializer
router = routers.DefaultRouter()




class ObjetivoEspecifico_ViewSet(viewsets.ModelViewSet):
    queryset = Objetivo_especifico.objects.all().order_by('-id')
    serializer_class = objeticoEspecifico_Serializer
router = routers.DefaultRouter()


class MetaEspecifico_ViewSet(viewsets.ModelViewSet):
    queryset = Meta_objetivo.objects.all().order_by('-id')
    serializer_class = metaObjeticoEspecifico_Serializer
router = routers.DefaultRouter()


class ActividaMeta_ViewSet(viewsets.ModelViewSet):
    queryset = Actividad_meta.objects.all().order_by('-id')
    serializer_class = actividadMeta_Serializer
router = routers.DefaultRouter()


class MedioVerificacion_ViewSet(viewsets.ModelViewSet):
    queryset = Medio_verificacion.objects.all().order_by('-id')
    serializer_class = medio_verificacion_Serializer
router = routers.DefaultRouter()


class IndicadorMedioPedi_ViewSet(viewsets.ModelViewSet):
    queryset = IndicadorMedioVerificacion_Pedi.objects.all().order_by('-id')
    serializer_class = indicador_medioPedi_Serializer
router = routers.DefaultRouter()


class poa_ViewSet(viewsets.ModelViewSet):
    queryset = Poa.objects.all().order_by('-id')
    serializer_class = poa_Serializer
router = routers.DefaultRouter()








@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def obj_estrategico_filtro_pedi(request,pedi):
    ob_estr = Objetivo_estrategico.objects.filter(pedi=pedi).order_by('id')
    serializer = objeticoEstrategico_Serializer(ob_estr, many=True)
    #print(serializer.data)
    return Response(serializer.data)


@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def obj_especifico_filtro_ObEstrategico(request,o_estrategico):
    ob_especifico = Objetivo_especifico.objects.filter(objetivo_estrategico=o_estrategico).order_by('id')
    serializer = objeticoEspecifico_Serializer(ob_especifico, many=True)
    #print(serializer.data)
    return Response(serializer.data)


@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def metaObjetivo_obEspecifico(request,o_especifico):
    meta_especifico = Meta_objetivo.objects.filter(objetivo_especifico=o_especifico).order_by('id')
    serializer = metaObjeticoEspecifico_Serializer(meta_especifico, many=True)
    #print(serializer.data)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def actividad_meta(request,meta):
    actividad = Actividad_meta.objects.filter(meta_objetivo=meta).order_by('id')
    serializer = actividadMeta_Serializer(actividad, many=True)
    #print(serializer.data)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def medioVerificacion_actividad(request,actividad):
    medio = Medio_verificacion.objects.filter(actividad_meta=actividad).order_by('id')
    serializer = medio_verificacion_Serializer(medio, many=True)
    #print(serializer.data)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def indicadorPedi_medio(request,medio):
    indicador = IndicadorMedioVerificacion_Pedi.objects.filter(medio_verificacion=medio).order_by('id')
    serializer = indicador_medioPedi_Serializer(indicador, many=True)
    #print(serializer.data)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def poaTabla_indicadorPedi(request,indicadorPedi):
    poa = Poa.objects.filter(indicadorPedi=indicadorPedi).order_by('id')
    serializer = poa_Serializer(poa, many=True)
    #print(serializer.data)
    return Response(serializer.data)