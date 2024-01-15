from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


from .models import Indicadores
from .serializers import  indicadores_Serializer
@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def listIndicadores_filtro_subcriterio(request,id):

    indicadores = Indicadores.objects.filter(subCriterio=id).order_by('numeracion') 
    print(indicadores)
    serializer = indicadores_Serializer(indicadores, many=True)
    return Response(serializer.data)