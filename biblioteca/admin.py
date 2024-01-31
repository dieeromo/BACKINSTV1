from django.contrib import admin

from .models import  CategoriaObra, TipoObra, TipoMaterial, EstadoObra, Obras
# Register your models here.

admin.site.register(CategoriaObra)
admin.site.register(TipoObra)
admin.site.register(TipoMaterial)
admin.site.register(EstadoObra)
admin.site.register(Obras)