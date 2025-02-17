from django.urls import path, include, re_path
from rest_framework import routers

from . import views
from .views import Evaluacion_evidencia,Evaluacion_evidencia_fil_ModeloCriterio, Evaluacion_evidencia_fil_responsable
from .views import CriterioEvaluacion_ViewSet,DocumentosEvaluacion_ViewSet, PeriodoAcademico_ViewSet
from .views import EstadisticasTotaldocumentos, EstadisticaDocumentos_indicador

from .views import Subcriterio_por_criterio,Indicador_por_subcriterio,Evaluacion_evidencia_fil_Indicador

router = routers.DefaultRouter()
router.register(r'criterios', CriterioEvaluacion_ViewSet)
router.register(r'documentos', DocumentosEvaluacion_ViewSet)
router.register(r'periodo', PeriodoAcademico_ViewSet)



urlpatterns = [
    path('evaluacion_evidencia/', Evaluacion_evidencia.as_view(), name='evaluacion_evidencia'),
    path('evaluacion_evidencia_modelocriterio/', Evaluacion_evidencia_fil_ModeloCriterio.as_view(), name='evaluacion_evidencia_modelocriterio'),
    path('evaluacion_documento_responsable/', Evaluacion_evidencia_fil_responsable.as_view(), name='evaluacion_evidencia_responsable'),
    path('deletearchivo/', views.deleteArchivoEvaluacion),

    path('estadistica_total_documentos/', EstadisticasTotaldocumentos, name='obtener_estados_documentos'),
    path('estadistica_indicador_documentos/', EstadisticaDocumentos_indicador),

       
    path('evaluacion_subcriterio_criterio/', Subcriterio_por_criterio.as_view(), name='evaluacion_subcriterio_criterio'),
    path('evaluacionindicador__subcriterio/', Indicador_por_subcriterio.as_view(), name='evaluacionindicador__subcriterio'),
    path('evaluacion_documento__indicador_all/', Evaluacion_evidencia_fil_Indicador.as_view(), name='evaluacion_documento__indicador_all'),
    
    
    path('evaluacion/', include(router.urls)),

    ####
   

]