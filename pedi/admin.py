from django.contrib import admin
from .models import Pedi_version, Objetivo_estrategico, Objetivo_especifico, Meta_objetivo
from .models import Actividad_meta,Medio_verificacion, IndicadorMedioVerificacion_Pedi
from .models import Poa
# Register your models here.
admin.site.register(Pedi_version)
admin.site.register(Objetivo_estrategico)
admin.site.register(Objetivo_especifico)
admin.site.register(Meta_objetivo)

admin.site.register(Actividad_meta)
admin.site.register(Medio_verificacion)


class PoaAdmin(admin.ModelAdmin):
    list_display = ('id','anio','indicadorPedi','NumeroSeguimiento','totalAnio','pro1','pro2')
    list_filter = ('NumeroSeguimiento','anio')
admin.site.register(Poa, PoaAdmin)


class IndicadorMedioVerificacion_PediAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','numeroPoa','entidadResponsable','total','anio1','anio2','anio3','anio4','anio5')
    list_filter = ('entidadResponsable','numeroPoa')
admin.site.register(IndicadorMedioVerificacion_Pedi, IndicadorMedioVerificacion_PediAdmin)
