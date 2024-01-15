from django.urls import path
from . import views


urlpatterns = [
    path('list_por_subcriterio/<int:id>/', views.listEvidencias_filtro_indicador),

]