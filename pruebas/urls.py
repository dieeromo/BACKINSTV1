from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.listar_archivos),
    path('register/', views.registroArchivo),
    path('pdf/', views.uploadArchivo),
]