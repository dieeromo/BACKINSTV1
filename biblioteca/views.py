from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required

from .models import  CategoriaObra, TipoObra, TipoMaterial, EstadoObra, Obras
from .serializers import  categoriaObra_Serializer, tipoObra_Serializer, tipoMaterial_Serializer
from .serializers import estadoObra_Serializer, obras_Serializer
from accounts.models import UserAccount
# Create your views here.s


@api_view(['GET'])
@login_required()
def listCategoria_obras(request):
    cat_obras = CategoriaObra.objects.filter().order_by('id') 
    serializer = categoriaObra_Serializer(cat_obras, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@login_required()
def listTipo_obras(request):
    tipo_obras = TipoObra.objects.filter().order_by('id') 
    serializer = tipoObra_Serializer(tipo_obras, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@login_required()
def listTipo_material(request):
    tipo_material = TipoMaterial.objects.filter().order_by('id') 
    serializer = tipoMaterial_Serializer(tipo_material, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@login_required()
def listEstado_obra(request):
    estadoObra = EstadoObra.objects.filter().order_by('id') 
    serializer = estadoObra_Serializer(estadoObra, many=True)
    return Response(serializer.data)




@api_view(['POST'])
#@permission_classes([IsAuthenticated])
@login_required()
def registroObra(request):

    data = request.data
    print(data['digitador'])
    categoria = CategoriaObra.objects.get(id=data['categoria'])
    tipo_obra = TipoObra.objects.get(id=data['tipo_obra'])
    tipo_material = TipoMaterial.objects.get(id=data['tipo_material'])
    estado_obra = EstadoObra.objects.get(id = data['estado_obra'])    
    digitador = UserAccount.objects.get(id=data['digitador'])
    
    try:
        documento = Obras.objects.create(
            codigo = data['codigo'],
            titulo = data['titulo'],
            editorial = data['editorial'],
            autor = data['autor'],
            anio_publicacion = data['anio_publicacion'],
            tomo = data['tomo'],
            ubicacion = data['ubicacion'],

            categoria = categoria,
            tipo_obra = tipo_obra,
            tipo_material = tipo_material,
            estado_obra = estado_obra,
            estado_activo = True,

            digitador = digitador,
            observacion = data['observacion']
        )

        serializer = obras_Serializer(documento, many=False)

        return Response(serializer.data)
    except:
        message = {'detalle': 'algo esta mal en el registro de la obra'}

        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
#@login_required()
def filtro_obras_libros(request):
    obras_libros = Obras.objects.filter().order_by('id') 
    serializer = obras_Serializer(obras_libros, many=True)
    return Response(serializer.data)




