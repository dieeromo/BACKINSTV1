from django.urls import path, include
from . import views
from .views import router
from rest_framework import routers
from . views import DependenciasInstitucionales_ViewSet

router = routers.DefaultRouter()
router.register(r'dependencias', DependenciasInstitucionales_ViewSet)

urlpatterns = [
    path('coordinaciones_carrera/list/', views.listCoordinaciones_carrera),
    path('coordinaciones_institucionales/list/', views.listCoordinaciones_institucionales),
    path('otras_comisiones/list/', views.list_otras_comisiones),

    path('be/', include(router.urls)),
    path('be/lista/public/', views.listBolsaEmpleoPublic),

]