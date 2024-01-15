from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


from .models import Coor_Carrera, Coor_Institucionales, Otras_Comisiones
from .serializers import  Coor_Carrera_Serializer, Coor_Institucionales_Serializer, Otras_comisiones_Serializer
@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def listCoordinaciones_carrera(request):
    carrera = Coor_Carrera.objects.filter().order_by('id') 
    serializer = Coor_Carrera_Serializer(carrera, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def listCoordinaciones_institucionales(request):
    coor_inst = Coor_Institucionales.objects.filter().order_by('id') 
    serializer = Coor_Institucionales_Serializer(coor_inst, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def list_otras_comisiones(request):
    otras = Otras_Comisiones.objects.filter().order_by('id') 
    serializer = Otras_comisiones_Serializer(otras, many=True)
    return Response(serializer.data)

#Mariela Arevalo de ipueran

# 