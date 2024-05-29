from django.contrib import admin

from .models import Coor_Carrera, Coor_Institucionales, Otras_Comisiones, BolsaEmpleo
from . models import TipoDependencia, DependenciasInstitucionales, OcurrenciaDependencias,HistorialDependencias
admin.site.register(Coor_Carrera)
admin.site.register(Coor_Institucionales),
admin.site.register(Otras_Comisiones)
admin.site.register(BolsaEmpleo)

admin.site.register(TipoDependencia)
admin.site.register(DependenciasInstitucionales)
admin.site.register(OcurrenciaDependencias)
admin.site.register(HistorialDependencias)


