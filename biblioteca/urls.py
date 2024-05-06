from django.urls import path, include
from . import views
from rest_framework import routers
from .views import UbicacionObras_ViewSet, CategoriasObras_ViewSet, TipoObras_ViewSet, AutoresObras_ViewSet
from .views import router

router = routers.DefaultRouter()
router.register(r'ubicacion', UbicacionObras_ViewSet)
router.register(r'categorias', CategoriasObras_ViewSet)
router.register(r'tipo_obras', TipoObras_ViewSet)
router.register(r'autores', AutoresObras_ViewSet)


urlpatterns = [
    path('register/obra/', views.registroObra),
   
    path('list/categoria_obra/', views.listCategoria_obras),
    path('list/tipo_obras/', views.listTipo_obras),
    path('list/tipo_material/', views.listTipo_material),
    path('list/estado_obra/', views.listEstado_obra),
    path('list/obras/', views.filtro_obras_libros),
    path('obras/', include(router.urls)),

    path('register/autor/', views.registroAutor),
    path('list/autor/', views.listAutores),

    path('register/obraautor/', views.registerObraAutor),
    path('list/obras_autores/todos/', views.listAutores_obras_todos),  #devuelve todos loa auores y obras
    path('carga/obras/', views.uploadObraDocumento),  #
    path('filtro/autores/', views.FilterAutores_obras),  #d
    path('filtro/titulo/<str:titulo>/', views.FilterTitulo_obras),  #d
    path('filtro/titulo/id/<int:id>/', views.FilterTitulo_obras_id),  #d
    path('filtro/autor_por_obra/id/<int:id>/', views.FilterAutores_obras_idObra),  #d
    path('delete/obra_entrada/', views.deleteObraEntrada),  #d

]