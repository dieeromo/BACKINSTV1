from django.contrib import admin

from .models import Evidencias




class EvidenciasAdmin(admin.ModelAdmin):
    list_display = ('indicador','evidencia')
admin.site.register(Evidencias,EvidenciasAdmin)