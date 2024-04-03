from django.urls import path
from . import views


urlpatterns = [
    path('list_por_indicador/<int:id>/', views.listEvidencias_filtro_indicador),

]