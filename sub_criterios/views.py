from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


from .models import SubCriterios
from .serializers import    subcriterios_Serializer
@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def listSubcriterios_filtro_criterio(request,id):

    subcriterios = SubCriterios.objects.filter(criterio=id).order_by('id') 
    serializer = subcriterios_Serializer(subcriterios, many=True)
    return Response(serializer.data)