# from rest_framework import generics, filters
# from rest_framework.pagination import PageNumberPagination
# from rest_framework import viewsets, routers
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from django_filters.rest_framework import DjangoFilterBackend
# from django.contrib.auth.decorators import login_required
# from .filters import ObrasAutores_Filter
# from .models import ObrasAutores
# from .serializers import obrasAutores_Serializer


# class Pagination(PageNumberPagination):
#     page_size = 100
#     page_size_query_param = 'page_size'
#     max_page_size = 2000
    
# class ObrasAutores_Filter_View(generics.ListAPIView):
#    queryset = ObrasAutores.objects.all().order_by('-id')
#    serializer_class = obrasAutores_Serializer
#    pagination_class = Pagination
#    filter_backends = [DjangoFilterBackend]
#    filterset_class = ObrasAutores_Filter
    