from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import UserAccount
from .serializers import UserCreateSerializer

@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def listUserAccount(request):
  

    usuarios = UserAccount.objects.filter().order_by('id')
  
  
    serializer = UserCreateSerializer(usuarios, many=True)
    #print(serializer.data)
    return Response(serializer.data)
