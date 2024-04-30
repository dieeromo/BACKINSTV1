from django.shortcuts import render
from rest_framework import serializers,routers, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required

from .models import TipoInventario,EstadoInventario,UbicacionInventario, InventarioIST
from. serializers import tipoInventario_Serializer,estadoInventario_Serializer,ubicacionInventario_Serializer,inventarioIST_Serializer
from accounts.models import UserAccount

## VISTA QUE DEVUELVE TODOS LOS TIPOS DE INVENTARIO ORDENADOS POR ID
@api_view(['GET'])
@login_required()
def list_tipoInventario(request):
    list = TipoInventario.objects.filter().order_by('id') 
    serializer = tipoInventario_Serializer(list, many=True)
    return Response(serializer.data)

## VISTA QUE DEVUELVE TODOS LOS ESTADOS DE INVENTARIO ORDENADOS POR ID
@api_view(['GET'])
@login_required()
def list_estadoInventario(request):
    list = EstadoInventario.objects.filter().order_by('id') 
    serializer = estadoInventario_Serializer(list, many=True)
    return Response(serializer.data)

## VISTA QUE DEVUELVE TODAS LAS UBICACIONES DE INVENTARIO ORDENADOS POR ID
@api_view(['GET'])
@login_required()
def list_ubicacionInventario(request):
    list = UbicacionInventario.objects.filter().order_by('id') 
    serializer = ubicacionInventario_Serializer(list, many=True)
    print(serializer.data)
    return Response(serializer.data)


#DEVUELVE TODOS LOS ITEM DE INVENTARIO, VISTA PRELIMINAR
#ESTO HAY QUE PAGINAR POR QUE SEGURAMENTE SERAN VARIOS CIENTOS DE ARTICULOS
@api_view(['GET'])
@login_required()
def list_inventarioIST(request):
    list = InventarioIST.objects.filter().order_by('id') 
    serializer = inventarioIST_Serializer(list, many=True)
    return Response(serializer.data)




@api_view(['POST'])
#@permission_classes([IsAuthenticated])
@login_required()
def register_inventario(request):
    data = request.data
    tipo = TipoInventario.objects.get(id=data['tipo'])
    estado = EstadoInventario.objects.get(id=data['estado'])
    ubicacion = UbicacionInventario.objects.get(id=data['ubicacion'])
    asignado = UserAccount.objects.get(id = data['asignado'])  
    digitador = UserAccount.objects.get(id = data['digitador'])  
    print(tipo)  
    print(estado)  
    print(ubicacion)
    print(asignado)  
    
    try:
        documento = InventarioIST.objects.create(
            cod_unico = data['cod_unico'],
            cod_senescyt = data['cod_senescyt'],
            cod_instituto = data['cod_instituto'],
            tipo = tipo,

            descripcion  = data['descripcion'],
            materiales = data['materiales'],
            marca = data['marca'],
            modelo = data['modelo'],

            serie = data['serie'],
            color = data['color'],

            estado = estado,
            ubicacion = ubicacion,
            asignado = asignado,
            digitador = digitador,
            observacion = data['observacion']
        )

        serializer = inventarioIST_Serializer(documento, many=False)

        return Response(serializer.data)
    except:
        message = {'detalle': 'algo esta mal en el registro del inventario'}

        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    





class Inventario_ViewSet(viewsets.ModelViewSet):
    queryset = InventarioIST.objects.all().order_by('-id')
    serializer_class = inventarioIST_Serializer
router = routers.DefaultRouter()
router.register(r'inventario', Inventario_ViewSet)

