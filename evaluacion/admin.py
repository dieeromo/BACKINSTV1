from django.contrib import admin
from .models import ModeloEvaluacion, CriterioEvaluacion, SubCriterioEvaluacion
from .models import TipoIndicador, IndicadorEvaluacion, EvidenciaEvaluacion
from .models import PeriodoAcademico, DocumentoEvaluacion
# Register your models here.


admin.site.register(ModeloEvaluacion)
admin.site.register(CriterioEvaluacion)
admin.site.register(SubCriterioEvaluacion)
admin.site.register(TipoIndicador)
admin.site.register(IndicadorEvaluacion)
admin.site.register(EvidenciaEvaluacion)
admin.site.register(PeriodoAcademico)
admin.site.register(DocumentoEvaluacion)
