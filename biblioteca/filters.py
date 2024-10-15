import django_filters
from .models import ObrasAutores
from django.db.models import Q
from django_filters import DateFromToRangeFilter


class ObrasAutores_Filter(django_filters.FilterSet):
    autor = django_filters.CharFilter(field_name='autor_id__nombres', lookup_expr='icontains')
    obra = django_filters.CharFilter(field_name='obra_id__titulo', lookup_expr='icontains')

    class Meta:
        model = ObrasAutores
        fields = ['autor', 'obra']
        