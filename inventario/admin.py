from django.contrib import admin

from .models import TipoInventario,EstadoInventario,UbicacionInventario,InventarioIST

# Register your models here.
admin.site.register(TipoInventario)
admin.site.register(EstadoInventario)

admin.site.register(UbicacionInventario)
admin.site.register(InventarioIST)
