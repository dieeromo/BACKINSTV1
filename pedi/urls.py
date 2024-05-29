from django.urls import path, include, re_path
from .views import router
from .views import PediVersion_ViewSet, ObjetivoEstrategico_ViewSet, ObjetivoEspecifico_ViewSet, MetaEspecifico_ViewSet
from .views import ActividaMeta_ViewSet, MedioVerificacion_ViewSet, IndicadorMedioPedi_ViewSet
from .views import poa_ViewSet
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'pedi', PediVersion_ViewSet)
router.register(r'estrategicos', ObjetivoEstrategico_ViewSet)
router.register(r'especificos', ObjetivoEspecifico_ViewSet)
router.register(r'metas_especificos', MetaEspecifico_ViewSet)
router.register(r'actividades', ActividaMeta_ViewSet)
router.register(r'medio_verificacion', MedioVerificacion_ViewSet)
router.register(r'indicador_medio_pedi', IndicadorMedioPedi_ViewSet)
router.register(r'poa', poa_ViewSet)

urlpatterns = [
    path('pedi/', include(router.urls)),
    path('objetivos_estrategicos/<int:pedi>/', views.obj_estrategico_filtro_pedi),
    path('objetivos_especificos/<int:o_estrategico>/', views.obj_especifico_filtro_ObEstrategico),
    path('metas_especificos/<int:o_especifico>/', views.metaObjetivo_obEspecifico),
    path('actividades_meta/<int:meta>/', views.actividad_meta),
    path('medio_verificacion/<int:actividad>/', views.medioVerificacion_actividad),
    path('indicador_pedi/<int:medio>/', views.indicadorPedi_medio),
    path('poa/<int:indicador>/', views.poaTabla_indicadorPedi),
    

]
