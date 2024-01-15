# views.py
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from rest_framework import status
from .models import ArchivoPDF
from .serializers import ArchivoSerializer

@api_view(['GET'])
def listar_archivos(request):
    archivos = ArchivoPDF.objects.all()
    serializer = ArchivoSerializer(archivos, many=True)
    return Response(serializer.data)


@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def registroArchivo(request):
    data = request.data
    try:
        carga = ArchivoPDF.objects.create(
            nombre = data['nombre'],
            archivo = request.FILES.get('archivo')
        )

        serializer = ArchivoSerializer(carga, many=False)

        return Response(serializer.data)
    except:
        message = {'detalle': 'algo esta mal en el registro del cliente'}

        return Response(message, status=status.HTTP_400_BAD_REQUEST)




@api_view(['PUT'])
#@permission_classes([IsAuthenticated])
def uploadArchivo(request):
    data = request.data
    archivo_id = data['id']
    arc = ArchivoPDF.objects.get(id=archivo_id)
    arc.archivo = request.FILES.get('archivo')
    arc.save()

    return Response('pdf subido')