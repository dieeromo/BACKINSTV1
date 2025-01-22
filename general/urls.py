from django.urls import path, include
from . import views
from .views import router
from rest_framework import routers
from . views import DependenciasInstitucionales_ViewSet,TipoDependencias_Crud, BolsaEmpleo_ViewSet
from . views import HistorialDependenciaInsatitucional_Crud

router = routers.DefaultRouter()
router.register(r'bolsaEmpleo', BolsaEmpleo_ViewSet)
router.register(r'dependencias', DependenciasInstitucionales_ViewSet)
router.register(r'tipo_dependencias', TipoDependencias_Crud)
router.register(r'historial_dependencia',HistorialDependenciaInsatitucional_Crud)

urlpatterns = [
    path('coordinaciones_carrera/list/', views.listCoordinaciones_carrera),
    path('coordinaciones_institucionales/list/', views.listCoordinaciones_institucionales),
    path('otras_comisiones/list/', views.list_otras_comisiones),

    path('be/', include(router.urls)),
    path('be/lista/public/', views.listBolsaEmpleoPublic),

]