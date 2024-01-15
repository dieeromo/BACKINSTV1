# serializers.py
from rest_framework import serializers
from .models import ArchivoPDF

class ArchivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchivoPDF
        fields = ['id','nombre', 'archivo']
