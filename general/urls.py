from django.urls import path
from . import views


urlpatterns = [
    path('coordinaciones_carrera/list/', views.listCoordinaciones_carrera),
    path('coordinaciones_institucionales/list/', views.listCoordinaciones_institucionales),
    path('otras_comisiones/list/', views.list_otras_comisiones),

]