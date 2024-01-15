from django.urls import path
from . import views


urlpatterns = [
    path('list_por_criterio/<int:id>/', views.listSubcriterios_filtro_criterio),

]