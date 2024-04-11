from django.contrib import admin

from .models import Coor_Carrera, Coor_Institucionales, Otras_Comisiones, BolsaEmpleo

admin.site.register(Coor_Carrera)
admin.site.register(Coor_Institucionales),
admin.site.register(Otras_Comisiones)
admin.site.register(BolsaEmpleo)


