from django.contrib import admin

from .models import ModalidadCarrera, Carreras_instituto, TipoAsignatura
from .models import Asignaturas_carreras, Semestre, Paralelo_Asignatura, Curso

admin.site.register(ModalidadCarrera)
admin.site.register(Carreras_instituto),
admin.site.register(TipoAsignatura)
admin.site.register(Asignaturas_carreras)
admin.site.register(Semestre)
admin.site.register(Paralelo_Asignatura)
admin.site.register(Curso)

