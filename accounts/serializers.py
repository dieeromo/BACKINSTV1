from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from .models import UserAccount
User = get_user_model()

from djoser.serializers import UserSerializer



class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'first_name', 'last_name')
        



class usuario_serializador_creado(UserSerializer):
    label = serializers.CharField(source='first_name.first_name', read_only=True)
    class Meta:
        model = UserAccount
        fields = ('id', 'email', 'first_name', 'last_name','is_rectora','is_investigacion','is_docente','is_administrativo3','label')
        #fields = '__all__'

