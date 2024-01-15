from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


from .models import Evidencias
from .serializers import  evidencias_Serializer
@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def listEvidencias_filtro_indicador(request,id):
  

    evidencia = Evidencias.objects.filter(indicador=id).order_by('numeracion')
    #evidencia2 = Evidencias.objects.get(indicador=id)
    #if evidencia2:
    #    print(evidencia2.__dict__)
    #else:
    #    print("objeto no encontrado")
    #print(evidencia2.id)
  
    serializer = evidencias_Serializer(evidencia, many=True)
    #print(serializer.data)
    return Response(serializer.data)