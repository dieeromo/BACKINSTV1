from django.urls import path, include
from .views import router
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'modalidadCarrera', views.ModalidadCarrera_ViewSet)
router.register(r'carrera', views.CarreraInstituto_ViewSet)
router.register(r'tipoAsignatura', views.TipoAsignatura_ViewSet)
router.register(r'asignatura', views.AsignaturasCarreras_ViewSet)
router.register(r'semestre', views.Semestre_ViewSet)
router.register(r'paralelo', views.ParaleloAsignatura_ViewSet)
router.register(r'curso', views.Curso_ViewSet)



urlpatterns = [
    path('pea/', include(router.urls)),


]