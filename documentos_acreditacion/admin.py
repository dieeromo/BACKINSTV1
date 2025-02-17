from django.contrib import admin

from .models import Documentos_acreditacion




class DocumentosAdmin(admin.ModelAdmin):
    list_display = ('documento',)
admin.site.register(Documentos_acreditacion,DocumentosAdmin)