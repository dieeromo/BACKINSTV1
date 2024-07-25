from django.urls import path, include, re_path
from rest_framework import routers

from . import views
from .views import Evaluacion_evidencia,Evaluacion_evidencia_fil_ModeloCriterio, Evaluacion_evidencia_fil_responsable
from .views import CriterioEvaluacion_ViewSet,DocumentosEvaluacion_ViewSet, PeriodoAcademico_ViewSet, Estadisticas

router = routers.DefaultRouter()
router.register(r'criterios', CriterioEvaluacion_ViewSet)
router.register(r'documentos', DocumentosEvaluacion_ViewSet)
router.register(r'periodo', PeriodoAcademico_ViewSet)



urlpatterns = [
    path('evaluacion_evidencia/', Evaluacion_evidencia.as_view(), name='evaluacion_evidencia'),
    path('evaluacion_evidencia_modelocriterio/', Evaluacion_evidencia_fil_ModeloCriterio.as_view(), name='evaluacion_evidencia_modelocriterio'),
    path('evaluacion_documento_responsable/', Evaluacion_evidencia_fil_responsable.as_view(), name='evaluacion_evidencia_responsable'),
    path('deletearchivo/', views.deleteArchivoEvaluacion),
    path('estadisticas/', Estadisticas.as_view(), name='estadisticas'),
    

    
    
    path('evaluacion/', include(router.urls)),

]