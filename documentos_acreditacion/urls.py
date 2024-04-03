from django.urls import path
from . import views


urlpatterns = [
    #registro de documentos
    path('register/<int:id_evidencia>/<int:id_responsable>/', views.registroDocumentosAcreditacion),
   #
    path('list/filter/<int:id>/', views.listDocumentosAcreditacionFilter),
    
    # para subir el archivo
    path('subir_archivo/', views.uploadArchivoDocumento),

    # todos los documentos
    path('list/all/', views.listDocumentosAcreditacionAll),

    #documentos filtrados por docente
    path('list/filter/docente/<int:id>/', views.listDocumentosAcreditacionFilterDocente),

    #vista para eliminar la definicion de documento
    path('delete/entrada/', views.deleteEntradaDocumento),
    
    #Actualizar el nombre del documento
    path('put/nombre_documento/', views.putNombreDocumento),
      
      #Borrar el archivo
    path('delete/nombre_documento/', views.deleteArchivoAcreditacion),
]