from django.shortcuts import render
from rest_framework import serializers, routers, viewsets
from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required

from .models import  CategoriaObra, TipoObra, TipoMaterial, EstadoObra, Obras, Autores
from .models import  ObrasAutores, Ubicacion_obras
from .serializers import  categoriaObra_Serializer, tipoObra_Serializer, tipoMaterial_Serializer
from .serializers import estadoObra_Serializer, obras_Serializer, autores_Serializer, obrasAutores_Serializer, ubicacionObras_Serializer
from accounts.models import UserAccount
# Create your views here.s

class Obras_crud(viewsets.ModelViewSet):
    queryset = Obras.objects.all().order_by('-id')
    serializer_class = obras_Serializer
    router = routers.DefaultRouter()


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

    categoria = CategoriaObra.objects.get(id=data['categoria'])
    tipo_obra = TipoObra.objects.get(id=data['tipo_obra'])
    tipo_material = TipoMaterial.objects.get(id=data['tipo_material'])
    estado_obra = EstadoObra.objects.get(id = data['estado_obra'])    
    digitador = UserAccount.objects.get(id=data['digitador'])
    ubicacion = Ubicacion_obras.objects.get(id=data['ubicacion'])
    
    try:
        documento = Obras.objects.create(
            codigo = data['codigo'],
            titulo = data['titulo'],
            editorial = data['editorial'],
            autor = data['autor'],
            anio_publicacion = data['anio_publicacion'],
            tomo = data['tomo'],
           # ubicacion = data['ubicacion'],
            ubicacion = ubicacion,

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




@api_view(['POST'])
@permission_classes([IsAuthenticated])
@login_required()
def registroAutor(request):
    data = request.data
    digitador = UserAccount.objects.get(id=data['digitador'])
    print (data)
    
    try:
        autor = Autores.objects.create(
            nombres = data['nombres'],
            estado = data['estado'],
            digitador = digitador,            
            observacion = data['observacion']
        )

        serializer = autores_Serializer(autor, many=False)

        return Response(serializer.data)
    except:
        message = {'detalle': 'algo esta mal en el registro de la obra'}

        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    
    
    
# @api_view(['GET'])
# @login_required()
# def listAutores(request):
#     autores = Autores.objects.filter().order_by('-id') 
#     serializer = autores_Serializer(autores, many=True)
#     return Response(serializer.data)







@api_view(['POST'])
@permission_classes([IsAuthenticated])
@login_required()
def registerObraAutor(request):
    data = request.data
 
    autor_id = Autores.objects.get(id=data['autor_id'])
    obra_id = Obras.objects.get(id=data['obra_id'])
    digitador = UserAccount.objects.get(id=data['digitador'])
  
    try:
        obrasAutores = ObrasAutores.objects.create(
            autor_id = autor_id,
            obra_id = obra_id,
            digitador = digitador,            
            observacion = data['observacion']
        )

        serializer = obrasAutores_Serializer(obrasAutores, many=False)

        return Response(serializer.data)
    except:
        message = {'detalle': 'algo esta mal en el registro de la obra'}

        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@login_required()
def listAutores_obras_todos(request):
    #try:
    listaObrasAutores = ObrasAutores.objects.filter().order_by('-id') 
    serializer = obrasAutores_Serializer( listaObrasAutores , many=True)
    return Response(serializer.data)
    #except:
    #    message = {'detalle': 'Algo esta mal en la peticion'}
    #    return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def uploadObraDocumento(request):

    data = request.data
    print('data',data)
    archivo_id = data['id']
  
    try:
        arc = Obras.objects.get(id=archivo_id)
    except Obras.DoesNotExist:
        return Response({'error':'El documento no existe'})
    
    try:
        arc.archivo = request.FILES.get('archivo')
        arc.save()
        return Response('pdf subido')
    except:
        return Response('falla al subir el pdf')



@api_view(['GET'])
#@login_required()
def FilterAutores_obras(request):
    data = request.data
    autor=''
    titulo=''
    if data['autor'] != '':
        autor = data['autor']
    if data['titulo']!= '':
        titulo = data['titulo']
    #try:
    listaObrasAutores = ObrasAutores.objects.filter(autor_id__nombres__icontains=autor,obra_id__titulo__icontains=titulo).order_by('-id') 
    serializer = obrasAutores_Serializer( listaObrasAutores , many=True)
    return Response(serializer.data)
    #except:
    #    message = {'detalle': 'Algo esta mal en la peticion'}
    #    return Response(message, status=status.HTTP_400_BAD_REQUEST)
    

    
class BibliotecaPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 2000

# Vista con filtros personalizados
class FilterObrasAutores_View(generics.ListAPIView):
    serializer_class = obrasAutores_Serializer
    pagination_class = BibliotecaPagination

    def get_queryset(self):
        # Tomamos los parámetros de la solicitud
        autor = self.request.query_params.get('autor', '')
        titulo = self.request.query_params.get('titulo', '')

        # Construimos el queryset aplicando los filtros según los parámetros
        queryset = ObrasAutores.objects.all()

        # Aplicamos los filtros solo si los parámetros tienen valor
        if autor:
            queryset = queryset.filter(autor_id__nombres__icontains=autor)
        if titulo:
            queryset = queryset.filter(obra_id__titulo__icontains=titulo)

        # Ordenamos por el campo 'id' en orden descendente
        return queryset.order_by('-id')
    


class listAutores(generics.ListAPIView):
    serializer_class = autores_Serializer
    pagination_class = BibliotecaPagination

    def get_queryset(self):
        # Tomamos los parámetros de la solicitud
        autor = self.request.query_params.get('autor', '')

        # Construimos el queryset aplicando los filtros según los parámetros
        queryset = Autores.objects.all()

        # Aplicamos los filtros solo si los parámetros tienen valor
        if autor:
            queryset = queryset.filter(nombres__icontains=autor)
        # Ordenamos por el campo 'id' en orden descendente
        return queryset.order_by('-id')
    



    
@api_view(['GET'])
#@login_required()
def FilterTitulo_obras(request, titulo):
    tempo_titulo = ''
    #try:
    if titulo!='':
        tempo_titulo= titulo
        
    listaObrasTitulo = Obras.objects.filter(titulo__icontains=tempo_titulo).order_by('-id') 
    serializer = obras_Serializer( listaObrasTitulo , many=True)
    return Response(serializer.data)
    #except:
    #    message = {'detalle': 'Algo esta mal en la peticion'}
    #    return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
#@login_required()
def FilterTitulo_obras_id(request, id):
    listaObrasTitulo = Obras.objects.filter(id=id).order_by('-id') 
    serializer = obras_Serializer( listaObrasTitulo , many=True)
    return Response(serializer.data)

@api_view(['GET'])
def FilterAutores_obras_idObra(request,id):
    listaObrasAutores = ObrasAutores.objects.filter(obra_id= id).order_by('-id') 
    serializer = obrasAutores_Serializer( listaObrasAutores , many=True)
    return Response(serializer.data)



@api_view(['DELETE'])
def deleteObraEntrada(request):
    data = request.data 
    print('id delete',data['id'])
    try: 
        documento = Obras.objects.get(id=data['id'])
        documento.delete()
        return Response ({'mensaje':'El documento  se elimino'})
    except Obras.DoesNotExist:
        return Response({'error':'El documento no existe'})
    except Exception as e:
        return Response ({'error':str(e)}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)




class UbicacionObras_ViewSet(viewsets.ModelViewSet):
    queryset = Ubicacion_obras.objects.all().order_by('-id')
    serializer_class = ubicacionObras_Serializer
router = routers.DefaultRouter()
#router.register(r'ubicacion', UbicacionObras_ViewSet)



class TipoObras_ViewSet(viewsets.ModelViewSet):
    queryset = TipoObra.objects.all().order_by('-id')
    serializer_class = tipoObra_Serializer
router = routers.DefaultRouter()
#router.register('tipo_obra', TipoObras_ViewSet)



class CategoriasObras_ViewSet(viewsets.ModelViewSet):
    queryset = CategoriaObra.objects.all().order_by('-id')
    serializer_class = categoriaObra_Serializer
router = routers.DefaultRouter()
#router.register(r'categoria_obra', CategoriasObras_ViewSet)

#class TipoMaterialObras_ViewSet(viewsets.ModelViewSet):
#    queryset = TipoMaterial.objects.all().order_by('-id')
#    serializer_class = tipoMaterial_Serializer
#router = routers.DefaultRouter()
#router.register(r'tipo_material_obra', TipoMaterialObras_ViewSet)


class AutoresObras_ViewSet(viewsets.ModelViewSet):
    queryset = Autores.objects.all().order_by('-id')
    serializer_class = autores_Serializer
router = routers.DefaultRouter()


