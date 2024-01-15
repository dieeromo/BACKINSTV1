from django.urls import path
from . import views


urlpatterns = [
    path('register/<int:id_evidencia>/<int:id_responsable>/', views.registroDocumentosAcreditacion),
    path('list/filter/<int:id>/', views.listDocumentosAcreditacionFilter),
    path('subir_archivo/', views.uploadArchivoDocumento),

    path('list/all/', views.listDocumentosAcreditacionAll),
]