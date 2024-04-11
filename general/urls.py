from django.urls import path, include
from . import views
from .views import router


urlpatterns = [
    path('coordinaciones_carrera/list/', views.listCoordinaciones_carrera),
    path('coordinaciones_institucionales/list/', views.listCoordinaciones_institucionales),
    path('otras_comisiones/list/', views.list_otras_comisiones),

    path('be/', include(router.urls)),

]